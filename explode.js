import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D (2026-11-25) — 두꺼운 뚜껑 45mm · 위아래 판 2장 · 얕은 칸 Ø50 × 8 셋(뒤 1 · 앞 2)
// 기준 구조: 뚜껑(떠 있는 뒤 경첩) 안에 위 열판(고정) + 떼는 위 판(볼록 3) + 뚜껑 보, 몸체 안 받침 위에 떼는 아래 판(얕은 칸 3) · 받침째 캠으로 +10 누름 · −9 뻥.
// 앞 갈고리 2 + 잠금 막대 · 양옆 C자 틀. 부품 번호 ①~⑭ = 2.5D 단면 · 층 분해와 같음. 단위 10cm. 22×22×20cm
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
const CELLS = [[0, -0.30], [-0.312, 0.24], [0.312, 0.24]];   // 3칸 중심(x, z) · 뒤 1 · 앞 2 — 2.5D (110,80)(78.8,134)(141.2,134)
const DR = 0.25;
const bodyH = 1.47, bandH = 0.08, lidY0 = 1.66, lidH = 0.45;
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
 [0, bodyH - 0.02, -0.91, W - 0.08, 0.04, 0.38], [0, bodyH - 0.02, 0.91, W - 0.08, 0.04, 0.38], [-0.91, bodyH - 0.02, 0, 0.38, 0.04, 1.44], [0.91, bodyH - 0.02, 0, 0.38, 0.04, 1.44]].forEach(([x, y, z, w, h, d]) => { const m = plain(w, h, d, M.inner); m.position.set(x, y, z); bodyG.add(m); });
