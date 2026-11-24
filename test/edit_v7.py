# -*- coding: utf-8 -*-
"""쌀참 r7 조립 — index.html = <head>(CSS 그대로) + test/body_v7.html(새 본문, SVG 4장 삽입) + GSAP 꼬리. README 에 r7 줄."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(root)
s = open('index.html', encoding='utf-8').read()
head = s[:s.index('<body>') + len('<body>\n')]
tail = s[s.index('<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js">'):]
body = open('test/body_v7.html', encoding='utf-8').read()
for key, name in [('{{CUT}}', 'iso_cut'), ('{{SEQ}}', 'iso_seq'), ('{{EXP}}', 'iso_explode'), ('{{HEAT}}', 'iso_heat')]:
    svg = open('test/%s.svg' % name, encoding='utf-8').read()
    assert body.count(key) == 1, key
    body = body.replace(key, svg)
out = head + body + tail
for bad in ['카세트', '슬라이드', '슬롯', '플랩', '앞문', '불려', '불림', '불린', '칩 몰드', '접시', '열선', '2~3mm', '25mm', '몰드 링', '190°C', '200~230', '깔때기', '밀대', '물통']:
    n = out.count(bad)
    if n: print('남음', bad, n, [out[max(0, i - 40):i + 40].replace('\n', ' ') for i in [out.find(bad)]])
    # 남은 것은 모두 「검토로 바뀐 것」 · 「다음 단계」 설명 안(옛 구조를 왜 뺐는지)
open('index.html', 'w', encoding='utf-8').write(out); print('index.html ok', len(out))
m = 'README.md'; t = open(m, encoding='utf-8').read()
line = "- r7(2026-11-25): 몰드 서랍 구조 — 카세트 · 깔때기 · 계량 컵 · 슬라이드 · 배출 슬롯 · 플랩 · 트레이 · 앞문 삭제. 마른 쌀 3g을 ⑫ 계량 숟가락으로 ⑥ 서랍 트레이(Ø6 오목 틀 15mm)에 넣고 밀어 넣음 → ⑤ 피스톤이 트레이째 20mm 올려 ⑦ 플러그(Ø59)가 13.5mm 들어가 누름 → 8~10mm 순간 하강(두께 8~10mm) → 천천히 → 서랍 잠금 해제 → 빼서 꺼냄. ⑬ ㅁ자 강철 틀(힘 길) · ⑧ 뒤 벽 김 구멍 → ⑩ 덕트 → 슬릿(김 길) · 칩 모드는 다음 단계. 2.5D test/gen_iso_v7.py · 본문 test/body_v7.html + edit_v7.py · 3D explode.js v7. 실사 8장은 옛 구조라 내림(재생성 예정).\n"
k = t.index('- r6:'); e = t.index('\n', k) + 1
t = t[:e] + line + t[e:]
open(m, 'w', encoding='utf-8').write(t); print('README ok')
