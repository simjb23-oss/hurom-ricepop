import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D v4 (기준 구조: 유리 상판 · 위 열판 · 몰드 링 고정, 아래 피스톤만 바닥 모터가 올리고 내림, 창 없음, 물통 없음)
// 부품 번호 ①~⑭ = 2.5D 단면 · 층 분해와 같음. 단위 10cm. 22×22×20cm
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
  window: new THREE.MeshPhysicalMaterial({ color: 0x7fa6c2, roughness: 0.05, transparent: true, opacity: 0.35, envMapIntensity: 1.2, depthWrite: false }),
  clear: new THREE.MeshPhysicalMaterial({ color: 0xdfeefa, roughness: 0.08, transparent: true, opacity: 0.45, envMapIntensity: 1.0, depthWrite: false }),
  rice: new THREE.MeshStandardMaterial({ color: 0xf6f2e6, roughness: 0.9 }),
  steel: new THREE.MeshStandardMaterial({ color: 0xb4b8bc, metalness: 0.6, roughness: 0.5 }),
  plate: new THREE.MeshStandardMaterial({ color: 0x8a8f96, metalness: 0.7, roughness: 0.45 }),
  heat: new THREE.MeshStandardMaterial({ color: 0xd19a3c, metalness: 0.4, roughness: 0.5, emissive: 0x6a4210, emissiveIntensity: 0.35 }),
  mold: new THREE.MeshStandardMaterial({ color: 0xdfe3e6, metalness: 0.3, roughness: 0.55 }),
  cracker: new THREE.MeshStandardMaterial({ color: 0xfff6e6, roughness: 0.95 }),
  dark: new THREE.MeshStandardMaterial({ color: 0x3a3d43, metalness: 0.3, roughness: 0.6 }),
  htr: new THREE.MeshStandardMaterial({ color: 0xc8503c, metalness: 0.3, roughness: 0.5, emissive: 0x7a2a1c, emissiveIntensity: 0.4 }),
  motor: new THREE.MeshStandardMaterial({ color: 0x55585e, metalness: 0.5, roughness: 0.5 }),
  board: new THREE.MeshStandardMaterial({ color: 0x1f6b3a, roughness: 0.6 }),
  guard: new THREE.MeshPhysicalMaterial({ color: 0x2b2f35, roughness: 0.3, transparent: true, opacity: 0.55, depthWrite: false }),
  inner: new THREE.MeshStandardMaterial({ color: 0xf1ede4, roughness: 0.8, transparent: true, opacity: 1 }),
  insul: new THREE.MeshStandardMaterial({ color: 0xe7d9c2, roughness: 0.9, transparent: true, opacity: 1 }),
  weight: new THREE.MeshStandardMaterial({ color: 0x9aa3ad, metalness: 0.6, roughness: 0.5 }),
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

