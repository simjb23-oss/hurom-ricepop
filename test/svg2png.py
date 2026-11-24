import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright
here = os.path.dirname(os.path.abspath(__file__))
names = sys.argv[1:] or ['iso_cut', 'iso_explode', 'iso_seq']
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1300, 'height': 1000})
    for n in names:
        svg = open(os.path.join(here, n + '.svg'), encoding='utf-8').read()
        pg.set_content('<html><head><link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@2.0/nanumsquare.css"></head><body style="margin:0;background:#fff"><div style="width:1240px;padding:20px">' + svg + '</div></body></html>')
        pg.wait_for_timeout(1500)
        el = pg.query_selector('svg'); el.screenshot(path=os.path.join(here, n + '.png')); print('png', n)
    b.close()
