# -*- coding: utf-8 -*-
"""쌀참 2D 설계도 생성기 v12 (2026-11-25) — 3면도 · 단면 A-A · 단면 B-B (준보 「단면도 2D설계도 2.5D분해도 티어다운」 msg_5fae3925)
좌표 · 부품 번호 · 높이는 gen_iso_v12.py 머리말과 같다(x 0..220 왼→오 · y 0..220 뒤→앞 · z 0..200 아래→위).
단면은 ③ 누르는 상태: 받침 ⑤ 137..149 · 아래 판 ⑥ 149..163 · 칸 바닥 155 · 위 판 ⑫ 163..169 · 볼록 끝 157 → 쌀 2mm.
"""
import math

FONT = 'font-family="NanumSquare, Pretendard, sans-serif"'
INK = '#1d1d22'; THIN = '#55555c'; HID = '#7d7d85'; ACC = '#d19a3c'; STEAM = '#d0782a'
PAPER = '#fbfaf6'
DEFS = '''<defs>
<pattern id="d2-steel" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="5" height="5" fill="#c9ced6"/><line x1="0" y1="0" x2="0" y2="5" stroke="#3c434d" stroke-width="1.2"/></pattern>
<pattern id="d2-alu" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#e9ecef"/><line x1="0" y1="0" x2="0" y2="8" stroke="#8b939d" stroke-width=".9"/></pattern>
<pattern id="d2-ins" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#f4ead3"/><circle cx="2" cy="2" r=".9" fill="#b49a62"/><circle cx="6" cy="6" r=".9" fill="#b49a62"/></pattern>
<pattern id="d2-plas" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><rect width="10" height="10" fill="#efe9dc"/><line x1="0" y1="0" x2="0" y2="10" stroke="#b9b0a0" stroke-width=".7"/></pattern>
<pattern id="d2-rub" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="4" fill="#3a3a40"/></pattern>
<marker id="d2-a" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,1.5 L10,5 L0,8.5 z" fill="#1d1d22"/></marker>
<marker id="d2-s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d0782a"/></marker>
<marker id="d2-f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#4f5864"/></marker>
</defs>'''
MAT = {'steel': 'url(#d2-steel)', 'alu': 'url(#d2-alu)', 'ins': 'url(#d2-ins)', 'plas': 'url(#d2-plas)', 'glass': '#141418', 'rub': '#3a3a40',
       'heat': '#c8452f', 'board': '#2f6b45', 'motor': '#5b6470', 'band': '#ffffff', 'void': PAPER}


