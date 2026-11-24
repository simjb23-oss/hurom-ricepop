import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D v7b (2026-11-25) — 몰드 서랍 구조 · 윗보 12 × 80 · 개스킷 · 펴개 숟가락
// 기준 구조: 검은 상판 · 위 열판 + 플러그 · ㅁ자 강철 틀 고정, 아래 피스톤만 바닥 모터가 20mm 올리고 내림(트레이째), 서랍은 사람이 당김.
// 카세트 · 슬라이드 · 앞문 · 배출 슬롯 · 트레이 없음. 부품 번호 ①~⑭ = 2.5D 단면 · 층 분해와 같음. 단위 10cm. 22×22×20cm
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
  handle: new THREE.MeshStandardMaterial({ color: 0x5a4632, roughness: 0.6 }),
};
const ghostable = [M.panel, M.band, M.glass, M.inner, M.insul];

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
// ⑪ 옆 패널(비스포크) — 4면 한 몸 (앞면은 서랍 앞판 · 부스러기 받침 턱 자리를 비움)
const panelH = H - 0.26;
const panels = new THREE.Group();
[[0, 0, -D / 2, 0], [W / 2, 0, 0, Math.PI / 2], [-W / 2, 0, 0, Math.PI / 2]].forEach(([x, , z, ry], i) => {
  const p = box(i < 1 ? W : D, panelH, 0.04, 0.012, M.panel); p.position.set(x, panelH / 2, z); p.rotation.y = ry; panels.add(p);
});
[[1.18, panelH], [0.58, 0.74], [0, 0.50]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });
[-1, 1].forEach(sg => { const p = box(0.56, 0.44, 0.04, 0.012, M.panel); p.position.set(sg * 0.82, 0.96, D / 2); panels.add(p); const q = box(0.66, 0.08, 0.04, 0.012, M.panel); q.position.set(sg * 0.77, 0.54, D / 2); panels.add(q); });
add(panels, V(0, 0, 0), V(0, 0, 2.6), '⑪ 옆 패널 4장 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더) · 서랍 앞판도 같은 색', 3);
// ⑩ 몸체 · 흰 띠 · 김 덕트 · 뒤 김 슬릿
const bodyG = new THREE.Group();
const shell = box(W - 0.08, panelH, D - 0.08, 0.02, M.inner); shell.position.y = panelH / 2; bodyG.add(shell);
const band = box(W, 0.1, D, 0.01, M.band); band.position.y = panelH + 0.05; bodyG.add(band);
const band2 = box(W - 0.02, 0.04, D - 0.02, 0.01, M.band); band2.position.y = panelH + 0.12; bodyG.add(band2);
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, panelH - 0.05, -D / 2 + 0.03); bodyG.add(slit);
const duct = box(0.28, 0.40, 0.12, 0.01, M.steel); duct.position.set(0, 1.56, -1.0); bodyG.add(duct);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 이중벽 공기층 · 김 덕트 → 뒤 김 슬릿', 3);
// ⑭ 검은 상판(창 없음) + 터치 + 숫자 (고정 · 카세트 덮개 없음)
const glassG = new THREE.Group();
const top = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); glassG.add(top);
[-0.72, -0.56].forEach(x => { const dot = cyl(0.025, 0.025, 0.01, M.band); dot.position.set(x, 0.022, D / 2 - 0.16); glassG.add(dot); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(-0.36, 0.022, D / 2 - 0.16); glassG.add(digit);
add(glassG, V(0, H - 0.02, 0), V(0, H + 2.3, 0), '⑭ 검은 불투명 내열 상판(유리 아님) · 숨은 터치 · 상태 불빛 · 숫자 — 창 없음 · 움직이지 않음', 3);
// ⑬ ㅁ자 강철 틀 — 바닥판(z 14..22) + 기둥 2(x 50..62 · 158..170, z 22..132) + 윗보(z 132..144) 한 몸
const frameG = new THREE.Group();
const fBase = plain(1.2, 0.08, 0.92, M.frame); fBase.position.set(0, 0.18, 0); frameG.add(fBase);
[-0.54, 0.54].forEach(x => { const c = plain(0.12, 1.10, 0.12, M.frame); c.position.set(x, 0.77, -0.06); frameG.add(c); });
const fBeam = plain(1.2, 0.12, 0.80, M.frame); fBeam.position.set(0, 1.38, 0); frameG.add(fBeam);
add(frameG, V(0, 0, 0), V(-2.3, 0.3, 0), '⑬ ㅁ자 강철 틀 — 바닥판 8t · 기둥 12 × 12 두 개 · 윗보 12 × 80(눕힌 강판 · 굽힘 약 52MPa): 누르는 힘 1.4~4.2kN이 이 안에서 닫힘(위 열판은 윗보에, 토글 핀은 바닥판에)', 2);
// ⑧ 열 상자(단열) — 앞 벽에 서랍 구멍(z 76..108) · 받침 구멍 · 뒤 벽 위 김 구멍 2
const hbY = 0.97; // 열 상자 중심 높이(z 44..150)
const heatBox = new THREE.Group();
{
  const w = 1.32, d = 1.0, h = 1.06, t = 0.06;
  const walls = [[0, 0, -d / 2 + t / 2, w, h, t], [-w / 2 + t / 2, 0, 0, t, h, d], [w / 2 - t / 2, 0, 0, t, h, d], [0, -h / 2 + t / 2, 0, w, t, d], [0, h / 2 - t / 2, 0, w, t, d],
    [0, 0.305, d / 2 - t / 2, w, 0.39, t], [0, -0.30, d / 2 - t / 2, w, 0.18, t], [-0.59, -0.05, d / 2 - t / 2, 0.14, 0.32, t], [0.59, -0.05, d / 2 - t / 2, 0.14, 0.32, t]];
  walls.forEach(([x, y, z, bw, bh, bd]) => { const m = plain(bw, bh, bd, M.insul); m.position.set(x, y, z); heatBox.add(m); });
  [-0.1, 0.1].forEach(x => { const v = cyl(0.04, 0.04, 0.08, M.dark, 16); v.rotation.x = Math.PI / 2; v.position.set(x, 0.40, -d / 2 + t / 2); heatBox.add(v); });
}
add(heatBox, V(0, hbY, 0.05), V(0, hbY + 0.9, 0.05), '⑧ 열 상자 — 강판 1.5 + 단열 5mm · 앞 벽에 서랍 구멍 · 뒤 벽 위 김 구멍 Ø8 × 2', 2);
// ⑦ 위 열판(z 118..132) + Ø59 플러그(104.5..118) · 속 시즈 히터 · NTC — 틀 윗보에 고정
const upper = new THREE.Group(); upper.add(box(0.88, 0.14, 0.76, 0.02, M.plate));
const plug = cyl(0.295, 0.295, 0.135, M.plate); plug.position.y = -0.1375; upper.add(plug);
const plugFace = cyl(0.29, 0.29, 0.012, M.heat); plugFace.position.y = -0.205; upper.add(plugFace);
const uRod = cyl(0.03, 0.03, 0.94, M.htr); uRod.rotation.z = Math.PI / 2; uRod.position.set(0, 0.0, -0.1); upper.add(uRod);
const ntc = box(0.06, 0.06, 0.08, 0.005, M.dark); ntc.position.set(0.43, 0.0, -0.26); upper.add(ntc);
add(upper, V(0, 1.25, 0), V(0, 2.45, 0), '⑦ 위 열판 220°C + Ø59 플러그 — 속 시즈 히터 450W(빨강) · NTC 상한 230°C · 틀 윗보에 고정', 2);
// ⑥ 몰드 서랍 — 프레임 바 2 + 뒤 바 + 안쪽 단열판 + 공기층 버팀 2 + 겉 앞판 + 손잡이 + ⑫ 계량 숟가락 (사람이 당김)
const drawerG = new THREE.Group();
[-0.45, 0.45].forEach(x => { const b = plain(0.06, 0.06, 0.88, M.dark); b.position.set(x, 0, 0); drawerG.add(b); });
const rearBar = plain(0.96, 0.06, 0.06, M.dark); rearBar.position.set(0, 0, -0.44); drawerG.add(rearBar);
const innerPl = plain(1.04, 0.32, 0.06, M.insul); innerPl.position.set(0, -0.02, 0.47); drawerG.add(innerPl);
[-0.4, 0.4].forEach(x => { const s = plain(0.04, 0.2, 0.46, M.dark); s.position.set(x, -0.02, 0.76); drawerG.add(s); });
const outerPl = box(1.08, 0.44, 0.08, 0.012, M.panel); outerPl.position.set(0, 0.02, 1.06); drawerG.add(outerPl);
const handle = box(0.68, 0.035, 0.03, 0.01, M.handle); handle.position.set(0, 0.02, 1.115); drawerG.add(handle);
const spoonH = box(0.3, 0.015, 0.03, 0.005, M.steel); spoonH.position.set(-0.3, -0.1, 0.52); drawerG.add(spoonH);
const spoonB = box(0.36, 0.012, 0.16, 0.004, M.steel); spoonB.position.set(0.03, -0.1, 0.52); drawerG.add(spoonB);   // 납작한 펴개 끝(폭 = 틀 지름)
add(drawerG, V(0, 0.94, 0), V(0, 0.94, 1.6), '⑥ 몰드 서랍 — 겉 앞판 + 단열 손잡이 · 46mm 공기층 버팀 · 안쪽 단열판(테두리 실리콘 개스킷) · 레일 프레임 · 잠금(완료 뒤 해제) · ⑫ 계량 겸 펴개 숟가락 클립', 1);
// ⑥ 몰드 트레이 — Ø78 × 18 · 틀 Ø60 × 15 · 플랜지 Ø88 (서랍에서 들어서 분리)
const trayG = new THREE.Group();
const trayBody = cyl(0.39, 0.39, 0.18, M.mold); trayBody.position.y = -0.03; trayG.add(trayBody);
const flange = cyl(0.44, 0.44, 0.06, M.mold); flange.position.y = 0.03; trayG.add(flange);
const cavity = cyl(0.30, 0.30, 0.012, M.cavity); cavity.position.y = 0.062; trayG.add(cavity);
const cracker = cyl(0.29, 0.29, 0.09, M.cracker); cracker.position.y = -0.03; cracker.visible = false; trayG.add(cracker);
add(trayG, V(0, 0.91, 0), V(0, 1.55, 1.6), '⑥ 몰드 트레이 — Ø6 오목 틀 15mm · 세라믹 코팅 · 서랍에서 들어서 씻음(재료가 닿는 유일한 그릇)', 1);
// ⑤ 아래 열판 = 받침(속 히터 · 퓨즈) + 피스톤 Ø70 (20mm 오르내림 · 트레이째 들어 올림)
const lower = new THREE.Group(); lower.add(box(0.80, 0.12, 0.72, 0.02, M.plate));
const piston = cyl(0.35, 0.35, 0.08, M.plate); piston.position.y = 0.10; lower.add(piston);
const face = cyl(0.35, 0.35, 0.012, M.heat); face.position.y = 0.145; lower.add(face);
const lRod = cyl(0.03, 0.03, 0.78, M.htr); lRod.rotation.z = Math.PI / 2; lRod.position.set(0, 0.0, -0.1); lower.add(lRod);
const fuse = box(0.06, 0.08, 0.08, 0.005, M.htr); fuse.position.set(0.43, 0.0, -0.26); lower.add(fuse);
add(lower, V(0, 0.66, 0), V(0, 0.66, 0), '⑤ 아래 열판 = 피스톤 Ø70 · 받침 속 시즈 히터 450W · 온도 퓨즈 250°C — 이것만 20mm 오르내림(트레이째)', 2);
// ④ 토글 링크 · 래치 스프링 · 리밋 2 · 푸시 로드 (바닥 칸 · 핀은 틀 바닥판)
const linkG = new THREE.Group();
const l2 = cyl(0.03, 0.03, 0.26, M.motor); l2.position.set(-0.08, 0, 0); l2.rotation.z = 0.7; linkG.add(l2);
const l3 = cyl(0.03, 0.03, 0.26, M.motor); l3.position.set(0.08, 0, 0); l3.rotation.z = -0.7; linkG.add(l3);
const rodUp = cyl(0.025, 0.025, 0.42, M.motor); rodUp.position.set(0, 0.28, 0); linkG.add(rodUp);
const spring = cyl(0.025, 0.025, 0.18, M.heat); spring.position.set(0.4, 0.02, 0); linkG.add(spring);
[[0.3, -0.06], [0.3, 0.14]].forEach(([x, y]) => { const sw = box(0.08, 0.06, 0.08, 0.005, M.dark); sw.position.set(x, y, 0); linkG.add(sw); });
add(linkG, V(0, 0.33, -0.1), V(-1.6, 0.33, -0.1), '④ 토글 링크 · 래치 스프링 8~10mm · 리밋 스위치 2 · 푸시 로드(열 상자 바닥 관통)', 2);
// ③ 승강 모터(바닥 오른쪽) + 크랭크
const motorG = new THREE.Group();
const motor = cyl(0.11, 0.11, 0.36, M.motor); motor.rotation.z = Math.PI / 2; motorG.add(motor);
const rod1 = cyl(0.025, 0.025, 0.5, M.motor); rod1.rotation.z = Math.PI / 2; rod1.position.set(-0.4, 0, 0); motorG.add(rod1);
add(motorG, V(0.78, 0.32, -0.2), V(2.3, 0.32, -0.2), '③ 승강 모터(웜) — 바닥 오른쪽 · 정전에도 자기 잠금', 2);
// ② 부스러기 받침(열 상자 바닥 · 얇은 스테인리스 · 앞으로 당김)
const panG = new THREE.Group();
const pan = plain(1.18, 0.02, 0.92, M.steel); panG.add(pan);
const panLip = box(0.88, 0.06, 0.04, 0.01, M.steel); panLip.position.set(0, 0.0, 0.58); panG.add(panLip);
add(panG, V(0, 0.53, 0.02), V(0, 0.53, 2.2), '② 부스러기 받침 — 열 상자 바닥 · 식은 뒤 앞으로 당겨 비움', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.03, 0.8, 1.0, 0.005, M.board), V(-0.95, 1.0, -0.1), V(-2.5, 1.0, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 서랍 잠금 · 자동 꺼짐', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.11, 0), V(0, -1.1, 0), '① 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', 3);

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
  // 단계: 0~.25 겉모습 · .25~.5 떼는 것(서랍 · 트레이 · 받침) · .5~.75 껍데기 투명(열 상자 · 틀 · 피스톤 움직임) · .75~1 분해
  const s = shown;
  const step = s < .25 ? 0 : s < .5 ? 1 : s < .75 ? 2 : 3;
  stepEls.forEach((e, i) => e.classList.toggle('on', i === step));
  const liftK = ease(THREE.MathUtils.clamp((s - .25) / .25, 0, 1));
  const ghostK = ease(THREE.MathUtils.clamp((s - .5) / .25, 0, 1));
  const expK = ease(THREE.MathUtils.clamp((s - .75) / .25, 0, 1));
  ghostable.forEach(m => { m.opacity = 1 - ghostK * 0.78 + expK * 0.25; m.depthWrite = m.opacity > 0.9; });
  M.inner.opacity = 1 - ghostK * 0.78 - expK * 0.1; M.inner.depthWrite = M.inner.opacity > 0.9;
  M.insul.opacity = 1 - ghostK * 0.85 + expK * 0.5; M.insul.depthWrite = M.insul.opacity > 0.9;
  // 열 상자 단계: 피스톤이 20mm(0.20) 올라가 트레이를 2mm 뒤부터 같이 들어 올림 · 토글도 같이
  const bob = (step === 2 && expK < 0.05) ? (0.5 - 0.5 * Math.cos((performance.now() - t0) / 900)) * 0.20 : 0;
  cracker.visible = step === 1 && liftK > 0.5;
  parts.forEach((p, i) => {
    let k = 0;
    if (p.showAt === 1) k = Math.max(liftK * 0.6, expK);
    else if (p.showAt === 2) k = Math.max(ghostK * 0.25, expK);
    else k = expK;
    if (p.showAt === 1 && liftK > 0.98 && ghostK > 0 && expK < 0.05) k = 0.6 * (1 - ghostK);   // 열 상자 단계에선 서랍을 다시 닫음
    p.mesh.position.lerpVectors(p.home, p.away, k);
    if (bob && expK < 0.05) {
      if (p.mesh === lower || p.mesh === linkG) p.mesh.position.y += bob;
      if (p.mesh === trayG) p.mesh.position.y += Math.max(0, bob - 0.02);
    }
    const vis = (p.showAt <= step) && k > 0.3 && !Q.has('nolabel');
    const el = labelEls[i];
    if (vis) {
      tmp.setFromMatrixPosition(p.mesh.matrixWorld).project(camera);
      const x = (tmp.x * .5 + .5) * canvas.clientWidth, y = (-tmp.y * .5 + .5) * canvas.clientHeight;
      el.style.transform = `translate(${x + 10}px,${y - 12 + ((i % 3) - 1) * 20}px)`; el.style.opacity = Math.min(1, (k - .3) * 3);
    } else el.style.opacity = 0;
  });
  const cx = 0, cd = 10.5 + expK * 6.5;
  const cy = THREE.MathUtils.lerp(1.3, 1.0, liftK) + expK * 1.0;
  camera.position.set(cx + Math.sin(yaw) * Math.cos(pitch) * cd, cy + Math.sin(pitch) * cd, Math.cos(yaw) * Math.cos(pitch) * cd);
  camera.lookAt(cx, cy - 0.2 + expK * 0.2, 0);
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
updateProgress(); frame();
