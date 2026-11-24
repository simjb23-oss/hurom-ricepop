import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8768', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
errors = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); ctx = b.new_context(viewport={'width': 1440, 'height': 900}); ctx.route('**/explode.js', lambda r: r.abort())
        pg = ctx.new_page(); pg.on('pageerror', lambda e: errors.append(str(e)))
        pg.goto('http://127.0.0.1:8768/index.html'); pg.wait_for_timeout(1200)
        h = pg.evaluate('document.body.scrollHeight'); y = 0
        while y < h: pg.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg.wait_for_timeout(60); y += 700
        pg.wait_for_timeout(800)
        for sel in sys.argv[1:] or ['#recipe', '#cutaway', '#feasible', '#design', '#clean', 'footer']:
            c = pg.evaluate('(s)=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:Math.min(r.height,5000)}}', sel)
            pg.screenshot(path=os.path.join(root, 'test', 'v3_' + sel.strip('#.') + '.png'), full_page=True, clip=c); print('shot', sel)
        print('scrollWidth:', pg.evaluate('document.documentElement.scrollWidth'), 'errors:', errors)
        b.close()
finally: srv.terminate()
