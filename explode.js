import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D v2 (2026-11-24)
// 디자인 언어 = 휴롬 식재료 세척기: 네모 큐브 · 검은 강화유리 상판 · 가운데 창 · 유리 아래 얇은 흰 띠 · 숨은 터치
// 단위 10cm. 쌀참 22×22×20cm, 세척기 39×34×32cm(참고로 왼쪽에 둠)
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
  panel: new THREE.MeshPhysicalMaterial({ color: PANEL.black, roughness: 0.5, clearcoat: 0.2, clearcoatRoughness: 0.5, transparent: true, opacity: 1 }),
  band: new THREE.MeshPhysicalMaterial({ color: 0xf7f7f4, roughness: 0.35, clearcoat: 0.4, transparent: true, opacity: 1 }),
  glass: new THREE.MeshPhysicalMaterial({ color: 0x0a0a0d, roughness: 0.05, clearcoat: 1, clearcoatRoughness: 0.03, envMapIntensity: 1.5, transparent: true, opacity: 1 }),
  window: new THREE.MeshPhysicalMaterial({ color: 0x7fa6c2, roughness: 0.05, transparent: true, opacity: 0.35, envMapIntensity: 1.2, depthWrite: false }),
  clear: new THREE.MeshPhysicalMaterial({ color: 0xdfeefa, roughness: 0.08, transparent: true, opacity: 0.45, envMapIntensity: 1.0, depthWrite: false }),
  rice: new THREE.MeshStandardMaterial({ color: 0xf6f2e6, roughness: 0.9 }),
  steel: new THREE.MeshStandardMaterial({ color: 0xb4b8bc, metalness: 0.6, roughness: 0.5 }),
  plate: new THREE.MeshStandardMaterial({ color: 0x8a8f96, metalness: 0.7, roughness: 0.45 }),
  heat: new THREE.MeshStandardMaterial({ color: 0xd19a3c, metalness: 0.4, roughness: 0.5, emissive: 0x6a4210, emissiveIntensity: 0.35 }),
  mold: new THREE.MeshStandardMaterial({ color: 0xdfe3e6, metalness: 0.3, roughness: 0.55 }),
  cracker: new THREE.MeshStandardMaterial({ color: 0xfff6e6, roughness: 0.95 }),
  dark: new THREE.MeshStandardMaterial({ color: 0x3a3d43, metalness: 0.3, roughness: 0.6 }),
  motor: new THREE.MeshStandardMaterial({ color: 0x55585e, metalness: 0.5, roughness: 0.5 }),
  board: new THREE.MeshStandardMaterial({ color: 0x1f6b3a, roughness: 0.6 }),
  guard: new THREE.MeshPhysicalMaterial({ color: 0x2b2f35, roughness: 0.3, transparent: true, opacity: 0.55, depthWrite: false }),
  inner: new THREE.MeshStandardMaterial({ color: 0xf1ede4, roughness: 0.8, transparent: true, opacity: 1 }),
  weight: new THREE.MeshStandardMaterial({ color: 0x9aa3ad, metalness: 0.6, roughness: 0.5 }),
  veg: new THREE.MeshStandardMaterial({ color: 0x7cae5a, roughness: 0.8 }),
};
const ghostable = [M.panel, M.band, M.glass, M.inner];

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

