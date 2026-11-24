import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8765', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
base = 'http://127.0.0.1:8765/index.html'
errors = []
def clip_of(pg, sel):
    return pg.evaluate('(s)=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height}}', sel)
def shoot_sec(pg, sel, name):
    pg.evaluate('(s)=>{const e=document.querySelector(s);scrollTo({top:e.getBoundingClientRect().top+scrollY-10,behavior:"instant"})}', sel); pg.wait_for_timeout(900)
    c = clip_of(pg, sel); c['height'] = min(c['height'], 4000)
    pg.screenshot(path=os.path.join(root, 'test', name + '.png'), full_page=True, clip=c)
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1440, 'height': 900})
        pg.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: errors.append(str(e)))
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{document.documentElement.style.scrollBehavior='auto'})")
        for name, q in [('3d_family', 'p=0&ang=32'), ('3d_lift', 'p=0.45&ang=32'), ('3d_heat', 'p=0.7&ang=40'), ('3d_explode', 'p=1&ang=40'), ('3d_cream', 'p=0.1&ang=28&color=cream&nowasher')]:
            pg.goto(base + '?' + q); pg.wait_for_timeout(2500)
            pg.evaluate("scrollTo({top:document.getElementById('structure').offsetTop+5,behavior:'instant'})"); pg.wait_for_timeout(3000)
            r = pg.evaluate('(()=>{const r=document.querySelector(".xv-stage").getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}})()')
            pg.screenshot(path=os.path.join(root, 'test', name + '.png'), clip=r)
        pg.goto(base); pg.wait_for_timeout(1500)
        h = pg.evaluate('document.body.scrollHeight'); y = 0
        while y < h:
            pg.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg.wait_for_timeout(80); y += 700
        pg.wait_for_timeout(1200)
        for sel, name in [('.hero', 'hero'), ('#problem', 'problem'), ('#safety', 'safety'), ('#design', 'design'), ('#how', 'how'), ('#modes', 'modes'), ('#cutaway', 'cutaway'), ('#clean', 'clean'), ('#spec', 'spec'), ('#biz', 'biz'), ('#feasible', 'feasible'), ('#decide', 'decide')]:
            shoot_sec(pg, sel, 'sec_' + name)
        print('scrollWidth 1440:', pg.evaluate('document.documentElement.scrollWidth'))
        pg2 = b.new_page(viewport={'width': 390, 'height': 844}); pg2.goto(base); pg2.wait_for_timeout(1500)
        h = pg2.evaluate('document.body.scrollHeight'); y = 0
        while y < h:
            pg2.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg2.wait_for_timeout(60); y += 600
        pg2.wait_for_timeout(1000)
        print('scrollWidth 390:', pg2.evaluate('document.documentElement.scrollWidth'))
        pg2.evaluate('scrollTo({top:0,behavior:"instant"})'); pg2.wait_for_timeout(500)
        pg2.screenshot(path=os.path.join(root, 'test', 'm_hero.png'))
        shoot_sec(pg2, '#design', 'm_design'); shoot_sec(pg2, '#spec', 'm_spec'); shoot_sec(pg2, '#cutaway', 'm_cutaway')
        b.close()
finally:
    srv.terminate()
print('errors:', len(errors)); [print(' -', e[:200]) for e in errors[:10]]
