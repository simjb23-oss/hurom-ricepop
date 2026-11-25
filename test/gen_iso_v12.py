# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 v12 (2026-11-25) — 「두꺼운 뚜껑 · 위아래 판 2장 · 얕은 칸」 구조(사진 8장과 같은 구조)
근거: 준보 사진(뚜껑 연 msg_e3098df3 · 색 5종 · 쌀 넣기 · 터치 · 세척 msg_2d24036c · 대표 msg_27c4e268) · 두팔 위임 msg_7b7a07c4
r11 에서 뺀 것: 관통 틀 · 플러그 · 피스톤 · 피스톤 머리 · 긁개 링 · 안내 핀 · 기둥 머리 잠금 핀 · 꺼내기 +16 · 뚜껑 위 터치

좌표(mm): x 0..220 왼→오, y 0..220 뒤→앞, z 0..200 아래→위. 보는 방향 = 앞·오른쪽·위.
3칸 Ø50 · 깊이 8 얕은 접시(둥근 바닥 · 곧은 벽 없음) · 중심 뒤 1 (110, 80) · 앞 2 (78.8, 134) (141.2, 134)
부품 번호(모든 그림 · 3D · 본문 공통):
 ① 바닥 무게판 · 고무발 · 기울기 센서  ② 코드 보관함(바닥 앞 · 열 상자 밖)  ③ 모터(웜 기어드 · 바닥 오른쪽)
 ④ 달팽이 캠 + 레버(1:2) + 푸시 로드(벨로즈) + 되돌림 스프링 2 + 캠 위치 센서
 ⑤ 아래 열판 = 받침 124 × 124 × 12(속 시즈 히터 450W · 온도 퓨즈 250°C · 판 감지 자석 스위치) — 캠으로 오르내림
 ⑥ 아래 판 = 알루미늄 124 × 124 × 14 · 얕은 칸 Ø50 × 8 셋(뒤 1 · 앞 2) · 손가락 홈 2 · 나사 없음 · 받침에 얹힘 · 테두리보다 2mm 낮음 · 떼어 씻음
 ⑦ 위 열판 = 뚜껑 안 고정 블록(속 시즈 히터 450W · NTC) — 전선은 여기까지
 ⑧ 열 상자(강판 + 단열 · 위 열림 · 뒤 벽 위 김 구멍 2) + 뚜껑 안 단열
 ⑨ 제어 보드  ⑩ 몸체 · 흰 띠 · 앞면(HUROM · 열림 단추 · 주황 불빛 + 숫자 2) · 김 덕트 · 뒤 김 슬릿  ⑪ 옆 패널 4장 · 비스포크
 ⑫ 위 판 = 알루미늄 124 × 124 × 6 · 얕은 볼록 셋(높이 6 · 경첩 쪽 1 · 먼 쪽 2 → 닫으면 뒤 1 · 앞 2) · 전선 없음 · 뒤 걸이 2 · 앞 스프링 걸쇠 · 실리콘 손잡이 2 · 떼어 씻음
 ⑬ 강철 틀 = 바닥판 10t + 양옆 C자 틀 8t 두 장(뒤 경첩 ~ 앞 걸림 ~ 바닥판) + 뚜껑 보 11t(뚜껑 안) + 앞 갈고리 2(뚜껑) + 잠금 막대(솔레노이드)
 ⑭ 뚜껑 45mm = 검은 유리 윗면 + 껍데기 + 떠 있는 경첩(세로 홈 · 댐퍼) + 위 판 떼는 단추(안쪽 앞 테)
높이(z): 고무발 0..6 · 무게판 6..12 · 틀 바닥판 12..22 · 코드 보관함 12..30(앞) · 캠 · 레버 · 모터 칸 22..115 · 열 상자 바닥 115..121 · 열 상자 벽 121..155(위 열림)
 · 받침 ⑤ 127..139(히터 130..136) · 아래 판 ⑥ 139..153(칸 바닥 145 · 윗면 153 = 테두리 155보다 2 낮음) · 몸체 테 · 흰 띠 147..155
 · 뚜껑 155..200: 위 판 ⑫ 163..169(볼록 157..163) · 위 열판 ⑦ 169..179(히터 172..177) · 단열 179..184 · 뚜껑 보 184..195 · 유리 196..200
 · 앞면: 흰 띠 147..155 · HUROM 130 · 열림 단추 112..122 · 불빛 + 숫자 95..103 · 코드 보관함 12..30
 · C자 틀 x 26..34 · 186..194, y 14..206, z 22..158 · 경첩 팔(뒤) z 150..172 · 세로 홈 8 · 앞 갈고리 x 36..42 · 178..184 · z 141..155 · 잠금 막대 y 200 · z 145
행정(⑤ + ⑥ 한 덩어리): 쉼(⑥ 윗면 153) → +10 누름(163 = 위 판 면에 닿아 세 칸이 막힘 · 볼록 끝 157 ↔ 칸 바닥 155 → 쌀 2mm) → 멈춤 8~10초
 → 캠 절벽 −9 뻥(⑥ 윗면 154 · 칸 바닥 146 · 볼록 끝 157 → 틈 11 = 떡뻥 9~11mm) → 받침 제자리 · 김 3초 → 잠금 풀림 · 앞 단추로 뚜껑 2cm 들림 → 사람이 열고 집기 → 쉼(−1)