// 치수(단위 10cm): 폭 2.2 · 깊이 2.2 · 높이 2.0. 바닥 y=0
const W = 2.2, D = 2.2, H = 2.0;
// 1 옆 패널(비스포크) — 4면을 한 몸으로(바닥 ~ 띠 아래)
const panelH = H - 0.26;
const panels = new THREE.Group();
[[0, 0, D / 2, 0], [0, 0, -D / 2, 0], [W / 2, 0, 0, Math.PI / 2], [-W / 2, 0, 0, Math.PI / 2]].forEach(([x, , z, ry], i) => {
  const p = box(i < 2 ? W : D, panelH, 0.04, 0.012, M.panel); p.position.set(x, panelH / 2, z); p.rotation.y = ry; panels.add(p);
});
add(panels, V(0, 0, 0), V(0, 0, 2.6), '① 옆 패널 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더)', 3);
// 2 흰 띠 몸체(안쪽 구조체 + 윗 흰 띠)
const bodyG = new THREE.Group();
const shell = box(W - 0.08, panelH, D - 0.08, 0.02, M.inner); shell.position.y = panelH / 2; bodyG.add(shell);
const band = box(W, 0.1, D, 0.01, M.band); band.position.y = panelH + 0.05; bodyG.add(band);
const band2 = box(W - 0.02, 0.04, D - 0.02, 0.01, M.band); band2.position.y = panelH + 0.12; bodyG.add(band2);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '② 몸체 · 흰 띠(이중벽 공기층)', 3);
// 3 검은 유리 상판 + 창 + 터치 점
const glassG = new THREE.Group();
const top = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); glassG.add(top);
const win = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.05, 0.7), M.window); win.position.set(0, 0.002, 0.05); glassG.add(win);
const winFrame = new THREE.Mesh(new THREE.BoxGeometry(0.96, 0.046, 0.76), M.dark); winFrame.position.set(0, -0.004, 0.05); glassG.add(winFrame);
[-0.3, -0.18].forEach(x => { const d = cyl(0.025, 0.025, 0.01, M.band); d.position.set(x, 0.022, D / 2 - 0.16); glassG.add(d); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(0.0, 0.022, D / 2 - 0.16); glassG.add(digit);
const flap = box(0.6, 0.02, 0.36, 0.005, M.glass); flap.position.set(0.55, 0.03, -0.72); glassG.add(flap);
add(glassG, V(0, H - 0.02, 0), V(0, H + 2.3, 0), '③ 검은 강화유리 상판 · 이중 유리 창 · 숨은 터치 · 뒤 덮개', 3);
// 4 곡물 카세트(뒤, 유리 덮개 아래)
const cassG = new THREE.Group();
const cass = box(0.56, 0.5, 0.32, 0.02, M.clear); cassG.add(cass);
const rice = box(0.5, 0.3, 0.26, 0.02, M.rice); rice.position.y = -0.08; cassG.add(rice);
add(cassG, V(0.55, H - 0.32, -0.72), V(0.55, H + 1.5, -1.9), '④ 곡물 카세트(약 200g · 60장) · 분리 세척', 1);
// 4b 물통 · 펌프(뒤 왼쪽)
const tankG = new THREE.Group();
tankG.add(box(0.4, 0.5, 0.32, 0.02, M.clear));
const water = box(0.34, 0.26, 0.26, 0.02, new THREE.MeshStandardMaterial({ color: 0x8fbfe0, transparent: true, opacity: 0.8 })); water.position.y = -0.08; tankG.add(water);
const pump = box(0.24, 0.14, 0.16, 0.02, M.dark); pump.position.set(0, -0.32, 0.12); tankG.add(pump);
add(tankG, V(-0.55, H - 0.32, -0.72), V(-1.3, H + 0.9, -1.6), '⑯ 물통 50mL · 마이크로 펌프 0.5mL/장 · 분리 세척', 1);
// 5 계량 슬라이드
add(box(0.3, 0.05, 0.2, 0.01, M.steel), V(0.3, H - 0.62, -0.5), V(1.8, H - 0.62, -1.1), '⑤ 계량 슬라이드 · 한 장 3g', 3);
// 열 상자(안쪽) — 6 위 열판 · 7 몰드 · 8 아래 열판
const hbY = 0.95; // 열 상자 중심 높이
const upper = new THREE.Group(); upper.add(box(0.9, 0.12, 0.9, 0.02, M.plate)); const uh = box(0.86, 0.02, 0.86, 0.005, M.heat); uh.position.y = -0.07; upper.add(uh);
add(upper, V(0, hbY + 0.2, 0.05), V(0, hbY + 1.5, 0.05), '⑥ 위 열판 · 200~230°C · 온도 센서', 2);
const moldG = new THREE.Group();
const moldRing = new THREE.Mesh(new THREE.TorusGeometry(0.33, 0.07, 16, 48), M.mold); moldRing.rotation.x = Math.PI / 2; moldG.add(moldRing);
const moldBase = cyl(0.33, 0.33, 0.03, M.mold); moldBase.position.y = -0.05; moldG.add(moldBase);
const cracker = cyl(0.29, 0.29, 0.03, M.cracker); cracker.position.y = -0.02; moldG.add(cracker);
add(moldG, V(0, hbY + 0.02, 0.05), V(0, hbY + 0.7, 1.5), '⑦ 몰드 Ø6 · 세라믹 코팅 · 원터치 분리 · 식기세척기', 1);
const lower = new THREE.Group(); lower.add(box(0.9, 0.12, 0.9, 0.02, M.plate)); const lh = box(0.86, 0.02, 0.86, 0.005, M.heat); lh.position.y = 0.07; lower.add(lh);
add(lower, V(0, hbY - 0.16, 0.05), V(0, hbY - 0.16, 0.05), '⑧ 아래 열판 · 온도 퓨즈', 2);
// 9 토글 링크 · 10 모터
const linkG = new THREE.Group();
const l1 = cyl(0.03, 0.03, 0.32, M.motor); l1.position.y = -0.16; linkG.add(l1);
const l2 = cyl(0.03, 0.03, 0.36, M.motor); l2.position.set(-0.1, -0.42, 0); l2.rotation.z = 0.6; linkG.add(l2);
const l3 = cyl(0.03, 0.03, 0.36, M.motor); l3.position.set(0.1, -0.42, 0); l3.rotation.z = -0.6; linkG.add(l3);
add(linkG, V(0, hbY - 0.22, 0.05), V(-1.6, hbY - 0.5, 0.05), '⑨ 토글 링크 · 닫힘 유지 → 천천히 개방', 2);
const motor = cyl(0.14, 0.14, 0.3, M.motor); motor.rotation.z = Math.PI / 2;
add(motor, V(0.45, hbY - 0.6, 0.05), V(1.9, hbY - 0.6, 0.05), '⑩ 기어드 모터', 2);
// 11 가림판 · 12 트레이
add(box(0.8, 0.3, 0.03, 0.01, M.guard), V(0, 0.72, D / 2 + 0.02), V(0, 0.72, D / 2 + 1.7), '⑪ 가림판 — 손이 몰드에 닿지 않게', 3);
const trayG = new THREE.Group(); trayG.add(box(0.8, 0.04, 0.42, 0.01, M.mold)); const tc = cyl(0.27, 0.27, 0.025, M.cracker); tc.position.set(0, 0.03, 0.02); trayG.add(tc);
add(trayG, V(0, 0.56, D / 2 + 0.16), V(0, 0.56, D / 2 + 2.3), '⑫ 트레이 — 떡뻥이 미끄러져 나옴', 3);
// 13 부스러기 서랍
const drawerG = new THREE.Group(); drawerG.add(box(1.4, 0.16, 1.2, 0.02, M.band)); const knob = box(0.3, 0.06, 0.03, 0.01, M.dark); knob.position.set(0, 0, 0.6); drawerG.add(knob);
add(drawerG, V(0, 0.28, 0.1), V(0, 0.28, 2.9), '⑬ 부스러기 서랍 — 앞으로 당겨 비움', 1);
// 14 제어 보드 · 15 바닥 무게판
add(box(0.5, 0.02, 0.9, 0.005, M.board), V(-0.75, 0.6, -0.1), V(-2.4, 0.6, -0.1), '⑭ 제어 보드 · 온도 · 기울기 · 인터록', 3);
add(box(W - 0.2, 0.05, D - 0.2, 0.01, M.weight), V(0, 0.12, 0), V(0, -1.1, 0), '⑮ 바닥 무게판 + 미끄럼 방지 고무', 3);

/* ---------- 참고: 휴롬 식재료 세척기(왼쪽) ---------- */
const washer = new THREE.Group();
{
  const w = 3.9, d = 3.4, h = 3.2;
  const body = box(w, h - 0.3, d, 0.03, new THREE.MeshPhysicalMaterial({ color: 0x1c1c1f, roughness: 0.5, clearcoat: 0.2 })); body.position.y = (h - 0.3) / 2; washer.add(body);
  const b1 = box(w, 0.1, d, 0.01, M.band); b1.position.y = h - 0.25; washer.add(b1);
  const b2 = box(w - 0.02, 0.04, d - 0.02, 0.01, M.band); b2.position.y = h - 0.17; washer.add(b2);
  const g = box(w + 0.02, 0.04, d + 0.02, 0.008, M.glass); g.position.y = h - 0.02; washer.add(g);
  const wn = new THREE.Mesh(new THREE.BoxGeometry(2.4, 0.05, 1.5), M.window); wn.position.set(0, h, -0.1); washer.add(wn);
  const basket = box(2.2, 0.3, 1.3, 0.02, M.clear); basket.position.set(0, h - 0.3, -0.1); washer.add(basket);
  for (let i = 0; i < 6; i++) { const v = new THREE.Mesh(new THREE.SphereGeometry(0.12, 16, 12), i % 2 ? M.veg : M.heat); v.position.set(-0.8 + i * 0.32, h - 0.3, -0.1 + (i % 2) * 0.3); washer.add(v); }
  for (let i = 0; i < 10; i++) { const dt = cyl(0.03, 0.03, 0.01, M.band); dt.position.set(-1.3 + i * 0.29, h + 0.01, d / 2 - 0.3); washer.add(dt); }
}
washer.position.set(-3.5, 0, 0);
if (!Q.has('nowasher')) scene.add(washer);

/* ---------- 라벨 ---------- */
const labelEls = parts.map(p => { const e = document.createElement('div'); e.className = 'xv-label'; e.textContent = p.label; labelLayer.appendChild(e); return e; });

/* ---------- 카메라 · 조작 ---------- */
let yaw = Q.has('ang') ? THREE.MathUtils.degToRad(+Q.get('ang')) : THREE.MathUtils.degToRad(32), pitch = 0.42, dist = 9.5;
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
function frame() {
  resize();
  shown += (progress - shown) * 0.08;
  yaw += (targetYaw - yaw) * 0.1;
  // 단계: 0~.25 세척기 옆 모습 · .25~.5 떼는 것 · .5~.75 껍데기 투명(열 상자) · .75~1 분해
  const s = shown;
  const step = s < .25 ? 0 : s < .5 ? 1 : s < .75 ? 2 : 3;
  stepEls.forEach((e, i) => e.classList.toggle('on', i === step));
  const liftK = ease(THREE.MathUtils.clamp((s - .25) / .25, 0, 1));
  const ghostK = ease(THREE.MathUtils.clamp((s - .5) / .25, 0, 1));
  const expK = ease(THREE.MathUtils.clamp((s - .75) / .25, 0, 1));
  ghostable.forEach(m => { m.opacity = 1 - ghostK * 0.78 + expK * 0.25; m.depthWrite = m.opacity > 0.9; });
  M.inner.opacity = 1 - ghostK * 0.78 - expK * 0.1; M.inner.depthWrite = M.inner.opacity > 0.9;
  parts.forEach((p, i) => {
    let k = 0;
    if (p.showAt === 1) k = Math.max(liftK * 0.6, expK);
    else if (p.showAt === 2) k = Math.max(ghostK * 0.25, expK);
    else k = expK;
    p.mesh.position.lerpVectors(p.home, p.away, k);
    const vis = (p.showAt <= step) && k > 0.3 && !Q.has('nolabel');
    const el = labelEls[i];
    if (vis) {
      tmp.setFromMatrixPosition(p.mesh.matrixWorld).project(camera);
      const x = (tmp.x * .5 + .5) * canvas.clientWidth, y = (-tmp.y * .5 + .5) * canvas.clientHeight;
      el.style.transform = `translate(${x + 10}px,${y - 12 + ((i % 3) - 1) * 20}px)`; el.style.opacity = Math.min(1, (k - .3) * 3);
    } else el.style.opacity = 0;
  });
  // 세척기는 첫 단계에서만 선명, 이후 사라짐
  washer.visible = !Q.has('nowasher') && liftK < 0.98;
    washer.position.x = -3.5 - liftK * 3.0;
  // 카메라: 처음엔 둘을 같이 보게 왼쪽으로 치우침, 분해 땐 메이커 중심
  const noW = Q.has('nowasher');
  const cx = noW ? 0 : THREE.MathUtils.lerp(-2.0, 0, liftK), cd = (noW ? 10.5 : THREE.MathUtils.lerp(17.5, 10.5, liftK)) + expK * 6.5;
  const cy = THREE.MathUtils.lerp(1.5, 1.0, liftK) + expK * 1.0;
  camera.position.set(cx + Math.sin(yaw) * Math.cos(pitch) * cd, cy + Math.sin(pitch) * cd, Math.cos(yaw) * Math.cos(pitch) * cd);
  camera.lookAt(cx, cy - 0.2 + expK * 0.2, 0);
  renderer.render(scene, camera);
  requestAnimationFrame(frame);
}
updateProgress(); frame();
