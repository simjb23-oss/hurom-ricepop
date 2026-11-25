import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8767', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2); errs = []
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); ctx = b.new_context(viewport={'width': 1440, 'height': 900}); ctx.route('**/explode.js', lambda r: r.abort())
        pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto('http://127.0.0.1:8767/index.html'); pg.wait_for_timeout(1500)
        h = pg.evaluate('document.body.scrollHeight'); y = 0
        while y < h: pg.evaluate(f'scrollTo({{top:{y},behavior:"instant"}})'); pg.wait_for_timeout(60); y += 700
        pg.wait_for_timeout(800)
        for sel, name in [('#drawings', 'sec_drawings'), ('#cutaway', 'sec_cutaway')]:
            c = pg.evaluate('(s)=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height}}', sel)
            print(name, c['height'])
            # 앞 4000px 과 뒤 부분 나눠 찍기
            yy = c['y']; k = 0
            while yy < c['y'] + c['height']:
                hh = min(3000, c['y'] + c['height'] - yy)
                pg.screenshot(path=os.path.join(root, 'test', '%s_%d.png' % (name, k)), full_page=True, clip={'x': c['x'], 'y': yy, 'width': c['width'], 'height': hh}); yy += hh; k += 1
        print('sw', pg.evaluate('document.documentElement.scrollWidth'), 'errs', errs)
        b.close()
finally:
    srv.terminate()
