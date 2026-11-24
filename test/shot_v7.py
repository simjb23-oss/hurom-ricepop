import sys, os, subprocess, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
srv = subprocess.Popen([sys.executable, '-m', 'http.server', '8768', '--bind', '127.0.0.1'], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1.2)
ids = sys.argv[1:] or ['top', 'safety', 'design', 'how', 'modes', 'heat', 'recipe', 'cutaway', 'clean', 'feasible']
try:
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1380, 'height': 900})
        pg.add_init_script("addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('.rv').forEach(e=>{e.style.opacity=1;e.style.transform='none'})})")
        pg.goto('http://127.0.0.1:8768/index.html?nolabel'); pg.wait_for_timeout(2500)
        pg.add_style_tag(content='.rv{opacity:1!important;transform:none!important}')
        for i in ids:
            pg.evaluate("document.getElementById('%s').scrollIntoView({behavior:'instant'})" % i); pg.wait_for_timeout(900)
            r = pg.evaluate("(()=>{const r=document.getElementById('%s').getBoundingClientRect();return {x:r.x,y:r.y+scrollY,width:r.width,height:Math.min(r.height,3200)}})()" % i)
            pg.screenshot(path=os.path.join(root, 'test', 'v7_%s.png' % i), clip=r, full_page=True); print('shot', i)
        b.close()
finally: srv.terminate()
