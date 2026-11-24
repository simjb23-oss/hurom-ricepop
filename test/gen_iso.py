# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 v4 — 아이소메트릭 단면 · 층 분해 · 동작 순서 5단계 (SVG)
기준 구조(2026-11-24 v4): 유리 상판 · 위 열판 · 몰드 링 고정, 아래 열판(피스톤)만 바닥 모터가 올리고 내림, 물통 없음, 22×22×20cm.
창 없음(위 열판이 고정이라 위에서 안 보이고, 앞창도 필요 없음 — 준보 2026-11-24). 앞문 = 겉 패널 + 안쪽 단열판 한 몸(왼쪽 경첩 · 인터록) · 아래에 배출 슬롯. 몰드 링은 앞문으로 뺌.
좌표(mm): x 0..220 왼→오, y 0..220 뒤→앞, z 0..200 아래→위. 보는 방향 = 앞·오른쪽·위.
부품 번호(모든 그림 · 3D · 본문 공통, 아래→위):
 ① 바닥 무게판 · 고무발 · 기울기 센서  ② 부스러기 서랍(앞 아래)  ③ 승강 모터(웜 · 바닥 오른쪽) · 밀대 모터  ④ 토글 링크 · 래치 스프링 · 리밋 스위치 2 (열 상자 바닥 아래 칸)
 ⑤ 아래 열판 = 피스톤 Ø6(오르내림 25mm) · 온도 퓨즈 · 밀대  ⑥ 몰드 링 Ø6(위 열판 아래 끼움 · 앞문으로 분리) · 칩 몰드(접시)  ⑦ 위 열판(고정 · 천장 기둥 2) · 온도 센서
 ⑧ 열 상자(강판 1.5 + 단열 5mm)  ⑨ 제어 보드  ⑩ 몸체 · 흰 띠 · 공기층 10mm · 뒤 김 슬릿  ⑪ 옆 패널 4장 · 비스포크
 ⑫ 곡물 카세트 200g · 계량 슬라이드 3g(뒤에서 몰드 위로 들어와 떨어뜨리고 돌아감)  ⑬ 앞문(겉 패널 + 단열판 · 배출 슬롯 · 가림판 플랩 · 인터록) · 트레이  ⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛 · 카세트 덮개(창 없음 · 유리 아님)
