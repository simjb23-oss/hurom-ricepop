import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8767', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
base = 'http://127.0.0.1:8767/index.html'
states = sys.argv[1:] or ['3d_family=p=0&ang=32', '3d_explode=p=1&ang=40', '3d_cream=p=0.1&ang=28&color=cream&nowasher']
try:
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1440, 'height': 900})
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{document.documentElement.style.scrollBehavior='auto'})")
        for st in states:
            name, q = st.split('=', 1)
            pg.goto(base + '?' + q); pg.wait_for_timeout(1500)
            pg.evaluate("scrollTo({top:document.getElementById('structure').offsetTop+5,behavior:'instant'})"); pg.wait_for_timeout(2500)
            r = pg.evaluate('(()=>{const r=document.querySelector(".xv-stage").getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}})()')
            pg.screenshot(path=os.path.join(root, 'test', name + '.png'), clip=r); print('shot', name)
        b.close()
finally:
    srv.terminate()
