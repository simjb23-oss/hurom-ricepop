import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D v10 (2026-11-25) — 「뚜껑형 3칸 Ø5 · 틀 고정」 구조 · 캠 구동 · 셀 3(앞 1 · 뒤 2) · 기둥은 열 상자 밖
// 기준 구조: 검은 뚜껑(뒤 경첩) 안에 위 열판 + 플러그 + 윗보, 몸체 안 강철 틀에 틀판(고정 · 들어서 씻음) · 피스톤만 캠으로 오르내림(10 · 9 · 16mm).
// 서랍 트레이 · 토글 · 래치 없음. 부품 번호 ①~⑭ = 2.5D 단면 · 층 분해와 같음. 단위 10cm. 22×22×20cm
// 좌표: x 좌우 · y 위 · z 앞(+). 2.5D(mm) → 3D: x=(x−110)/100, y=z/100, z=(y−110)/100
const canvas = document.getElementById('xv-canvas');
const labelLayer = document.getElementById('xv-labels');
const stepEls = [...document.querySelectorAll('.xv-step')];
const Q = new URLSearchParams(location.search);

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.1;
renderer.outputColorSpace = THREE.SRGBColorSpace;
const scene = new THREE.Scene();
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
scene.add(new THREE.HemisphereLight(0xffffff, 0xe8e0d0, 0.9));
const sun = new THREE.DirectionalLight(0xfff8ee, 1.4); sun.position.set(-3, 9, 6); scene.add(sun);
const fill = new THREE.DirectionalLight(0xffffff, 0.5); fill.position.set(6, 3, 2); scene.add(fill);
const rim = new THREE.DirectionalLight(0xffffff, 0.9); rim.position.set(2, 5, -7); scene.add(rim);
const camera = new THREE.PerspectiveCamera(26, 1, 0.1, 100);

/* ---------- 재질 ---------- */
const PANEL = { black: 0x1c1c1f, white: 0xf4f4f1, cream: 0xeadfc9, sage: 0xa9b8a3, lavender: 0xc3b6d6 };
const M = {
  panel: new THREE.MeshPhysicalMaterial({ color: PANEL.cream, roughness: 0.5, clearcoat: 0.2, clearcoatRoughness: 0.5, transparent: true, opacity: 1 }),
  band: new THREE.MeshPhysicalMaterial({ color: 0xf7f7f4, roughness: 0.35, clearcoat: 0.4, transparent: true, opacity: 1 }),
  lid: new THREE.MeshPhysicalMaterial({ color: 0x1e1e22, roughness: 0.45, clearcoat: 0.35, clearcoatRoughness: 0.3, transparent: true, opacity: 1 }),
  glass: new THREE.MeshPhysicalMaterial({ color: 0x141417, roughness: 0.32, clearcoat: 0.5, clearcoatRoughness: 0.25, envMapIntensity: 1.1, transparent: true, opacity: 1 }),
  rice: new THREE.MeshStandardMaterial({ color: 0xf6f2e6, roughness: 0.9 }),
  steel: new THREE.MeshStandardMaterial({ color: 0xb4b8bc, metalness: 0.6, roughness: 0.5 }),
  frame: new THREE.MeshStandardMaterial({ color: 0x4f5864, metalness: 0.6, roughness: 0.45 }),
  plate: new THREE.MeshStandardMaterial({ color: 0x8a8f96, metalness: 0.7, roughness: 0.45 }),
  heat: new THREE.MeshStandardMaterial({ color: 0xd19a3c, metalness: 0.4, roughness: 0.5, emissive: 0x6a4210, emissiveIntensity: 0.35 }),
  mold: new THREE.MeshStandardMaterial({ color: 0xdfe3e6, metalness: 0.3, roughness: 0.55 }),
  cavity: new THREE.MeshStandardMaterial({ color: 0xb9bec4, metalness: 0.3, roughness: 0.7 }),
  cracker: new THREE.MeshStandardMaterial({ color: 0xfff6e6, roughness: 0.95 }),
  dark: new THREE.MeshStandardMaterial({ color: 0x3a3d43, metalness: 0.3, roughness: 0.6 }),
  htr: new THREE.MeshStandardMaterial({ color: 0xc8503c, metalness: 0.3, roughness: 0.5, emissive: 0x7a2a1c, emissiveIntensity: 0.4 }),
  motor: new THREE.MeshStandardMaterial({ color: 0x55585e, metalness: 0.5, roughness: 0.5 }),
  board: new THREE.MeshStandardMaterial({ color: 0x1f6b3a, roughness: 0.6 }),
  inner: new THREE.MeshStandardMaterial({ color: 0xf1ede4, roughness: 0.8, transparent: true, opacity: 1 }),
  insul: new THREE.MeshStandardMaterial({ color: 0xe7d9c2, roughness: 0.9, transparent: true, opacity: 1 }),
  weight: new THREE.MeshStandardMaterial({ color: 0x9aa3ad, metalness: 0.6, roughness: 0.5 }),
};
const ghostable = [M.panel, M.band, M.lid, M.glass, M.inner, M.insul];

