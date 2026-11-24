# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(root)
def R(s, a, b):
    assert a in s, 'MISSING ' + a[:60]; return s.replace(a, b)
p = 'test/gen_iso.py'; s = open(p, encoding='utf-8').read()
s = R(s, "위 창 없음(고정 위 열판에 가려 보이지 않음) → 앞문 창(열 상자 문 = 이중 유리 창 + 배출 슬롯). 몰드 링은 앞문으로 뺌.", "창 없음(위 열판이 고정이라 위에서 안 보이고, 앞창도 필요 없음 — 준보 2026-11-24). 앞문 = 겉 패널 + 안쪽 단열판 한 몸(왼쪽 경첩 · 인터록) · 아래에 배출 슬롯. 몰드 링은 앞문으로 뺌.")
s = R(s, "⑬ 앞문(이중 유리 창 · 배출 슬롯 · 가림판 플랩 · 인터록) · 트레이  ⑭ 검은 강화유리 상판 · 터치 · 카세트 덮개(창 없음)", "⑬ 앞문(겉 패널 + 단열판 · 배출 슬롯 · 가림판 플랩 · 인터록) · 트레이  ⑭ 검은 강화유리 상판 · 터치 · 카세트 덮개(창 없음)")
# 단면
s = R(s, "    I.poly([(70, 157, 100), (150, 157, 100), (150, 157, 138), (70, 157, 138)], WIN, '#5c7f96', .8, .45)   # 앞문 창(안쪽 유리)\n", "")
s = R(s, "    I.poly([(60, 220, 100), (160, 220, 100), (160, 220, 142), (60, 220, 142)], SMOKE, '#8a8a90', .8, .35)        # 바깥 창(몸체 앞)\n",
         "    I.line([(60, 220, 50), (160, 220, 50), (160, 220, 146), (60, 220, 146), (60, 220, 50)], '#8a5d12', 1.2, '4 3')   # 앞문 겉 패널(몸체 앞 · 왼쪽 경첩)\n    I.line([(64, 220, 54), (64, 220, 142)], '#8a5d12', 2.2)   # 경첩\n")
s = R(s, "    I.label((110, 157, 119), L, 300, '⑬ 앞문 — 열 상자 문 · 안쪽 붕규산 창', '점선 = 잘라낸 앞 절반 · 여기로 몰드 링을 빼고 열판을 닦음', 'l')\n    I.label((110, 220, 121), L, 356, '바깥 이중 유리 창(몸체 앞) — 부푸는 게 보임', None, 'l')",
         "    I.label((110, 157, 119), L, 300, '⑬ 앞문 안쪽 단열판 — 열 상자 문', '점선 = 잘라낸 앞 절반 · 여기로 몰드 링을 빼고 열판을 닦음', 'l')\n    I.label((110, 220, 130), L, 356, '⑬ 앞문 겉 패널 — 옆 패널과 같은 색 · 왼쪽 경첩', '창 없음 · 식어야 열림(인터록)', 'l')")
s = R(s, "'⑭ 검은 강화유리 상판 · 터치 · 카세트 덮개 — 창 없음', '위 열판이 고정이라 위에선 안 보임 → 창은 앞문에'", "'⑭ 검은 강화유리 상판 · 터치 · 카세트 덮개 — 창 없음', '위 열판이 고정이라 창을 내도 보이지 않음'")
# 분해
s = R(s, "    I.box(50, 196, z + 6, 120, 6, 94, INSUL); I.poly([(70, 202, z + 56), (150, 202, z + 56), (150, 202, z + 94), (70, 202, z + 94)], WIN, '#5c7f96', .8, .9)\n", "    I.box(50, 196, z + 6, 120, 6, 94, INSUL)\n")
s = R(s, "    I.poly([(60, 250, z + 100), (160, 250, z + 100), (160, 250, z + 142), (60, 250, z + 142)], SMOKE, '#8a8a90', .8, .9)\n", "    I.line([(60, 250, z + 50), (160, 250, z + 50), (160, 250, z + 146), (60, 250, z + 146), (60, 250, z + 50)], '#8a5d12', 1.2, '4 3')\n")
s = R(s, "'⑩ 몸체 · 흰 띠 · 김 슬릿 · 바깥 창(앞)'", "'⑩ 몸체 · 흰 띠 · 김 슬릿 · 앞문 자리(점선)'")
s = R(s, "'⑬ 앞문 — 안쪽 창 · 슬롯 · 인터록'", "'⑬ 앞문(안쪽 단열판) · 슬롯 · 인터록'")
# 동작 순서: 창 띠 삭제
s = R(s, "        o.append('<rect x=\"30\" y=\"92\" width=\"8\" height=\"44\" fill=\"#9ec3dd\" stroke=\"#5c7f96\" stroke-width=\".8\"/>')\n", "")
s = R(s, "<text x=\"22\" y=\"126\" font-size=\"9\" fill=\"#5c7f96\" text-anchor=\"middle\">창</text>", "<text x=\"22\" y=\"126\" font-size=\"9\" fill=\"#6a6a70\" text-anchor=\"middle\">문</text>")
open(p, 'w', encoding='utf-8').write(s)
p = 'explode.js'; s = open(p, encoding='utf-8').read()
s = R(s, "[[1.42, panelH], [0.94, 1.00], [0.44, 0.70], [0, 0.12]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });\n[-1, 1].forEach(sg => { const p = box(0.5, 1.3, 0.04, 0.012, M.panel); p.position.set(sg * (W / 2 - 0.25), 0.77, D / 2); panels.add(p); });",
         "[[1.46, panelH], [0.44, 0.50], [0, 0.12]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });\n[-1, 1].forEach(sg => { const p = box(0.6, 1.34, 0.04, 0.012, M.panel); p.position.set(sg * (W / 2 - 0.3), 0.79, D / 2); panels.add(p); });")