const W = 2.2, D = 2.2, H = 2.0;
// ⑪ 옆 패널(비스포크) — 4면 한 몸 (앞면은 창 · 플랩 · 서랍 자리를 비움)
const panelH = H - 0.26;
const panels = new THREE.Group();
[[0, 0, -D / 2, 0], [W / 2, 0, 0, Math.PI / 2], [-W / 2, 0, 0, Math.PI / 2]].forEach(([x, , z, ry], i) => {
  const p = box(i < 1 ? W : D, panelH, 0.04, 0.012, M.panel); p.position.set(x, panelH / 2, z); p.rotation.y = ry; panels.add(p);
});
[[1.46, panelH], [0.44, 0.50], [0, 0.12]].forEach(([y0, y1]) => { const p = box(W, y1 - y0, 0.04, 0.012, M.panel); p.position.set(0, (y0 + y1) / 2, D / 2); panels.add(p); });
[-1, 1].forEach(sg => { const p = box(0.6, 1.34, 0.04, 0.012, M.panel); p.position.set(sg * (W / 2 - 0.3), 0.79, D / 2); panels.add(p); });
add(panels, V(0, 0, 0), V(0, 0, 2.6), '⑪ 옆 패널 4장 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더)', 3);
// ⑩ 몸체 · 흰 띠 · 바깥 이중 유리 창(앞) · 가림판 플랩
const bodyG = new THREE.Group();
const shell = box(W - 0.08, panelH, D - 0.08, 0.02, M.inner); shell.position.y = panelH / 2; bodyG.add(shell);
const band = box(W, 0.1, D, 0.01, M.band); band.position.y = panelH + 0.05; bodyG.add(band);
const band2 = box(W - 0.02, 0.04, D - 0.02, 0.01, M.band); band2.position.y = panelH + 0.12; bodyG.add(band2);
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, panelH - 0.05, -D / 2 + 0.03); bodyG.add(slit);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 이중벽 공기층 · 뒤 김 슬릿', 3);
// ⑭ 검은 유리 상판(창 없음) + 터치 + 카세트 덮개 (고정)
const glassG = new THREE.Group();
const top = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); glassG.add(top);
[-0.36, -0.24, -0.12].forEach(x => { const d = cyl(0.025, 0.025, 0.01, M.band); d.position.set(x, 0.022, D / 2 - 0.16); glassG.add(d); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(0.1, 0.022, D / 2 - 0.16); glassG.add(digit);
const flap = box(0.7, 0.02, 0.58, 0.005, M.glass); flap.position.set(0.61, 0.03, -0.77); glassG.add(flap);
add(glassG, V(0, H - 0.02, 0), V(0, H + 2.3, 0), '⑭ 검은 불투명 내열 상판(유리 아님) · 숨은 터치 · 상태 불빛 · 카세트 덮개 — 창 없음 · 움직이지 않음', 3);
// ⑫ 곡물 카세트 + 깔때기 + 계량 슬라이드
const cassG = new THREE.Group();
const cass = box(0.56, 0.58, 0.46, 0.02, M.clear); cassG.add(cass);
const rice = box(0.5, 0.3, 0.4, 0.02, M.rice); rice.position.y = -0.08; cassG.add(rice);
add(cassG, V(0.58, H - 0.51, -0.75), V(0.58, H + 1.5, -1.9), '⑫ 곡물 카세트(약 200g · 60장) · 분리 세척', 1);
const slideG = new THREE.Group(); const funnel = box(0.3, 0.26, 0.24, 0.01, M.steel); funnel.position.set(0, 0.16, -0.46); slideG.add(funnel);
slideG.add(box(0.3, 0.06, 0.7, 0.01, M.steel)); const cup = box(0.24, 0.06, 0.14, 0.01, M.dark); cup.position.set(0, 0.0, 0.26); slideG.add(cup);
add(slideG, V(0, 0.83, -0.35), V(1.9, 0.83, -1.1), '⑫ 계량 슬라이드 · 앞머리 컵 3g — 밀어내기 겸용(떡뻥을 슬롯으로 밀고, 컵이 가운데서 낙하)', 3);
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
const slot = new THREE.Mesh(new THREE.BoxGeometry(0.76, 0.22, 0.07), M.dark); slot.position.set(0, -0.14, 0); doorG.add(slot);
const doorOut = box(1.0, 0.96, 0.04, 0.012, M.panel); doorOut.position.set(0, 0.01, 0.58); doorG.add(doorOut);
const flapM = new THREE.Mesh(new THREE.BoxGeometry(0.84, 0.22, 0.02), M.guard); flapM.position.set(0, -0.15, 0.6); doorG.add(flapM);
const slotOut = new THREE.Mesh(new THREE.BoxGeometry(0.84, 0.22, 0.02), M.dark); slotOut.position.set(0, -0.15, 0.58); doorG.add(slotOut);
const hinge = box(0.02, 0.9, 0.02, 0.005, M.dark); hinge.position.set(-0.49, 0.01, 0.6); doorG.add(hinge);
add(doorG, V(0, hbY, 0.05 + 0.47), V(0, hbY, 0.05 + 1.6), '⑬ 앞문 — 겉 패널 + 안쪽 단열판 한 몸 · 배출 슬롯 · 가림판 플랩 · 왼쪽 경첩 · 인터록(식어야 열림)', 1);
// ⑦ 위 열판(고정, 천장 기둥 2)
const upper = new THREE.Group(); upper.add(box(0.96, 0.14, 0.8, 0.02, M.plate)); const uh = box(0.92, 0.02, 0.76, 0.005, M.heat); uh.position.y = -0.08; upper.add(uh);
const uRod = cyl(0.03, 0.03, 1.02, M.htr); uRod.rotation.z = Math.PI / 2; uRod.position.set(0, 0.0, -0.1); upper.add(uRod);
[-0.34, 0.34].forEach(x => { const post = cyl(0.04, 0.04, 0.26, M.steel); post.position.set(x, 0.2, 0); upper.add(post); });
add(upper, V(0, hbY + 0.14, 0.05), V(0, hbY + 1.5, 0.05), '⑦ 위 열판 220°C · 속 시즈 히터 450W(빨강 · 양 끝 단자) · NTC 상한 230°C — 고정', 2);
// ⑥ 몰드 링(위 열판 아래 끼움 · 고정) — 앞문으로 뺌
const moldG = new THREE.Group();
const moldRing = new THREE.Mesh(new THREE.TorusGeometry(0.31, 0.03, 16, 48), M.mold); moldRing.rotation.x = Math.PI / 2; moldG.add(moldRing);
add(moldG, V(0, hbY + 0.02, 0.05), V(0, hbY - 0.25, 1.7), '⑥ 몰드 링 Ø6 · 세라믹 코팅 — 앞문 열고 빼서 씻음', 1);
// ⑤ 아래 열판 = 받침(속 히터) + 피스톤 Ø6 + 히터 면 + 배출 턱 (움직임) + 떡뻥
const lower = new THREE.Group(); lower.add(box(0.96, 0.12, 0.8, 0.02, M.plate));
const piston = cyl(0.3, 0.3, 0.08, M.plate); piston.position.y = 0.10; lower.add(piston);
const face = cyl(0.3, 0.3, 0.02, M.heat); face.position.y = 0.15; lower.add(face);
const cracker = cyl(0.29, 0.29, 0.04, M.cracker); cracker.position.y = 0.18; lower.add(cracker);
const lRod = cyl(0.03, 0.03, 1.02, M.htr); lRod.rotation.z = Math.PI / 2; lRod.position.set(0, 0.0, -0.1); lower.add(lRod);
const chute = box(0.6, 0.02, 0.12, 0.005, M.plate); chute.position.set(0, 0.15, 0.46); lower.add(chute);
add(lower, V(0, hbY - 0.11, 0.05), V(0, hbY - 0.11, 0.05), '⑤ 아래 열판 = 피스톤 Ø6 · 속 시즈 히터 450W · 온도 퓨즈 250°C · 배출 턱(앞) — 이것만 25mm 오르내림', 2);
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
const dfront = box(1.0, 0.32, 0.04, 0.012, M.band); dfront.position.set(0, 0, 0.84); drawerG.add(dfront);
const knob = box(0.3, 0.04, 0.02, 0.008, M.dark); knob.position.set(0, 0.02, 0.87); drawerG.add(knob);
add(drawerG, V(0, 0.27, D / 2 - 0.84), V(0, 0.27, D / 2 + 2.2), '② 부스러기 서랍 — 앞으로 당겨 비움', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.03, 0.8, 1.0, 0.005, M.board), V(-0.95, 1.0, -0.1), V(-2.5, 1.0, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 인터록', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.12, 0), V(0, -1.1, 0), '① 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', 3);

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
  // 단계: 0~.25 겉모습 · .25~.5 떼는 것 · .5~.75 껍데기 투명(열 상자 · 아래 판 움직임) · .75~1 분해
  const s = shown;
  const step = s < .25 ? 0 : s < .5 ? 1 : s < .75 ? 2 : 3;
  stepEls.forEach((e, i) => e.classList.toggle('on', i === step));
  const liftK = ease(THREE.MathUtils.clamp((s - .25) / .25, 0, 1));
  const ghostK = ease(THREE.MathUtils.clamp((s - .5) / .25, 0, 1));
  const expK = ease(THREE.MathUtils.clamp((s - .75) / .25, 0, 1));
  ghostable.forEach(m => { m.opacity = 1 - ghostK * 0.78 + expK * 0.25; m.depthWrite = m.opacity > 0.9; });
  M.inner.opacity = 1 - ghostK * 0.78 - expK * 0.1; M.inner.depthWrite = M.inner.opacity > 0.9;
  M.insul.opacity = 1 - ghostK * 0.85 + expK * 0.5; M.insul.depthWrite = M.insul.opacity > 0.9;
  // 열 상자 단계: 아래 열판 · 몰드 · 토글이 천천히 오르내림(25mm = 0.25)
  const bob = (step === 2 && expK < 0.05) ? (0.5 - 0.5 * Math.cos((performance.now() - t0) / 900)) * 0.25 : 0;
  parts.forEach((p, i) => {
    let k = 0;
    if (p.showAt === 1) k = Math.max(liftK * 0.6, expK);
    else if (p.showAt === 2) k = Math.max(ghostK * 0.25, expK);
    else k = expK;
    p.mesh.position.lerpVectors(p.home, p.away, k);
    if (bob && (p.mesh === lower || p.mesh === linkG) && expK < 0.05 && liftK > 0.98) p.mesh.position.y -= bob;
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