/* ---------- 부품 만들기 ---------- */
const root = new THREE.Group(); scene.add(root);
const parts = []; // {mesh, home, away, label, showAt}
function add(mesh, home, away, label, showAt = 3, group = root) {
  mesh.position.copy(home); group.add(mesh);
  parts.push({ mesh, home: home.clone(), away: away ? away.clone() : home.clone(), label, showAt });
  return mesh;
}
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const box = (w, h, d, r, m) => new THREE.Mesh(new RoundedBoxGeometry(w, h, d, 4, r), m);
const cyl = (rt, rb, h, m, seg = 40) => new THREE.Mesh(new THREE.CylinderGeometry(rt, rb, h, seg), m);
const plain = (w, h, d, m) => new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m);

const W = 2.2, D = 2.2, H = 2.0;
const CELLS = [[0, 0.32], [-0.312, -0.22], [0.312, -0.22]];   // 3칸 중심(x, z) · 앞 1 · 뒤 2 — 2.5D (110,142)(78.8,88)(141.2,88)
const PR = 0.248, CR = 0.31, CRI = 0.25;
const bodyH = 1.50, bandH = 0.08, lidY0 = 1.58, lidH = 0.42;
// ⑪ 옆 패널(비스포크) — 4면 한 몸 (앞면 맨 아래엔 ② 코드 보관함 덮개 자리를 비움)
const panels = new THREE.Group();
[[0, -D / 2, 0], [W / 2, 0, Math.PI / 2], [-W / 2, 0, Math.PI / 2]].forEach(([x, z, ry], i) => {
  const p = box(i < 1 ? W : D, bodyH, 0.04, 0.012, M.panel); p.position.set(x, bodyH / 2, z); p.rotation.y = ry; panels.add(p);
});
[[0.30, bodyH], [0, 0.12]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });
[-1, 1].forEach(sg => { const p = box(0.36, 0.18, 0.04, 0.012, M.panel); p.position.set(sg * 0.92, 0.21, D / 2); panels.add(p); });
add(panels, V(0, 0, 0), V(0, 0, 2.6), '⑪ 옆 패널 4장 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더) · 코드 보관함 덮개도 같은 색', 3);
// ⑩ 몸체 · 흰 띠(뚜껑 밑 테) · 김 덕트 · 뒤 김 슬릿 · 뒤 경첩 받침
const bodyG = new THREE.Group();
// 몸체 속 껍데기: 벽 4 + 바닥 + 윗면 테(열 상자 자리 1.32 × 1.0 은 뚫림)
[[0, bodyH / 2, -D / 2 + 0.06, W - 0.08, bodyH, 0.04], [0, bodyH / 2, D / 2 - 0.06, W - 0.08, bodyH, 0.04], [-W / 2 + 0.06, bodyH / 2, 0, 0.04, bodyH, D - 0.08], [W / 2 - 0.06, bodyH / 2, 0, 0.04, bodyH, D - 0.08], [0, 0.03, 0, W - 0.08, 0.06, D - 0.08],
 [0, bodyH - 0.02, -0.88, W - 0.08, 0.04, 0.44], [0, bodyH - 0.02, 0.88, W - 0.08, 0.04, 0.44], [-0.91, bodyH - 0.02, 0, 0.38, 0.04, 2.12], [0.91, bodyH - 0.02, 0, 0.38, 0.04, 2.12]].forEach(([x, y, z, w, h, d]) => { const m = plain(w, h, d, M.inner); m.position.set(x, y, z); bodyG.add(m); });
