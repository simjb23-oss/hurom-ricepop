# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 — 아이소메트릭 단면 · 층 분해 · 동작 순서 (SVG)
좌표(mm): x 0..220 왼→오, y 0..220 뒤→앞, z 0..200 아래→위. 보는 방향 = 앞·오른쪽·위.
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
        """left = +y 면(앞·왼쪽으로 보이는 면), right = +x 면, top = +z 면."""
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

# 색
PANEL = '#ebe4d6'; BODY = '#f4f1ea'; BAND = '#ffffff'; GLASS = '#15151a'; WIN = '#9ec3dd'; STEEL = '#b9bec4'; PLATE = '#8a8f96'
HEAT = '#d19a3c'; MOLD = '#dfe3e6'; CRACK = '#fff3dc'; DARK = '#4a4e55'; MOTOR = '#5a5e66'; BOARD = '#2f7a46'; CLEAR = '#dcecf7'
WATER = '#8fbfe0'; RICE = '#f3eedf'; INSUL = '#e7d9c2'; RED = '#e06c5a'

def cutaway():
    I = Iso(1.5, 560, 268, cut_y=110)
    W, D, H = 220, 220, 200
    # ---- 껍데기(뒤 벽 · 바닥 · 왼 벽) : 옆 패널 0~180, 흰 띠 180~190, 몸체 190~196
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)   # 뒤 벽: +y 면 = 안쪽
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))                 # 바닥
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col) # 왼 벽: +x 면 = 안쪽
    # 뒤 김 슬릿(뒤 벽 안쪽 면 위) + 화살
    I.poly([(70, 8, 172), (150, 8, 172), (150, 8, 180), (70, 8, 180)], '#2b2b30', 'none', 0, .85)
    # ---- 안쪽 부품
    I.box(14, 14, 8, 192, 192, 6, STEEL)                                        # 무게판
    I.box(14, 60, 40, 3, 100, 80, BOARD)                                        # 제어 보드(왼 벽 안쪽, 세움)
    I.box(18, 12, 46, 26, 30, 34, MOTOR)                                        # 기어 모터(왼쪽 공기층 뒤)
    I.box(40, 48, 16, 140, 150, 28, BAND, top=shade(BAND, -.06))               # 부스러기 서랍
    # 물통 · 펌프(뒤 왼쪽)
    I.box(24, 12, 120, 40, 46, 58, CLEAR, op=.85); I.box(28, 16, 122, 32, 38, 26, WATER, op=.9)
    I.box(28, 60, 104, 24, 16, 14, DARK)
    I.line([(40, 76, 112), (40, 90, 112), (100, 70, 130), (104, 72, 124)], '#6a6a70', 2.2)
    # 곡물 카세트 · 계량 슬라이드 · 투입관(뒤 오른쪽)
    I.box(140, 12, 120, 56, 46, 58, CLEAR, op=.85); I.box(144, 16, 122, 48, 38, 30, RICE)
    I.box(150, 58, 112, 30, 20, 6, STEEL)
    I.line([(165, 60, 112), (120, 70, 128), (116, 72, 124)], '#6a6a70', 2.4)
    # 열 상자(강판 1.5 + 단열 5 ≈ 6mm 벽) x 44..176 · y 60..160 · z 50..150
    I.box(44, 60, 50, 132, 6, 100, INSUL)                                       # 뒤 벽
    I.box(44, 66, 50, 6, 94, 100, INSUL)                                        # 왼 벽
    I.box(50, 66, 50, 120, 94, 5, INSUL, top=shade(INSUL, -.08))               # 바닥
    # 토글 링크 · 밀대 · 리밋 스위치
    I.line([(31, 42, 64), (31, 100, 64), (110, 100, 64), (110, 100, 78)], MOTOR, 5)  # 크랭크 → 푸시 로드 → 리프트
    I.line([(96, 100, 78), (110, 100, 66), (124, 100, 78)], MOTOR, 4.2)        # 토글 두 링크
    I.box(160, 96, 55, 8, 8, 6, DARK); I.box(160, 96, 72, 8, 8, 6, DARK)       # 리밋 스위치 2
    # 아래 열판 · 히터 · 퓨즈
    I.box(62, 70, 78, 96, 80, 12, PLATE); I.box(62, 70, 90, 96, 80, 2, HEAT, hatch_cut=False)
    I.box(158, 84, 80, 6, 8, 8, RED, hatch_cut=False)
    # 몰드 · 떡뻥(단면)
    I.box(70, 78, 92, 80, 64, 12, MOLD); I.box(78, 86, 94, 64, 48, 8, CRACK, hatch_cut=False, top=CRACK)
    # 위 열판 · 히터 · 센서
    I.box(62, 70, 104, 96, 80, 2, HEAT, hatch_cut=False); I.box(62, 70, 106, 96, 80, 12, PLATE)
    I.box(158, 84, 108, 6, 8, 8, HEAT, hatch_cut=False)
    # 열 상자 오른 벽 · 윗판(안쪽 유리 창)
    I.box(170, 66, 50, 6, 94, 100, INSUL)
    I.box(44, 60, 146, 132, 100, 4, INSUL)
    I.poly([(84, 74, 150), (136, 74, 150), (136, 110, 150), (84, 110, 150)], WIN, '#5c7f96', .8, .9)
    # 김 흐름(열 상자 → 뒤 슬릿)
    I.line([(110, 62, 152), (110, 30, 170), (110, 12, 178), (110, -14, 190)], HEAT, 1.6, '4 4', .9, marker='marker-end="url(#arr)"')
    # ---- 오른 벽(패널 · 띠 · 몸체) + 공기층 치수
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(212, 8, z0, 8, 212, h, col)
    # ---- 유리 상판(검은 강화유리 4mm) + 창 + 뒤 덮개 윤곽 + 잠금 표시
    I.box(-2, -2, 196, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    I.poly([(80, 70, 200), (140, 70, 200), (140, 110, 200), (80, 110, 200)], WIN, '#cfe6f5', .8, .55)
    I.line([(136, 4, 200), (206, 4, 200), (206, 62, 200), (136, 62, 200), (136, 4, 200)], '#9a9aa2', 1, '3 3', .9)
    I.poly([(190, 48, 200.2), (198, 48, 200.2), (198, 58, 200.2), (190, 58, 200.2)], HEAT, 'none', 0)
    # ---- 앞쪽(잘라낸 절반) 고스트 + 배출 슬롯 · 가림판 · 트레이 · 터치
    I.ghost_box(0, 110, 0, 220, 110, 200)
    I.line([(70, 220, 74), (150, 220, 74), (150, 220, 92), (70, 220, 92), (70, 220, 74)], '#8a8a90', 1, '4 3')
    I.ghost_box(60, 224, 56, 100, 60, 4, '#9a948a', 1, '3 3'); I.ghost_box(60, 222, 74, 100, 3, 28, '#9a948a', 1, '3 3')
    for x in (38, 54): sx, sy = I.P(x, 196, 200); I.out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="none" stroke="#8a8a90" stroke-dasharray="2 2"/>' % (sx, sy))
    I.line([(66, 196, 200), (88, 196, 200)], '#8a8a90', 2, '2 2')
    # 공기층 치수선(열 상자 오른 벽 ↔ 몸체 안쪽)
    I.line([(176, 100, 100), (212, 100, 100)], '#6a6a70', 1, None, 1, marker='marker-start="url(#arrg)" marker-end="url(#arrg)"')
    # ---- 라벨
    R = 850; L = 300
    I.label((110, 110, 200), R, 60, '① 검은 강화유리 상판 4mm · 이중 유리 창', '꺼져 있으면 매끈한 유리판 · 창으로 부푸는 걸 봅니다', 'r')
    I.label((170, 30, 200), R, 108, '② 뒤 덮개 · 덮개 잠금(솔레노이드)', '카세트 · 물통 자리 · 열판이 식어야 열립니다', 'r')
    I.label((168, 20, 160), R, 156, '③ 곡물 카세트 200g(60장) · 계량 슬라이드 3g', '마른 낟알만 · 분리 세척', 'r')
    I.label((194, 100, 100), R, 204, '④ 이중벽 공기층 10mm + 단열 5mm', '겉면 60°C 이하 · 흰 무광 그대로', 'r')
    I.label((161, 88, 112), R, 252, '⑤ 위 열판 200~230°C · 온도 센서(NTC)', None, 'r')
    I.label((150, 110, 98), R, 290, '⑥ 몰드 Ø6 · 세라믹 코팅 · 원터치 분리', '떡뻥용 · 칩용 바꿔 끼움 · 식기세척기', 'r')
    I.label((161, 88, 84), R, 338, '⑦ 아래 열판 · 온도 퓨즈(2중 차단)', None, 'r')
    I.label((164, 100, 75), R, 376, '⑧ 리밋 스위치 2 — 닫힘 · 열림 위치', None, 'r')
    I.label((110, 110, 70), R, 414, '⑨ 토글 링크 — 사점 잠금 · 2~3mm 순간 개방', '그 뒤 모터가 천천히 끝까지', 'r')
    I.label((110, 100, 64), R, 452, '⑩ 푸시 로드 · 밀대 — 모터에서 열 상자로', None, 'r')
    I.label((180, 110, 30), R, 500, '⑪ 부스러기 서랍 — 앞으로 당겨 비움', None, 'r')
    I.label((206, 110, 11), R, 540, '⑫ 바닥 무게판 + 미끄럼 방지 고무 · 기울기 센서', None, 'r')
    I.label((44, 44, 150), L, 92, '⑬ 물통 50mL · 마이크로 펌프', '한 장에 0.5mL 안개 · 분리 세척', 'l')
    I.label((110, 8, 176), L, 150, '⑭ 뒤 김 슬릿(위) — 김은 뒤로만', None, 'l')
    I.label((15, 110, 80), L, 236, '⑮ 제어 보드 — 온도 · 기울기 · 인터록 · 자동 꺼짐', None, 'l')
    I.label((110, 68, 148), L, 290, '열 상자 안쪽 유리(붕규산) — 창의 안쪽 겹', None, 'l')
    I.label((110, 220, 83), L, 470, '⑯ 앞 배출 슬롯 · 가림판 · 트레이', '점선 = 잘라낸 앞 절반 · 떡뻥은 가림판 뒤로 나옵니다', 'l')
    I.label((31, 30, 70), L, 400, '⑩ 기어 모터(웜) — 왼쪽 공기층 뒤', '높이를 안 먹는 자리', 'l')
    I.label((46, 196, 200), L, 520, '유리 아래 터치 3 · 숫자 2자리(앞)', None, 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm · 열 상자 132 × 100 × 100mm(단열 포함) · 절단면은 앞뒤 가운데(y = 110) · 빗금 = 잘린 면', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 900W~1kW · 바닥부터 적층: 고무발 6 · 무게판 6 · 서랍 28 · 링크 공간 32 · 열 상자 100 · 공기층 18 · 유리 4 = 194mm(여유 6mm)', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1200 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def hollow(I, x0, y0, z0, w, d, h, t, color, top=None, inner=None):
    """위가 뚫린 상자(벽 4 + 바닥)"""
    inner = inner or shade(color, .08)
    I.box(x0, y0, z0, w, t, h, color, left=inner, top=top)                 # 뒤
    I.box(x0, y0 + t, z0, t, d - 2 * t, h, color, right=inner, top=top)    # 왼
    I.box(x0 + t, y0 + t, z0, w - 2 * t, d - 2 * t, t, color, top=inner)   # 바닥
    I.box(x0 + w - t, y0 + t, z0, t, d - 2 * t, h, color, top=top)         # 오른
    I.box(x0, y0 + d - t, z0, w, t, h, color, top=top)                     # 앞

def exploded():
    I = Iso(0.86, 480, 760)
    W, D, H = 220, 220, 200
    lifts = {}
    # L0 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 서랍
    z = 48; I.box(40, 40, z, 140, 150, 28, BAND, top=shade(BAND, -.06)); I.box(80, 190, z + 8, 60, 4, 10, DARK)
    # L2 모터 · 토글 · 리밋 · 보드
    z = 105; I.box(80, 12, z, 40, 32, 34, MOTOR); I.line([(110, 44, z + 18), (110, 110, z + 18), (110, 110, z + 32)], MOTOR, 4.5)
    I.line([(96, 110, z + 32), (110, 110, z + 20), (124, 110, z + 32)], MOTOR, 3.8)
    I.box(160, 106, z + 9, 8, 8, 6, DARK); I.box(160, 106, z + 26, 8, 8, 6, DARK); I.box(14, 60, z, 3, 100, 80, BOARD)
    # L3 아래 열판 · 퓨즈
    z = 175; I.box(62, 70, z, 96, 80, 12, PLATE); I.box(62, 70, z + 12, 96, 80, 2, HEAT); I.box(158, 84, z + 2, 6, 8, 8, RED)
    # L4 몰드 · 떡뻥 · 칩 몰드(옆)
    z = 222; I.box(70, 78, z, 80, 64, 12, MOLD); I.box(78, 86, z + 2, 64, 48, 8, CRACK, top=CRACK)
    I.box(200, 78, z, 80, 64, 6, MOLD)
    # L5 위 열판 · 센서
    z = 268; I.box(62, 70, z, 96, 80, 2, HEAT); I.box(62, 70, z + 2, 96, 80, 12, PLATE); I.box(158, 84, z + 4, 6, 8, 8, HEAT)
    # L6 열 상자(단열) + 윗판(안쪽 유리)
    z = 318; hollow(I, 44, 60, z, 132, 100, 100, 6, INSUL)
    z2 = 440; I.box(44, 60, z2, 132, 100, 4, INSUL); I.poly([(84, 74, z2 + 4), (136, 74, z2 + 4), (136, 126, z2 + 4), (84, 126, z2 + 4)], WIN, '#5c7f96', .8, .9)
    # L7 몸체(흰 띠) + 옆 패널 4장(바깥으로 벌림)
    z = 486; hollow(I, 8, 8, z, 204, 204, 182, 4, BODY)
    I.box(0, 0, z + 180, 220, 220, 10, BAND); I.box(2, 2, z + 190, 216, 216, 6, BODY)
    for (x0, y0, w, d) in [(-30, 8, 4, 204), (246, 8, 4, 204), (8, -30, 204, 4), (8, 246, 204, 4)]:
        I.box(x0, y0, z, w, d, 180, PANEL)
    # L8 카세트 · 슬라이드 · 물통 · 펌프
    z = 700; I.box(140, 12, z, 56, 46, 58, CLEAR, op=.85); I.box(144, 16, z + 2, 48, 38, 30, RICE); I.box(150, 58, z - 10, 30, 20, 6, STEEL)
    I.box(24, 12, z, 40, 46, 58, CLEAR, op=.85); I.box(28, 16, z + 2, 32, 38, 26, WATER, op=.9); I.box(28, 60, z - 16, 24, 16, 14, DARK)
    # L9 유리 상판 · 창 · 터치 · 뒤 덮개
    z = 790; I.box(-2, -2, z, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    I.poly([(80, 70, z + 4), (140, 70, z + 4), (140, 150, z + 4), (80, 150, z + 4)], WIN, '#cfe6f5', .8, .6)
    I.line([(136, 4, z + 4), (206, 4, z + 4), (206, 62, z + 4), (136, 62, z + 4), (136, 4, z + 4)], '#9a9aa2', 1, '3 3')
    for x in (38, 54): sx, sy = I.P(x, 196, z + 4); I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/>' % (sx, sy))
    I.poly([(66, 192, z + 4.2), (88, 192, z + 4.2), (88, 200, z + 4.2), (66, 200, z + 4.2)], '#fff', 'none', 0)
    # 앞: 가림판 · 트레이(앞으로 벌림)
    I.box(60, 262, 110, 100, 60, 4, MOLD); I.box(60, 258, 128, 100, 3, 28, DARK, op=.6)
    # 조립 축(점선)
    I.line([(110, 110, 0), (110, 110, 800)], '#b8b2a6', 1, '3 6', .8)
    # 라벨
    R = 700; L = 280
    I.label((110, 110, 794), R, 48, '⑩ 검은 강화유리 상판 · 창 · 터치 · 뒤 덮개', None, 'r')
    I.label((168, 20, 740), R, 112, '⑨ 곡물 카세트 · 계량 슬라이드 3g', None, 'r')
    I.label((44, 44, 730), L, 112, '⑨ 물통 50mL · 마이크로 펌프', None, 'l')
    I.label((212, 110, 580), R, 236, '⑧ 몸체(안쪽 구조) · 흰 띠', None, 'r')
    I.label((248, 110, 580), R, 272, '옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((110, 110, 444), L, 380, '⑦ 열 상자 윗판 · 안쪽 유리(붕규산)', None, 'l')
    I.label((176, 110, 370), R, 420, '⑦ 열 상자 — 강판 1.5 + 단열 5mm', None, 'r')
    I.label((158, 110, 276), R, 490, '⑥ 위 열판 · 히터 · 온도 센서', None, 'r')
    I.label((150, 110, 228), R, 546, '⑤ 몰드 Ø6 + 떡뻥 · 옆은 칩 몰드(얕은 접시)', None, 'r')
    I.label((158, 110, 181), R, 600, '④ 아래 열판 · 히터 · 온도 퓨즈', None, 'r')
    I.label((164, 110, 125), R, 660, '③ 토글 링크 · 기어 모터 · 리밋 스위치 2', None, 'r')
    I.label((15, 110, 145), L, 620, '③ 제어 보드', None, 'l')
    I.label((180, 110, 62), R, 720, '② 부스러기 서랍', None, 'r')
    I.label((206, 110, 3), R, 790, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.label((110, 292, 112), L, 790, '⑪ 가림판 · 트레이(앞)', None, 'l')
    I.text(480, 940, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼는 것은 ⑤ 몰드 · ⑨ 카세트 · 물통 · ② 서랍 · ⑪ 트레이 다섯 가지뿐입니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1000 960" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def sequence():
    """동작 순서 — 옆에서 본 열 상자 4장면 (2D)"""
    o = []
    o.append('<svg viewBox="0 0 1100 330" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS))
    titles = [('① 잠금 · 누르기', '덮개 잠김(인터록) → 토글이 사점에서 몰드를 닫아 유지 · 열판 200~230°C · 8~10초'),
              ('② 2~3mm 순간 개방', '래치 해제 → 위 열판이 스프링으로 2~3mm만 튐 → 쌀이 「뻥」 부풉니다 · 잠긴 열 상자 안에서만'),
              ('③ 천천히 열기', '모터가 0.5~1초에 걸쳐 끝까지 올립니다 · 리밋 스위치가 열림 위치를 확인'),
              ('④ 배출 · 다음 장', '밀대가 떡뻥을 앞 슬롯 → 가림판 뒤 트레이로 · 계량 3g + 0.5mL 안개 → 다시 ①')]
    for i in range(4):
        x0 = 20 + i * 268
        o.append('<g transform="translate(%d,0)">' % x0)
        o.append('<rect x="0" y="14" width="248" height="300" rx="16" fill="#fff" stroke="#e6e1d7"/>')
        o.append('<text x="18" y="44" font-size="15" font-weight="800" fill="#15151a">%s</text>' % titles[i][0])
        # 열 상자 윤곽
        o.append('<rect x="36" y="70" width="176" height="150" rx="8" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
        # 덮개 잠금 아이콘
        lock = '#d19a3c' if i < 3 else '#9aa3ad'
        o.append('<rect x="190" y="58" width="22" height="16" rx="3" fill="%s"/><path d="M195 58 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lock, lock))
        # 아래 열판 · 몰드
        o.append('<rect x="60" y="160" width="128" height="14" rx="3" fill="#8a8f96"/><rect x="60" y="158" width="128" height="3" fill="#d19a3c"/>')
        o.append('<rect x="76" y="140" width="96" height="18" rx="4" fill="#dfe3e6" stroke="#9aa3ad"/>')
        # 위 열판 위치
        up = [0, 5, 40, 40][i]; yU = 126 - up
        o.append('<rect x="60" y="%d" width="128" height="14" rx="3" fill="#8a8f96"/><rect x="60" y="%d" width="128" height="3" fill="#d19a3c"/>' % (yU, yU + 14))
        # 떡뻥
        if i == 0: o.append('<rect x="100" y="144" width="48" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c"/>')
        elif i == 1:
            o.append('<ellipse cx="124" cy="146" rx="42" ry="9" fill="#fff3dc" stroke="#d19a3c"/>')
            for a in range(0, 360, 45):
                r = math.radians(a); o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2"/>' % (124 + 50 * math.cos(r), 146 + 20 * math.sin(r), 124 + 60 * math.cos(r), 146 + 28 * math.sin(r)))
            o.append('<text x="124" y="110" font-size="13" font-weight="800" fill="#8a5d12" text-anchor="middle">2~3mm · 뻥</text>')
        elif i == 2: o.append('<ellipse cx="124" cy="150" rx="44" ry="8" fill="#fff3dc" stroke="#d19a3c"/>')
        else:
            o.append('<ellipse cx="44" cy="150" rx="30" ry="7" fill="#fff3dc" stroke="#d19a3c"/>')
            o.append('<rect x="150" y="142" width="8" height="16" rx="2" fill="#55585e"/><line x1="150" y1="150" x2="92" y2="150" stroke="#55585e" stroke-width="2" marker-end="url(#arrg)"/>')
            o.append('<path d="M20 150 h-4" stroke="#8a8a90"/><rect x="2" y="150" width="34" height="14" fill="none" stroke="#8a8a90" stroke-dasharray="3 2"/>')
            o.append('<rect x="60" y="76" width="128" height="14" rx="3" fill="#8a8f96"/>')
        # 토글 링크(아래)
        if i == 0: o.append('<path d="M124 174 v22 M124 196 l-18 18 M124 196 l18 18" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/><text x="124" y="232" font-size="11" fill="#6a6a70" text-anchor="middle">사점 잠금</text>')
        else: o.append('<path d="M124 174 v18 M124 192 l-14 20 M124 192 l14 20" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
        # 모터 화살(③)
        if i == 2: o.append('<line x1="200" y1="150" x2="200" y2="96" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="126" font-size="11" fill="#8a5d12">모터</text>')
        if i == 1: o.append('<line x1="200" y1="140" x2="200" y2="118" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="132" font-size="11" fill="#8a5d12">스프링</text>')
        # 설명
        words = titles[i][1].split(' · ')
        for k, w in enumerate(words): o.append('<text x="18" y="%d" font-size="12" fill="#6a6a70">%s</text>' % (246 + k * 18, w))
        o.append('</g>')
        if i < 3: o.append('<text x="%d" y="150" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + 258))
    o.append('</svg>')
    return '\n'.join(o)

if __name__ == '__main__':
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence)]:
        with open(os.path.join(here, name + '.svg'), 'w', encoding='utf-8') as f: f.write(fn())
        print('wrote', name)
