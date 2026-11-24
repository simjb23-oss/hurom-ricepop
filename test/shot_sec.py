import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8766', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
base = 'http://127.0.0.1:8766/index.html'
errors = []
def shoot_sec(pg, sel, name):
    pg.evaluate('(s)=>{const e=document.querySelector(s);scrollTo({top:e.getBoundingClientRect().top+scrollY-10,behavior:"instant"})}', sel); pg.wait_for_timeout(700)
    c = pg.evaluate('(s)=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:Math.min(r.height,4000)}}', sel)
    pg.screenshot(path=os.path.join(root, 'test', name + '.png'), full_page=True, clip=c)
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={'width': 1440, 'height': 900})
        ctx.route('**/explode.js', lambda r: r.abort())
        pg = ctx.new_page()
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        pg.goto(base); pg.wait_for_timeout(1500)
        h = pg.evaluate('document.body.scrollHeight'); y = 0
        while y < h:
            pg.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg.wait_for_timeout(70); y += 700
        pg.wait_for_timeout(1000)
        for sel, name in [('.hero', 'hero'), ('#problem', 'problem'), ('#safety', 'safety'), ('#design', 'design'), ('#how', 'how'), ('#modes', 'modes'), ('#cutaway', 'cutaway'), ('#clean', 'clean'), ('#spec', 'spec'), ('#gain', 'gain'), ('#biz', 'biz'), ('#feasible', 'feasible'), ('#plan', 'plan'), ('#decide', 'decide')]:
            shoot_sec(pg, sel, 'sec_' + name)
        print('scrollWidth 1440:', pg.evaluate('document.documentElement.scrollWidth'))
        ctx2 = b.new_context(viewport={'width': 390, 'height': 844}); ctx2.route('**/explode.js', lambda r: r.abort())
        pg2 = ctx2.new_page(); pg2.goto(base); pg2.wait_for_timeout(1500)
        h = pg2.evaluate('document.body.scrollHeight'); y = 0
        while y < h:
            pg2.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg2.wait_for_timeout(50); y += 600
        pg2.wait_for_timeout(800)
        print('scrollWidth 390:', pg2.evaluate('document.documentElement.scrollWidth'))
        pg2.evaluate('scrollTo({top:0,behavior:"instant"})'); pg2.wait_for_timeout(400)
        pg2.screenshot(path=os.path.join(root, 'test', 'm_hero.png'))
        shoot_sec(pg2, '#design', 'm_design'); shoot_sec(pg2, '#spec', 'm_spec'); shoot_sec(pg2, '#cutaway', 'm_cutaway'); shoot_sec(pg2, '#gain', 'm_gain')
        b.close()
finally:
    srv.terminate()
print('errors:', len(errors)); [print(' -', e[:200]) for e in errors[:10]]