// 흰 띠(뚜껑 밑 테): 열 상자 자리는 뚫린 테 4 조각
[[0, -0.88, W, 0.44], [0, 0.88, W, 0.44], [-0.91, 0, 0.38, 2.12], [0.91, 0, 0.38, 2.12]].forEach(([x, z, w, d]) => { const m = box(w, bandH, d, 0.01, M.band); m.position.set(x, bodyH + bandH / 2, z); bodyG.add(m); });
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, 1.42, -D / 2 + 0.03); bodyG.add(slit);
const duct = box(0.28, 0.22, 0.12, 0.01, M.steel); duct.position.set(0, 1.33, -0.56); bodyG.add(duct);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠(뚜껑 밑 테) · 이중벽 공기층 · 김 덕트 → 뒤 김 슬릿', 3);
// ⑬ 강철 틀 — 바닥판 10t(z 12..22) + 기둥 2(x 50..62 · 158..170, z 22..136) + 기둥 머리(136..158) + 잠금 핀 2 · 솔레노이드
const frameG = new THREE.Group();
const fBase = plain(1.72, 0.10, 0.92, M.frame); fBase.position.set(0, 0.17, -0.04); frameG.add(fBase);
[-0.78, 0.78].forEach(x => { const c = plain(0.12, 1.14, 0.12, M.frame); c.position.set(x, 0.79, -0.04); frameG.add(c); });
const pins = [];
[-0.78, 0.78].forEach(x => {
  const h = plain(0.24, 0.30, 0.24, M.frame); h.position.set(x, 1.51, -0.04); frameG.add(h);
  const pin = cyl(0.05, 0.05, 0.32, M.dark, 16); pin.rotation.z = Math.PI / 2; pin.position.set(x, 1.51, -0.04); frameG.add(pin); pins.push(pin);
});
const sol = box(0.10, 0.10, 0.12, 0.01, M.motor); sol.position.set(-0.97, 1.45, -0.08); frameG.add(sol);
add(frameG, V(0, 0, 0), V(-2.3, 0.3, 0), '⑬ 강철 틀 — 바닥판 10t · 기둥 12 × 12 두 개(열 상자 밖) · 기둥 머리 + 잠금 핀 Ø10 × 2(솔레노이드 해제): 뚜껑을 닫으면 뚜껑 윗보가 핀에 걸려 ㅁ자가 되고, 누르는 힘 4.2~8.8kN이 이 안에서만 돎', 2);
// ⑧ 열 상자(위 열림) — 앞 벽 막힘 · 뒤 벽 위 김 구멍 2 · 틀판 턱 + 자리 핀 2
const hbY = 1.10; // 열 상자 중심 높이(z 62..158)
const heatBox = new THREE.Group();
{
  const w = 1.44, d = 1.32, h = 0.96, t = 0.06;
  const walls = [[0, 0, -d / 2 + t / 2, w, h, t], [-w / 2 + t / 2, 0, 0, t, h, d], [w / 2 - t / 2, 0, 0, t, h, d], [0, -h / 2 + t / 2, 0, w, t, d],
    [0, 0, d / 2 - t / 2, w, h, t]];
  walls.forEach(([x, y, z, bw, bh, bd]) => { const m = plain(bw, bh, bd, M.insul); m.position.set(x, y, z); heatBox.add(m); });
  [-0.1, 0.1].forEach(x => { const v = cyl(0.04, 0.04, 0.08, M.dark, 16); v.rotation.x = Math.PI / 2; v.position.set(x, 0.17, -d / 2 + t / 2); heatBox.add(v); });
  [[0, -0.60, 1.32, 0.06], [0, 0.60, 1.32, 0.06], [-0.63, 0, 0.06, 1.26], [0.63, 0, 0.06, 1.26]].forEach(([x, z, bw, bd]) => { const l = plain(bw, 0.04, bd, M.frame); l.position.set(x, 0.04, z); heatBox.add(l); });
}
add(heatBox, V(0, hbY, 0.0), V(0, hbY + 0.9, 0.0), '⑧ 열 상자 144 × 132 — 강판 1.5 + 단열 5mm · 위 열림(뚜껑 안 단열이 덮음) · 틀판 턱 · 뒤 벽 위 김 구멍 Ø8 × 2 · 앞 벽 막힘', 2);
// ⑥ 틀판 — 알루미늄 108 × 82 × 4 + Ø60 × 16 틀(아래로) · 앞 탭 · 자리 핀 구멍 2 (들어서 씻음)
const trayG = new THREE.Group();
const plateMesh = plain(1.24, 0.04, 1.08, M.mold); trayG.add(plateMesh);
const crackers = [];
CELLS.forEach(([cx, cz]) => {
  const hole = cyl(CRI, CRI, 0.045, M.cavity); hole.position.set(cx, 0.0, cz); trayG.add(hole);
  const ringM = new THREE.Mesh(new THREE.CylinderGeometry(CR, CR, 0.16, 48, 1, true), M.mold); ringM.position.set(cx, -0.10, cz); trayG.add(ringM);
  const ringTop = new THREE.Mesh(new THREE.RingGeometry(CRI, CR, 48), M.mold); ringTop.rotation.x = -Math.PI / 2; ringTop.position.set(cx, 0.021, cz); trayG.add(ringTop);
  const cracker = cyl(0.24, 0.24, 0.10, M.cracker); cracker.position.set(cx, 0.0, cz); cracker.visible = false; trayG.add(cracker); crackers.push(cracker);
});
[-0.54, 0.54].forEach(x => { const h = cyl(0.03, 0.03, 0.045, M.dark, 12); h.position.set(x, 0.0, -0.48); trayG.add(h); });   // 안내 핀 구멍 2(뒤)
const tab = box(0.2, 0.03, 0.08, 0.01, M.cavity); tab.position.set(0, 0, 0.58); trayG.add(tab);
add(trayG, V(0, 1.18, 0.0), V(0, 2.9, 0.6), '⑥ 틀판 — Ø50 × 16 틀 3개(삼각) · 세라믹 코팅 · 턱에 얹히고 뚜껑 안내 핀 2로 플러그와 정렬 · 앞 탭 잡고 들어 올려 씻음(틀 바닥 = 피스톤 윗면) · 한 번에 3장', 1);
// ⑦ 위 열판 + 플러그 · ⑬ 뚜껑 윗보 · ⑧ 뚜껑 안 단열 · ⑭ 뚜껑 껍데기 · 상판 · 터치 · 열림 단추 — 한 몸(뒤 경첩으로 열림)
const lidPivot = new THREE.Group();            // 경첩 축: 몸체 뒤 위(z = −1.10, y = 1.58)
const lidG = new THREE.Group(); lidPivot.add(lidG);
const PZ = 1.10;                                // 경첩에서 몸체 가운데까지
const lidShell = box(W, lidH, D, 0.03, M.lid); lidShell.position.set(0, lidH / 2, PZ); lidG.add(lidShell);
const lidTop = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); lidTop.position.set(0, lidH, PZ); lidG.add(lidTop);
[-0.72, -0.56].forEach(x => { const dot = cyl(0.025, 0.025, 0.01, M.band); dot.position.set(x, lidH + 0.022, PZ + D / 2 - 0.16); lidG.add(dot); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(-0.36, lidH + 0.022, PZ + D / 2 - 0.16); lidG.add(digit);
const lidNotch = box(0.40, 0.03, 0.03, 0.01, M.dark); lidNotch.position.set(0, 0.03, PZ + D / 2 + 0.005); lidG.add(lidNotch);   // 앞 손가락 홈
const lidIns = plain(1.44, 0.10, 1.32, M.insul); lidIns.position.set(0, 0.08, PZ - 0.0); lidG.add(lidIns);
const bar = plain(1.76, 0.30, 0.40, M.frame); bar.position.set(0, -0.07, PZ - 0.04); lidG.add(bar);
const upper = box(1.32, 0.14, 1.12, 0.02, M.plate); upper.position.set(0, -0.29, PZ - 0.04); lidG.add(upper);
CELLS.forEach(([cx, cz]) => {
  const plug = cyl(PR, PR, 0.055, M.plate); plug.position.set(cx, -0.3875, PZ + cz); lidG.add(plug);
  const plugFace = cyl(PR - 0.01, PR - 0.01, 0.012, M.heat); plugFace.position.set(cx, -0.41, PZ + cz); lidG.add(plugFace);
});
[-0.54, 0.54].forEach(x => { const gp = cyl(0.025, 0.025, 0.12, M.dark, 12); gp.position.set(x, -0.42, PZ - 0.48); lidG.add(gp); });   // 안내 핀 2(뒤)
const uRod = cyl(0.03, 0.03, 1.2, M.htr); uRod.rotation.z = Math.PI / 2; uRod.position.set(0, -0.29, PZ - 0.1); lidG.add(uRod);
const ntc = box(0.06, 0.06, 0.08, 0.005, M.dark); ntc.position.set(0.58, -0.29, PZ - 0.36); lidG.add(ntc);
const hinge = cyl(0.04, 0.04, 1.0, M.dark, 20); hinge.rotation.z = Math.PI / 2; hinge.position.set(0, 0.02, 0.04); lidG.add(hinge);   // 숨긴 경첩(뚜껑 뒤 안쪽)
add(lidPivot, V(0, lidY0, -PZ), V(0, lidY0 + 2.4, -PZ), '⑭ 뚜껑 — 검은 불투명 내열 상판(터치 · 상태 불빛 · 숫자) · 숨긴 뒤 경첩 · 앞 손가락 홈 · 열림 스위치(열리면 히터 꺼짐) · 안에 ⑦ 위 열판 220°C + Ø49.6 플러그 3 + 안내 핀 2(속 시즈 히터 450W · NTC) · ⑬ 뚜껑 윗보 40 × 30 · ⑧ 단열 10', 1);
// ⑤ 아래 열판 = 받침(속 히터 · 퓨즈) + 피스톤 Ø59.6 × 13 (10 · 9 · 16mm 오르내림) + 되돌림 스프링 2
const lower = new THREE.Group(); lower.add(box(1.20, 0.12, 1.00, 0.02, M.plate));
CELLS.forEach(([cx, cz]) => {
  const piston = cyl(PR, PR, 0.06, M.plate); piston.position.set(cx, 0.09, cz); lower.add(piston);
  const wiper = cyl(PR + 0.012, PR + 0.012, 0.012, M.dark); wiper.position.set(cx, 0.115, cz); lower.add(wiper);   // 긁개 링
  const head = cyl(PR, PR, 0.06, M.steel); head.position.set(cx, 0.155, cz); lower.add(head);   // 떼는 머리(1/4 돌려 끼움)
  const face = cyl(PR, PR, 0.012, M.heat); face.position.set(cx, 0.19, cz); lower.add(face);
});
const lRod = cyl(0.03, 0.03, 1.08, M.htr); lRod.rotation.z = Math.PI / 2; lRod.position.set(0, 0.0, -0.1); lower.add(lRod);
const fuse = box(0.06, 0.08, 0.08, 0.005, M.htr); fuse.position.set(0.56, 0.0, -0.40); lower.add(fuse);
[-0.50, 0.50].forEach(x => { const sp = cyl(0.025, 0.025, 0.12, M.heat); sp.position.set(x, -0.12, -0.06); lower.add(sp); });
add(lower, V(0, 0.86, -0.04), V(0, 0.86, -0.04), '⑤ 아래 열판 = 피스톤 Ø49.6 × 3(틀 안 · 틈 0.2 · 둘레 긁개 링 · 위에 스테인리스 머리 6t — 1/4 돌려 빼서 씻음) + 받침 12t 속 시즈 히터 450W · 온도 퓨즈 250°C — 받침째 캠으로 오르내림(누름 10 · 뻥 9 · 꺼내기 16) · 되돌림 스프링 2', 2);
// ④ 달팽이 캠 + 레버(1:2) + 푸시 로드 + 캠 위치 센서 (바닥 칸)
const camG = new THREE.Group();
const camDisc = cyl(0.17, 0.17, 0.06, M.motor, 36); camDisc.rotation.z = Math.PI / 2; camDisc.position.set(0.2, 0.40, -0.1); camG.add(camDisc);
const camLobe = cyl(0.10, 0.10, 0.06, M.motor, 24); camLobe.rotation.z = Math.PI / 2; camLobe.position.set(0.2, 0.47, -0.08); camG.add(camLobe);
const lever = plain(0.46, 0.04, 0.05, M.motor); lever.position.set(0.21, 0.50, -0.1); camG.add(lever);
const pivot = plain(0.08, 0.30, 0.08, M.frame); pivot.position.set(0.42, 0.37, -0.1); camG.add(pivot);
const rodUp = cyl(0.025, 0.025, 0.30, M.motor); rodUp.position.set(0, 0.65, -0.1); camG.add(rodUp);
const sensor = box(0.08, 0.06, 0.08, 0.005, M.dark); sensor.position.set(-0.06, 0.29, -0.1); camG.add(sensor);
add(camG, V(0, 0, 0), V(-1.6, 0, 0), '④ 달팽이 캠 + 레버(1:2) + 푸시 로드(열 상자 바닥 관통 · 벨로즈) + 캠 위치 센서 — 한 바퀴 = 한 장(올림 10 → 멈춤 → 절벽 9 → 올림 16 → 제자리)', 2);
// ③ 모터(웜 기어드 · 바닥 오른쪽 · 캠 축 직결)
const motorG = new THREE.Group();
const motor = cyl(0.11, 0.11, 0.34, M.motor); motor.rotation.z = Math.PI / 2; motorG.add(motor);
const shaft = cyl(0.025, 0.025, 0.5, M.motor); shaft.rotation.z = Math.PI / 2; shaft.position.set(-0.42, 0, 0); motorG.add(shaft);
add(motorG, V(0.79, 0.38, -0.1), V(2.3, 0.38, -0.1), '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결 · 정전에도 자기 잠금', 2);
// ② 코드 보관함(바닥 앞 · 열 상자 밖 · 코드는 뒤 홈으로)
const panG = new THREE.Group();
const pan = plain(1.4, 0.02, 0.5, M.steel); panG.add(pan);
const panFront = box(1.4, 0.18, 0.05, 0.012, M.panel); panFront.position.set(0, 0.09, 0.27); panG.add(panFront);
const notch = box(0.28, 0.03, 0.02, 0.005, M.dark); notch.position.set(0, 0.09, 0.30); panG.add(notch);
[0.20, 0.16, 0.12].forEach((r, k) => { const c = new THREE.Mesh(new THREE.TorusGeometry(r, 0.018, 8, 40), M.dark); c.rotation.x = Math.PI / 2; c.scale.set(2.2, 1, 1); c.position.set(0, 0.03 + k * 0.035, 0); panG.add(c); });
add(panG, V(0, 0.13, 0.81), V(0, 0.13, 2.4), '② 코드 보관함 — 맨 아래 앞 · 열 상자 밖 가장 시원한 곳 · 코드를 감아 두고 쓸 땐 뒤 홈으로 · 덮개는 옆 패널과 같은 색', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.03, 0.7, 1.0, 0.005, M.board), V(-0.95, 0.95, -0.1), V(-2.5, 0.95, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 뚜껑 잠금 · 캠 위치 · 자동 꺼짐', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.09, 0), V(0, -1.1, 0), '① 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', 3);

/* ---------- 라벨 ---------- */
const labelEls = parts.map(p => { const e = document.createElement('div'); e.className = 'xv-label'; e.textContent = p.label; labelLayer.appendChild(e); return e; });

/* ---------- 카메라 · 조작 ---------- */
let yaw = Q.has('ang') ? THREE.MathUtils.degToRad(+Q.get('ang')) : THREE.MathUtils.degToRad(32), pitch = 0.42;
let targetYaw = yaw, dragging = false, lx = 0, ly = 0;
canvas.addEventListener('pointerdown', e => { dragging = true; lx = e.clientX; ly = e.clientY; canvas.setPointerCapture(e.pointerId); });
canvas.addEventListener('pointermove', e => { if (!dragging) return; targetYaw += (e.clientX - lx) * 0.008; pitch = THREE.MathUtils.clamp(pitch + (e.clientY - ly) * 0.004, 0.08, 1.2); lx = e.clientX; ly = e.clientY; });
canvas.addEventListener('pointerup', () => { dragging = false; });
canvas.addEventListener('pointercancel', () => { dragging = false; });

/* ---------- 스크롤 → 진행도 ---------- */
const sec = document.getElementById('structure');
let progress = Q.has('p') ? +Q.get('p') : 0, shown = progress;
function updateProgress() {
  if (Q.has('p')) return;
  const r = sec.getBoundingClientRect();
  const total = sec.offsetHeight - innerHeight;
  progress = THREE.MathUtils.clamp(-r.top / Math.max(total, 1), 0, 1);
}
addEventListener('scroll', updateProgress, { passive: true });

/* ---------- 색 바꾸기 ---------- */
document.querySelectorAll('[data-xv-color]').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('[data-xv-color]').forEach(x => x.classList.toggle('on', x === b));
  M.panel.color.set(PANEL[b.dataset.xvColor]);
}));
if (Q.has('color') && PANEL[Q.get('color')]) M.panel.color.set(PANEL[Q.get('color')]);