s = R(s, "const outWin = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.42, 0.03), M.glass); outWin.position.set(0, 1.21, D / 2 + 0.005); bodyG.add(outWin);\nconst flapM = new THREE.Mesh(new THREE.BoxGeometry(0.88, 0.24, 0.02), M.guard); flapM.position.set(0, 0.82, D / 2 + 0.01); bodyG.add(flapM);\nadd(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 바깥 이중 유리 창(앞) · 가림판 플랩 · 뒤 김 슬릿', 3);",
         "add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 이중벽 공기층 · 뒤 김 슬릿', 3);")
s = R(s, "const inWin = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.38, 0.07), M.window); inWin.position.set(0, 0.22, 0); doorG.add(inWin);\nconst slot = new THREE.Mesh(new THREE.BoxGeometry(0.76, 0.22, 0.07), M.dark); slot.position.set(0, -0.14, 0); doorG.add(slot);\nadd(doorG, V(0, hbY, 0.05 + 0.47), V(0, hbY, 0.05 + 1.5), '⑬ 앞문 — 열 상자 문 · 안쪽 창 · 배출 슬롯 · 인터록(식어야 열림)', 2);",
         "const slot = new THREE.Mesh(new THREE.BoxGeometry(0.76, 0.22, 0.07), M.dark); slot.position.set(0, -0.14, 0); doorG.add(slot);\nconst doorOut = box(1.0, 0.96, 0.04, 0.012, M.panel); doorOut.position.set(0, 0.01, 0.58); doorG.add(doorOut);\nconst flapM = new THREE.Mesh(new THREE.BoxGeometry(0.84, 0.22, 0.02), M.guard); flapM.position.set(0, -0.15, 0.6); doorG.add(flapM);\nconst slotOut = new THREE.Mesh(new THREE.BoxGeometry(0.84, 0.22, 0.02), M.dark); slotOut.position.set(0, -0.15, 0.58); doorG.add(slotOut);\nconst hinge = box(0.02, 0.9, 0.02, 0.005, M.dark); hinge.position.set(-0.49, 0.01, 0.6); doorG.add(hinge);\nadd(doorG, V(0, hbY, 0.05 + 0.47), V(0, hbY, 0.05 + 1.6), '⑬ 앞문 — 겉 패널 + 안쪽 단열판 한 몸 · 배출 슬롯 · 가림판 플랩 · 왼쪽 경첩 · 인터록(식어야 열림)', 1);")
s = R(s, "const dfront = box(1.18, 0.32, 0.04, 0.012, M.band); dfront.position.set(-0.15, 0, 0.84); drawerG.add(dfront);\nconst knob = box(0.3, 0.04, 0.02, 0.008, M.dark); knob.position.set(-0.15, 0.02, 0.87); drawerG.add(knob);",
         "const dfront = box(1.0, 0.32, 0.04, 0.012, M.band); dfront.position.set(0, 0, 0.84); drawerG.add(dfront);\nconst knob = box(0.3, 0.04, 0.02, 0.008, M.dark); knob.position.set(0, 0.02, 0.87); drawerG.add(knob);")
s = R(s, "창은 앞문, 물통 없음)", "창 없음, 물통 없음)")
open(p, 'w', encoding='utf-8').write(s); print('ok')