// 흰 띠(뚜껑 밑 테): 열 상자 자리는 뚫린 테 4 조각
[[0, -0.91, W, 0.38], [0, 0.91, W, 0.38], [-0.91, 0, 0.38, 1.44], [0.91, 0, 0.38, 1.44]].forEach(([x, z, w, d]) => { const m = box(w, bandH, d, 0.01, M.band); m.position.set(x, bodyH + bandH / 2, z); bodyG.add(m); });
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, 1.32, -D / 2 + 0.03); bodyG.add(slit);
const duct = box(0.28, 0.22, 0.12, 0.01, M.steel); duct.position.set(0, 1.39, -0.78); bodyG.add(duct);
// 앞면: 열림 단추 · 주황 불빛 + 숫자 2 · 앞 테 걸림 구멍 2
const openBtn = box(0.30, 0.10, 0.03, 0.04, M.band); openBtn.position.set(0, 1.17, D / 2 + 0.02); bodyG.add(openBtn);
const amber = cyl(0.015, 0.015, 0.02, M.heat, 12); amber.rotation.x = Math.PI / 2; amber.position.set(-0.12, 0.99, D / 2 + 0.02); bodyG.add(amber);
const digits = box(0.16, 0.06, 0.01, 0.003, M.dark); digits.position.set(0.04, 0.99, D / 2 + 0.02); bodyG.add(digits);
[-0.71, 0.71].forEach(x => { const h = plain(0.06, 0.02, 0.06, M.dark); h.position.set(x, bodyH + bandH + 0.002, 0.90); bodyG.add(h); });
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 앞면(열림 단추 · 주황 불빛 + 숫자 2) · 앞 테 걸림 구멍 2 · 김 덕트 → 뒤 김 슬릿', 3);
// ⑬ 강철 틀 — 바닥판 10t + 양옆 C자 틀 8t(아래 변 · 뒤 변 = 경첩 팔 · 앞 변 = 걸림 귀) + 잠금 막대 · 솔레노이드
const frameG = new THREE.Group();
const fBase = plain(1.72, 0.10, 1.92, M.frame); fBase.position.set(0, 0.17, 0); frameG.add(fBase);
[-0.80, 0.80].forEach(x => {
  const low = plain(0.08, 0.12, 1.92, M.frame); low.position.set(x, 0.28, 0); frameG.add(low);
  const back = plain(0.08, 1.24, 0.14, M.frame); back.position.set(x, 0.96, -0.89); frameG.add(back);
  const front = plain(0.08, 1.24, 0.14, M.frame); front.position.set(x, 0.96, 0.89); frameG.add(front);
  const arm = plain(0.08, 0.24, 0.18, M.frame); arm.position.set(x, 1.62, -0.97); frameG.add(arm);          // 경첩 팔(세로 홈)
  const slot = plain(0.085, 0.12, 0.03, M.dark); slot.position.set(x, 1.62, -1.0); frameG.add(slot);
});
const lockBar = cyl(0.02, 0.02, 1.64, M.dark, 12); lockBar.rotation.z = Math.PI / 2; lockBar.position.set(0, 1.45, 0.90); frameG.add(lockBar);
const sol = box(0.12, 0.10, 0.10, 0.01, M.motor); sol.position.set(-0.92, 1.42, 0.86); frameG.add(sol);
const damper = cyl(0.03, 0.03, 0.20, M.motor, 12); damper.rotation.z = Math.PI / 2; damper.position.set(-0.40, 1.56, -0.94); frameG.add(damper);
add(frameG, V(0, 0, 0), V(-2.3, 0.3, 0), '⑬ 강철 틀 — 바닥판 10t + 양옆 C자 틀 8t × 2(뒤 = 떠 있는 경첩 팔 · 앞 = 걸림 귀) + 잠금 막대 · 솔레노이드 · 댐퍼: 닫으면 뚜껑 보가 경첩 축과 앞 갈고리 2로 이 틀에 걸려, 누르는 힘 2.9~8.8kN이 껍데기 밖으로 나가지 않음', 2);
// ⑧ 열 상자(위 열림) — 144 × 144 × 40 · 뒤 벽 위 김 구멍 2
const hbY = 1.35; // 열 상자 중심 높이(z 115..155)
const heatBox = new THREE.Group();
{
  const w = 1.44, d = 1.44, h = 0.40, t = 0.06;
  const walls = [[0, 0, -d / 2 + t / 2, w, h, t], [-w / 2 + t / 2, 0, 0, t, h, d], [w / 2 - t / 2, 0, 0, t, h, d], [0, -h / 2 + t / 2, 0, w, t, d], [0, 0, d / 2 - t / 2, w, h, t]];
  walls.forEach(([x, y, z, bw, bh, bd]) => { const m = plain(bw, bh, bd, M.insul); m.position.set(x, y, z); heatBox.add(m); });
  [-0.1, 0.1].forEach(x => { const v = cyl(0.04, 0.04, 0.08, M.dark, 16); v.rotation.x = Math.PI / 2; v.position.set(x, 0.14, -d / 2 + t / 2); heatBox.add(v); });
}
add(heatBox, V(0, hbY, 0.0), V(0, hbY + 0.45, 0.0), '⑧ 열 상자 144 × 144 × 40 — 강판 + 단열 · 위 열림(뚜껑이 덮음) · 뒤 벽 위 김 구멍 Ø8 × 2', 2);
// 얕은 접시 · 볼록 = 구의 일부(반지름 R) — 깊이 h · 입구 반지름 r
function cap(r, h, m) {
  const R = (r * r + h * h) / (2 * h), th = Math.asin(r / R);
  const g = new THREE.SphereGeometry(R, 40, 10, 0, Math.PI * 2, 0, th);
  const c = new THREE.Mesh(g, m); c.rotation.x = Math.PI; c.userData.R = R; return c;   // 꼭지가 아래
}
function holedPlate(w, d, t, holes, m) {
  const sh = new THREE.Shape(); sh.moveTo(-w / 2, -d / 2); sh.lineTo(w / 2, -d / 2); sh.lineTo(w / 2, d / 2); sh.lineTo(-w / 2, d / 2); sh.lineTo(-w / 2, -d / 2);
  holes.forEach(([x, z]) => { const hp = new THREE.Path(); hp.absarc(x, -z, DR, 0, Math.PI * 2, false); sh.holes.push(hp); });
  const g = new THREE.ExtrudeGeometry(sh, { depth: t, bevelEnabled: false, curveSegments: 40 });
  const mesh = new THREE.Mesh(g, m); mesh.rotation.x = -Math.PI / 2; return mesh;          // 아래면 y=0 · 윗면 y=t
}
const dishMat = new THREE.MeshStandardMaterial({ color: 0xc9ced3, metalness: 0.5, roughness: 0.45, side: THREE.DoubleSide });
// ⑥ 아래 판 — 알루미늄 124 × 124 × 14 · 얕은 칸 Ø50 × 8 셋 · 손가락 홈 2 · 받침에 얹힘(떼어 씻음)
const trayG = new THREE.Group();
trayG.add(holedPlate(1.24, 1.24, 0.14, CELLS, M.mold));
const crackers = [];
CELLS.forEach(([cx, cz]) => {
  const c = cap(DR, 0.08, dishMat); c.position.set(cx, 0.14 - 0.08 + c.userData.R, cz); trayG.add(c);
  const cracker = cyl(0.23, 0.21, 0.10, M.cracker); cracker.position.set(cx, 0.12, cz); cracker.visible = false; trayG.add(cracker); crackers.push(cracker);
});
[-0.62, 0.62].forEach(x => { const n = plain(0.03, 0.05, 0.16, M.dark); n.position.set(x, 0.09, 0); trayG.add(n); });   // 손가락 홈 2
add(trayG, V(0, 1.39, 0.0), V(0, 2.5, 0.3), '⑥ 아래 판 — 알루미늄 14t · 얕은 칸 Ø50 × 8 셋(뒤 1 · 앞 2 · 둥근 바닥) · 나사 없이 받침에 얹힘 · 테두리보다 2mm 낮음 · 손가락 홈 2로 들어 빼서 씻음', 1);
// ⑭ 뚜껑 = 껍데기(45mm · 아래 8mm는 치마) · 검은 유리 윗면 · ⑬ 뚜껑 보 + 앞 갈고리 2 · ⑧ 단열 · ⑦ 위 열판(고정) — 떠 있는 경첩으로 열림
const lidPivot = new THREE.Group();            // 경첩 축: 몸체 뒤 위(z = −1.00, y = 1.66)
const lidG = new THREE.Group(); lidPivot.add(lidG);
const PZ = 1.00;                                // 경첩에서 몸체 가운데까지
const LB = 1.55 - lidY0;                        // 뚜껑 밑면(경첩 기준)
const lidShell = box(W, 0.33, D, 0.03, M.lid); lidShell.position.set(0, LB + 0.08 + 0.165, PZ); lidG.add(lidShell);
[[0, -1.06, W, 0.08], [0, 1.06, W, 0.08], [-1.06, 0, 0.08, D], [1.06, 0, 0.08, D]].forEach(([x, z, w, d]) => { const k = plain(w, 0.08, d, M.lid); k.position.set(x, LB + 0.04, PZ + z); lidG.add(k); });   // 치마
const lidTop = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); lidTop.position.set(0, LB + 0.43, PZ); lidG.add(lidTop);
const upperHeat = box(1.32, 0.10, 1.32, 0.02, M.plate); upperHeat.position.set(0, LB + 0.19, PZ); lidG.add(upperHeat);
const uRod = cyl(0.03, 0.03, 1.2, M.htr); uRod.rotation.z = Math.PI / 2; uRod.position.set(0, LB + 0.19, PZ - 0.1); lidG.add(uRod);
const ntc = box(0.06, 0.06, 0.08, 0.005, M.dark); ntc.position.set(0.58, LB + 0.19, PZ - 0.5); lidG.add(ntc);
[-0.74, 0.74].forEach(x => { const hk = plain(0.06, 0.16, 0.06, M.steel); hk.position.set(x, LB - 0.06, PZ + 0.90); lidG.add(hk); });   // 앞 갈고리 2
const relBtn = box(0.10, 0.04, 0.03, 0.01, M.dark); relBtn.position.set(0, LB + 0.06, PZ + 0.98); lidG.add(relBtn);                // 위 판 떼는 단추
const hinge = cyl(0.04, 0.04, 1.68, M.dark, 20); hinge.rotation.z = Math.PI / 2; hinge.position.set(0, 0, 0); lidG.add(hinge);    // 경첩 축
add(lidPivot, V(0, lidY0, -PZ), V(0, lidY0 + 2.4, -PZ), '⑭ 뚜껑 45mm — 검은 유리 윗면(아무것도 없음) · 떠 있는 경첩 + 댐퍼(마지막 2cm 수평) · 안에 ⑦ 위 열판 220°C(속 시즈 히터 450W · NTC · 고정) · ⑬ 뚜껑 보 11t + 앞 갈고리 2 · ⑧ 단열 · 위 판 떼는 단추', 1);
const lidIns = plain(1.44, 0.05, 1.44, M.insul); add(lidIns, V(0, LB + 0.265, PZ), V(0, LB + 0.265, PZ), '', 9, lidG);
const bar = plain(1.76, 0.11, 1.96, M.frame); add(bar, V(0, LB + 0.345, PZ), V(0, LB + 0.345, PZ), '', 9, lidG);
// ⑫ 위 판 — 알루미늄 6t · 얕은 볼록 3(높이 6) · 전선 없음 · 뒤 걸이 2 · 앞 걸쇠 · 실리콘 손잡이 2 (뚜껑 안 · 떼어 씻음)
const upperG = new THREE.Group();
upperG.add(box(1.24, 0.06, 1.24, 0.01, M.mold));
CELLS.forEach(([cx, cz]) => { const c = cap(0.22, 0.06, M.mold); c.position.set(cx, -0.03 - 0.06 + c.userData.R, cz); upperG.add(c); });
[-0.54, 0.54].forEach(x => { const t = plain(0.10, 0.06, 0.06, M.dark); t.position.set(x, 0.03, -0.64); upperG.add(t); });                     // 뒤 걸이 2
[-0.32, 0.32].forEach(x => { const t = box(0.16, 0.06, 0.08, 0.02, new THREE.MeshStandardMaterial({ color: 0x8d9096, roughness: 0.9 })); t.position.set(x, -0.01, 0.62); upperG.add(t); });   // 실리콘 손잡이 2
add(upperG, V(0, LB + 0.11, PZ), V(0, LB - 0.6, PZ), '⑫ 위 판 — 알루미늄 6t · 얕은 볼록 3(경첩 쪽 1 · 먼 쪽 2 → 닫으면 뒤 1 · 앞 2) · 전선 없음 · 뒤 걸이 2 + 앞 걸쇠 · 단추 누르고 실리콘 손잡이로 빼서 씻음(50°C 넘으면 단추 잠김)', 1, lidG);
// ⑤ 받침 = 124 × 124 × 12 · 속 시즈 히터 450W · 온도 퓨즈 · 판 감지 — ⑥을 얹고 캠으로 +10 · −9
const lower = new THREE.Group(); lower.add(box(1.24, 0.12, 1.24, 0.02, M.plate));
const lRod = cyl(0.03, 0.03, 1.08, M.htr); lRod.rotation.z = Math.PI / 2; lRod.position.set(0, 0.0, -0.1); lower.add(lRod);
const fuse = box(0.06, 0.08, 0.08, 0.005, M.htr); fuse.position.set(0.56, 0.0, -0.46); lower.add(fuse);
const sense = cyl(0.03, 0.03, 0.02, M.board, 12); sense.position.set(-0.5, 0.065, 0.5); lower.add(sense);
[-0.50, 0.50].forEach(x => { const sp = cyl(0.025, 0.025, 0.06, M.heat); sp.position.set(x, -0.09, 0); lower.add(sp); });
add(lower, V(0, 1.33, 0), V(0, 1.33, 0), '⑤ 받침 12t — 속 시즈 히터 450W · 온도 퓨즈 250°C · 판 감지 자석 스위치(판이 없으면 켜지지 않음) — ⑥ 아래 판을 얹고 캠으로 +10 누름 → −9 뻥', 2);
// ④ 달팽이 캠 + 레버(1:2) + 푸시 로드 + 캠 위치 센서 (바닥 칸)
const camG = new THREE.Group();
const camDisc = cyl(0.17, 0.17, 0.06, M.motor, 36); camDisc.rotation.z = Math.PI / 2; camDisc.position.set(0.2, 0.52, -0.18); camG.add(camDisc);
const camLobe = cyl(0.10, 0.10, 0.06, M.motor, 24); camLobe.rotation.z = Math.PI / 2; camLobe.position.set(0.2, 0.59, -0.16); camG.add(camLobe);
const lever = plain(0.46, 0.04, 0.05, M.motor); lever.position.set(0.21, 0.72, -0.18); camG.add(lever);
const pivot = plain(0.08, 0.50, 0.08, M.frame); pivot.position.set(0.42, 0.47, -0.18); camG.add(pivot);
const rodUp = cyl(0.025, 0.025, 0.55, M.motor); rodUp.position.set(0, 0.995, -0.18); camG.add(rodUp);
const sensor = box(0.08, 0.06, 0.08, 0.005, M.dark); sensor.position.set(-0.06, 0.40, -0.18); camG.add(sensor);
add(camG, V(0, 0, 0), V(-1.6, 0, 0), '④ 달팽이 캠 + 레버(1:2) + 푸시 로드(열 상자 바닥 관통 · 벨로즈) + 캠 위치 센서 — 한 바퀴 = 세 장(올림 10 → 멈춤 8~10초 → 절벽 9 → 제자리)', 2);
// ③ 모터(웜 기어드 · 바닥 오른쪽 · 캠 축 직결)
const motorG = new THREE.Group();
const motor = cyl(0.11, 0.11, 0.34, M.motor); motor.rotation.z = Math.PI / 2; motorG.add(motor);
const shaft = cyl(0.025, 0.025, 0.5, M.motor); shaft.rotation.z = Math.PI / 2; shaft.position.set(-0.42, 0, 0); motorG.add(shaft);
add(motorG, V(0.70, 0.52, -0.18), V(2.3, 0.52, -0.18), '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결 · 정전에도 자기 잠금', 2);
// ② 코드 보관함(바닥 앞 · 열 상자 밖 · 코드는 뒤 홈으로)
const panG = new THREE.Group();
const pan = plain(1.4, 0.02, 0.5, M.steel); panG.add(pan);
const panFront = box(1.4, 0.18, 0.05, 0.012, M.panel); panFront.position.set(0, 0.09, 0.27); panG.add(panFront);
const notch = box(0.28, 0.03, 0.02, 0.005, M.dark); notch.position.set(0, 0.09, 0.30); panG.add(notch);
[0.20, 0.16, 0.12].forEach((r, k) => { const c = new THREE.Mesh(new THREE.TorusGeometry(r, 0.018, 8, 40), M.dark); c.rotation.x = Math.PI / 2; c.scale.set(2.2, 1, 1); c.position.set(0, 0.03 + k * 0.035, 0); panG.add(c); });
add(panG, V(0, 0.13, 0.81), V(0, 0.13, 2.4), '② 코드 보관함 — 맨 아래 앞 · 열 상자 밖 가장 시원한 곳 · 코드를 감아 두고 쓸 땐 뒤 홈으로 · 덮개는 옆 패널과 같은 색', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.03, 0.7, 1.0, 0.005, M.board), V(-0.95, 0.95, -0.1), V(-2.5, 0.95, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 뚜껑 잠금 · 판 감지 · 캠 위치 · 자동 꺼짐', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.09, 0), V(0, -1.1, 0), '① 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', 3);

/* ---------- 라벨 ---------- */
const labelEls = parts.map(p => { if (!p.label) { const e = document.createElement('div'); e.style.display = 'none'; labelLayer.appendChild(e); return e; } const e = document.createElement('div'); e.className = 'xv-label'; e.textContent = p.label; labelLayer.appendChild(e); return e; });

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
  // 단계: 0~.25 겉모습 · .25~.5 떼는 것(뚜껑 열림 · 위 판 · 아래 판 · 코드 보관함) · .5~.75 껍데기 투명(열 상자 · 틀 · 받침 움직임) · .75~1 분해
  const s = shown;
  const step = s < .25 ? 0 : s < .5 ? 1 : s < .75 ? 2 : 3;
  stepEls.forEach((e, i) => e.classList.toggle('on', i === step));
  const liftK = ease(THREE.MathUtils.clamp((s - .25) / .25, 0, 1));
  const ghostK = ease(THREE.MathUtils.clamp((s - .5) / .25, 0, 1));
  const expK = ease(THREE.MathUtils.clamp((s - .75) / .25, 0, 1));
  ghostable.forEach(m => { m.opacity = 1 - ghostK * 0.78 + expK * 0.25; m.depthWrite = m.opacity > 0.9; });
  M.inner.opacity = 1 - ghostK * 0.78 - expK * 0.1; M.inner.depthWrite = M.inner.opacity > 0.9;
  M.insul.opacity = 1 - ghostK * 0.85 + expK * 0.5; M.insul.depthWrite = M.insul.opacity > 0.9;
  // 열 상자 단계: 받침 + 아래 판이 10mm(0.10) 올라갔다 내려옴 · 캠도 같이 돎
  const bob = (step === 2 && expK < 0.05) ? (0.5 - 0.5 * Math.cos((performance.now() - t0) / 900)) * 0.10 : 0;
  camDisc.rotation.x = (performance.now() - t0) / 900;
  // 뚜껑: 떼는 단계에서 뒤 경첩으로 110° 열림 · 열 상자 단계에선 다시 닫힘 · 분해에선 닫힌 채 위로
  const openK = (liftK > 0.98 && ghostK > 0 && expK < 0.05) ? (1 - ghostK) : (expK > 0.05 ? 0 : liftK);
  lidG.rotation.x = -openK * 1.92;
  crackers.forEach(c => { c.visible = step === 1 && liftK > 0.5; });
  parts.forEach((p, i) => {
    let k = 0;
    if (p.showAt === 1) k = Math.max(liftK * 0.6, expK);
    else if (p.showAt === 2) k = Math.max(ghostK * 0.25, expK);
    else k = expK;
    if (p.showAt === 1 && liftK > 0.98 && ghostK > 0 && expK < 0.05) k = 0.6 * (1 - ghostK);   // 열 상자 단계에선 판 두 장 · 보관함을 다시 넣음
    if (p.mesh === lidPivot) k = expK;                                                           // 뚜껑은 회전으로 열리고, 분해에서만 위로
    p.mesh.position.lerpVectors(p.home, p.away, k);
    if (bob && expK < 0.05) {
      if (p.mesh === lower || p.mesh === trayG) p.mesh.position.y += bob;
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