class D:
    def __init__(s): s.o = []
    def a(s, t): s.o.append(t)
    def rect(s, x, y, w, h, fill='none', stroke=INK, sw=1.2, rx=0, dash=None, op=1):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        s.a('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="%.2f"%s opacity="%.2f"/>' % (x, y, w, h, rx, fill, stroke, sw, d, op))
    def line(s, pts, stroke=INK, sw=1, dash=None, m0=None, m1=None, op=1):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        mk = (' marker-start="url(#%s)"' % m0 if m0 else '') + (' marker-end="url(#%s)"' % m1 if m1 else '')
        s.a('<polyline points="%s" fill="none" stroke="%s" stroke-width="%.2f"%s%s opacity="%.2f" stroke-linejoin="round"/>' % (' '.join('%.1f,%.1f' % p for p in pts), stroke, sw, d, mk, op))
    def path(s, d_, fill='none', stroke=INK, sw=1.2, dash=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        s.a('<path d="%s" fill="%s" stroke="%s" stroke-width="%.2f"%s/>' % (d_, fill, stroke, sw, d))
    def circle(s, x, y, r, fill='none', stroke=INK, sw=1.2, dash=None):
        d = ' stroke-dasharray="%s"' % dash if dash else ''
        s.a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%.2f"%s/>' % (x, y, r, fill, stroke, sw, d))
    def text(s, x, y, t, size=12, w=700, fill=INK, anchor='middle', rot=None):
        r = ' transform="rotate(%d %.1f %.1f)"' % (rot, x, y) if rot else ''
        s.a('<text x="%.1f" y="%.1f" font-size="%.1f" font-weight="%d" fill="%s" text-anchor="%s"%s>%s</text>' % (x, y, size, w, fill, anchor, r, t))
    # 치수선: 두 점 사이 · off 만큼 띄움 · 글자
    def dimh(s, x0, x1, y, t, yref=None, size=11.5):
        if yref is not None:
            for x in (x0, x1): s.line([(x, yref), (x, y + (4 if y > yref else -4))], THIN, .7)
        s.line([(x0, y), (x1, y)], INK, .8, None, 'd2-a', 'd2-a')
        s.a('<rect x="%.1f" y="%.1f" width="%.1f" height="14" fill="%s"/>' % ((x0 + x1) / 2 - len(t) * 3.6 - 3, y - 16, len(t) * 7.2 + 6, PAPER))
        s.text((x0 + x1) / 2, y - 4, t, size, 700)
    def dimv(s, y0, y1, x, t, xref=None, size=11.5, side=1):
        if xref is not None:
            for y in (y0, y1): s.line([(xref, y), (x + (4 if x > xref else -4), y)], THIN, .7)
        s.line([(x, y0), (x, y1)], INK, .8, None, 'd2-a', 'd2-a')
        tx = x + 5 * side
        s.text(tx, (y0 + y1) / 2 + 4, t, size, 700, INK, 'start' if side > 0 else 'end')
    def balloon(s, x, y, tx, ty, n, note=None, anchor='start'):
        s.line([(x, y), (tx, ty)], THIN, .8)
        s.circle(x, y, 2.4, INK, 'none')
        s.circle(tx, ty, 11, '#fff', INK, 1.1)
        s.text(tx, ty + 4.5, n, 13, 800)
        if note:
            s.text(tx + (16 if anchor == 'start' else -16), ty + 4.5, note, 11.5, 700, THIN, anchor)
    def svg(s, w, h):
        return '<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" %s>%s<rect width="%d" height="%d" fill="%s"/>\n%s</svg>' % (w, h, FONT, DEFS, w, h, PAPER, '\n'.join(s.o))


CELLS = [(110, 80), (78.8, 134), (141.2, 134)]
DR = 25


def title_block(g, x, y, name, scale):
    g.rect(x, y, 300, 92, '#fff', INK, 1.4)
    g.line([(x, y + 34), (x + 300, y + 34)], INK, .8); g.line([(x + 150, y + 34), (x + 150, y + 92)], INK, .8); g.line([(x, y + 63), (x + 300, y + 63)], INK, .8)
    g.text(x + 12, y + 24, '휴롬 쌀참 · ' + name, 15, 800, INK, 'start')
    g.text(x + 12, y + 54, '단위 mm', 11.5, 700, THIN, 'start'); g.text(x + 162, y + 54, '척도 ' + scale, 11.5, 700, THIN, 'start')
    g.text(x + 12, y + 83, '3각법', 11.5, 700, THIN, 'start'); g.text(x + 162, y + 83, '2026-11-25', 11.5, 700, THIN, 'start')


def three_view():
    S = 1.55
    g = D()
    # ---- 배치: 위 = 평면도 · 아래 = 정면도 · 오른쪽 = 우측면도 (3각법)
    fx0, fy0 = 110, 520          # 정면도 왼쪽 위(x 0 · z 200)
    ty0 = 110                     # 평면도 위(y 0 = 뒤)
    sx0 = fx0 + 220 * S + 130     # 우측면도 왼쪽(y 220 = 앞)
    FX = lambda x: fx0 + x * S
    FZ = lambda z: fy0 + (200 - z) * S
    TY = lambda y: ty0 + y * S
    SY = lambda y: sx0 + (220 - y) * S

    # ===== 정면도
    g.text(FX(110), FZ(0) + 70, '정면도', 14, 800)
    for x0 in (14, 186):
        g.rect(FX(x0), FZ(6), 20 * S, 6 * S, MAT['rub'], INK, .8)                           # 고무발
    g.path('M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Z' % (
        FX(0), FZ(147), FX(0), FZ(16), FX(0), FZ(6), FX(10), FZ(6), FX(210), FZ(6), FX(220), FZ(6), FX(220), FZ(16), FX(220), FZ(147)), '#f1e9d8', INK, 1.6)
    g.rect(FX(0), FZ(155), 220 * S, 8 * S, '#fff', INK, 1.4)                                  # 흰 띠
    g.path('M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Z' % (
        FX(0), FZ(155), FX(0), FZ(192), FX(0), FZ(200), FX(8), FZ(200), FX(212), FZ(200), FX(220), FZ(200), FX(220), FZ(192), FX(220), FZ(155)), '#24242a', INK, 1.6)
    g.line([(FX(2), FZ(196)), (FX(218), FZ(196))], '#6c6c74', .9)                            # 유리 윗면 선
    g.text(FX(110), FZ(128), 'HUROM', 13, 800, '#6b6b72')
    g.rect(FX(96), FZ(122), 28 * S, 10 * S, '#fff', INK, 1.1, rx=7)                          # 열림 단추
    g.text(FX(110), FZ(115), '열림', 9.5, 800, THIN)
    g.circle(FX(96), FZ(99), 2.6, '#f0a23a', INK, .6)                                         # 주황 불빛
    g.text(FX(110), FZ(95.5), '30', 13, 800, '#c8452f')
    g.rect(FX(40), FZ(30), 140 * S, 18 * S, '#e9e0cc', INK, 1.1, rx=5)                        # ② 코드 보관함
    g.rect(FX(100), FZ(24), 20 * S, 4 * S, '#cfc5ae', THIN, .6, rx=3)
    # 숨은선: 열 상자 · 판 · 갈고리 · 잠금 막대
    g.rect(FX(48), FZ(153), 124 * S, 14 * S, 'none', HID, .8, dash='4 3')
    g.rect(FX(48), FZ(169), 124 * S, 6 * S, 'none', HID, .8, dash='4 3')
    for x0 in (36, 178): g.rect(FX(x0), FZ(155), 6 * S, 14 * S, 'none', HID, .9, dash='3 2')
    g.line([(FX(30), FZ(145)), (FX(190), FZ(145))], HID, .9, '8 3 2 3')
    g.line([(FX(110), FZ(206)), (FX(110), FZ(-6))], THIN, .6, '12 3 2 3')                    # 중심선
    # 치수
    g.dimh(FX(0), FX(220), FZ(0) + 34, '220', FZ(0))
    g.dimv(FZ(200), FZ(0), FX(220) + 40, '200', FX(220))
    g.dimv(FZ(200), FZ(155), FX(0) - 18, '45', FX(0), side=-1)
    g.dimv(FZ(155), FZ(147), FX(0) - 18, '8', FX(0), side=-1)
    g.dimv(FZ(147), FZ(0), FX(0) - 18, '147', FX(0), side=-1)
    g.dimh(FX(40), FX(180), FZ(30) - 12, '140 (코드 보관함)', None, 10.5)
    g.dimv(FZ(30), FZ(12), FX(180) + 12, '18', FX(180))
    g.dimv(FZ(122), FZ(112), FX(124) + 30, '10 (단추)', FX(124))
    g.line([(FX(181), FZ(150)), (FX(160), FZ(180))], '#c9c9cf', .7); g.text(FX(158), FZ(182), '앞 갈고리 2 · 잠금 막대(숨은선)', 10.5, 700, '#e8e8ec', 'end')

    # ===== 평면도
    g.text(FX(110), ty0 - 56, '평면도', 14, 800)
    g.rect(FX(0), TY(0), 220 * S, 220 * S, '#24242a', INK, 1.6, rx=14 * S)
    g.rect(FX(3), TY(3), 214 * S, 214 * S, 'none', '#6c6c74', .8, rx=11 * S)
    for x0 in (26, 186):                                                                      # 경첩 팔(뒤 · 뚜껑 홈에 보임)
        g.rect(FX(x0), TY(4), 8 * S, 18 * S, '#e9e0cc', INK, 1, rx=2)
    g.rect(FX(48), TY(48), 124 * S, 124 * S, 'none', '#b6b6bd', .9, dash='5 3')
    for (cx, cy) in CELLS:
        g.circle(FX(cx), TY(cy), DR * S, 'none', '#c9c9cf', 1, '5 3')
        g.line([(FX(cx - 31), TY(cy)), (FX(cx + 31), TY(cy))], '#9a9aa2', .6, '10 2 2 2')
        g.line([(FX(cx), TY(cy - 31)), (FX(cx), TY(cy + 31))], '#9a9aa2', .6, '10 2 2 2')
    g.line([(FX(70), TY(2)), (FX(150), TY(2))], STEAM, 2, '4 2')                              # 뒤 김 슬릿(뒤 면)
    g.text(FX(110), TY(0) - 6, '뒤 김 슬릿 80', 10.5, 700, STEAM)
    g.dimh(FX(0), FX(220), TY(0) - 26, '220', TY(0))
    g.dimv(TY(0), TY(220), FX(0) - 22, '220', FX(0), side=-1)
    # 칸 위치 치수(오른쪽)
    xr = FX(220) + 22
    g.dimv(TY(0), TY(80), xr, '80', FX(220)); g.dimv(TY(80), TY(134), xr, '54', None); g.dimv(TY(134), TY(220), xr, '86', None)
    g.dimh(FX(78.8), FX(141.2), TY(134) + 50, '62.4', None, 10.5)
    g.line([(FX(141.2 + 17.7), TY(134 + 17.7)), (FX(205), TY(200))], THIN, .7); g.text(FX(206), TY(203) + 2, 'Ø50 × 깊이 8 · 3칸(숨은선)', 10.5, 700, '#e8e8ec', 'end')
    g.text(FX(110), TY(30) + 4, '검은 유리 윗면 — 아무것도 없음', 11, 700, '#9a9aa2')

    # ===== 우측면도 (왼쪽 = 앞)
    g.text(SY(110), FZ(0) + 70, '우측면도', 14, 800)
    for y0 in (14, 186): g.rect(SY(y0 + 20), FZ(6), 20 * S, 6 * S, MAT['rub'], INK, .8)
    g.path('M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Z' % (
        SY(220), FZ(147), SY(220), FZ(16), SY(220), FZ(6), SY(210), FZ(6), SY(10), FZ(6), SY(0), FZ(6), SY(0), FZ(16), SY(0), FZ(147)), '#f1e9d8', INK, 1.6)
    g.rect(SY(220), FZ(155), 220 * S, 8 * S, '#fff', INK, 1.4)
    g.path('M%.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (
        SY(220), FZ(155), SY(220), FZ(192), SY(220), FZ(200), SY(212), FZ(200), SY(8), FZ(200), SY(0), FZ(200), SY(0), FZ(192), SY(0), FZ(178), SY(24), FZ(178), SY(24), FZ(155)), '#24242a', INK, 1.6)
    g.line([(SY(218), FZ(196)), (SY(2), FZ(196))], '#6c6c74', .9)
    # 떠 있는 경첩 팔 + 세로 홈 + 축
    g.rect(SY(22), FZ(178), 22 * S, 28 * S, '#e9e0cc', INK, 1.1, rx=3)
    g.rect(SY(11) - 4, FZ(170), 8, 14 * S, '#fff', INK, .9, rx=4)
    g.circle(SY(11), FZ(166), 4, '#3a3a40', INK, .8)
    g.line([(SY(11), FZ(170)), (SY(-30), FZ(186))], THIN, .7); g.text(SY(-32), FZ(186) - 4, '떠 있는 경첩 — 세로 홈 8', 10.5, 700, THIN, 'start')
    g.line([(SY(0), FZ(132)), (SY(-26), FZ(132))], STEAM, 1.6, '4 2', None, 'd2-s'); g.text(SY(-28), FZ(132) + 16, '김(뒤로만)', 10.5, 700, STEAM, 'start')
    g.rect(SY(212), FZ(30), 20 * S, 18 * S, 'none', HID, .8, dash='4 3')                    # 코드 보관함(숨은)
    g.dimh(SY(220), SY(0), FZ(0) + 34, '220', FZ(0))
    g.dimv(FZ(178), FZ(150), SY(0) + 26, '28 (팔)', SY(0))
    g.text(SY(220) + 4, FZ(140), '앞', 11, 800, ACC, 'start'); g.text(SY(0) - 4, FZ(140), '뒤', 11, 800, ACC, 'end')

    title_block(g, 900, 960, '3면도', '1:4 (화면)')
    g.text(30, 1040, '바깥 220 × 220 × 200 · 몸체 147 + 흰 띠 8 + 뚜껑 45 · 모서리 R14(평면) · 점선 = 숨은선(열 상자 · 판 · 칸 · 갈고리 · 잠금 막대) · 무게 약 7kg', 11.5, 700, THIN, 'start')
    return g.svg(1240, 1060)