힘: 칸 안 압력 0.5~1.5MPa × 19.6cm² × 3 = 2.9~8.8kN → ⑫ 위 판 → ⑦ 위 열판 → 뚜껑 보 ⑬ → (뒤) 경첩 축 · (앞) 갈고리 2 + 잠금 막대 → C자 틀 2 → 바닥판 → 캠 축 ④ → 레버 → 푸시 로드 → 받침 ⑤ → ⑥ 아래 판. 껍데기엔 힘 없음
김: 칸 안(막힘) → 절벽에서 칸이 열림 → 위 판과 아래 판 사이 틈 → 뒤 벽 위 김 구멍 2 → 덕트 → 뒤 김 슬릿 (+ 뚜껑이 2cm 들릴 때 조금)
쌀: 숟가락 3g → 칸(아래 판 위 한 겹) → 누르기 · 뻥 → 칸 안 떡뻥 → 뚜껑 열고 집기. 기계 안을 흐르는 쌀 없음
"""
import sys, os, math
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_iso import Iso, shade, DEFS, FONT, PANEL, BODY, BAND, GLASS, STEEL, PLATE, HEAT, MOLD, CRACK, DARK, MOTOR, BOARD, RICE, INSUL, RED, HTR, hollow

FRAME = '#4f5864'; LID = '#26262b'; ALU = '#d5d9de'; SIL = '#8d9096'
UP, DROP = 10, 9
CELLS = [(110, 80), (78.8, 134), (141.2, 134)]   # 뒤 1 · 앞 2
DR = 25          # 칸 · 볼록 반지름
PZ0 = 139        # 아래 판 밑면(쉼)

def circ(cx, cy, z, r, n=28, cut=None):
    return [(cx + r * math.cos(2 * math.pi * i / n), (min(cy + r * math.sin(2 * math.pi * i / n), cut) if cut else cy + r * math.sin(2 * math.pi * i / n)), z) for i in range(n)]

def dish(I, cx, cy, ztop, cut=None, rice=False, cake=False):
    """얕은 접시 칸(Ø50 · 깊이 8) — 윗면 테두리 원 + 안쪽 둥근 바닥(그림자)"""
    I.poly(circ(cx, cy, ztop, DR, cut=cut), shade(ALU, -.25), '#6a6f76', .8)
    I.poly(circ(cx, cy + 3, ztop - 4, DR * .72, cut=cut), shade(ALU, -.12), 'none', 0)
    I.poly(circ(cx, cy + 5, ztop - 7, DR * .42, cut=cut), shade(ALU, -.02), 'none', 0)
    if cake: I.cylz(cx, cy, ztop - 6, DR - 2, 9, CRACK, sw=.6)
    if rice:
        for k in range(6):
            sx, sy = I.P(cx - 14 + k * 5.6, cy - 4 + (k % 2) * 7, ztop - 6)
            I.out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="%s" stroke="#b9b2a2" stroke-width=".6"/>' % (sx, sy, RICE))

def cam_pts(cx, y, cz, phase=0.0, seg=36):
    pts = []
    for i in range(seg):
        a = 2 * math.pi * i / seg; t = ((a / (2 * math.pi)) + phase) % 1.0
        r = 10 + 8 * (t if t < 0.92 else 0)
        pts.append((cx, y + r * math.cos(a), cz + r * math.sin(a)))
    return pts

def cframe(I, x0, ghost=False):
    """⑬ C자 틀(옆 판 8t): 아래 바닥판 ~ 뒤 경첩 팔 ~ 앞 걸림 귀. 가운데는 비움(ㄷ자)"""
    I.box(x0, 14, 22, 8, 192, 12, FRAME)          # 아래 변
    I.box(x0, 14, 34, 8, 14, 124, FRAME)          # 뒤 변(경첩까지)
    I.box(x0, 192, 34, 8, 14, 124, FRAME)         # 앞 변(걸림 귀)

def cutaway():
    CUT = 134
    I = Iso(1.5, 560, 268, cut_y=CUT)
    W = 220
    # ---- 껍데기 뒤 벽 · 바닥 · 왼 벽 (몸체 0..147 · 흰 띠 147..155 · 뚜껑 155..196 · 유리 196..200)
    for (z0, h, col) in [(0, 147, PANEL), (147, 8, BAND), (155, 41, LID)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))
    for (z0, h, col) in [(0, 147, PANEL), (147, 8, BAND), (155, 41, LID)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col)
    I.poly([(70, 8, 128), (150, 8, 128), (150, 8, 136), (70, 8, 136)], '#2b2b30', 'none', 0, .85)    # 뒤 김 슬릿
    I.box(96, 26, 128, 28, 12, 22, STEEL, op=.9)                                                     # 김 덕트
    # ---- 바닥 칸: 무게판 · 바닥판 · 보드 · 모터 · 캠 · 레버 · 푸시 로드
    I.box(14, 14, 6, 192, 192, 6, STEEL)
    I.box(24, 14, 12, 172, 192, 10, FRAME)                                      # ⑬ 바닥판
    I.box(14, 50, 60, 3, 90, 50, BOARD)                                         # ⑨ 보드
    I.box(160, 70, 40, 34, 44, 24, MOTOR)                                       # ③ 모터
    I.line([(160, 92, 52), (138, 92, 52)], MOTOR, 5)
    I.poly(cam_pts(130, 92, 52, 0.3), MOTOR, '#2b2b30', 0.9, .95)               # ④ 캠
    I.box(148, 88, 22, 8, 8, 50, FRAME)                                         # 레버 받침
    I.line([(152, 92, 72), (110, 92, 72)], MOTOR, 4.5)                          # 레버
    I.line([(110, 92, 72), (110, 92, 127)], MOTOR, 5)                           # 푸시 로드
    I.box(100, 88, 40, 8, 8, 6, DARK)                                           # 캠 위치 센서
    # ---- C자 틀(왼) · 열 상자(뒤 · 왼 · 바닥) · 김 구멍 2
    cframe(I, 26)
    I.box(38, 38, 115, 144, 6, 40, INSUL)
    for x0 in (100, 112): I.poly([(x0, 44.2, 146), (x0 + 8, 44.2, 146), (x0 + 8, 44.2, 152), (x0, 44.2, 152)], '#2b2b30', 'none', 0, .9)
    I.box(38, 44, 115, 6, 132, 40, INSUL)
    I.box(44, 44, 115, 132, 132, 6, INSUL, top=shade(INSUL, -.08))
    # ---- ⑤ 받침(쉼) · 히터 · 퓨즈 · 판 감지
    I.box(48, 48, 127, 124, 124, 12, PLATE)
    I.box(54, 76, 130, 112, 16, 6, HTR, hatch_cut=False, faces='l')
    I.box(160, 60, 129, 6, 8, 8, RED, hatch_cut=False)
    I.line([(60, 100, 121), (60, 100, 127)], HEAT, 2.4, '3 2'); I.line([(160, 100, 121), (160, 100, 127)], HEAT, 2.4, '3 2')
    # ---- ⑥ 아래 판(쉼 · 윗면 153) + 얕은 칸 3 + 마른 쌀
    I.box(48, 48, PZ0, 124, 124, 14, ALU)
    for (cx, cy) in CELLS: dish(I, cx, cy, 153, cut=CUT, rice=True)
    I.box(48, 104, 146, 3, 16, 5, DARK, hatch_cut=False)                       # 손가락 홈(왼)
    for (cx, cy) in CELLS[1:]:                                                 # 절단면의 칸 단면(둥근 바닥 · 깊이 8)
        I.poly([(cx + d, CUT, 153 - 8 * (1 - (d / DR) ** 2)) for d in range(-25, 26, 2)], '#f7f2e8', '#6a6f76', 1)
        for k in range(5): sx, sy = I.P(cx - 12 + k * 6, CUT, 146.5 + abs(k - 2) * .8); I.out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="%s" stroke="#b9b2a2" stroke-width=".6"/>' % (sx, sy, RICE))
    # ---- ⑭ 뚜껑 안: ⑫ 위 판 + 볼록 · ⑦ 위 열판 · ⑧ 단열 · ⑬ 뚜껑 보 · 걸이 · 떼는 단추
    for (cx, cy) in CELLS: I.cylz(cx, min(cy, CUT - 1), 157, DR - 3, 6, ALU)
    I.box(48, 48, 163, 124, 124, 6, ALU)
    I.box(52, 46, 160, 10, 6, 6, DARK); I.box(158, 46, 160, 10, 6, 6, DARK)    # 뒤 걸이 2
    for (cx, cy) in CELLS[1:]:                                                 # 절단면의 볼록 단면(높이 6)
        I.poly([(cx + d, CUT, 163 - 6 * (1 - (d / (DR - 3)) ** 2)) for d in range(-22, 23, 2)], ALU, '#6a6f76', 1)
    I.box(44, 44, 169, 132, 132, 10, PLATE)
    I.box(50, 76, 172, 120, 16, 5, HTR, hatch_cut=False, faces='l')
    I.box(166, 60, 172, 6, 8, 6, HEAT, hatch_cut=False)                        # NTC
    I.box(38, 38, 179, 144, 144, 5, INSUL)
    I.box(22, 10, 184, 176, 196, 11, FRAME)                                    # ⑬ 뚜껑 보
    # ---- 경첩 팔(뒤 · C자 틀 위) + 세로 홈 + 댐퍼
    for x0 in (26, 186):
        I.box(x0, 4, 150, 8, 18, 24, FRAME)
        I.line([(x0 + 8, 10, 156), (x0 + 8, 10, 168)], '#15151a', 3)
    I.line([(26, 10, 166), (194, 10, 166)], DARK, 4)                           # 경첩 축
    I.box(60, 12, 152, 20, 8, 8, MOTOR)                                         # 댐퍼
    # ---- 김 길 · 힘 길
    I.line([(110, 80, 156), (110, 60, 152), (110, 46, 150)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    I.line([(110, 38, 150), (110, 30, 140), (110, 10, 132), (110, -14, 132)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    I.line([(141, 110, 140), (141, 110, 158)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(141, 110, 172), (141, 110, 188)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(190, 20, 175), (190, 20, 26)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    I.line([(60, 110, 120), (60, 110, 136)], HEAT, 1.8, None, 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')
    # ---- 오른 벽 · C자 틀(오른)
    cframe(I, 186)
    I.box(176, 44, 115, 6, 132, 40, INSUL)
    for (z0, h, col) in [(0, 147, PANEL), (147, 8, BAND), (155, 41, LID)]:
        I.box(212, 8, z0, 8, 212, h, col)
    I.box(-2, -2, 196, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    # ---- 앞 고스트: 앞면 · 갈고리 · 잠금 막대 · 칸 앞 절반
    I.ghost_box(0, CUT, 0, 220, 220 - CUT, 200)
    I.line([(40, 220, 12), (180, 220, 12), (180, 220, 30), (40, 220, 30), (40, 220, 12)], '#8a8a90', 1.2, '4 3')   # ② 코드 보관함
    I.line([(60, 220, 147), (160, 220, 147)], '#8a8a90', 1, '3 3')
    I.line([(96, 220, 112), (124, 220, 112), (124, 220, 122), (96, 220, 122), (96, 220, 112)], '#8a8a90', 1.2, '3 3')   # 열림 단추
    I.line([(98, 220, 99), (122, 220, 99)], HEAT, 3)                                                            # 불빛 · 숫자
    for x0 in (36, 178): I.line([(x0 + 3, 200, 155), (x0 + 3, 200, 141), (x0 + 7, 200, 141)], '#6a6a70', 3)     # 앞 갈고리 2
    I.line([(30, 200, 145), (190, 200, 145)], '#6a6a70', 2.4, '6 3')                                            # 잠금 막대
    for (cx, cy) in CELLS[1:]:
        I.line([(cx + DR * math.cos(2 * math.pi * k / 24), cy + DR * math.sin(2 * math.pi * k / 24), 153) for k in range(25) if math.sin(2 * math.pi * k / 24) >= -0.05], '#9aa3ad', 1, '3 3')
    I.line([(200, 200, 200), (200, 170, 236)], HEAT, 1.6, '4 3', 1, marker='marker-end="url(#arr)"')
    # ---- 라벨
    R = 820; L = 330
    I.label((110, 110, 200), R, 56, '⑭ 뚜껑 45mm — 검은 유리 윗면 · 떠 있는 경첩(뒤)', '윗면엔 아무것도 없음 · 열림은 몸체 앞 단추 · 마지막 2cm는 수평으로 내려옴', 'r')
    I.label((160, 110, 190), R, 102, '⑬ 뚜껑 보 11t — 뒤는 경첩 축, 앞은 갈고리 2', '누르는 힘 2.9~8.8kN이 보 → 경첩 · 갈고리 → C자 틀 → 바닥판(회색 화살)', 'r')
    I.label((160, 110, 182), R, 148, '⑧ 뚜껑 안 단열 5 — 위 열판 위', None, 'r')
    I.label((160, 90, 175), R, 184, '⑦ 위 열판 — 뚜껑 안 고정 · 속 시즈 히터 450W · NTC', '전선은 여기까지 · 위 판엔 전선이 없음', 'r')
    I.label((150, 110, 166), R, 230, '⑫ 위 판 — 알루미늄 6t · 얕은 볼록 3(높이 6) · 떼어 씻음', '뒤 걸이 2 + 앞 걸쇠 · 단추 누르고 실리콘 손잡이로 당김 · 50°C 넘으면 단추 잠김', 'r')
    I.label((150, 110, 150), R, 276, '⑥ 아래 판 — 알루미늄 14t · 얕은 칸 Ø50 × 8 셋(뒤 1 · 앞 2)', '받침에 얹힘 · 테두리보다 2mm 낮음 · 손가락 홈 2로 들어 뺌', 'r')
    I.label((160, 110, 133), R, 322, '⑤ 받침 12t — 속 시즈 히터 450W · 온도 퓨즈 · 판 감지', '⑥과 한 덩어리로 +10 누름 → −9 뻥(주황 ↕)', 'r')
    I.label((110, 92, 100), R, 372, '④ 달팽이 캠 + 레버(1:2) + 푸시 로드(벨로즈)', '올림 10 → 멈춤 8~10초 → 절벽 9mm(뻥) → 제자리 · 위치 센서', 'r')
    I.label((190, 92, 52), R, 418, '③ 모터(웜 기어드) — 바닥 오른쪽 · 자기 잠금', None, 'r')
    I.label((194, 110, 100), R, 454, '⑬ C자 틀 8t × 2 — 경첩 팔 · 앞 걸림 귀 · 바닥판을 이음', '몸체 안쪽에 숨김 · 겉 껍데기엔 힘이 걸리지 않음', 'r')
    I.label((206, 110, 9), R, 500, '① 바닥 무게판 + 고무발 · 기울기 센서', None, 'r')
    I.label((30, 10, 168), L, 110, '⑭ 떠 있는 경첩 — 팔의 세로 홈 + 댐퍼', '뚜껑이 수평으로 내려와 볼록이 칸에 똑바로', 'l')
    I.label((110, 8, 132), L, 162, '⑩ 뒤 김 슬릿 — 김은 뒤로만', None, 'l')
    I.label((104, 44.2, 149), L, 198, '⑧ 뒤 벽 위 김 구멍 Ø8 × 2 → 덕트', None, 'l')
    I.label((15, 100, 85), L, 240, '⑨ 제어 보드 — 온도 · 잠금 · 판 감지 · 캠 위치', None, 'l')
    I.label((39, 200, 148), L, 290, '⑬ 앞 갈고리 2 + 잠금 막대(점선)', '닫으면 막대가 갈고리를 잡음 · 누르고 「뻥」 하는 동안 안 풀림', 'l')
    I.label((110, 220, 117), L, 340, '⑩ 앞면 — HUROM · 열림 단추 · 주황 불빛 + 숫자 2', '남은 초를 셈(30 → 0) · 점선 = 잘라낸 앞 절반', 'l')
    I.label((60, 110, 128), L, 390, '움직임 ↕ — ⑤ 받침 + ⑥ 아래 판(10 · 9)', None, 'l')
    I.label((110, 220, 21), L, 440, '② 코드 보관함 — 맨 아래 앞 · 열 상자 밖', '코드를 감아 두고 쓸 땐 뒤 홈으로 뺌', 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm(몸체 155 + 뚜껑 45) · 열 상자 144 × 144 × 40mm(단열 포함 · 위 열림) · 3칸 Ø5 × 깊이 8(뒤 1 · 앞 2) · 절단면은 앞 두 칸의 중심(y = 134) · 그림은 쉬는 상태(뚜껑 닫힘 · 잠김)', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 약 1kW(시즈 히터 450W × 2 + 모터 · 제어) · 한 번에 3장 · 칸 안 압력 0.5~1.5MPa × 3칸 = 2.9~8.8kN · 바닥부터: 고무발 6 · 무게판 6 · 바닥판 10 · 캠 · 모터 칸 93 · 열 상자 40 · 뚜껑 45 = 200mm', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1260 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def exploded():
    I = Iso(0.86, 480, 760)
    # L0 ① 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 ⑬ 바닥판 + C자 틀 2 + 잠금 막대 · ③ 모터 · ④ 캠 · 레버 · 로드
    z = 40; I.box(24, 14, z, 172, 192, 10, FRAME)
    I.box(160, 70, z + 14, 34, 44, 24, MOTOR); I.line([(160, 92, z + 26), (138, 92, z + 26)], MOTOR, 5)
    I.poly(cam_pts(130, 92, z + 26, 0.3), MOTOR, '#2b2b30', 0.9, .95)
    I.box(148, 88, z + 10, 8, 8, 30, FRAME); I.line([(152, 92, z + 36), (110, 92, z + 36)], MOTOR, 4.5); I.line([(110, 92, z + 36), (110, 92, z + 70)], MOTOR, 5)
    for x0 in (26, 186):
        I.box(x0, 14, z + 10, 8, 192, 10, FRAME); I.box(x0, 14, z + 20, 8, 14, 110, FRAME); I.box(x0, 192, z + 20, 8, 14, 110, FRAME)
        I.box(x0, 4, z + 118, 8, 18, 24, FRAME); I.line([(x0 + 8, 10, z + 124), (x0 + 8, 10, z + 136)], '#15151a', 3)
    I.line([(30, 200, z + 112), (190, 200, z + 112)], '#6a6a70', 3)
    I.box(10, 196, z + 106, 14, 10, 12, MOTOR)                                                        # 잠금 솔레노이드
    # L2 ⑨ 보드
    I.box(14, 50, 130, 3, 90, 50, BOARD)
    # L3 ② 코드 보관함
    z = 160; I.box(40, 156, z, 140, 58, 3, STEEL, op=.95); I.box(40, 208, z, 140, 6, 18, PANEL); I.line([(96, 215, z + 9), (124, 215, z + 9)], '#8a8a90', 2.4)
    for k in range(3): I.line([(60 + k * 3, 170 + k * 3, z + 4 + k * 3), (160 - k * 3, 170 + k * 3, z + 4 + k * 3), (160 - k * 3, 200 - k * 3, z + 4 + k * 3), (60 + k * 3, 200 - k * 3, z + 4 + k * 3), (60 + k * 3, 170 + k * 3, z + 4 + k * 3)], '#2b2b30', 2)
    # L4 ⑩ 몸체 + ⑪ 옆 패널 + 앞면
    z = 200; hollow(I, 8, 8, z, 204, 204, 139, 4, BODY)
    I.box(0, 0, z + 147, 220, 220, 8, BAND)
    I.poly([(70, 8, z + 128), (150, 8, z + 128), (150, 8, z + 136), (70, 8, z + 136)], '#2b2b30', 'none', 0, .85)
    for (x0, y0, w, d) in [(-30, 8, 4, 204), (246, 8, 4, 204), (8, -30, 204, 4), (8, 246, 204, 4)]:
        I.box(x0, y0, z, w, d, 147, PANEL)
    I.line([(40, 250, z + 12), (180, 250, z + 12), (180, 250, z + 30), (40, 250, z + 30), (40, 250, z + 12)], '#8a8a90', 1.2, '4 3')
    I.line([(96, 250, z + 112), (124, 250, z + 112), (124, 250, z + 122), (96, 250, z + 122), (96, 250, z + 112)], '#6a6a70', 1.4)
    I.line([(100, 250, z + 99), (120, 250, z + 99)], HEAT, 3)
    for x0 in (36, 178): I.poly([(x0, 216, z + 155), (x0 + 6, 216, z + 155), (x0 + 6, 210, z + 155), (x0, 210, z + 155)], '#2b2b30', 'none', 0)   # 앞 테 걸림 구멍 2
    # L5 ⑧ 열 상자(위 열림 · 뒤 김 구멍 2)
    z = 400; hollow(I, 38, 38, z, 144, 144, 40, 6, INSUL)
    for x0 in (100, 112): I.poly([(x0, 38, z + 30), (x0 + 8, 38, z + 30), (x0 + 8, 38, z + 36), (x0, 38, z + 36)], '#2b2b30', 'none', 0, .9)
    # L6 ⑤ 받침(속 히터 · 퓨즈 · 판 감지)
    z = 480; I.box(48, 48, z, 124, 124, 12, PLATE); I.box(54, 76, z + 12, 112, 6, 3, HTR); I.box(160, 60, z + 2, 6, 8, 8, RED)
    I.out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#2f7a46"/>' % I.P(60, 160, z + 12))
    # L7 ⑥ 아래 판(얕은 칸 3 · 손가락 홈 2) + 숟가락
    z = 540; I.box(48, 48, z, 124, 124, 14, ALU)
    for (cx, cy) in CELLS: dish(I, cx, cy, z + 14)
    I.box(44, 104, z + 6, 4, 16, 6, DARK); I.box(172, 104, z + 6, 4, 16, 6, DARK)
    I.box(196, 120, z + 6, 6, 36, 3, STEEL); I.box(190, 150, z + 6, 18, 22, 3, STEEL)                  # 계량 숟가락 3g
    # L8 ⑫ 위 판(볼록 3 · 뒤 걸이 2 · 실리콘 손잡이 2)
    z = 650
    for (cx, cy) in CELLS: I.cylz(cx, cy, z - 6, DR - 3, 6, ALU)
    I.box(48, 48, z, 124, 124, 6, ALU)
    I.box(52, 42, z, 10, 6, 6, DARK); I.box(158, 42, z, 10, 6, 6, DARK)
    I.box(70, 172, z + 1, 16, 8, 6, SIL); I.box(134, 172, z + 1, 16, 8, 6, SIL)
    # L9 ⑭ 뚜껑 = ⑦ 위 열판 · ⑧ 단열 · ⑬ 뚜껑 보 + 갈고리 2 · 껍데기 · 유리 · 떼는 단추
    z = 720
    I.box(44, 44, z, 132, 132, 10, PLATE); I.box(50, 76, z + 10, 120, 6, 3, HTR); I.box(166, 60, z + 2, 6, 8, 6, HEAT)
    I.box(38, 38, z + 16, 144, 144, 5, INSUL)
    I.box(22, 10, z + 24, 176, 196, 11, FRAME)
    for x0 in (36, 178): I.box(x0, 198, z + 4, 6, 6, 20, '#6a6a70')
    I.box(104, 204, z - 2, 12, 4, 6, DARK)                                                              # 위 판 떼는 단추(안쪽 앞 테)
    z = 780; I.box(4, 4, z, 212, 212, 41, LID, top=shade(LID, .1))
    I.box(-2, -2, z + 41, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    I.line([(110, 110, 0), (110, 110, 825)], '#b8b2a6', 1, '3 6', .8)
    R = 690; L = 280
    I.label((110, 110, 825), R, 40, '⑭ 뚜껑 45mm — 검은 유리 윗면 · 떠 있는 경첩 · 윗면엔 아무것도 없음', None, 'r')
    I.label((186, 110, 760), R, 84, '⑬ 뚜껑 보 11t + 앞 갈고리 2 — 경첩 축과 잠금 막대에 걸림', None, 'r')
    I.label((176, 110, 739), R, 120, '⑧ 뚜껑 안 단열 5', None, 'r')
    I.label((172, 110, 726), R, 154, '⑦ 위 열판 — 뚜껑 안 고정 · 속 시즈 히터 450W · NTC', None, 'r')
    I.label((112, 204, 719), L - 10, 190, '⑭ 위 판 떼는 단추(안쪽 앞 테) — 50°C 넘으면 잠김', None, 'l')
    I.label((172, 110, 654), R, 214, '⑫ 위 판 — 알루미늄 6t · 얕은 볼록 3 · 뒤 걸이 2 · 실리콘 손잡이 2', '전선 없음 · 떼어 식기세척기', 'r')
    I.label((212, 110, 300), R, 520, '⑩ 몸체 · 흰 띠 · 앞면(열림 단추 · 불빛 + 숫자) · 김 덕트 · 뒤 슬릿', '앞 테 걸림 구멍 2 · 맨 아래 코드 보관함 덮개', 'r')
    I.label((248, 110, 300), R, 566, '⑪ 옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((172, 110, 552), R, 290, '⑥ 아래 판 — 알루미늄 14t · 얕은 칸 Ø50 × 8 셋(뒤 1 · 앞 2) · 손가락 홈 2', '나사 없음 · 받침에 얹힘 · 떼어 식기세척기', 'r')
    I.label((198, 140, 549), L + 40, 330, '계량 숟가락 3g', None, 'l')
    I.label((172, 110, 490), R, 356, '⑤ 받침 12t — 속 시즈 히터 450W · 온도 퓨즈 · 판 감지 자석 스위치', '⑥을 얹고 캠으로 +10 · −9', 'r')
    I.label((182, 110, 430), R, 410, '⑧ 열 상자 144 × 144 × 40 — 강판 + 단열 · 위 열림 · 뒤 벽 김 구멍 2', None, 'r')
    I.label((160, 200, 166), R, 600, '② 코드 보관함 — 바닥 앞 · 열 상자 밖', None, 'r')
    I.label((15, 95, 155), L, 600, '⑨ 제어 보드', None, 'l')
    I.label((194, 200, 120), R, 640, '⑬ 강철 틀 — 바닥판 10t + C자 틀 8t × 2(경첩 팔 · 앞 걸림 귀) + 잠금 막대 · 솔레노이드', '뚜껑 보 · 갈고리와 함께 닫혀 누르는 힘 2.9~8.8kN이 여기서만 돎', 'r')
    I.label((130, 92, 66), R, 700, '④ 달팽이 캠 + 레버(1:2) + 푸시 로드 + 위치 센서 — 한 바퀴 = 세 장', None, 'r')
    I.label((194, 92, 66), R, 740, '③ 모터(웜 기어드) — 바닥 오른쪽', None, 'r')
    I.label((206, 110, 3), R, 800, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.text(480, 962, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼어 씻는 것은 ⑥ 아래 판과 ⑫ 위 판 두 장뿐입니다. 부품 14개, 번호는 단면 · 동작 · 3D · 본문과 같습니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1250 980" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

# ---------------- 옆 단면(동작 순서 · 가열) ----------------
S = 1.05
def SX(y): return 32 + (182 - y) * S             # 앞(y 182) = x 32 · 뒤(y 38) = x 183
def SZ(z): return 250 - (z - 100) * S            # z 100 = y 250 · z 200 = y 145

def _rect(o, y0, y1, z0, z1, fill, extra=''):
    x = SX(y1); w = (y1 - y0) * S; yy = SZ(z1); h = (z1 - z0) * S
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" %s/>' % (x, yy, w, h, fill, extra))

def _dish_path(o, yc, ztop, depth=8, r=25, fill='#c4c9cf'):
    """옆 단면의 얕은 접시(둥근 바닥) — 칸 자리를 판 색 위에 비워 그림"""
    x0, x1 = SX(yc + r), SX(yc - r); xm = (x0 + x1) / 2
    o.append('<path d="M%.1f %.1f Q %.1f %.1f %.1f %.1f Z" fill="%s" stroke="#6a6f76" stroke-width=".7"/>' % (x0, SZ(ztop), xm, SZ(ztop - 2 * depth), x1, SZ(ztop), fill))

def _dome_path(o, yc, zbase, h=6, r=22):
    x0, x1 = SX(yc + r), SX(yc - r); xm = (x0 + x1) / 2
    o.append('<path d="M%.1f %.1f Q %.1f %.1f %.1f %.1f Z" fill="#d5d9de" stroke="#6a6f76" stroke-width=".7"/>' % (x0, SZ(zbase), xm, SZ(zbase - 2 * h), x1, SZ(zbase), ))

def _panel(o, lift=0, lid_up=0, lid_open=False, cake=None, rice=True, lock=False, steam=False, press=False, spoon=False, heater_on=True, pop=False, wash=False):
    """옆 단면 한 칸(왼쪽 = 앞). lift = ⑤ + ⑥ 올라간 mm · lid_up = 뚜껑 들린 mm(0 · 20) · lid_open = 뚜껑 젖힘"""
    o.append('<rect x="22" y="84" width="214" height="196" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
    lk = '#d19a3c' if lock else '#9aa3ad'
    o.append('<rect x="206" y="92" width="20" height="14" rx="3" fill="%s"/><path d="M211 92 v-5 a5 5 0 0 1 10 0 v5" fill="none" stroke="%s" stroke-width="2.2"/>' % (lk, lk))
    o.append('<text x="30" y="274" font-size="9.5" fill="#6a6a70">앞</text>')
    # 몸체 앞 · 뒤 껍데기 · 흰 띠 · 열 상자 벽 · 바닥 · 김 구멍
    _rect(o, 176, 182, 100, 155, '#ebe4d6'); _rect(o, 176, 182, 147, 155, '#ffffff', 'stroke="#d8d2c4" stroke-width=".6"')
    _rect(o, 38, 44, 100, 155, '#ebe4d6'); _rect(o, 38, 44, 147, 155, '#ffffff', 'stroke="#d8d2c4" stroke-width=".6"')
    _rect(o, 44, 50, 115, 155, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"'); _rect(o, 170, 176, 115, 155, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 50, 170, 115, 121, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 44, 50, 146, 152, '#15151a')
    # 앞 갈고리 걸림 · 잠금 막대(앞 y 196..200 대신 앞 벽 안쪽에 그림)
    _rect(o, 172, 176, 141, 147, '#15151a' if lock else '#9aa3ad')
    # ⑤ 받침 + ⑥ 아래 판(lift)
    zp = lift
    if not wash:
        _rect(o, 52, 168, 127 + zp, 139 + zp, '#8a8f96', 'rx="2"'); _rect(o, 76, 92, 130 + zp, 136 + zp, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
        _rect(o, 52, 168, 139 + zp, 153 + zp, '#d5d9de', 'stroke="#9aa3ad" stroke-width=".6"')
        for yc in (80, 134):
            _dish_path(o, yc, 153 + zp, fill='#f7f2e8' if lid_open or lid_up else '#eef0f2')
            bottom = 145 + zp
            if cake == 'pressed':
                _rect(o, yc - 18, yc + 18, bottom, bottom + 2, '#e9dcc0', 'stroke="#d19a3c" stroke-width=".6"')
            elif cake in ('puffed', 'done'):
                _rect(o, yc - 22, yc + 22, bottom, bottom + 10.5, '#fff3dc', 'rx="5" stroke="#d19a3c"')
            elif rice:
                for k in range(5): o.append('<circle cx="%.1f" cy="%.1f" r="1.8" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (SX(yc + 12 - k * 6), SZ(bottom + 1.8)))
        for yy in (60, 160):
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="1.4" stroke-dasharray="2 2"/>' % (SX(yy), SZ(121), SX(yy), SZ(127 + zp)))
    else:
        _rect(o, 52, 168, 127, 139, '#8a8f96', 'rx="2"'); _rect(o, 76, 92, 130, 136, '#9a9a9e', 'rx="3"')
        o.append('<text x="%.1f" y="%.1f" font-size="10" font-weight="800" fill="#8a5d12">⑥ · ⑫ 빼서 싱크대로</text>' % (SX(160), SZ(146)))
    if spoon:
        o.append('<path d="M%.1f %.1f l-20 -26 l-10 0" fill="none" stroke="#9aa3ad" stroke-width="3" stroke-linecap="round"/>' % (SX(140), SZ(158)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">숟가락 3g × 3</text>' % (SX(176), SZ(178)))
    # ⑭ 뚜껑(lid_up 만큼 위로 · 젖히면 뒤로 세운 모습)
    if lid_open:
        # 뒤 경첩에서 세운 뚜껑(옆에서 보면 세로 막대) — 안쪽 면(⑫ 위 판 · 볼록)이 앞을 봄
        x = SX(38) + 2
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#2a2a2f"/>' % (x, SZ(155) - 104, 45 * S * .9, 104))
        if not wash:
            o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#d5d9de" stroke="#9aa3ad" stroke-width=".6"/>' % (x - 6 * S, SZ(155) - 96, 6 * S, 86))
        o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#6a6a70" text-anchor="end">뚜껑(젖힘) · 안쪽 ⑫</text>' % (x - 4, SZ(155) - 108))
    else:
        u = lid_up
        _rect(o, 38, 182, 163 + u, 196 + u, '#2a2a2f', 'rx="3"'); _rect(o, 38, 46, 155 + u, 163 + u, '#2a2a2f'); _rect(o, 174, 182, 155 + u, 163 + u, '#2a2a2f'); _rect(o, 36, 184, 196 + u, 200 + u, '#101014', 'rx="2"')
        _rect(o, 44, 176, 184 + u, 195 + u, '#4f5864')
        _rect(o, 44, 176, 179 + u, 184 + u, '#e7d9c2')
        _rect(o, 48, 172, 169 + u, 179 + u, '#8a8f96', 'rx="2"'); _rect(o, 76, 92, 172 + u, 177 + u, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
        _rect(o, 52, 168, 163 + u, 169 + u, '#d5d9de', 'stroke="#9aa3ad" stroke-width=".6"')
        for yc in (80, 134): _dome_path(o, yc, 163 + u)
        _rect(o, 176, 180, 141 + u, 155 + u, '#6a6a70')                                              # 앞 갈고리
        o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#fff">뚜껑</text>' % (SX(182) + 4, SZ(188 + u)))
        if u > 0: o.append('<text x="%.1f" y="%.1f" font-size="9.5" font-weight="800" fill="#8a5d12">2cm 들림</text>' % (SX(70), SZ(205 + u)))
    if press:
        for yc in (80, 134):
            for d in (-12, 0, 12):
                x = SX(yc + d)
                o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.3" marker-end="url(#arrh)"/>' % (x, SZ(172), x, SZ(166)))
                o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.3" marker-end="url(#arrh)"/>' % (x, SZ(138 + zp), x, SZ(146 + zp)))
    if steam:
        o.append('<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" stroke="#d19a3c" stroke-width="1.6" stroke-dasharray="3 3" marker-end="url(#arr)"/>' % (SX(90), SZ(158), SX(70), SZ(156), SX(56), SZ(152), SX(46), SZ(149)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#8a5d12">김 → 뒤 구멍</text>' % (SX(150), SZ(170)))
    if pop: o.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="800" fill="#8a5d12">9mm 툭 · 뻥 × 3</text>' % (SX(178), SZ(116)))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(110), SZ(127 + (zp if not wash else 0)), SX(110), SZ(102)))
    o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">④ 캠 · ③ 모터 ↓</text>' % (SX(104), SZ(104)))

def sequence(only=None):
    """동작 순서 ①~⑥ — 옆에서 본 열 상자(왼쪽 = 앞). ⑤ + ⑥만 캠으로 오르내리고, 뚜껑은 사람이 여닫음"""
    pw = 252; gap = 16
    titles = [('① 뚜껑 열고 쌀 넣기', '예열 끝 · 5초', '예열 불빛 → 열림 단추(히터 꺼짐)|숟가락으로 마른 쌀 3g씩 세 칸에|얕은 칸 바닥에 한 겹|⑥ 아래 판은 받침 위에 얹혀 있음'),
              ('② 뚜껑 닫기 · 딸깍', '220°C · 1초', '떠 있는 경첩 → 마지막 2cm 수평|볼록 3이 칸 3 위에 똑바로|앞 갈고리 2를 잠금 막대가 잡음 → 시작'),
              ('③ 올려 누르기 8~10초', '220°C · 8~10초', '캠이 ⑤ + ⑥을 10mm 올림|칸 테두리가 위 판에 닿아 세 칸이 막힘|쌀 2mm · 물기가 끓어 압력 ↑ · 캠 멈춤'),
              ('④ 순간 하강 9mm', '220°C · 0.1초', '캠 절벽 → ⑤ + ⑥이 9mm 툭|세 칸이 한꺼번에 「뻥」|틈 11mm = 떡뻥 두께 · 뚜껑은 잠긴 채'),
              ('⑤ 완료 · 열고 집기', '완료 불빛 · 3초', '받침 제자리 · 김 3초 → 잠금 막대 풀림|앞 단추 → 뚜껑 2cm 들려 김이 뒤로|젖히고 세 칸에서 집기 · 3장 약 35초'),
              ('⑥ 판 두 장 씻기', '식은 뒤', '위 판: 안쪽 앞 단추 + 실리콘 손잡이|아래 판: 손가락 홈 2로 들어 뺌|판이 없으면 판 감지로 켜지지 않음')]
    cfg = [dict(lift=0, lid_open=True, rice=True, spoon=True, heater_on=False),
           dict(lift=0, lock=True, rice=True),
           dict(lift=UP, lock=True, cake='pressed', press=True),
           dict(lift=UP - DROP, lock=True, cake='puffed', pop=True, steam=True),
           dict(lift=0, lid_open=True, cake='done', heater_on=False),
           dict(lift=0, lid_open=True, wash=True, heater_on=False)]
    idx = range(6) if only is None else [only]
    N = len(idx)
    o = ['<svg viewBox="0 0 %d 400" xmlns="http://www.w3.org/2000/svg" %s>%s' % (14 + N * (pw + gap), FONT, DEFS)]
    for n, i in enumerate(idx):
        x0 = 14 + n * (pw + gap)
        o.append('<g transform="translate(%d,0)">' % x0)
        o.append('<rect x="0" y="12" width="%d" height="376" rx="16" fill="#fff" stroke="#e6e1d7"/>' % pw)
        o.append('<text x="16" y="40" font-size="15" font-weight="800" fill="#15151a">%s</text>' % titles[i][0])
        o.append('<rect x="16" y="47" width="118" height="14" rx="7" fill="#fbe9e4"/><text x="75" y="57.5" font-size="10" font-weight="800" fill="#c8503c" text-anchor="middle">%s</text>' % titles[i][1])
        o.append('<g transform="translate(0,-8)">'); _panel(o, **cfg[i]); o.append('</g>')
        if i == 2: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 10</text>' % (SX(182) - 4, SZ(124), SX(182) - 4, SZ(138), SX(182) - 2, SZ(116)))
        for k, w in enumerate(titles[i][2].split('|')): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (318 + k * 16, w))
        o.append('</g>')
        if n < N - 1: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

def heating():
    o = ['<svg viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS)]
    o.append('<g transform="translate(20,20) scale(1.75) translate(-22,-84)">')
    _panel(o, lift=UP, lock=True, cake='pressed', press=True)
    o.append('</g>')
    o.append('<text x="30" y="22" font-size="12" font-weight="800" fill="#15151a">누르는 중(③) · 옆 단면(뒤 칸 + 앞 칸, 3칸 중 2칸이 보임) · 왼쪽 = 앞 · 뚜껑 닫힘 · 잠김</text>')
    def lab(py, pz, sx, sy, t, sub=None):
        px = 20 + 1.75 * (SX(py) - 22); pyy = 20 + 1.75 * (SZ(pz) - 84)
        o.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#d19a3c" stroke="#fff" stroke-width="1.2"/><polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (px, pyy, px, pyy, sx - 14, sy - 4, sx - 6, sy - 4))
        o.append('<text x="%d" y="%d" font-size="13.5" font-weight="800" fill="#15151a">%s</text>' % (sx, sy, t))
        if sub: o.append('<text x="%d" y="%d" font-size="11.5" font-weight="600" fill="#6a6a70">%s</text>' % (sx, sy + 15, sub))
    LX = 500
    lab(60, 190, LX, 60, '⑬ 뚜껑 보 11t — 뒤 경첩 축 + 앞 갈고리 2 · 잠금 막대', '힘 2.9~8.8kN이 보 → 경첩 · 갈고리 → C자 틀 → 바닥판으로 닫힘 · 껍데기엔 힘 없음')
    lab(88, 174, LX, 112, '⑦ 위 열판 — 뚜껑 안 고정 · 속 시즈 히터 450W(빨강) · NTC', '220°C 유지 · 상한 230°C · 전선은 여기까지')
    lab(150, 166, LX, 164, '⑫ 위 판 — 얕은 볼록 3(높이 6) · 전선 없음 · 떼어 씻음', '볼록 끝과 칸 바닥 사이 2mm = 눌린 쌀 · 칸 테두리가 판 면에 닿아 막힘')
    lab(165, 150, LX, 216, '⑥ 아래 판 — 얕은 칸 Ø50 × 8 셋 · 받침에 얹힘', '10mm 올라간 상태 · 칸 안 물기가 끓어 0.5~1.5MPa')
    lab(84, 133, LX, 268, '⑤ 받침 — 속 시즈 히터 450W(빨강) · 온도 퓨즈 250°C', '캠이 일정 반지름에서 멈춰 있어 모터엔 힘이 안 걸림')
    steps = [('① 열 전달 · 8~10초', '220°C 판 두 장이 쌀을 바로 데움'), ('② 압력 ↑', '막힌 칸 안 물기가 끓어 0.5~1.5MPa'), ('③ 9mm 순간 하강', '캠 절벽 → 세 칸 「뻥」 · 약 10mm')]
    for k, (t, d) in enumerate(steps):
        x = 500 + k * 230
        o.append('<rect x="%d" y="330" width="214" height="64" rx="12" fill="#fff" stroke="#e6e1d7"/>' % x)
        o.append('<text x="%d" y="356" font-size="13.5" font-weight="800" fill="#8a5d12">%s</text><text x="%d" y="378" font-size="11.5" fill="#6a6a70">%s</text>' % (x + 14, t, x + 14, d))
        if k < 2: o.append('<text x="%d" y="368" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x + 222))
    o.append('<rect x="30" y="424" width="560" height="72" rx="12" fill="#fbe9e4"/>')
    o.append('<text x="48" y="452" font-size="13.5" font-weight="800" fill="#c8503c">김 길 — 칸 → 두 판 사이 틈 → 뒤 벽 위 구멍 Ø8 × 2 → 덕트 → 뒤 김 슬릿</text>')
    o.append('<text x="48" y="474" font-size="11.5" fill="#6a6a70">순간 하강 때 칸이 열리며 김이 나옴(3장 약 1.35g) · 뚜껑이 2cm 들릴 때 남은 김도 뒤로 · 덕트 아래 물받이 홈</text>')
    o.append('<rect x="610" y="424" width="560" height="72" rx="12" fill="#f3efe6"/>')
    o.append('<text x="628" y="452" font-size="13.5" font-weight="800" fill="#15151a">전기 — 220V 직결 · 약 1kW = 시즈 히터 450W × 2 + 모터 · 제어</text>')
    o.append('<text x="628" y="474" font-size="11.5" fill="#6a6a70">예열 약 4분 → 「예열 완료」 불빛 · 판이 없거나 뚜껑이 열리면 히터 꺼짐 · NTC 2 + 온도 퓨즈 2중 차단</text>')
    o.append('</svg>')
    return '\n'.join(o)

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence), ('iso_heat', heating)]:
        with open(os.path.join(here, name + '.svg'), 'w', encoding='utf-8') as f: f.write(fn())
        print('wrote', name)
    img = os.path.join(os.path.dirname(here), 'img')
    for n, i in [('step1', 0), ('step2', 2), ('step3', 4)]:
        with open(os.path.join(img, n + '.svg'), 'w', encoding='utf-8') as f: f.write(sequence(only=i))
        print('wrote', n)
