import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/addons/geometries/RoundedBoxGeometry.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

// 휴롬 쌀참 · 구조 3D (기준 구조: 유리 상판 · 위 열판 고정, 아래 열판만 바닥 모터가 올리고 내림, 물통 없음)
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
// ⑪ 옆 패널(비스포크) — 4면 한 몸
const panelH = H - 0.26;
const panels = new THREE.Group();
[[0, 0, D / 2, 0], [0, 0, -D / 2, 0], [W / 2, 0, 0, Math.PI / 2], [-W / 2, 0, 0, Math.PI / 2]].forEach(([x, , z, ry], i) => {
  const p = box(i < 2 ? W : D, panelH, 0.04, 0.012, M.panel); p.position.set(x, panelH / 2, z); p.rotation.y = ry; panels.add(p);
});
add(panels, V(0, 0, 0), V(0, 0, 2.6), '⑪ 옆 패널 4장 · 비스포크(블랙 · 화이트 · 크림 · 세이지 · 라벤더)', 3);
// ⑩ 몸체 · 흰 띠
const bodyG = new THREE.Group();
const shell = box(W - 0.08, panelH, D - 0.08, 0.02, M.inner); shell.position.y = panelH / 2; bodyG.add(shell);
const band = box(W, 0.1, D, 0.01, M.band); band.position.y = panelH + 0.05; bodyG.add(band);
const band2 = box(W - 0.02, 0.04, D - 0.02, 0.01, M.band); band2.position.y = panelH + 0.12; bodyG.add(band2);
const slit = box(0.8, 0.03, 0.02, 0.005, M.dark); slit.position.set(0, panelH - 0.05, -D / 2 + 0.03); bodyG.add(slit);
add(bodyG, V(0, 0, 0), V(0, 0, 0), '⑩ 몸체 · 흰 띠 · 이중벽 공기층 · 뒤 김 슬릿', 3);
// ⑭ 검은 유리 상판 + 창 + 터치 + 뒤 덮개 (고정)
const glassG = new THREE.Group();
const top = box(W + 0.02, 0.04, D + 0.02, 0.008, M.glass); glassG.add(top);
const win = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.05, 0.7), M.window); win.position.set(0, 0.002, 0.05); glassG.add(win);
const winFrame = new THREE.Mesh(new THREE.BoxGeometry(0.96, 0.046, 0.76), M.dark); winFrame.position.set(0, -0.004, 0.05); glassG.add(winFrame);
[-0.3, -0.18].forEach(x => { const d = cyl(0.025, 0.025, 0.01, M.band); d.position.set(x, 0.022, D / 2 - 0.16); glassG.add(d); });
const digit = box(0.14, 0.01, 0.06, 0.003, M.band); digit.position.set(0.0, 0.022, D / 2 - 0.16); glassG.add(digit);
const flap = box(0.6, 0.02, 0.36, 0.005, M.glass); flap.position.set(0.55, 0.03, -0.72); glassG.add(flap);
add(glassG, V(0, H - 0.02, 0), V(0, H + 2.3, 0), '⑭ 검은 강화유리 상판 · 이중 유리 창 · 숨은 터치 · 뒤 덮개 — 움직이지 않음', 3);
// ⑫ 곡물 카세트 + 계량 슬라이드
const cassG = new THREE.Group();
const cass = box(0.56, 0.5, 0.32, 0.02, M.clear); cassG.add(cass);
const rice = box(0.5, 0.3, 0.26, 0.02, M.rice); rice.position.y = -0.08; cassG.add(rice);
add(cassG, V(0.55, H - 0.32, -0.72), V(0.55, H + 1.5, -1.9), '⑫ 곡물 카세트(약 200g · 60장) · 분리 세척', 1);
add(box(0.3, 0.05, 0.2, 0.01, M.steel), V(0.3, H - 0.62, -0.5), V(1.8, H - 0.62, -1.1), '⑫ 계량 슬라이드 · 한 장 3g', 3);
// ⑧ 열 상자(단열) — 속이 빈 상자 + 윗판 창
const hbY = 0.95; // 열 상자 중심 높이
const heatBox = new THREE.Group();
{
  const w = 1.32, d = 1.0, h = 1.0, t = 0.06;
  const walls = [[0, 0, -d / 2 + t / 2, w, h, t], [0, 0, d / 2 - t / 2, w, h, t], [-w / 2 + t / 2, 0, 0, t, h, d], [w / 2 - t / 2, 0, 0, t, h, d], [0, -h / 2 + t / 2, 0, w, t, d], [0, h / 2 - t / 2, 0, w, t, d]];
  walls.forEach(([x, y, z, bw, bh, bd]) => { const m = new THREE.Mesh(new THREE.BoxGeometry(bw, bh, bd), M.insul); m.position.set(x, y, z); heatBox.add(m); });
  const iw = new THREE.Mesh(new THREE.BoxGeometry(0.78, 0.02, 0.5), M.window); iw.position.set(0, h / 2 + 0.005, 0.05); heatBox.add(iw);
}
add(heatBox, V(0, hbY, 0.05), V(0, hbY + 0.9, 0.05), '⑧ 열 상자 — 강판 1.5 + 단열 5mm · 안쪽 유리 윗판', 2);
// ⑦ 위 열판(고정, 천장 기둥 2)
const upper = new THREE.Group(); upper.add(box(0.9, 0.12, 0.9, 0.02, M.plate)); const uh = box(0.86, 0.02, 0.86, 0.005, M.heat); uh.position.y = -0.07; upper.add(uh);
[-0.3, 0.3].forEach(x => { const post = cyl(0.03, 0.03, 0.26, M.steel); post.position.set(x, 0.19, 0); upper.add(post); });
add(upper, V(0, hbY + 0.17, 0.05), V(0, hbY + 1.5, 0.05), '⑦ 위 열판 · 200~230°C · 온도 센서 — 고정', 2);
// ⑥ 몰드 + 떡뻥
const moldG = new THREE.Group();
const moldRing = new THREE.Mesh(new THREE.TorusGeometry(0.33, 0.07, 16, 48), M.mold); moldRing.rotation.x = Math.PI / 2; moldG.add(moldRing);
const moldBase = cyl(0.33, 0.33, 0.03, M.mold); moldBase.position.y = -0.05; moldG.add(moldBase);
const cracker = cyl(0.29, 0.29, 0.03, M.cracker); cracker.position.y = -0.02; moldG.add(cracker);
add(moldG, V(0, hbY - 0.02, 0.05), V(0, hbY + 0.7, 1.5), '⑥ 몰드 Ø6 · 세라믹 코팅 · 위로 들면 분리 · 식기세척기', 1);
// ⑤ 아래 열판(움직임)
const lower = new THREE.Group(); lower.add(box(0.9, 0.12, 0.9, 0.02, M.plate)); const lh = box(0.86, 0.02, 0.86, 0.005, M.heat); lh.position.y = 0.07; lower.add(lh);
add(lower, V(0, hbY - 0.2, 0.05), V(0, hbY - 0.2, 0.05), '⑤ 아래 열판 · 온도 퓨즈 — 이것만 25mm 오르내림', 2);
// ④ 토글 링크 · 래치 스프링 · 리밋 2 (아래 판 밑)
const linkG = new THREE.Group();
const l2 = cyl(0.03, 0.03, 0.3, M.motor); l2.position.set(-0.1, -0.1, 0); l2.rotation.z = 0.7; linkG.add(l2);
const l3 = cyl(0.03, 0.03, 0.3, M.motor); l3.position.set(0.1, -0.1, 0); l3.rotation.z = -0.7; linkG.add(l3);
const spring = cyl(0.025, 0.025, 0.22, M.heat); spring.position.set(0.36, -0.1, 0); linkG.add(spring);
[-0.06, -0.2].forEach(y => { const sw = box(0.08, 0.06, 0.08, 0.01, M.dark); sw.position.set(0.5, y, 0.4); linkG.add(sw); });
add(linkG, V(0, hbY - 0.28, 0.05), V(-1.6, hbY - 0.5, 0.05), '④ 토글 링크 · 래치 스프링 2~3mm · 리밋 스위치 2', 2);
// ③ 기어 모터(바닥 오른쪽, 서랍 옆) + 푸시 로드
const motorG = new THREE.Group();
const motor = cyl(0.14, 0.14, 0.4, M.motor); motor.rotation.x = Math.PI / 2; motorG.add(motor);
const rod1 = cyl(0.025, 0.025, 0.5, M.motor); rod1.rotation.z = Math.PI / 2; rod1.position.set(-0.3, 0, 0); motorG.add(rod1);
const rod2 = cyl(0.025, 0.025, 0.3, M.motor); rod2.position.set(-0.55, 0.15, 0); motorG.add(rod2);
add(motorG, V(0.58, 0.3, 0), V(2.2, 0.3, 0), '③ 기어 모터(웜) — 바닥 오른쪽 · 밀대', 2);
// ⑬ 가림판 · 트레이(앞)
const frontG = new THREE.Group();
const guard = box(0.8, 0.3, 0.03, 0.01, M.guard); guard.position.set(0, 0.16, -0.14); frontG.add(guard);
frontG.add(box(0.8, 0.04, 0.42, 0.01, M.mold)); const tc = cyl(0.27, 0.27, 0.025, M.cracker); tc.position.set(0, 0.03, 0.02); frontG.add(tc);
add(frontG, V(0, 0.56, D / 2 + 0.16), V(0, 0.56, D / 2 + 2.3), '⑬ 가림판 · 트레이 — 떡뻥이 미끄러져 나옴', 3);
// ② 부스러기 서랍(왼쪽 · 앞)
const drawerG = new THREE.Group(); drawerG.add(box(1.1, 0.16, 1.2, 0.02, M.band)); const knob = box(0.3, 0.06, 0.03, 0.01, M.dark); knob.position.set(0, 0, 0.6); drawerG.add(knob);
add(drawerG, V(-0.15, 0.28, 0.1), V(-0.15, 0.28, 2.9), '② 부스러기 서랍 — 앞으로 당겨 비움', 1);
// ⑨ 제어 보드 · ① 바닥 무게판
add(box(0.5, 0.02, 0.9, 0.005, M.board), V(-0.75, 0.6, -0.1), V(-2.4, 0.6, -0.1), '⑨ 제어 보드 · 온도 · 기울기 · 인터록', 3);
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
    if (bob && (p.mesh === lower || p.mesh === moldG || p.mesh === linkG) && expK < 0.05 && liftK > 0.98) p.mesh.position.y -= bob;
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