# ---------------------------------------------------------------- 단면
def section(kind='B'):
    """kind 'B' = B-B 좌우 단면(y = 134, 앞 두 칸 중심, 앞에서 봄) · 'A' = A-A 앞뒤 단면(x = 78.8, 앞 왼쪽 칸 중심, 오른쪽에서 봄 · 왼쪽 = 앞)"""
    S = 2.6
    g = D()
    ox, oz = 150, 40
    if kind == 'B':
        H = lambda u: ox + u * S              # u = x
    else:
        H = lambda u: ox + (220 - u) * S      # u = y (왼쪽 = 앞)
    V = lambda z: oz + (205 - z) * S

    def R(u0, u1, z0, z1, mat, sw=1, rx=0):
        a, b = sorted((H(u0), H(u1)))
        g.rect(a, V(z1), b - a, (z1 - z0) * S, MAT.get(mat, mat), INK, sw, rx)

    # 껍데기(⑩ 몸체 · 흰 띠 · ⑭ 뚜껑 옆 · ⑪ 옆 패널) — 두께 4
    for (u0, u1) in ((0, 4), (216, 220)):
        R(u0, u1, 6, 147, 'plas'); R(u0, u1, 147, 155, 'band'); R(u0, u1, 155, 196, 'plas')
    R(0, 220, 6, 9, 'plas')                                     # 바닥 껍데기
    R(-2, 222, 196, 200, 'glass')                               # 유리 윗면
    for u0 in (14, 186): R(u0, u0 + 20, 0, 6, 'rub')            # 고무발
    R(14, 206, 9, 12, 'steel')                                  # ① 무게판(6 → 그림 3)
    if kind == 'B':
        R(24, 196, 12, 22, 'steel')                             # ⑬ 바닥판
        for u0 in (26, 186):                                    # ⑬ C자 틀 아래 변(절단) + 세운 변(뒤 · 앞, 단면 너머 = 가는 선)
            R(u0, u0 + 8, 22, 34, 'steel')
            g.rect(H(u0), V(158), 8 * S, (158 - 34) * S, 'none', '#4f5864', 1, dash='7 3')
        R(14, 17, 60, 110, 'board')                             # ⑨ 보드(왼 벽)
        g.rect(H(160), V(64), 34 * S, 24 * S, 'none', '#5b6470', 1.1, dash='5 3')     # ③ 모터(y 70..114, 너머)
        g.circle(H(130), V(52), 18 * S, 'none', '#5b6470', 1.1, '5 3')                 # ④ 캠(너머)
        g.line([(H(152), V(72)), (H(110), V(72))], '#5b6470', 2, '5 3')               # 레버
        g.line([(H(110), V(72)), (H(110), V(137))], '#5b6470', 2.4, '5 3')            # 푸시 로드
        hb0, hb1 = 38, 182
    else:
        R(188, 14, 12, 22, 'steel')                             # ⑬ 바닥판(앞은 코드 보관함까지)
        R(192, 212, 12, 30, 'plas')                             # ② 코드 보관함
        g.rect(H(212), V(28), 18 * S, 14 * S, PAPER, INK, .8)
        g.line([(H(114), V(64)), (H(70), V(64))], '#5b6470', 1.1, '5 3'); g.line([(H(114), V(40)), (H(70), V(40))], '#5b6470', 1.1, '5 3')   # 모터(너머)
        g.circle(H(92), V(52), 18 * S, 'none', '#5b6470', 1.1, '5 3')                  # ④ 캠(너머 · x 130)
        g.line([(H(92), V(72)), (H(92), V(137))], '#5b6470', 2.4, '5 3')              # 푸시 로드(너머 · x 110)
        # 뒤: 김 덕트 · 슬릿 · 경첩 팔 · 축
        R(26, 38, 128, 150, 'steel', .8)
        g.rect(H(8), V(136), 4 * S, 8 * S, PAPER, 'none', 0)                         # 뒤 슬릿(구멍)
        g.rect(H(22), V(178), 18 * S, 28 * S, 'none', '#4f5864', 1, dash='7 3')      # 경첩 팔(너머 · x 26)
        g.circle(H(10), V(166), 2.4 * S, '#3a3a40', INK, .8)                          # 경첩 축
        g.rect(H(10) - 4, V(172), 8, 12 * S, 'none', INK, .8, rx=4)                   # 세로 홈
        # 앞: 잠금 막대(절단) · 갈고리(너머)
        R(197, 203, 142, 148, 'steel')
        g.line([(H(203), V(155)), (H(203), V(141)), (H(199), V(141))], '#4f5864', 2.4, '5 3')
        hb0, hb1 = 38, 182
    # ⑧ 열 상자(강판 + 단열) · 위 열림
    R(hb0, hb0 + 6, 115, 155, 'ins'); R(hb1 - 6, hb1, 115, 155, 'ins'); R(hb0, hb1, 115, 121, 'ins')
    if kind == 'A':
        g.rect(H(44) - 1, V(152), 2, 6 * S, PAPER, 'none', 0)                         # (뒤 벽 김 구멍은 x 100..120 — 표시만)
    # ⑤ 받침(누름 +10 → 137..149) + 히터 단면
    R(48, 172, 137, 149, 'alu', 1.2)
    for u in ((62, 92, 128, 158) if kind == 'B' else (60, 90, 130, 160)):
        g.circle(H(u), V(143), 3 * S, MAT['heat'], INK, .8)
    # ⑥ 아래 판 149..163 · 칸(둥근 바닥 깊이 8)
    dishes = [78.8, 141.2] if kind == 'B' else [134]
    a, b = sorted((H(48), H(172)))
    top, bot = V(163), V(149)
    d = 'M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z' % (a, bot, a, top, b, top, b, bot)
    g.path(d, MAT['alu'], INK, 1.2)
    for c in dishes:
        pts = ['%.1f,%.1f' % (H(c + k), V(163 - 8 * (1 - (k / DR) ** 2))) for k in range(-25, 26)]
        g.a('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.1"/>' % (' '.join(pts), PAPER, INK))
    # 손가락 홈(B 만 보임)
    if kind == 'B':
        for u in (48, 169): g.rect(H(u), V(160), 3 * S, 5 * S, PAPER, INK, .7)
    # ⑫ 위 판 163..169 + 볼록(아래로 6) · 쌀 2mm
    R(48, 172, 163, 169, 'alu', 1.2)
    for c in dishes:
        pts = ['%.1f,%.1f' % (H(c + k), V(163 - 6 * (1 - (k / 22.0) ** 2))) for k in range(-22, 23)]
        g.a('<polygon points="%s" fill="url(#d2-alu)" stroke="%s" stroke-width="1.1"/>' % (' '.join(pts), INK))
        for k in range(-18, 19, 4):
            zr = 163 - 8 * (1 - (k / DR) ** 2)
            g.circle(H(c + k), V(zr + 1.3), 1.1 * S, '#f3eddc', '#a89c80', .6)
    # ⑦ 위 열판 169..179 + 히터 · ⑧ 뚜껑 단열 179..184 · ⑬ 뚜껑 보 184..195
    R(44, 176, 169, 179, 'alu', 1.2)
    for u in ((62, 92, 128, 158) if kind == 'B' else (60, 90, 130, 160)):
        g.circle(H(u), V(174.5), 2.6 * S, MAT['heat'], INK, .8)
    R(38, 182, 179, 184, 'ins')
    if kind == 'B': R(22, 198, 184, 195, 'steel')
    else: R(206, 10, 184, 195, 'steel')
    # 밀봉선(위 판 면 163 · 굵은 금색)
    g.line([(H(48), V(163)), (H(172), V(163))], ACC, 2.2)

    # ---- 힘 · 김 화살
    if kind == 'B':
        g.line([(H(110), V(152)), (H(110), V(160))], '#4f5864', 2.2, None, None, 'd2-f')
        g.line([(H(110), V(184)), (H(110), V(194))], '#4f5864', 2.2, None, None, 'd2-f')
        g.line([(H(30), V(186)), (H(30), V(40))], '#4f5864', 2, '8 4', None, 'd2-f')
    else:
        g.line([(H(134) + 36, V(170)), (H(60), V(161)), (H(46), V(153)), (H(32), V(140)), (H(4), V(140)), (H(-14), V(140))], STEAM, 1.8, '5 3', None, 'd2-s')

    # ---- 높이 자(왼쪽 · z 값)
    zs = [0, 6, 12, 22, 115, 121, 137, 149, 155, 163, 169, 179, 184, 195, 200] if kind == 'B' else [0, 12, 30, 115, 137, 149, 155, 163, 169, 184, 200]
    xr = ox - 40
    g.line([(xr, V(0)), (xr, V(200))], INK, .9)
    for z in zs:
        g.line([(xr - 5, V(z)), (xr + 5, V(z))], INK, .9)
        g.text(xr - 9, V(z) + 4, str(z), 10.5, 700, THIN, 'end')
    g.text(xr, V(200) - 14, 'z (mm)', 10.5, 800, THIN)
    # ---- 풍선(번호 = 2.5D · 3D · 본문과 같음)
    W = 1240
    if kind == 'B':
        B = [  # (u, z, 풍선 x, 풍선 y, 번호, 메모, 쪽)
            (120, 198, 1000, 60, '⑭', '뚜껑 45 · 검은 유리 윗면 4', 'L'),
            (150, 190, 1000, 100, '⑬', '뚜껑 보 11t — 힘을 경첩 · 갈고리로', 'L'),
            (150, 181.5, 1000, 140, '⑧', '뚜껑 단열 5 · 열 상자 단열 6', 'L'),
            (150, 176, 1000, 180, '⑦', '위 열판 10 · 시즈 히터 450W · NTC', 'L'),
            (165, 166, 1000, 220, '⑫', '위 판 6 · 볼록 6 · 전선 없음', 'L'),
            (165, 156, 1000, 260, '⑥', '아래 판 14 · 칸 Ø50 × 8 · 쌀 2mm', 'L'),
            (165, 143, 1000, 300, '⑤', '받침 12 · 히터 450W · 판 감지', 'L'),
            (178, 130, 1000, 340, '⑧', '열 상자 144 × 144 × 40 · 위 열림', 'L'),
            (190, 28, 1000, 470, '⑬', 'C자 틀 8t × 2 · 바닥판 10t', 'L'),
            (178, 52, 1000, 420, '③', '모터(너머 · 점선)', 'L'),
            (196, 10, 1000, 520, '①', '무게판 · 고무발 4', 'L'),
            (15.5, 85, 40, 330, '⑨', '', 'R'),
            (130, 60, 40, 400, '④', '', 'R'),
            (2, 100, 40, 250, '⑪', '', 'R'),
            (2, 151, 40, 180, '⑩', '', 'R'),
        ]
    else:
        B = [
            (110, 198, 1000, 60, '⑭', '뚜껑 · 뒤 = 떠 있는 경첩 축', 'L'),
            (120, 190, 1000, 100, '⑬', '뚜껑 보 11t → 뒤 축 · 앞 갈고리', 'L'),
            (150, 176, 1000, 150, '⑦', '위 열판 · 히터', 'L'),
            (150, 166, 1000, 190, '⑫', '위 판 · 볼록 1(단면)', 'L'),
            (110, 156, 1000, 230, '⑥', '아래 판 · 앞 칸 단면', 'L'),
            (90, 143, 1000, 270, '⑤', '받침 · 히터(+10 올라간 상태)', 'L'),
            (40, 130, 1000, 320, '⑧', '열 상자 · 뒤 벽 위 김 구멍 Ø8 × 2', 'L'),
            (200, 145, 1000, 380, '⑬', '잠금 막대(단면) · 앞 갈고리(점선)', 'L'),
            (202, 21, 1000, 440, '②', '코드 보관함 · 열 상자 밖', 'L'),
            (100, 17, 1000, 490, '⑬', '바닥판 10t', 'L'),
            (92, 52, 40, 400, '④', '', 'R'),
        ]
    for (u, z, bx, by, n, note, side) in B:
        if side == 'L':
            g.balloon(H(u), V(z), bx, by, n, note, 'start')
        else:
            g.balloon(H(u), V(z), bx, by, n, None)
    # 범례
    ly = 585
    for i, (m, t) in enumerate([('steel', '강 · 스테인리스'), ('alu', '알루미늄'), ('ins', '단열재'), ('plas', '수지 껍데기'), ('glass', '강화유리'), ('heat', '시즈 히터')]):
        x = 150 + i * 150
        g.rect(x, ly, 26, 16, MAT[m], INK, .8); g.text(x + 34, ly + 13, t, 11.5, 700, THIN, 'start')
    g.line([(1050, ly + 8), (1080, ly + 8)], ACC, 2.2); g.text(1086, ly + 13, '밀봉면', 11.5, 700, THIN, 'start')
    name = '단면 B-B (y 134)' if kind == 'B' else '단면 A-A (x 78.8)'
    note = ('③ 누르는 상태 · 앞 두 칸 중심을 좌우로 자름 · 회색 화살 = 힘(칸 → 위 판 → 위 열판 → 뚜껑 보 → C자 틀 → 바닥판) · 점선 = 단면 너머의 부품'
            if kind == 'B' else
            '③ 누르는 상태 · 앞 왼쪽 칸 중심을 앞뒤로 자름(왼쪽 = 앞) · 주황 점선 = 김(뻥 뒤 두 판 사이 → 뒤 벽 위 구멍 → 덕트 → 뒤 슬릿)')
    title_block(g, 900, 616, name, '1:2 (화면)')
    g.text(150, 640, note, 11.5, 700, THIN, 'start')
    g.text(150, 660, '쌀: 숟가락 3g → 칸 한 겹 → 볼록이 2mm로 누름 → 220°C 8~10초 → 절벽 −9 → 칸 안 떡뻥 9~11mm → 뚜껑 열고 집기', 11.5, 700, THIN, 'start')
    return g.svg(W, 720)


