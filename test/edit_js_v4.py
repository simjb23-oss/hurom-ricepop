# -*- coding: utf-8 -*-
"""explode.js 를 v4 기준 구조로 교체(부품 만들기 구간)"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(root)
p = 'test/gen_iso.py'; s = open(p, encoding='utf-8').read()
s = s.replace('viewBox="0 0 1000 980"', 'viewBox="0 0 1090 980"'); open(p, 'w', encoding='utf-8').write(s)
p = 'explode.js'; s = open(p, encoding='utf-8').read()
i = s.index('const W = 2.2'); j = s.index('/* ---------- 라벨 ---------- */')
new = r'''const W = 2.2, D = 2.2, H = 2.0;
// ⑪ 옆 패널(비스포크) — 4면 한 몸 (앞면은 창 · 플랩 · 서랍 자리를 비움)
const panelH = H - 0.26;
const panels = new THREE.Group();
[[0, 0, -D / 2, 0], [W / 2, 0, 0, Math.PI / 2], [-W / 2, 0, 0, Math.PI / 2]].forEach(([x, , z, ry], i) => {
  const p = box(i < 1 ? W : D, panelH, 0.04, 0.012, M.panel); p.position.set(x, panelH / 2, z); p.rotation.y = ry; panels.add(p);
});
[[1.42, panelH], [0.94, 1.00], [0.44, 0.70], [0, 0.12]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });
[-1, 1].forEach(sg => { const p = box(0.5, 1.3, 0.04, 0.012, M.panel); p.position.set(sg * (W / 2 - 0.25), 0.77, D / 2); panels.add(p); });
add(panels, V(0, 0, 0), V(0, 0, 2.6), '⑪ 옆 패널 4장 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더)', 3);
// ⑩ 몸체 · 흰 띠 · 바깥 이중 유리 창(앞) · 가림판 플랩
const bodyG = new THREE.Group();
const shell = box(W - 0.08, panelH, D - 0.08, 0.02, M.inner); shell.position.y = panelH / 2; bodyG.add(shell);
const band = box(W, 0.1, D, 0.01, M.band); band.position.y = panelH + 0.05; bodyG.add(band);
const band2 = box(W - 0.02, 0.04, D - 0.02, 0.01, M.band); band2.position.y = panelH + 0.12; bodyG.add(band2);
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, panelH - 0.05, -D / 2 + 0.03); bodyG.add(slit);
const outWin = new THREE.Mesh(new THREE.BoxGeometry(1.0, 0.42, 0.03), M.glass); outWin.position.set(0, 1.21, D / 2 + 0.005); bodyG.add(outWin);
const flapM = new THREE.Mesh(new THREE.BoxGeometry(0.88, 0.24, 0.02), M.guard); flapM.position.set(0, 0.82, D / 2 + 0.01); bodyG.add(flapM);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 바깥 이중 유리 창(앞) · 가림판 플랩 · 뒤 김 슬릿', 3);
// ⑭ 검은 유리 상판(창 없음) + 터치 + 카세트 덮개 (고정)
const glassG = new THREE.Group();
const top = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); glassG.add(top);
[-0.3, -0.18].forEach(x => { const d = cyl(0.025, 0.025, 0.01, M.band); d.position.set(x, 0.022, D / 2 - 0.16); glassG.add(d); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(0.0, 0.022, D / 2 - 0.16); glassG.add(digit);
const flap = box(0.7, 0.02, 0.58, 0.005, M.glass); flap.position.set(0.61, 0.03, -0.77); glassG.add(flap);
add(glassG, V(0, H - 0.02, 0), V(0, H + 2.3, 0), '⑭ 검은 강화유리 상판 · 숨은 터치 · 카세트 덮개 — 창 없음 · 움직이지 않음', 3);
// ⑫ 곡물 카세트 + 깔때기 + 계량 슬라이드
const cassG = new THREE.Group();
const cass = box(0.56, 0.58, 0.46, 0.02, M.clear); cassG.add(cass);
const rice = box(0.5, 0.3, 0.4, 0.02, M.rice); rice.position.y = -0.08; cassG.add(rice);
add(cassG, V(0.58, H - 0.51, -0.75), V(0.58, H + 1.5, -1.9), '⑫ 곡물 카세트(약 200g · 60장) · 분리 세척', 1);
const slideG = new THREE.Group(); const funnel = box(0.3, 0.26, 0.24, 0.01, M.steel); funnel.position.set(0, 0.16, -0.46); slideG.add(funnel);
slideG.add(box(0.3, 0.06, 0.7, 0.01, M.steel));
add(slideG, V(0, 0.91, -0.35), V(1.9, 0.91, -1.1), '⑫ 계량 슬라이드 · 한 장 3g — 뒤 벽 틈으로 몰드 위까지', 3);
// ⑧ 열 상자(단열) — 앞면 없음(= 앞문)
const hbY = 0.97; // 열 상자 중심 높이(z 44..150)
const heatBox = new THREE.Group();
{
  const w = 1.32, d = 1.0, h = 1.06, t = 0.06;
  const walls = [[0, 0, -d / 2 + t / 2, w, h, t], [-w / 2 + t / 2, 0, 0, t, h, d], [w / 2 - t / 2, 0, 0, t, h, d], [0, -h / 2 + t / 2, 0, w, t, d], [0, h / 2 - t / 2, 0, w, t, d]];
  walls.forEach(([x, y, z, bw, bh, bd]) => { const m = new THREE.Mesh(new THREE.BoxGeometry(bw, bh, bd), M.insul); m.position.set(x, y, z); heatBox.add(m); });
}
add(heatBox, V(0, hbY, 0.05), V(0, hbY + 0.9, 0.05), '⑧ 열 상자 — 강판 1.5 + 단열 5mm · 앞면은 앞문', 2);
// ⑬ 앞문(열 상자 문) — 안쪽 붕규산 창 · 배출 슬롯 · 왼쪽 경첩 · 인터록
const doorG = new THREE.Group();
const doorP = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.94, 0.06), M.insul); doorG.add(doorP);
const inWin = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.38, 0.07), M.window); inWin.position.set(0, 0.22, 0); doorG.add(inWin);
const slot = new THREE.Mesh(new THREE.BoxGeometry(0.76, 0.22, 0.07), M.dark); slot.position.set(0, -0.14, 0); doorG.add(slot);
add(doorG, V(0, hbY, 0.05 + 0.47), V(0, hbY, 0.05 + 1.5), '⑬ 앞문 — 열 상자 문 · 안쪽 창 · 배출 슬롯 · 인터록(식어야 열림)', 2);
// ⑦ 위 열판(고정, 천장 기둥 2)
const upper = new THREE.Group(); upper.add(box(0.96, 0.14, 0.8, 0.02, M.plate)); const uh = box(0.92, 0.02, 0.76, 0.005, M.heat); uh.position.y = -0.08; upper.add(uh);
[-0.34, 0.34].forEach(x => { const post = cyl(0.04, 0.04, 0.26, M.steel); post.position.set(x, 0.2, 0); upper.add(post); });
add(upper, V(0, hbY + 0.14, 0.05), V(0, hbY + 1.5, 0.05), '⑦ 위 열판 · 200~230°C · 온도 센서 — 고정', 2);
// ⑥ 몰드 링(위 열판 아래 끼움 · 고정) — 앞문으로 뺌
const moldG = new THREE.Group();
const moldRing = new THREE.Mesh(new THREE.TorusGeometry(0.31, 0.03, 16, 48), M.mold); moldRing.rotation.x = Math.PI / 2; moldG.add(moldRing);
add(moldG, V(0, hbY + 0.02, 0.05), V(0, hbY - 0.25, 1.7), '⑥ 몰드 링 Ø6 · 세라믹 코팅 — 앞문 열고 빼서 씻음', 1);
// ⑤ 아래 열판 = 받침 + 피스톤 Ø6 + 히터 면 + 밀대 (움직임) + 떡뻥
const lower = new THREE.Group(); lower.add(box(0.96, 0.12, 0.8, 0.02, M.plate));
const piston = cyl(0.3, 0.3, 0.08, M.plate); piston.position.y = 0.10; lower.add(piston);
const face = cyl(0.3, 0.3, 0.02, M.heat); face.position.y = 0.15; lower.add(face);
const cracker = cyl(0.29, 0.29, 0.04, M.cracker); cracker.position.y = 0.18; lower.add(cracker);
const pusher = box(0.88, 0.14, 0.04, 0.01, M.dark); pusher.position.set(0, 0.13, -0.38); lower.add(pusher);
add(lower, V(0, hbY - 0.11, 0.05), V(0, hbY - 0.11, 0.05), '⑤ 아래 열판 = 피스톤 Ø6 · 온도 퓨즈 · 밀대 — 이것만 25mm 오르내림', 2);
// ④ 토글 링크 · 래치 스프링 · 리밋 2 · 푸시 로드 (열 상자 바닥 아래 칸)
const linkG = new THREE.Group();
const l2 = cyl(0.03, 0.03, 0.26, M.motor); l2.position.set(-0.08, 0, 0); l2.rotation.z = 0.7; linkG.add(l2);
const l3 = cyl(0.03, 0.03, 0.26, M.motor); l3.position.set(0.08, 0, 0); l3.rotation.z = -0.7; linkG.add(l3);
const rodUp = cyl(0.025, 0.025, 0.52, M.motor); rodUp.position.set(0, 0.36, 0); linkG.add(rodUp);
const spring = cyl(0.025, 0.025, 0.2, M.heat); spring.position.set(0.4, 0.02, 0); linkG.add(spring);
[0.04, 0.16].forEach(y => { const sw = box(0.08, 0.06, 0.08, 0.01, M.dark); sw.position.set(0.3, y - 0.08, -0.08); linkG.add(sw); });
add(linkG, V(0, 0.29, -0.1), V(-1.6, 0.29, -0.1), '④ 토글 링크 · 래치 스프링 2~3mm · 리밋 스위치 2 · 푸시 로드', 2);
// ③ 승강 모터(바닥 오른쪽) + 크랭크
const motorG = new THREE.Group();
const motor = cyl(0.12, 0.12, 0.42, M.motor); motor.rotation.z = Math.PI / 2; motorG.add(motor);
const rod1 = cyl(0.025, 0.025, 0.4, M.motor); rod1.rotation.z = Math.PI / 2; rod1.position.set(-0.38, 0, 0); motorG.add(rod1);
add(motorG, V(0.7, 0.27, -0.2), V(2.3, 0.27, -0.2), '③ 승강 모터(웜) — 바닥 오른쪽 · 정전에도 자기 잠금', 2);
// ⑬ 트레이(앞 · 슬롯 아래) — 빼서 씻음
const frontG = new THREE.Group();
frontG.add(box(1.0, 0.04, 0.56, 0.01, M.mold)); const tc = cyl(0.33, 0.33, 0.04, M.cracker); tc.position.set(0, 0.04, 0.06); frontG.add(tc);
add(frontG, V(0, 0.68, D / 2 + 0.2), V(0, 0.68, D / 2 + 2.3), '⑬ 트레이 — 떡뻥이 플랩을 밀고 미끄러져 나옴', 1);
// ② 부스러기 서랍(앞 아래 · 얇게) + 서랍 앞판
const drawerG = new THREE.Group(); const dbox = box(0.8, 0.26, 1.64, 0.02, M.band); dbox.position.set(-0.3, 0, 0); drawerG.add(dbox);
const dfront = box(1.18, 0.32, 0.04, 0.012, M.band); dfront.position.set(-0.15, 0, 0.84); drawerG.add(dfront);
const knob = box(0.3, 0.04, 0.02, 0.008, M.dark); knob.position.set(-0.15, 0.02, 0.87); drawerG.add(knob);
add(drawerG, V(0, 0.27, D / 2 - 0.84), V(0, 0.27, D / 2 + 2.2), '② 부스러기 서랍 — 앞으로 당겨 비움', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.03, 0.8, 1.0, 0.005, M.board), V(-0.95, 1.0, -0.1), V(-2.5, 1.0, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 인터록', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.12, 0), V(0, -1.1, 0), '① 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', 3);

'''
s = s[:i] + new + s[j:]
a = "if (bob && (p.mesh === lower || p.mesh === moldG || p.mesh === linkG) && expK < 0.05 && liftK > 0.98) p.mesh.position.y -= bob;"
assert a in s
s = s.replace(a, "if (bob && (p.mesh === lower || p.mesh === linkG) && expK < 0.05 && liftK > 0.98) p.mesh.position.y -= bob;")
s = s.replace("// 휴롬 쌀참 · 구조 3D (기준 구조: 유리 상판 · 위 열판 고정, 아래 열판만 바닥 모터가 올리고 내림, 물통 없음)",
              "// 휴롬 쌀참 · 구조 3D v4 (기준 구조: 유리 상판 · 위 열판 · 몰드 링 고정, 아래 피스톤만 바닥 모터가 올리고 내림, 창은 앞문, 물통 없음)")
open(p, 'w', encoding='utf-8').write(s); print('js ok')
