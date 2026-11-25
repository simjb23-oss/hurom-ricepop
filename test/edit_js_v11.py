# -*- coding: utf-8 -*-
# 3D r11: ② 부스러기 서랍 → 코드 보관함(바닥 앞) · 피스톤 = 몸통 + 긁개 링 + 떼는 머리 · 열 상자 앞 벽 막힘
import io, os
p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'explode.js')
s = io.open(p, encoding='utf-8').read()
R = [
 ("(앞면 아래엔 ② 부스러기 서랍 앞판 자리를 비움)", "(앞면 맨 아래엔 ② 코드 보관함 덮개 자리를 비움)"),
 ("[[0.84, bodyH], [0, 0.62]].forEach(", "[[0.30, bodyH], [0, 0.12]].forEach("),
 ("const p = box(0.56, 0.22, 0.04, 0.012, M.panel); p.position.set(sg * 0.82, 0.73, D / 2);", "const p = box(0.36, 0.18, 0.04, 0.012, M.panel); p.position.set(sg * 0.92, 0.21, D / 2);"),
 ("· 부스러기 서랍 앞판도 같은 색'", "· 코드 보관함 덮개도 같은 색'"),
 ("— 앞 벽 아래 부스러기 서랍 구멍 · ", "— 앞 벽 막힘 · "),
 ("[0, 0.11, d / 2 - t / 2, w, 0.74, t], [-0.65, -0.37, d / 2 - t / 2, 0.14, 0.22, t], [0.65, -0.37, d / 2 - t / 2, 0.14, 0.22, t]]", "[0, 0, d / 2 - t / 2, w, h, t]]"),
 ("김 구멍 Ø8 × 2 · 앞 아래 서랍 구멍'", "김 구멍 Ø8 × 2 · 앞 벽 막힘'"),
 ("  const piston = cyl(PR, PR, 0.13, M.plate); piston.position.set(cx, 0.125, cz); lower.add(piston);\n  const face = cyl(PR, PR, 0.012, M.heat); face.position.set(cx, 0.19, cz); lower.add(face);",
  "  const piston = cyl(PR, PR, 0.06, M.plate); piston.position.set(cx, 0.09, cz); lower.add(piston);\n  const wiper = cyl(PR + 0.012, PR + 0.012, 0.012, M.dark); wiper.position.set(cx, 0.115, cz); lower.add(wiper);   // 긁개 링\n  const head = cyl(PR, PR, 0.06, M.steel); head.position.set(cx, 0.155, cz); lower.add(head);   // 떼는 머리(1/4 돌려 끼움)\n  const face = cyl(PR, PR, 0.012, M.heat); face.position.set(cx, 0.19, cz); lower.add(face);"),
 ("'⑤ 아래 열판 = 피스톤 Ø49.6 × 3(틀 안 · 틈 0.2) + 받침", "'⑤ 아래 열판 = 피스톤 Ø49.6 × 3(틀 안 · 틈 0.2 · 둘레 긁개 링 · 위에 스테인리스 머리 6t — 1/4 돌려 빼서 씻음) + 받침"),
 ("""// ② 부스러기 서랍(열 상자 바닥 · 앞 아래로 당김)
const panG = new THREE.Group();
const pan = plain(1.2, 0.02, 1.2, M.steel); panG.add(pan);
const panFront = box(1.08, 0.18, 0.06, 0.012, M.panel); panFront.position.set(0, 0.04, 0.58); panG.add(panFront);
const notch = box(0.28, 0.03, 0.02, 0.005, M.dark); notch.position.set(0, 0.04, 0.62); panG.add(notch);
add(panG, V(0, 0.71, 0.46), V(0, 0.71, 2.2), '② 부스러기 서랍 — 열 상자 바닥 · 식은 뒤 앞 아래로 당겨 비움 · 앞판은 옆 패널과 같은 색', 1);""",
 """// ② 코드 보관함(바닥 앞 · 열 상자 밖 · 코드는 뒤 홈으로)
const panG = new THREE.Group();
const pan = plain(1.4, 0.02, 0.5, M.steel); panG.add(pan);
const panFront = box(1.4, 0.18, 0.05, 0.012, M.panel); panFront.position.set(0, 0.09, 0.27); panG.add(panFront);
const notch = box(0.28, 0.03, 0.02, 0.005, M.dark); notch.position.set(0, 0.09, 0.30); panG.add(notch);
[0.20, 0.16, 0.12].forEach((r, k) => { const c = new THREE.Mesh(new THREE.TorusGeometry(r, 0.018, 8, 40), M.dark); c.rotation.x = Math.PI / 2; c.scale.set(2.2, 1, 1); c.position.set(0, 0.03 + k * 0.035, 0); panG.add(c); });
add(panG, V(0, 0.13, 0.81), V(0, 0.13, 2.4), '② 코드 보관함 — 맨 아래 앞 · 열 상자 밖 가장 시원한 곳 · 코드를 감아 두고 쓸 땐 뒤 홈으로 · 덮개는 옆 패널과 같은 색', 1);"""),
 ("떼는 것(뚜껑 열림 · 틀판 · 부스러기 서랍)", "떼는 것(뚜껑 열림 · 틀판 · 피스톤 머리 · 코드 보관함)"),
]
for a, b in R:
    assert a in s, a[:60]
    s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8').write(s)
print('ok', s.count('부스러기'))