def detail():
    """상세 — 칸 하나(앞 왼쪽 Ø50) · 세 상태: 쉼 · ③ 누름 · ④ 뻥. 5:1(화면)"""
    S = 4.2
    g = D()
    states = [('쉼 — 쌀 넣고 닫음', 153, '틈 12'), ('③ 누름 +10 — 밀봉 · 220°C 8~10초', 163, '쌀 2'), ('④ 뻥 −9 — 절벽', 154, '떡뻥 11')]
    for i, (name, ptop, gap) in enumerate(states):
        x0 = 40 + i * 400
        H = lambda k: x0 + 180 + k * S
        V = lambda z: 40 + (175 - z) * S
        g.text(x0 + 180, 30, name, 13.5, 800)
        # 위 판 ⑫ (163..169) + 볼록(157..163)
        g.rect(H(-40), V(169), 80 * S, 6 * S, 'url(#d2-alu)', INK, 1.1)
        pts = ['%.1f,%.1f' % (H(k), V(163 - 6 * (1 - (k / 22.0) ** 2))) for k in range(-22, 23)]
        g.a('<polygon points="%s" fill="url(#d2-alu)" stroke="%s" stroke-width="1.1"/>' % (' '.join(pts), INK))
        # 아래 판 ⑥ (ptop-14 .. ptop) + 칸 깊이 8
        bot = ptop - 14
        pts = ['%.1f,%.1f' % (H(-40), V(bot)), '%.1f,%.1f' % (H(-40), V(ptop))] + ['%.1f,%.1f' % (H(k), V(ptop - 8 * (1 - (k / 25.0) ** 2))) for k in range(-25, 26)] + ['%.1f,%.1f' % (H(40), V(ptop)), '%.1f,%.1f' % (H(40), V(bot))]
        g.a('<polygon points="%s" fill="url(#d2-alu)" stroke="%s" stroke-width="1.1"/>' % (' '.join(pts), INK))
        # 쌀 · 떡뻥
        if i == 0:
            for k in range(-16, 17, 4): g.circle(H(k), V(ptop - 8 * (1 - (k / 25.0) ** 2) + 1.4), 1.3 * S, '#f3eddc', '#a89c80', .7)
        elif i == 1:
            pts = ['%.1f,%.1f' % (H(k), V(155 + 8 * (k / 25.0) ** 2)) for k in range(-22, 23)] + ['%.1f,%.1f' % (H(k), V(163 - 6 * (1 - (k / 22.0) ** 2))) for k in range(22, -23, -1)]
            g.a('<polygon points="%s" fill="#f3eddc" stroke="#a89c80" stroke-width=".8"/>' % ' '.join(pts))
            g.line([(H(-40), V(163)), (H(40), V(163))], ACC, 2.4)
            g.text(H(0), V(136), '칸이 막혀 물기가 끓음 · 칸 안 0.5~1.5MPa', 11.5, 800, '#c8452f')
        else:
            pts = ['%.1f,%.1f' % (H(k), V(154 - 8 * (1 - (k / 25.0) ** 2))) for k in range(-24, 25)] + ['%.1f,%.1f' % (H(k), V(min(163, 163 - 6 * (1 - (k / 22.0) ** 2)) - .3)) for k in range(24, -25, -1)]
            g.a('<polygon points="%s" fill="#f0e2bf" stroke="#a88a4a" stroke-width="1"/>' % ' '.join(pts))
            g.line([(H(-26), V(158.5)), (H(-38), V(158.5))], STEAM, 1.6, '4 2', None, 'd2-s')
            g.text(H(-32), V(172), '김 → 두 판 사이 → 뒤', 11, 800, STEAM)
        # 치수: 볼록 끝 157 ↔ 칸 바닥
        cb = ptop - 8
        if i != 1:
            g.dimv(V(157), V(cb), H(30), gap, H(0), 11.5)
        else:
            g.dimv(V(157), V(155), H(30), gap, H(0), 11.5)
        if i == 0:
            g.dimv(V(163), V(153), H(-48), '10', H(-40), 11.5, -1)
        # 받침 ⑤ 표시
        g.rect(H(-40), V(bot), 80 * S, 4 * S, 'url(#d2-alu)', INK, .8, op=.6)
        g.text(H(-40) + 6, V(bot - 4) - 6, '⑤ 받침', 11, 700, THIN, 'start')
        g.text(H(40) + 4, V(166) + 4, '⑫', 12, 800, INK, 'start'); g.text(H(40) + 4, V(ptop - 7) + 4, '⑥', 12, 800, INK, 'start')
    g.text(40, 300, '볼록 끝은 늘 z 157(뚜껑 안 고정) · 움직이는 건 받침 + 아래 판 한 덩어리 · 쉼 153 → 누름 163(두 판이 닿아 칸이 막힘) → 절벽 154 · 떡뻥 두께 = 볼록 끝 ↔ 칸 바닥 틈', 11.5, 700, THIN, 'start')
    return g.svg(1240, 320)


if __name__ == '__main__':
    import os, sys
    sys.stdout.reconfigure(encoding='utf-8')
    here = os.path.dirname(os.path.abspath(__file__))
    for n, f in (('d2_three', three_view), ('d2_bb', lambda: section('B')), ('d2_aa', lambda: section('A')), ('d2_detail', detail)):
        open(os.path.join(here, n + '.svg'), 'w', encoding='utf-8').write(f()); print('svg', n)