높이(z): 고무발 6 · 무게판 8..14 · 서랍 · 토글 · 모터 칸 14..44 · 열 상자 44..150 · 카세트 · 보드 · 공기층 150..196 · 상판 196..200
"""
import sys, math
sys.stdout.reconfigure(encoding='utf-8')
C30 = math.cos(math.radians(30)); S30 = 0.5
FONT = 'font-family="NanumSquare, Pretendard, sans-serif"'

def shade(hexc, f):
    hexc = hexc.lstrip('#'); r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
    if f >= 0: r, g, b = [int(v + (255 - v) * f) for v in (r, g, b)]
    else: r, g, b = [int(v * (1 + f)) for v in (r, g, b)]
    return '#%02x%02x%02x' % (r, g, b)

class Iso:
    def __init__(self, scale, ox, oy, cut_y=None):
        self.s = scale; self.ox = ox; self.oy = oy; self.cut = cut_y; self.out = []
    def P(self, x, y, z):
        return (self.ox + (x - y) * C30 * self.s, self.oy + (x + y) * S30 * self.s - z * self.s)
    def pts(self, lst):
        return ' '.join('%.1f,%.1f' % self.P(*p) for p in lst)
    def poly(self, lst, fill, stroke='#2b2b30', sw=0.9, op=1, extra=''):
        self.out.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" opacity="%s" %s/>' % (self.pts(lst), fill, stroke, sw, op, extra))
    def box(self, x0, y0, z0, w, d, h, color, top=None, left=None, right=None, hatch_cut=True, op=1, sw=0.9, stroke='#2b2b30', faces='tlr'):
        y1 = y0 + d; cutface = False
        if self.cut is not None:
            if y0 >= self.cut: return
            if y1 > self.cut: y1 = self.cut; cutface = True
        x1 = x0 + w; z1 = z0 + h
        ct = top or shade(color, .18); cl = left or color; cr = right or shade(color, -.18)
        if 'l' in faces:
            self.poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], cl, stroke, sw, op)
            if cutface and hatch_cut:
                self.poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], 'url(#hatch)', 'none', 0, op)
        if 'r' in faces:
            self.poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], cr, stroke, sw, op)
        if 't' in faces:
            self.poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], ct, stroke, sw, op)
    def cylz(self, cx, cy, z0, r, h, color, seg=24, op=1, sw=0.8):
        """z축 원기둥(옆면 띠 + 윗면 타원). 절단(cut)은 무시하고 통째로 그림"""
        cl = (lambda y: min(y, self.cut)) if self.cut is not None else (lambda y: y)
        top = [(cx + r * math.cos(2 * math.pi * i / seg), cl(cy + r * math.sin(2 * math.pi * i / seg)), z0 + h) for i in range(seg)]
        bot = [(x, y, z0) for (x, y, _) in top]
        # 옆면: 보이는 쪽(앞·오른쪽) 반만
        for i in range(seg):
            a, b = top[i], top[(i + 1) % seg]
            ang = 2 * math.pi * (i + .5) / seg
            # 보는 방향(앞 y+, 오른 x+)을 향한 면만
            if math.cos(ang) + math.sin(ang) > -0.2:
                f = shade(color, -.25 + .3 * (math.cos(ang - math.pi / 4)))
                self.poly([bot[i], bot[(i + 1) % seg], b, a], f, color, 0.3, op)
        self.poly(top, shade(color, .18), '#2b2b30', sw, op)
    def ringz(self, cx, cy, z0, r, ri, h, color, seg=28, op=1):
        """z축 링(바깥 r · 안쪽 ri)"""
        self.cylz(cx, cy, z0, r, h, color, seg, op)
        cl = (lambda y: min(y, self.cut)) if self.cut is not None else (lambda y: y)
        inner = [(cx + ri * math.cos(2 * math.pi * i / seg), cl(cy + ri * math.sin(2 * math.pi * i / seg)), z0 + h) for i in range(seg)]
        self.poly(inner, shade(color, -.35), '#2b2b30', 0.7, op)
    def line(self, lst, stroke='#2b2b30', sw=1.2, dash=None, op=1, cap='round', marker=''):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        self.out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="%s" stroke-linejoin="round" opacity="%s"%s %s/>' % (self.pts(lst), stroke, sw, cap, op, d, marker))
    def ghost_box(self, x0, y0, z0, w, d, h, stroke='#8a8a90', sw=1, dash='5 5'):
        x1, y1, z1 = x0 + w, y0 + d, z0 + h
        E = [((x0, y0, z0), (x1, y0, z0)), ((x1, y0, z0), (x1, y1, z0)), ((x1, y1, z0), (x0, y1, z0)), ((x0, y1, z0), (x0, y0, z0)),
             ((x0, y0, z1), (x1, y0, z1)), ((x1, y0, z1), (x1, y1, z1)), ((x1, y1, z1), (x0, y1, z1)), ((x0, y1, z1), (x0, y0, z1)),
             ((x0, y0, z0), (x0, y0, z1)), ((x1, y0, z0), (x1, y0, z1)), ((x1, y1, z0), (x1, y1, z1)), ((x0, y1, z0), (x0, y1, z1))]
        for a, b in E: self.line([a, b], stroke, sw, dash, .9)
    def text(self, sx, sy, s, size=13, weight=700, fill='#15151a', anchor='start', extra=''):
        self.out.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s" %s>%s</text>' % (sx, sy, size, weight, fill, anchor, extra, s))
    def label(self, p3, sx, sy, s, sub=None, side='r', color='#15151a', dot='#d19a3c'):
        ax, ay = self.P(*p3)
        ex = sx - 8 if side == 'r' else sx + 8
        self.out.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s" stroke="#fff" stroke-width="1.2"/>' % (ax, ay, dot))
        self.out.append('<polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (ax, ay, ex - (14 if side == 'r' else -14), sy - 4, ex, sy - 4))
        self.text(sx, sy, s, 13.5, 800, color, 'start' if side == 'r' else 'end')
        if sub: self.text(sx, sy + 15, sub, 11.5, 600, '#6a6a70', 'start' if side == 'r' else 'end')
    def svg(self):
        return '\n'.join(self.out)

DEFS = '''<defs>
<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="7" stroke="#8a5d12" stroke-width="1.1" opacity=".55"/></pattern>
<linearGradient id="glassT" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a3a40"/><stop offset=".5" stop-color="#101014"/><stop offset="1" stop-color="#2c2c32"/></linearGradient>
<marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d19a3c"/></marker>
<marker id="arrg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6a6a70"/></marker>
</defs>'''

# 색(옆 패널 기본 = 크림)
PANEL = '#ebe4d6'; BODY = '#f4f1ea'; BAND = '#ffffff'; GLASS = '#15151a'; WIN = '#9ec3dd'; STEEL = '#b9bec4'; PLATE = '#8a8f96'
HEAT = '#d19a3c'; MOLD = '#dfe3e6'; CRACK = '#fff3dc'; DARK = '#4a4e55'; MOTOR = '#5a5e66'; BOARD = '#2f7a46'; CLEAR = '#dcecf7'
RICE = '#f3eedf'; INSUL = '#e7d9c2'; RED = '#e06c5a'; SMOKE = '#3a3f47'

# ---- 치수(mm) ----
# 열 상자 ⑧: x 44..176 · y 60..160 · z 44..150 (벽 6 = 강판 1.5 + 단열 5) · 앞면(y 154..160)은 앞문 ⑬
# 위 열판 ⑦(고정): z 104..118, 히터 면 102..104, 천장(z 144)에 기둥 2. 몰드 링 ⑥: Ø60 · z 96..102 · 위 열판 아래 끼움
# 아래 열판 ⑤(움직임): 받침 z 80..92 + 피스톤 Ø60 z 92..100 + 히터 면 100..102 (닫힘 = 피스톤이 링 안으로 6mm) · 열림 = 25mm 아래
# 계량 슬라이드 ⑫: 뒤 벽 틈(z 86..96)으로 들어와 몰드 위(y 110)에서 3g 떨어뜨리고 돌아감
# 앞문 ⑬: y 154..160 · x 50..170 · z 50..144 · 창 x 70..150 z 100..138 · 슬롯 x 72..148 z 72..94 (열린 떡뻥 윗면 87)
# 몸체 앞면: 서랍 앞판 z 12..44 · 트레이 z 66..70(앞으로 56) · 가림판 플랩 z 70..94 · 바깥 창 z 100..142
DOWN = 25
CX, CY = 110, 110

def cutaway():
    I = Iso(1.5, 560, 268, cut_y=110)
    W, D, H = 220, 220, 200
    # ---- 껍데기(뒤 벽 · 바닥 · 왼 벽)
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col)
    I.poly([(70, 8, 172), (150, 8, 172), (150, 8, 180), (70, 8, 180)], '#2b2b30', 'none', 0, .85)   # 뒤 김 슬릿
    # ---- 바닥 칸: 무게판 · 서랍(앞 · 왼) · 토글(가운데) · 모터(오른쪽) · 보드(왼 벽)
    I.box(14, 14, 8, 192, 192, 6, STEEL)                                        # ① 무게판
    I.box(14, 60, 60, 3, 100, 80, BOARD)                                        # ⑨ 제어 보드(왼 벽 · 열 상자 옆)
    I.box(40, 48, 14, 80, 164, 26, BAND, top=shade(BAND, -.06))                # ② 서랍(왼쪽 · 앞까지)
    I.box(158, 70, 14, 44, 40, 24, MOTOR)                                       # ③ 승강 모터(바닥 오른쪽)
    I.line([(158, 90, 26), (130, 100, 26)], MOTOR, 5)                           # 크랭크 → 푸시 로드(가로)
    # ④ 토글 링크(열 상자 바닥 아래 칸, 접힘 = 열린 상태) · 래치 스프링 · 리밋 2
    I.line([(130, 100, 26), (110, 100, 18), (110, 100, 30)], MOTOR, 4.2)
    I.line([(96, 100, 24), (110, 100, 18), (124, 100, 24), (110, 100, 30)], MOTOR, 4.2)
    I.box(140, 96, 16, 8, 8, 6, DARK); I.box(140, 96, 34, 8, 8, 6, DARK)
    I.line([(150, 100, 18), (150, 100, 40)], HEAT, 2.4, '3 2')                 # 래치 스프링
    # ---- 열 상자 뒤 · 왼 · 바닥(푸시 로드 관통)
    I.box(44, 60, 44, 132, 6, 106, INSUL)
    I.box(44, 66, 44, 6, 94, 106, INSUL)
    I.box(50, 66, 44, 120, 94, 6, INSUL, top=shade(INSUL, -.08))
    zb = 80 - DOWN                                                              # 아래 열판 받침 밑면(열림)
    I.line([(110, 100, 30), (110, 100, zb)], MOTOR, 5)                          # 푸시 로드(바닥 관통)
    # ---- 곡물 카세트 · 깔때기 · 계량 슬라이드(뒤 벽 틈으로 몰드 위까지)
    I.box(140, 12, 120, 56, 46, 58, CLEAR, op=.85); I.box(144, 16, 122, 48, 38, 30, RICE)
    I.box(104, 34, 96, 30, 24, 26, STEEL, op=.9)                                # 깔때기(카세트 → 슬라이드)
    I.box(95, 40, 88, 30, 70, 6, STEEL)                                         # 계량 슬라이드(들어온 상태 · y 40..110)
    I.line([(110, 108, 88), (110, 108, 78)], HEAT, 1.6, '2 2', .9, marker='marker-end="url(#arr)"')   # 낟알 떨어짐
    # ---- ⑤ 아래 열판(내려간 상태): 받침 + 피스톤 Ø60 + 히터 면 + 퓨즈 · 밀대 · 떡뻥
    I.box(62, 70, 80 - DOWN, 96, 80, 12, PLATE)
    I.cylz(CX, CY, 92 - DOWN, 30, 8, PLATE); I.cylz(CX, CY, 100 - DOWN, 30, 2, HEAT)
    I.box(158, 84, 82 - DOWN, 6, 8, 8, RED, hatch_cut=False)
    I.box(66, 72, 92 - DOWN, 88, 4, 14, DARK)                                   # 밀대(받침 뒤, 앞으로 쓸어냄)
    I.cylz(CX, CY, 102 - DOWN, 34, 10, CRACK, op=.92)                           # 부푼 떡뻥 Ø7 × 10
    # 움직임 화살(↕ 25mm)
    I.line([(66, 108, 92 - DOWN), (66, 108, 92)], HEAT, 1.8, None, 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')
    # ---- ⑥ 몰드 링(위 열판 아래 고정) · ⑦ 위 열판(고정) · 히터 · 센서 · 기둥 2
    I.ringz(CX, CY, 96, 32, 30, 6, MOLD)
    I.box(62, 70, 102, 96, 80, 2, HEAT, hatch_cut=False); I.box(62, 70, 104, 96, 80, 14, PLATE)
    I.box(158, 84, 108, 6, 8, 8, HEAT, hatch_cut=False)
    I.box(72, 100, 118, 8, 8, 26, STEEL); I.box(140, 100, 118, 8, 8, 26, STEEL)
    # ---- 열 상자 오른 벽 · 천장(창 없음)
    I.box(170, 66, 44, 6, 94, 106, INSUL)
    I.box(44, 60, 144, 132, 100, 6, INSUL)
    # 김 흐름(뒤로)
    I.line([(110, 62, 150), (110, 30, 170), (110, 12, 178), (110, -14, 190)], HEAT, 1.6, '4 4', .9, marker='marker-end="url(#arr)"')
    # ---- 오른 벽
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(212, 8, z0, 8, 212, h, col)
    # ---- ⑭ 유리 상판(창 없음) · 카세트 덮개 · 터치
    I.box(-2, -2, 196, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    I.line([(136, 4, 200), (206, 4, 200), (206, 62, 200), (136, 62, 200), (136, 4, 200)], '#9a9aa2', 1, '3 3', .9)
    I.poly([(190, 48, 200.2), (198, 48, 200.2), (198, 58, 200.2), (190, 58, 200.2)], HEAT, 'none', 0)
    # ---- 앞 절반 고스트: 앞문(창 · 슬롯) · 바깥 창 · 가림판 플랩 · 트레이 · 서랍 앞판 · 터치
    I.ghost_box(0, 110, 0, 220, 110, 200)
    I.ghost_box(50, 154, 50, 120, 6, 94, '#9a948a', 1, '3 3')                                   # 앞문
    I.line([(72, 157, 72), (148, 157, 72), (148, 157, 94), (72, 157, 94), (72, 157, 72)], '#8a5d12', 1.2, '3 2')  # 앞문 슬롯
    I.line([(60, 220, 50), (160, 220, 50), (160, 220, 146), (60, 220, 146), (60, 220, 50)], '#8a5d12', 1.2, '4 3')   # 앞문 겉 패널(몸체 앞 · 왼쪽 경첩)
    I.line([(64, 220, 54), (64, 220, 142)], '#8a5d12', 2.2)   # 경첩
    I.poly([(66, 220, 70), (154, 220, 70), (154, 220, 94), (66, 220, 94)], SMOKE, '#8a8a90', .8, .25)           # 가림판 플랩
    I.ghost_box(60, 220, 66, 100, 56, 4, '#9a948a', 1, '3 3')                                                   # 트레이
    I.line([(36, 220, 12), (154, 220, 12), (154, 220, 44), (36, 220, 44), (36, 220, 12)], '#8a8a90', 1, '4 3')  # 서랍 앞판
    for x in (38, 54): sx, sy = I.P(x, 196, 200); I.out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="none" stroke="#8a8a90" stroke-dasharray="2 2"/>' % (sx, sy))
    I.line([(66, 196, 200), (88, 196, 200)], '#8a8a90', 2, '2 2')
    I.line([(176, 100, 100), (212, 100, 100)], '#6a6a70', 1, None, 1, marker='marker-start="url(#arrg)" marker-end="url(#arrg)"')
    # ---- 라벨
    R = 850; L = 300
    I.label((110, 110, 200), R, 56, '⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛 · 카세트 덮개', '창 없음(위 열판이 고정이라 창을 내도 안 보임) · 유리 아님', 'r')
    I.label((168, 20, 160), R, 104, '⑫ 곡물 카세트 200g · 계량 슬라이드 3g', '뒤 벽 틈으로 몰드 위까지 들어와 떨어뜨리고 돌아감', 'r')
    I.label((194, 100, 100), R, 152, '⑩ 이중벽 공기층 10mm + ⑧ 단열 5mm', '겉면 60°C 이하', 'r')
    I.label((161, 88, 112), R, 198, '⑦ 위 열판 200~230°C · 센서 — 고정(천장 기둥 2)', None, 'r')
    I.label((142, 110, 99), R, 240, '⑥ 몰드 링 Ø6 · 세라믹 — 위 열판 아래 끼움(고정)', '앞문 열고 돌려 빼서 씻음 · 칩은 접시 몰드를 피스톤 위에', 'r')
    I.label((140, 118, 102 - DOWN), R, 290, '⑤ 아래 열판 = 피스톤 Ø6 · 퓨즈 — 이것만 25mm 오르내림', '그림은 내려간(열린) 상태 · 닫히면 링 안으로 6mm', 'r')
    I.label((70, 74, 100 - DOWN), R, 338, '⑤ 밀대 — 받침 뒤에서 앞으로, 떡뻥을 슬롯으로', None, 'r')
    I.label((110, 100, 50), R, 378, '푸시 로드 — 열 상자 바닥 관통', None, 'r')
    I.label((110, 100, 24), R, 416, '④ 토글 링크 — 사점 잠금 · 래치 스프링 2~3mm · 리밋 2', '열 상자 바닥 아래 칸 · 그 뒤 모터가 천천히 끝까지', 'r')
    I.label((202, 90, 38), R, 464, '③ 승강 모터(웜) — 바닥 오른쪽 · 정전에도 자기 잠금', None, 'r')
    I.label((120, 110, 27), R, 504, '② 부스러기 서랍 — 앞으로 당겨 비움 · 열선에서 50mm 이상', None, 'r')
    I.label((206, 110, 11), R, 544, '① 바닥 무게판 + 고무발 · 기울기 센서', None, 'r')
    I.label((110, 8, 176), L, 150, '⑩ 뒤 김 슬릿(위) — 김은 뒤로만', None, 'l')
    I.label((15, 110, 100), L, 226, '⑨ 제어 보드 — 온도 · 기울기 · 인터록 · 자동 꺼짐', None, 'l')
    I.label((110, 157, 119), L, 300, '⑬ 앞문 안쪽 단열판 — 열 상자 문', '점선 = 잘라낸 앞 절반 · 여기로 몰드 링을 빼고 열판을 닦음', 'l')
    I.label((110, 220, 130), L, 356, '⑬ 앞문 겉 패널 — 옆 패널과 같은 색 · 왼쪽 경첩', '창 없음 · 식어야 열림(인터록)', 'l')
    I.label((66, 108, 92 - DOWN / 2), L, 408, '움직임 ↕ 25mm — 아래 판만', None, 'l')
    I.label((110, 220, 82), L, 450, '⑬ 배출 슬롯 · 가림판 플랩 · 트레이', '떡뻥은 플랩을 밀고 트레이로 · 트레이는 빼서 씻음', 'l')
    I.label((95, 220, 28), L, 504, '② 서랍 앞판', None, 'l')
    I.label((46, 196, 200), L, 548, '터치 3 · 상태 불빛(예열 · 굽는 중 · 완료) · 숫자 2자리', None, 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm · 열 상자 132 × 100 × 106mm(단열 포함) · 절단면은 앞뒤 가운데(y = 110) · 빗금 = 잘린 면', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 900W~1kW · 바닥부터: 고무발 6 · 무게판 8 · 서랍 · 토글 · 모터 칸 30 · 열 상자 106 · 카세트 · 공기층 46 · 상판 4 = 200mm', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1260 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def hollow(I, x0, y0, z0, w, d, h, t, color, top=None, inner=None, front=True):
    inner = inner or shade(color, .08)
    I.box(x0, y0, z0, w, t, h, color, left=inner, top=top)
    I.box(x0, y0 + t, z0, t, d - 2 * t, h, color, right=inner, top=top)
    I.box(x0 + t, y0 + t, z0, w - 2 * t, d - 2 * t, t, color, top=inner)
    I.box(x0 + w - t, y0 + t, z0, t, d - 2 * t, h, color, top=top)
    if front: I.box(x0, y0 + d - t, z0, w, t, h, color, top=top)

def exploded():
    I = Iso(0.86, 480, 760)
    W, D, H = 220, 220, 200
    # L0 ① 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 ② 서랍(앞 · 왼) + ③ 모터(오른쪽) + ④ 토글(가운데)
    z = 48; I.box(40, 48, z, 80, 164, 26, BAND, top=shade(BAND, -.06)); I.box(36, 212, z - 2, 118, 3, 32, BODY); I.box(80, 215, z + 10, 30, 3, 6, DARK)
    I.box(158, 70, z, 44, 40, 24, MOTOR); I.line([(158, 90, z + 12), (130, 100, z + 12), (110, 100, z + 4), (110, 100, z + 18)], MOTOR, 4.5)
    I.line([(96, 100, z + 10), (110, 100, z + 4), (124, 100, z + 10), (110, 100, z + 18)], MOTOR, 4.2)
    I.line([(150, 100, z + 2), (150, 100, z + 26)], HEAT, 2.6, '3 2'); I.box(140, 96, z, 8, 8, 6, DARK); I.box(140, 96, z + 20, 8, 8, 6, DARK)
    I.line([(110, 100, z + 18), (110, 100, z + 60)], MOTOR, 4.5)
    # L2 ⑨ 보드(왼 벽)
    I.box(14, 60, 118, 3, 100, 80, BOARD)
    # L3 ⑤ 아래 열판 = 받침 + 피스톤 + 히터 면 + 퓨즈 + 밀대
    z = 170; I.box(62, 70, z, 96, 80, 12, PLATE); I.cylz(CX, CY, z + 12, 30, 8, PLATE); I.cylz(CX, CY, z + 20, 30, 2, HEAT)
    I.box(158, 84, z + 2, 6, 8, 8, RED); I.box(66, 72, z + 12, 88, 4, 14, DARK)
    # L4 ⑥ 몰드 링 · 칩 몰드(옆) · 떡뻥
    z = 228; I.ringz(CX, CY, z, 32, 30, 6, MOLD); I.cylz(CX, CY, z - 22, 34, 10, CRACK)
    I.cylz(210, 110, z, 32, 4, MOLD)
    # L5 ⑦ 위 열판 · 센서 · 기둥 2
    z = 268; I.box(62, 70, z, 96, 80, 2, HEAT); I.box(62, 70, z + 2, 96, 80, 14, PLATE); I.box(158, 84, z + 4, 6, 8, 8, HEAT)
    I.box(72, 100, z + 16, 8, 8, 26, STEEL); I.box(140, 100, z + 16, 8, 8, 26, STEEL)
    # L6 ⑧ 열 상자(앞면 없음) + ⑬ 앞문(앞으로 뺌)
    z = 318; hollow(I, 44, 60, z, 132, 100, 106, 6, INSUL, front=False); I.box(44, 60, z + 100, 132, 100, 6, INSUL)
    I.box(50, 196, z + 6, 120, 6, 94, INSUL)
    I.poly([(72, 202, z + 28), (148, 202, z + 28), (148, 202, z + 50), (72, 202, z + 50)], '#2b2b30', 'none', 0, .7)
    I.box(48, 196, z + 2, 4, 6, 102, STEEL)
    # L7 ⑩ 몸체(흰 띠) + ⑪ 옆 패널 4장 + 바깥 창 · 슬롯 · 트레이
    z = 486; hollow(I, 8, 8, z, 204, 204, 182, 4, BODY)
    I.box(0, 0, z + 180, 220, 220, 10, BAND); I.box(2, 2, z + 190, 216, 216, 6, BODY)
    I.poly([(70, 8, z + 172), (150, 8, z + 172), (150, 8, z + 180), (70, 8, z + 180)], '#2b2b30', 'none', 0, .85)
    for (x0, y0, w, d) in [(-30, 8, 4, 204), (246, 8, 4, 204), (8, -30, 204, 4), (8, 246, 204, 4)]:
        I.box(x0, y0, z, w, d, 180, PANEL)
    I.line([(60, 250, z + 50), (160, 250, z + 50), (160, 250, z + 146), (60, 250, z + 146), (60, 250, z + 50)], '#8a5d12', 1.2, '4 3')
    I.poly([(66, 250, z + 70), (154, 250, z + 70), (154, 250, z + 94), (66, 250, z + 94)], SMOKE, '#8a8a90', .8, .6)
    I.box(60, 262, z + 60, 100, 56, 4, MOLD)
    # L8 ⑫ 카세트 · 깔때기 · 슬라이드
    z = 700; I.box(140, 12, z, 56, 46, 58, CLEAR, op=.85); I.box(144, 16, z + 2, 48, 38, 30, RICE); I.box(104, 34, z - 24, 30, 24, 26, STEEL, op=.9); I.box(95, 40, z - 32, 30, 70, 6, STEEL)
    # L9 ⑭ 유리 상판 · 터치 · 카세트 덮개(창 없음)
    z = 790; I.box(-2, -2, z, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    I.line([(136, 4, z + 4), (206, 4, z + 4), (206, 62, z + 4), (136, 62, z + 4), (136, 4, z + 4)], '#9a9aa2', 1, '3 3')
    for x in (38, 54): sx, sy = I.P(x, 196, z + 4); I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/>' % (sx, sy))
    I.poly([(66, 192, z + 4.2), (88, 192, z + 4.2), (88, 200, z + 4.2), (66, 200, z + 4.2)], '#fff', 'none', 0)
    I.line([(110, 110, 0), (110, 110, 800)], '#b8b2a6', 1, '3 6', .8)
    # 라벨
    R = 700; L = 280
    I.label((110, 110, 794), R, 48, '⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛 · 카세트 덮개', None, 'r')
    I.label((168, 20, 740), R, 112, '⑫ 곡물 카세트 · 깔때기 · 계량 슬라이드 3g', None, 'r')
    I.label((212, 110, 580), R, 236, '⑩ 몸체 · 흰 띠 · 김 슬릿 · 앞문 자리(점선)', None, 'r')
    I.label((248, 110, 580), R, 272, '⑪ 옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((110, 202, 318 + 76), L, 380, '⑬ 앞문(안쪽 단열판) · 슬롯 · 인터록', None, 'l')
    I.label((176, 110, 370), R, 420, '⑧ 열 상자 — 강판 + 단열 5mm(앞 = 앞문)', None, 'r')
    I.label((158, 110, 276), R, 490, '⑦ 위 열판 · 히터 · 센서 — 고정(기둥 2)', None, 'r')
    I.label((142, 110, 232), R, 546, '⑥ 몰드 링 Ø6(위 열판 아래) + 떡뻥 · 옆은 칩 몰드', None, 'r')
    I.label((140, 118, 192), R, 600, '⑤ 아래 열판 = 피스톤 Ø6 · 퓨즈 · 밀대 — 오르내림', None, 'r')
    I.label((110, 100, 56), R, 660, '④ 토글 링크 · 래치 스프링 · 리밋 2 · 푸시 로드', None, 'r')
    I.label((15, 110, 145), L, 620, '⑨ 제어 보드', None, 'l')
    I.label((180, 90, 60), R, 756, '③ 승강 모터(웜) — 바닥 오른쪽', None, 'r')
    I.label((80, 180, 60), R, 720, '② 부스러기 서랍 · 서랍 앞판', None, 'r')
    I.label((206, 110, 3), R, 800, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.label((110, 290, 548), L, 790, '⑬ 트레이(앞) · 가림판 플랩', None, 'l')
    I.text(480, 962, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼어 씻는 것은 ⑥ 몰드 링 · ⑫ 카세트 · ② 서랍 · ⑬ 트레이 네 가지뿐입니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1090 980" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def sequence():
    """동작 순서 5단계 — 옆에서 본 열 상자(왼쪽 = 앞). 위 열판 · 몰드 링 고정, 아래 피스톤만 움직임"""
    o = []
    o.append('<svg viewBox="0 0 1340 400" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS))
    titles = [('① 올려서 잠금', '모터가 피스톤을 올려 링 안으로 · 토글 사점에서 잠김 · 낟알 3g은 링 안'),
              ('② 누르기 8~10초', '열판 200~230°C · 링 안에서 압력이 오름 · 위 열판 · 링은 제자리'),
              ('③ 2~3mm 순간 하강', '래치 해제 · 스프링이 피스톤을 2~3mm 툭 · 압력이 한순간에 풀려 「뻥」 · 잠긴 열 상자 안'),
              ('④ 천천히 내리기', '모터가 0.5~1초에 걸쳐 끝까지 · 떡뻥은 피스톤 위에 얹혀 링 밖으로 · 리밋 스위치 확인'),
              ('⑤ 배출 · 다음 장', '밀대가 떡뻥을 앞 슬롯으로 · 플랩 밀고 트레이로 · 슬라이드가 다음 3g을 떨어뜨림')]
    pw = 252; gap = 16
    for i in range(5):
        x0 = 14 + i * (pw + gap)
        o.append('<g transform="translate(%d,0)">' % x0)
        o.append('<rect x="0" y="12" width="%d" height="376" rx="16" fill="#fff" stroke="#e6e1d7"/>' % pw)
        o.append('<text x="16" y="40" font-size="15" font-weight="800" fill="#15151a">%s</text>' % titles[i][0])
        # 열 상자(옆 단면): x 36..216 · y 62..238 · 왼쪽 = 앞(앞문)
        o.append('<rect x="36" y="62" width="180" height="176" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
        lock = '#d19a3c' if i < 4 else '#9aa3ad'
        o.append('<rect x="192" y="50" width="22" height="16" rx="3" fill="%s"/><path d="M197 50 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lock, lock))
        # 앞문(왼 벽): 창(위) · 슬롯(아래) · 트레이(밖)
        o.append('<rect x="30" y="62" width="8" height="176" rx="2" fill="#e7d9c2" stroke="#b9b2a2"/>')
        o.append('<rect x="29" y="150" width="10" height="20" fill="#fff" stroke="#8a5d12" stroke-width="1" stroke-dasharray="3 2"/>')
        o.append('<rect x="2" y="170" width="30" height="4" rx="1" fill="#dfe3e6" stroke="#9aa3ad"/>')
        o.append('<text x="22" y="86" font-size="9.5" fill="#6a6a70" text-anchor="middle">앞</text><text x="22" y="126" font-size="9" fill="#6a6a70" text-anchor="middle">문</text>')
        # 위 열판(고정) · 기둥 2 · 히터 면 · 몰드 링(고정, 아래 매달림)
        o.append('<rect x="80" y="62" width="6" height="42" fill="#b9bec4"/><rect x="168" y="62" width="6" height="42" fill="#b9bec4"/>')
        o.append('<rect x="70" y="102" width="112" height="16" rx="3" fill="#8a8f96"/><rect x="70" y="118" width="112" height="3" fill="#d19a3c"/>')
        o.append('<rect x="96" y="121" width="6" height="9" fill="#dfe3e6" stroke="#9aa3ad" stroke-width=".8"/><rect x="150" y="121" width="6" height="9" fill="#dfe3e6" stroke="#9aa3ad" stroke-width=".8"/>')
        o.append('<text x="188" y="113" font-size="9.5" fill="#6a6a70">고정</text>')
        # 계량 슬라이드(뒤 벽 틈 y 134..140) — ⑤에서만 들어옴
        o.append('<rect x="200" y="133" width="16" height="7" fill="#b9bec4" stroke="#8a8f96" stroke-width=".6"/>')
        # 아래 피스톤: 닫힘 = 면 y 124(링 안 6px) · 열림 = +40
        down = [0, 0, 4, 40, 40][i]
        yF = 124 + down                                       # 히터 면 윗선
        o.append('<rect x="70" y="%d" width="112" height="12" rx="3" fill="#8a8f96"/>' % (yF + 12))   # 받침
        o.append('<rect x="102" y="%d" width="48" height="12" fill="#8a8f96"/><rect x="102" y="%d" width="48" height="3" fill="#d19a3c"/>' % (yF, yF - 1))  # 피스톤 + 면
        o.append('<rect x="70" y="%d" width="6" height="14" fill="#4a4e55"/>' % (yF - 2))            # 밀대(받침 뒤 = 오른쪽? 아니, 앞=왼쪽이니 밀대는 뒤=오른쪽)
        o.pop(); o.append('<rect x="176" y="%d" width="6" height="14" fill="#4a4e55"/>' % (yF - 2))
        # 떡뻥 · 낟알
        if i == 0:
            for k in range(6): o.append('<circle cx="%d" cy="%d" r="2.2" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (108 + k * 7, yF - 4))
        elif i == 1:
            o.append('<rect x="104" y="%d" width="44" height="3" fill="#e9dcc0" stroke="#d19a3c" stroke-width=".6"/>' % (yF - 4))
            for k in range(4): o.append('<path d="M%d %d q3 -6 0 -12" fill="none" stroke="#d19a3c" stroke-width="1.6" opacity=".8"/>' % (110 + k * 10, yF - 6))
        elif i == 2:
            o.append('<rect x="103" y="%d" width="46" height="8" rx="4" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 9))
            for a in range(0, 360, 40):
                r = math.radians(a); o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2"/>' % (126 + 36 * math.cos(r), yF - 5 + 12 * math.sin(r), 126 + 46 * math.cos(r), yF - 5 + 20 * math.sin(r)))
            o.append('<text x="60" y="%d" font-size="13" font-weight="800" fill="#8a5d12">2~3mm · 뻥</text>' % (yF + 44))
        elif i == 3:
            o.append('<rect x="100" y="%d" width="52" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 11))
        else:
            o.append('<rect x="44" y="%d" width="52" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 11))      # 슬롯 지나는 떡뻥
            o.append('<rect x="8" y="160" width="22" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c" opacity=".6"/>')     # 트레이 위
            o.append('<line x1="150" y1="%d" x2="100" y2="%d" stroke="#55585e" stroke-width="2" marker-end="url(#arrg)"/>' % (yF - 6, yF - 6))
            o.append('<rect x="104" y="%d" width="46" height="4" fill="#4a4e55"/>' % (yF - 10))   # 밀대가 앞으로 나온 자리
            o.append('<rect x="112" y="133" width="104" height="7" fill="#b9bec4" stroke="#8a8f96" stroke-width=".6"/><rect x="118" y="134" width="14" height="5" fill="#f3eedf"/>')   # 슬라이드 들어옴
            for k in range(3): o.append('<circle cx="%d" cy="%d" r="2" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (124, 146 + k * 6))
            o.append('<text x="196" y="156" font-size="9.5" fill="#6a6a70" text-anchor="end">계량 3g</text>')
        # 토글(열 상자 바닥 아래 칸) · 푸시 로드 · 모터
        o.append('<line x1="126" y1="%d" x2="126" y2="252" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (yF + 24))
        if i < 3: o.append('<path d="M126 252 v8 M126 260 l-14 14 M126 260 l14 14" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
        else: o.append('<path d="M126 252 l-16 8 l16 8 M126 252 l16 8 l-16 8" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
        o.append('<line x1="126" y1="276" x2="126" y2="288" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
        o.append('<rect x="106" y="286" width="40" height="14" rx="4" fill="#5a5e66"/><text x="152" y="297" font-size="10" fill="#6a6a70">모터(바닥)</text>')
        if i == 0: o.append('<text x="152" y="268" font-size="10.5" fill="#6a6a70">사점 잠금</text><line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">올림</text>' % (yF + 60, yF + 26, yF + 46))
        if i == 1: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">누름</text>' % (yF + 50, yF + 26, yF + 42))
        if i == 2: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">스프링</text>' % (yF + 10, yF + 34, yF + 26))
        if i == 3: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">천천히</text>' % (yF - 30, yF + 10, yF - 8))
        words = titles[i][1].split(' · ')
        for k, w in enumerate(words): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (322 + k * 16, w))
        o.append('</g>')
        if i < 4: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

if __name__ == '__main__':
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence)]:
        with open(os.path.join(here, name + '.svg'), 'w', encoding='utf-8') as f: f.write(fn())
        print('wrote', name)