/* ---------- 리사이즈 ---------- */
function resize() {
  const w = canvas.clientWidth, h = canvas.clientHeight;
  if (canvas.width !== w * renderer.getPixelRatio() || canvas.height !== h * renderer.getPixelRatio()) { renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
}
addEventListener('resize', resize);

/* ---------- 렌더 ---------- */
const ease = t => t < .5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
const tmp = new THREE.Vector3();
let t0 = performance.now();
function frame() {
  resize();
  shown += (progress - shown) * 0.08;
  yaw += (targetYaw - yaw) * 0.1;
  // 단계: 0~.25 겉모습 · .25~.5 떼는 것(뚜껑 열림 · 틀판 · 피스톤 머리 · 코드 보관함) · .5~.75 껍데기 투명(열 상자 · 틀 · 피스톤 움직임) · .75~1 분해
  const s = shown;
  const step = s < .25 ? 0 : s < .5 ? 1 : s < .75 ? 2 : 3;
  stepEls.forEach((e, i) => e.classList.toggle('on', i === step));
  const liftK = ease(THREE.MathUtils.clamp((s - .25) / .25, 0, 1));
  const ghostK = ease(THREE.MathUtils.clamp((s - .5) / .25, 0, 1));
  const expK = ease(THREE.MathUtils.clamp((s - .75) / .25, 0, 1));
  ghostable.forEach(m => { m.opacity = 1 - ghostK * 0.78 + expK * 0.25; m.depthWrite = m.opacity > 0.9; });
  M.inner.opacity = 1 - ghostK * 0.78 - expK * 0.1; M.inner.depthWrite = M.inner.opacity > 0.9;
  M.insul.opacity = 1 - ghostK * 0.85 + expK * 0.5; M.insul.depthWrite = M.insul.opacity > 0.9;
  // 열 상자 단계: 피스톤이 10mm(0.10) 올라갔다 내려옴 · 캠도 같이 돎
  const bob = (step === 2 && expK < 0.05) ? (0.5 - 0.5 * Math.cos((performance.now() - t0) / 900)) * 0.10 : 0;
  camDisc.rotation.x = (performance.now() - t0) / 900;
  // 뚜껑: 떼는 단계에서 뒤 경첩으로 110° 열림 · 열 상자 단계에선 다시 닫힘 · 분해에선 닫힌 채 위로
  const openK = (liftK > 0.98 && ghostK > 0 && expK < 0.05) ? (1 - ghostK) : (expK > 0.05 ? 0 : liftK);
  lidG.rotation.x = -openK * 1.92;
  crackers.forEach(c => { c.visible = step === 1 && liftK > 0.5; c.position.y = 0.02 + liftK * 0.06; });
  parts.forEach((p, i) => {
    let k = 0;
    if (p.showAt === 1) k = Math.max(liftK * 0.6, expK);
    else if (p.showAt === 2) k = Math.max(ghostK * 0.25, expK);
    else k = expK;
    if (p.showAt === 1 && liftK > 0.98 && ghostK > 0 && expK < 0.05) k = 0.6 * (1 - ghostK);   // 열 상자 단계에선 틀판 · 서랍을 다시 넣음
    if (p.mesh === lidPivot) k = expK;                                                           // 뚜껑은 회전으로 열리고, 분해에서만 위로
    p.mesh.position.lerpVectors(p.home, p.away, k);
    if (bob && expK < 0.05) {
      if (p.mesh === lower) p.mesh.position.y += bob;
    }
    const vis = (p.showAt <= step) && (k > 0.3 || (p.mesh === lidPivot && openK > 0.3)) && !Q.has('nolabel');
    const el = labelEls[i];
    if (vis) {
      tmp.setFromMatrixPosition(p.mesh.matrixWorld).project(camera);
      const x = (tmp.x * .5 + .5) * canvas.clientWidth, y = (-tmp.y * .5 + .5) * canvas.clientHeight;
      el.style.transform = `translate(${x + 10}px,${y - 12 + ((i % 3) - 1) * 20}px)`; el.style.opacity = Math.min(1, (Math.max(k, p.mesh === lidPivot ? openK : 0) - .3) * 3);
    } else el.style.opacity = 0;
  });
  const cx = 0, cd = 10.5 + expK * 6.5;
  const cy = THREE.MathUtils.lerp(1.3, 1.1, liftK) + expK * 1.0;
  camera.position.set(cx + Math.sin(yaw) * Math.cos(pitch) * cd, cy + Math.sin(pitch) * cd, Math.cos(yaw) * Math.cos(pitch) * cd);
  camera.lookAt(cx, cy - 0.2 + expK * 0.2, 0);
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
updateProgress(); frame();
