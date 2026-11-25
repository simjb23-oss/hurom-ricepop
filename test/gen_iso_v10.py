# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 v10 (2026-11-25) — 「뚜껑형 3칸 Ø5 · 틀 고정」 구조(준보 「가 뚜껑형」 msg_3779d746 · 「3개나 5개」 msg_c733a03a · 「응응」 msg_c5a4e63e · 두팔 msg_b413ad68)
3칸: Ø50 셀 3개 삼각(중심 (110,142) · (78.8,88) · (141.2,88), 원 중심 (110,106) 반지름 36) · 한 번에 같이 누름 · 힘 3 × 1.5MPa × 19.6cm² = 8.8kN
열 상자 안 132 × 120(x 44..176 · y 50..170) · 기둥은 열 상자 바깥(x 26..38 · 182..194) · 윗보 40 × 30(z 136..166 · 굽힘 약 55MPa) · 잠금 핀 Ø10 × 2 · 뚜껑 안내 핀 2(뒤)가 틀판 구멍에 먼저 들어가 정렬 (준보 「가자」 msg_a055c8ce · 「외부 구조도 바뀌어도 된다 · 새롭게」 msg_c91ce084 · msg_492e8e2c)
업소용 떡뻥 기계와 같은 자리: 틀은 기계(강철 틀)에 고정, 위 열판 + 플러그는 뚜껑 안에, 아래 피스톤만 오르내림. 서랍 트레이 삭제.
구동은 두팔 안(msg_590aa8ca)의 캠 하나: 모터 1 + 달팽이 캠 1 + 레버 + 되돌림 스프링 — 토글 · 래치 · 리밋 2 삭제.
흐름: 뚜껑 열고(히터 꺼짐) 숟가락으로 마른 쌀 3g을 틀에(바닥 = 피스톤 윗면) → 뚜껑 닫으면 잠금 핀 2가 윗보를 기둥 머리에 걸어 ㅁ자 틀이 닫힘 · 플러그가 틀 안으로 3.5mm
 → 시작 → 캠이 피스톤을 10mm 올려 쌀 1.5mm로 누름(220°C · 8~10초) → 캠 절벽에서 피스톤이 9mm 툭(뻥 · 틀 안) → 완료 · 잠금 핀 풀림 · 뚜껑 10mm 들림 → 사람이 뚜껑 젖힘
 → 뚜껑 열림 스위치 → 캠이 피스톤을 16mm 올려 떡뻥을 틀 위로 → 집기 → 피스톤 제자리.
힘: 플러그 ⑦ ← 위 열판 ← 뚜껑 윗보 ⑬ ← 잠금 핀 2 ← 기둥 머리 · 기둥 2 ← 바닥판 ← 캠 축 ④ → 레버 → 푸시 로드 → 피스톤 ⑤ → 쌀 (강철 틀 안에서 닫힘 · 몸체 · 뚜껑 껍데기엔 힘 없음)
김: 틀 안 → (순간 하강 · 뚜껑 열릴 때) 틀판 위 공간 → 뒤 벽 위 김 구멍 2 → 덕트 → 몸체 뒤 김 슬릿 (+ 뚜껑 열 때 조금)
쌀: 숟가락 3g → 틀(피스톤 윗면 위 한 겹) → 누르기 · 뻥 → 틀 안 떡뻥 → 피스톤이 틀 위로 올림 → 집기. 기계 안을 흐르는 쌀 없음

좌표(mm): x 0..220 왼→오, y 0..220 뒤→앞, z 0..200 아래→위. 보는 방향 = 앞·오른쪽·위.
부품 번호(모든 그림 · 3D · 본문 공통):
 ① 바닥 무게판 · 고무발 · 기울기 센서  ② 부스러기 서랍(열 상자 바닥 · 앞 아래 작은 서랍)  ③ 모터(웜 기어드 · 바닥 오른쪽 · 캠 축 직결)
 ④ 캠 축 = 달팽이 캠(Ø20~36 · 한 바퀴 = 한 장) + 레버(1:2) + 푸시 로드(열 상자 바닥 관통 · 벨로즈) + 되돌림 스프링 2 + 캠 위치 센서
 ⑤ 아래 열판 = 받침(속 시즈 히터 450W · 퓨즈 250°C) + 피스톤 Ø59.6 × 13(틀 안을 오르내림 · 쉼 → +10 누름 → −9 뻥 → +16 꺼내기)
 ⑥ 틀판 = 알루미늄 판 108 × 82 × 4 + Ø60 × 16 틀(아래로) · 세라믹 코팅 · 턱에 얹히고 자리 핀 2 · 앞 탭 잡고 들어 올려 씻음
 ⑦ 위 열판 + Ø59.6 플러그 6mm(뚜껑 안 · 뚜껑 윗보에 볼트) · 속 시즈 히터 450W · NTC  ⑧ 열 상자(강판 1.5 + 단열 5 · 위 열림 · 뒤 벽 위 김 구멍 2) + 뚜껑 안 단열 10
 ⑨ 제어 보드  ⑩ 몸체 · 흰 띠(뚜껑 밑 테) · 공기층 10 · 김 덕트 · 뒤 김 슬릿  ⑪ 옆 패널 4장 · 비스포크  ⑫ 계량 겸 펴개 숟가락 3g(뚜껑 뒤쪽 홈 · 자석)
 ⑬ 강철 틀 = 바닥판 10t + 기둥 12 × 12 두 개 + 기둥 머리(잠금 핀 Ø8 × 2 · 스프링 · 솔레노이드 해제) + 뚜껑 윗보 40 × 22(뚜껑 안 · 위 열판 고정) — 닫으면 ㅁ자
 ⑭ 뚜껑 = 검은 불투명 내열 상판(터치 · 상태 불빛 · 숫자) + 껍데기 + 뒤 경첩 + 열림 단추 + 열림 스위치(열리면 히터 꺼짐)
높이(z): 고무발 0..6 · 무게판 6..12 · 틀 바닥판 12..22 · 캠 · 레버 · 모터 칸 22..62 · 열 상자 바닥 62..68 · 부스러기 서랍 70..82(앞) · 받침 80..92(히터 83..89) · 피스톤 92..105(쉼 윗면 105)
 · 틀판 턱 112..116 · 틀판 116..120(틀 104..120 아래로) · 플러그 116.5..122 · 위 열판 122..136(히터 126..132) · 윗보 136..158 · 기둥 22..136 · 기둥 머리 136..158 · 잠금 핀 z 147
 · 몸체 테 150..158(흰 띠) · 뚜껑 158..200(단열 158..168 · 공기 168..196 · 상판 196..200) · 김 구멍 124..130(뒤 벽) · 뒤 슬릿 138..146
행정: 쉼 105 → +10 누름(윗면 115 · 플러그 밑 116.5 → 쌀 1.5mm) → −9 뻥(106 · 떡뻥 106..116.5 ≈ 10.5mm · 플러그는 아직 틀 안 3.5) → 뚜껑 열린 뒤 +16(121 · 틀 위 1mm) → 쉼
"""
import sys, os, math
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_iso import Iso, shade, DEFS, FONT, PANEL, BODY, BAND, GLASS, STEEL, PLATE, HEAT, MOLD, CRACK, DARK, MOTOR, BOARD, RICE, INSUL, RED, HTR, hollow

FRAME = '#4f5864'   # 강철 틀(짙은 청회색)
LID = '#26262b'     # 뚜껑 껍데기(검정)
CX, CY = 110, 110
UP = 10            # 누름 행정
DROP = 9           # 순간 하강
EJ = 16            # 꺼내기 행정
RING_Z0, RING_Z1 = 104, 120
CELLS = [(110, 142), (78.8, 88), (141.2, 88)]   # 3칸 중심(앞 1 · 뒤 2)
CR, CRI = 31, 25                              # 틀 바깥 Ø62 · 안 Ø50
PR = 24.8                                     # 피스톤 · 플러그 반지름(Ø49.6)
REST = 105         # 피스톤 쉼 윗면

def cam_pts(cx, y, cz, phase=0.0, seg=36):
    """달팽이 캠 — y 평면에 놓인 원판(캠 축 = x 방향). r 10 → 18 로 자라다 절벽. phase 는 그림용"""
    pts = []
    for i in range(seg):
        a = 2 * math.pi * i / seg
        t = ((a / (2 * math.pi)) + phase) % 1.0
        r = 10 + 8 * (t if t < 0.92 else 0)
        pts.append((cx, y + r * math.cos(a), cz + r * math.sin(a)))
    return pts

def frame_base(I):
    """⑬ 바닥판(z 12..22, 10t)"""
    I.box(24, 60, 12, 172, 92, 10, FRAME)
def frame_cols(I):
    """⑬ 기둥 2(x 26..38 · 182..194, y 100..112, z 22..136) — 열 상자 바깥"""
    I.box(26, 100, 22, 12, 12, 114, FRAME); I.box(182, 100, 22, 12, 12, 114, FRAME)
def frame_heads(I, locked=True):
    """⑬ 기둥 머리(z 136..158 · 윗보 끝을 감쌈) + 잠금 핀 Ø8(x 방향 · z 147)"""
    for x0 in (20, 176):
        I.box(x0, 94, 136, 24, 24, 30, FRAME, op=.92)
        if locked: I.box(x0 - 4, 107, 146, 32, 10, 10, DARK)

def cutaway():
    I = Iso(1.5, 560, 268, cut_y=106)
    W, D, H = 220, 220, 200
    # ---- 껍데기 뒤 벽 · 바닥 · 왼 벽 (몸체 0..150 · 흰 띠 150..158 · 뚜껑 158..196 · 상판 196..200) · 뒤 김 슬릿 · 덕트
    for (z0, h, col) in [(0, 150, PANEL), (150, 8, BAND), (158, 38, LID)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))
    for (z0, h, col) in [(0, 150, PANEL), (150, 8, BAND), (158, 38, LID)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col)
    I.poly([(70, 8, 138), (150, 8, 138), (150, 8, 146), (70, 8, 146)], '#2b2b30', 'none', 0, .85)   # 뒤 김 슬릿
    I.box(96, 32, 122, 28, 12, 22, STEEL, op=.9)                                                     # 김 덕트(뒤 벽 구멍 → 슬릿)
    I.box(60, 2, 150, 100, 10, 10, DARK)                                                             # ⑭ 경첩(뒤 · x 60..160)
    # ---- 바닥 칸: 무게판 · 틀 바닥판 · 보드 · 모터 · 캠 축 · 레버 · 푸시 로드
    I.box(14, 14, 6, 192, 192, 6, STEEL)                                        # ① 무게판
    frame_base(I)
    I.box(14, 60, 60, 3, 100, 70, BOARD)                                        # ⑨ 제어 보드(왼 벽)
    I.box(172, 72, 26, 34, 44, 24, MOTOR)                                       # ③ 모터(바닥 오른쪽 · 캠 축 직결)
    I.line([(172, 96, 40), (138, 96, 40)], MOTOR, 5)                            # 캠 축(x 방향)
    I.poly(cam_pts(130, 96, 40, 0.3), MOTOR, '#2b2b30', 0.9, .95)               # ④ 달팽이 캠(그림은 쉼 자리)
    I.box(148, 92, 22, 8, 8, 30, FRAME)                                         # 레버 받침(바닥판에)
    I.line([(152, 96, 50), (110, 96, 50)], MOTOR, 4.5)                          # 레버(받침 → 푸시 로드 · 1:2)
    I.line([(110, 96, 50), (110, 96, 80)], MOTOR, 5)                            # 푸시 로드(바닥 관통 · 벨로즈 · 받침 가운데)
    I.box(100, 92, 26, 8, 8, 6, DARK)                                           # 캠 위치 센서
    # ---- 열 상자 뒤 · 왼 · 바닥(위 열림) · 김 구멍 2
    frame_cols(I)                                                               # ⑬ 기둥 2(열 상자 바깥)
    I.box(38, 44, 62, 144, 6, 96, INSUL)
    I.poly([(100, 50.2, 124), (108, 50.2, 124), (108, 50.2, 130), (100, 50.2, 130)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 50.2, 124), (120, 50.2, 124), (120, 50.2, 130), (112, 50.2, 130)], '#2b2b30', 'none', 0, .9)
    I.box(38, 50, 62, 6, 126, 96, INSUL)
    I.box(44, 50, 62, 132, 126, 6, INSUL, top=shade(INSUL, -.08))
    I.box(50, 52, 70, 120, 120, 2, STEEL, op=.9)                                # ② 부스러기 서랍 바닥판(얇은 판 · 앞으로 당김)
    # ---- ⑤ 아래 열판(쉴 때): 받침(속 히터) + 피스톤 Ø59.6 + 퓨즈 + 되돌림 스프링 2
    I.box(50, 56, 80, 120, 100, 12, PLATE)
    I.box(56, 96, 83, 108, 20, 6, HTR, hatch_cut=False, faces='l')
    I.line([(60, 100, 68), (60, 100, 80)], HEAT, 2.4, '3 2'); I.line([(160, 100, 68), (160, 100, 80)], HEAT, 2.4, '3 2')
    for (cx, cy) in CELLS[1:]: I.cylz(cx, cy, 92, PR, REST - 92, PLATE); I.cylz(cx, cy, REST - 0.5, PR, 0.5, HEAT)
    I.box(164, 70, 82, 6, 8, 8, RED, hatch_cut=False)
    # ---- ⑥ 틀판: 턱(뒤 · 왼 · 오른) · 자리 핀 2 · 판 + Ø60 틀(아래로 16) · 마른 쌀 한 겹(피스톤 윗면)
    I.box(44, 50, 112, 132, 6, 4, FRAME); I.box(44, 50, 112, 6, 126, 4, FRAME)
    I.box(54, 60, 116, 4, 4, 6, DARK); I.box(162, 60, 116, 4, 4, 6, DARK)         # 뚜껑 안내 핀이 들어갈 구멍 자리(뒤 2)
    for (cx, cy) in CELLS[1:]: I.ringz(cx, cy, RING_Z0, CR, CRI, RING_Z1 - RING_Z0, MOLD)   # 뒤 틀 2(앞 틀은 잘린 앞 절반)
    for (cx, cy) in CELLS[1:]:
        for k in range(5): I.out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="%s" stroke="#b9b2a2" stroke-width=".6"/>' % (I.P(cx - 12 + k * 6, cy + 10 - (k % 2) * 4, REST + 1) + (RICE,)))
    I.box(48, 56, 116, 8, 108, 4, MOLD); I.box(164, 56, 116, 8, 108, 4, MOLD)     # 틀판 좌 · 우 띠(틀 둘레는 링)
    I.box(56, 56, 116, 108, 4, 4, MOLD); I.box(100, 104, 116, 20, 2, 4, MOLD)     # 틀판 뒤 띠 · 가운데 조각
    I.box(170, 50, 112, 6, 126, 4, FRAME)                                        # 턱 오른쪽
    # ---- ⑦ 위 열판 + 플러그(뚜껑 안) · 히터 · NTC · ⑬ 윗보 · 기둥 머리 · 잠금 핀 · 솔레노이드
    for (cx, cy) in CELLS[1:]: I.cylz(cx, cy, 116.5, PR, 5.5, PLATE)
    I.box(54, 60, 110, 4, 4, 12, DARK); I.box(162, 60, 110, 4, 4, 12, DARK)       # 뚜껑 안내 핀 2(뒤 · 틀판 구멍에 먼저 들어감)
    I.box(44, 50, 122, 132, 112, 14, PLATE)
    I.box(50, 96, 126, 120, 20, 6, HTR, hatch_cut=False, faces='l')
    I.box(166, 70, 126, 6, 8, 8, HEAT, hatch_cut=False)
    I.box(22, 86, 136, 176, 40, 30, FRAME)                                       # 윗보 40 × 30(뚜껑 안 · 양 끝이 기둥 머리에)
    frame_heads(I, locked=True)
    I.box(8, 96, 140, 10, 12, 10, MOTOR)                                         # 잠금 솔레노이드(핀 2를 당김)
    # ---- 열 상자 오른 벽 · 뚜껑 안 단열(위 덮개) · 뚜껑 열림 스위치
    I.box(176, 50, 62, 6, 126, 96, INSUL)
    I.box(38, 44, 166, 144, 132, 10, INSUL)
    I.box(100, 44, 150, 10, 6, 8, DARK)
    # ---- 김 길(점선 화살): 틀 → 틀판 위 → 뒤 벽 김 구멍 → 덕트 → 슬릿 → 밖
    I.line([(110, 104, 121), (110, 80, 128), (110, 52, 127)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    I.line([(110, 44, 128), (110, 38, 142), (110, 10, 142), (110, -14, 150)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    # ---- 힘 길(굵은 회색 화살): 캠 → 레버 → 로드 → 피스톤 → 쌀 → 플러그 → 위 열판 → 윗보 → 잠금 핀 → 기둥 → 바닥판 → 캠 축
    I.line([(141, 88, 84), (141, 88, 104)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(141, 88, 124), (141, 88, 138)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(188, 106, 150), (188, 106, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    I.line([(32, 106, 150), (32, 106, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    # 움직임 화살(피스톤 ↕)
    I.line([(60, 100, 105), (60, 100, 121)], HEAT, 1.8, None, 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')
    # ---- 오른 벽(몸체 · 띠 · 뚜껑)
    for (z0, h, col) in [(0, 150, PANEL), (150, 8, BAND), (158, 38, LID)]:
        I.box(212, 8, z0, 8, 212, h, col)
    # ---- ⑭ 상판(창 없음) · 터치
    I.box(-2, -2, 196, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    # ---- 앞 절반 고스트: 부스러기 서랍 앞판 · 뚜껑 열림 단추 · 터치 · 틀판 탭
    I.ghost_box(0, 110, 0, 220, 110, 200)
    I.line([(60, 220, 64), (160, 220, 64), (160, 220, 82), (60, 220, 82), (60, 220, 64)], '#8a8a90', 1.2, '4 3')   # ② 부스러기 서랍 앞판(아래)
    I.line([(96, 221, 73), (124, 221, 73)], '#8a8a90', 2.4)                                             # 손가락 홈
    I.line([(60, 220, 150), (160, 220, 150), (160, 220, 158), (60, 220, 158), (60, 220, 150)], '#8a8a90', 1, '3 3')   # 흰 띠(뚜껑 밑 테) 앞
    I.line([(96, 220, 164), (124, 220, 164), (124, 220, 172), (96, 220, 172), (96, 220, 164)], '#8a8a90', 1, '3 3')   # ⑭ 뚜껑 열림 단추(앞)
    I.line([(100, 164, 116), (120, 164, 116), (120, 164, 122), (100, 164, 122), (100, 164, 116)], '#9aa3ad', 1, '3 3')   # ⑥ 틀판 앞 탭
    gx, gy = CELLS[0]
    for (r, z) in ((CR, RING_Z0), (CR, RING_Z1), (PR, 122)):
        I.line([(gx + r * math.cos(2 * math.pi * k / 24), gy + r * math.sin(2 * math.pi * k / 24), z) for k in range(25)], '#9aa3ad', 1, '3 3')   # 앞 틀 · 플러그(잘린 앞 절반 · 점선)
    for x in (38, 54): sx, sy = I.P(x, 196, 200); I.out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="none" stroke="#8a8a90" stroke-dasharray="2 2"/>' % (sx, sy))
    I.line([(66, 196, 200), (88, 196, 200)], '#8a8a90', 2, '2 2')
    I.line([(176, 100, 100), (212, 100, 100)], '#6a6a70', 1, None, 1, marker='marker-start="url(#arrg)" marker-end="url(#arrg)"')
    # 뚜껑 열리는 방향(경첩 뒤)
    I.line([(200, 200, 200), (200, 170, 236)], HEAT, 1.6, '4 3', 1, marker='marker-end="url(#arr)"')
    # ---- 라벨(오른쪽은 검은 뚜껑 위라 흰 바탕)
    I.out.append('<rect x="790" y="34" width="470" height="280" rx="12" fill="#fff" opacity=".86"/>')
    R = 820; L = 330
    I.label((110, 110, 200), R, 56, '⑭ 뚜껑 — 검은 내열 상판 · 터치 · 상태 불빛 · 뒤 경첩', '열면 히터 꺼짐(열림 스위치) · 앞 열림 단추 · 완료 뒤에만 열림', 'r')
    I.label((150, 110, 163), R, 104, '⑧ 뚜껑 안 단열 10 — 열 상자 위를 덮음', '⑩ 흰 띠 = 뚜껑 밑 테(몸체 150..158)', 'r')
    I.label((150, 110, 147), R, 148, '⑬ 뚜껑 윗보 40 × 30 + 기둥 머리 + 잠금 핀 Ø10 × 2', '닫으면 핀이 걸려 ㅁ자 틀 · 힘 4.2~8.8kN이 이 안에서만(회색 화살) · 기둥은 열 상자 밖', 'r')
    I.label((160, 80, 129), R, 194, '⑦ 위 열판 220°C + Ø49.6 플러그 3개 + 안내 핀 2 — 뚜껑 윗보에', '속 시즈 히터 450W · NTC 230°C · 안내 핀이 틀판에 먼저 들어가 정렬 · 플러그는 틀 안 3.5mm', 'r')
    I.label((150, 88, 118), R, 240, '⑥ 틀판 — 알루미늄 4t + Ø50 × 16 틀 3개(삼각) · 턱 + 핀 구멍', '세라믹 코팅 · 앞 탭 잡고 들어 씻음 · 틀 바닥 = 피스톤 윗면 · 앞 칸은 점선', 'r')
    I.label((141, 100, 100), R, 286, '⑤ 피스톤 Ø49.6 × 3(틈 0.2) + 받침 12t 속 히터 450W · 퓨즈', '받침째 +10 누름 → −9 뻥 → +16 꺼내기 · 되돌림 스프링 2(주황 점선)', 'r')
    I.label((160, 100, 71), R, 330, '② 부스러기 서랍 — 열 상자 바닥 · 앞 아래로 당겨 비움', None, 'r')
    I.label((110, 96, 66), R, 366, '푸시 로드 — 열 상자 바닥 관통(벨로즈) · 받침 가운데', None, 'r')
    I.label((131, 96, 50), R, 402, '④ 레버(1:2) + 달팽이 캠 — 한 바퀴 = 한 장', '올림 10 → 멈춤 8~10초 → 절벽(뻥 9) → 올림 16 → 제자리 · 위치 센서', 'r')
    I.label((200, 90, 44), R, 448, '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결 · 자기 잠금', None, 'r')
    I.label((206, 110, 11), R, 488, '① 바닥 무게판 + 고무발 · 기울기 센서', None, 'r')
    I.label((110, 6, 155), L, 130, '⑭ 경첩(뒤) — 뚜껑이 뒤로 젖혀짐', None, 'l')
    I.label((110, 8, 142), L, 166, '⑩ 뒤 김 슬릿 — 김은 뒤로', None, 'l')
    I.label((104, 50.2, 127), L, 202, '⑧ 뒤 벽 위 김 구멍 Ø8 × 2 → 덕트', None, 'l')
    I.label((13, 102, 145), L, 238, '잠금 솔레노이드 — 완료 뒤 핀 2를 당김', None, 'l')
    I.label((15, 110, 95), L, 290, '⑨ 제어 보드 — 온도 · 기울기 · 뚜껑 잠금 · 캠 위치', None, 'l')
    I.label((110, 220, 168), L, 330, '⑭ 열림 단추(앞) — 점선 = 잘라낸 앞 절반', '완료 뒤 눌러 열기 · 뚜껑이 10mm 들려 김이 빠진 뒤 젖힘', 'l')
    I.label((110, 164, 119), L, 378, '⑥ 틀판 앞 탭 — 식은 뒤 들어 올림 · 앞 칸 Ø5(점선)', None, 'l')
    I.label((60, 100, 113), L, 420, '움직임 ↕ — 받침 + 피스톤 3(10 · 9 · 16)', None, 'l')
    I.label((110, 220, 73), L, 464, '② 부스러기 서랍 앞판 — 앞 아래 작은 서랍', None, 'l')
    I.label((46, 196, 200), L, 520, '터치 · 상태 불빛(예열 · 굽는 중 · 완료 · 열어도 돼요) · 숫자 2', None, 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm(몸체 158 + 뚜껑 42) · 열 상자 144 × 132 × 96mm(단열 포함 · 위 열림) · 3칸 Ø5 삼각(앞 1 · 뒤 2) · 절단면은 세 칸의 중심(y = 106) · 앞 칸은 점선 · 그림은 쉬는 상태(뚜껑 닫힘 · 잠김)', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 약 1kW(시즈 히터 450W × 2 + 모터 · 제어) · 한 번에 3장 · 누르는 힘 3 × 1.4~2.9kN = 4.2~8.8kN · 바닥부터: 고무발 6 · 무게판 6 · 틀 바닥판 10 · 캠 · 모터 칸 40 · 열 상자 96 · 뚜껑 42 = 200mm', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1260 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def exploded():
    I = Iso(0.86, 480, 760)
    W, D, H = 220, 220, 200
    # L0 ① 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 ⑬ 바닥판 + 기둥 2 + ③ 모터 + ④ 캠 · 레버 · 푸시 로드
    z = 44; I.box(24, 60, z, 172, 92, 10, FRAME)
    I.box(172, 72, z + 14, 34, 44, 24, MOTOR); I.line([(172, 96, z + 28), (138, 96, z + 28)], MOTOR, 5)
    I.poly(cam_pts(130, 96, z + 28, 0.3), MOTOR, '#2b2b30', 0.9, .95)
    I.box(148, 92, z + 10, 8, 8, 30, FRAME); I.line([(152, 96, z + 38), (110, 96, z + 38)], MOTOR, 4.5); I.line([(110, 96, z + 38), (110, 96, z + 66)], MOTOR, 5)
    I.box(100, 92, z + 14, 8, 8, 6, DARK)
    I.box(26, 100, z + 10, 12, 12, 80, FRAME); I.box(182, 100, z + 10, 12, 12, 80, FRAME)
    for x0 in (20, 176): I.box(x0, 94, z + 90, 24, 24, 30, FRAME, op=.92); I.box(x0 - 4, 107, z + 100, 32, 10, 10, DARK)   # 기둥 머리 + 잠금 핀(분해도에선 기둥 위에)
    I.box(8, 96, z + 94, 10, 12, 10, MOTOR)
    # L2 ⑨ 보드(왼 벽)
    I.box(14, 60, 150, 3, 100, 70, BOARD)
    # L3 ② 부스러기 서랍(얇은 판 + 앞판)
    z = 190; I.box(50, 52, z, 120, 120, 2, STEEL, op=.95); I.box(46, 172, z - 6, 128, 8, 18, PANEL); I.line([(96, 181, z + 3), (124, 181, z + 3)], '#8a8a90', 2.4)
    # L4 ⑤ 아래 열판 = 받침(속 히터) + 피스톤 Ø59.6 + 퓨즈 + 스프링 2
    z = 232; I.box(50, 56, z, 120, 100, 12, PLATE); I.box(56, 96, z + 12, 108, 6, 3, HTR)
    for (cx, cy) in CELLS: I.cylz(cx, cy, z + 12, PR, 13, PLATE); I.cylz(cx, cy, z + 24.5, PR, 0.5, HEAT)
    I.box(164, 70, z + 2, 6, 8, 8, RED); I.line([(60, 100, z - 14), (60, 100, z)], HEAT, 2.4, '3 2'); I.line([(160, 100, z - 14), (160, 100, z)], HEAT, 2.4, '3 2')
    # L5 ⑧ 열 상자(위 열림 · 앞 벽 아래 부스러기 서랍 구멍 · 뒤 벽 위 김 구멍 2) + 턱(틀판 자리) + 자리 핀 2
    z = 300; hollow(I, 38, 44, z, 144, 132, 96, 6, INSUL, front=False)
    I.box(38, 170, z + 22, 144, 6, 74, INSUL); I.box(38, 170, z, 14, 6, 22, INSUL); I.box(168, 170, z, 14, 6, 22, INSUL)   # 앞 벽(아래 서랍 구멍)
    I.poly([(100, 44, z + 62), (108, 44, z + 62), (108, 44, z + 68), (100, 44, z + 68)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 44, z + 62), (120, 44, z + 62), (120, 44, z + 68), (112, 44, z + 68)], '#2b2b30', 'none', 0, .9)
    for (x0, y0, w, d) in [(44, 50, 132, 6), (44, 50, 6, 126), (170, 50, 6, 126), (44, 164, 132, 6)]: I.box(x0, y0, z + 50, w, d, 4, FRAME)
    I.box(54, 60, z + 54, 4, 4, 4, DARK); I.box(162, 60, z + 54, 4, 4, 4, DARK)
    # L6 ⑥ 틀판(판 + Ø60 틀 아래로 + 앞 탭 + 자리 핀 구멍 2) · ⑫ 숟가락
    z = 440
    for (cx, cy) in CELLS: I.ringz(cx, cy, z - 16, CR, CRI, 16, MOLD)
    I.box(48, 56, z, 124, 108, 4, MOLD, op=.96)
    for (cx, cy) in CELLS: I.ringz(cx, cy, z, CR, CRI, 4, MOLD)
    I.box(100, 164, z, 20, 8, 4, '#9aa3ad')                                                          # 앞 탭
    for x0 in (56, 164): I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#55585e"/>' % I.P(x0, 62, z + 4))   # 안내 핀 구멍 2(뒤)
    I.box(150, 14, z + 4, 6, 36, 3, STEEL); I.box(140, -6, z + 4, 26, 20, 3, STEEL)                   # ⑫ 계량 겸 펴개 숟가락(뚜껑 뒤 홈에 자석)
    # L7 ⑩ 몸체(흰 띠 · 김 덕트 · 뒤 슬릿 · 앞 아래 서랍 구멍) + ⑪ 옆 패널 4장
    z = 540; hollow(I, 8, 8, z, 204, 204, 142, 4, BODY)
    I.box(0, 0, z + 150, 220, 220, 8, BAND)
    I.poly([(70, 8, z + 138), (150, 8, z + 138), (150, 8, z + 146), (70, 8, z + 146)], '#2b2b30', 'none', 0, .85)
    I.box(96, 10, z + 122, 28, 10, 22, STEEL, op=.9)
    for (x0, y0, w, d) in [(-30, 8, 4, 204), (246, 8, 4, 204), (8, -30, 204, 4), (8, 246, 204, 4)]:
        I.box(x0, y0, z, w, d, 150, PANEL)
    I.line([(60, 250, z + 64), (160, 250, z + 64), (160, 250, z + 82), (60, 250, z + 82), (60, 250, z + 64)], '#8a8a90', 1.2, '4 3')
    I.box(60, 2, z + 150, 100, 10, 10, DARK)                                                          # ⑭ 경첩(뒤)
    # L8 ⑭ 뚜껑 = ⑦ 위 열판 + 플러그 · ⑬ 윗보 · ⑧ 단열 · 껍데기 · 상판 · 터치 · 열림 단추
    z = 760
    for (cx, cy) in CELLS: I.cylz(cx, cy, z - 5.5, PR, 5.5, PLATE)
    I.box(54, 60, z - 12, 4, 4, 12, DARK); I.box(162, 60, z - 12, 4, 4, 12, DARK)
    I.box(44, 50, z, 132, 112, 14, PLATE); I.box(50, 96, z + 14, 120, 6, 3, HTR); I.box(166, 70, z + 4, 6, 8, 8, HEAT)
    I.box(22, 86, z + 14, 176, 40, 30, FRAME)
    z = 830; I.box(38, 44, z, 144, 132, 10, INSUL)
    I.box(8, 8, z + 10, 204, 204, 28, LID, top=shade(LID, .1))
    I.box(-2, -2, z + 38, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    for x in (38, 54): sx, sy = I.P(x, 196, z + 42); I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/>' % (sx, sy))
    I.poly([(66, 192, z + 42.2), (88, 192, z + 42.2), (88, 200, z + 42.2), (66, 200, z + 42.2)], '#fff', 'none', 0)
    I.box(90, 214, z + 12, 40, 6, 6, DARK)                                                           # 앞 손가락 홈(열림)
    I.line([(110, 110, 0), (110, 110, 880)], '#b8b2a6', 1, '3 6', .8)
    # 라벨
    R = 690; L = 280
    I.label((110, 110, 874), R, 48, '⑭ 뚜껑 — 검은 내열 상판 · 터치 · 상태 불빛 · 앞 손가락 홈(열림) · 숨긴 경첩 · 열림 스위치', None, 'r')
    I.label((176, 110, 836), R, 94, '⑧ 뚜껑 안 단열 10 — 열 상자 위를 덮음', None, 'r')
    I.label((160, 110, 786), R, 140, '⑬ 뚜껑 윗보 40 × 30 — 위 열판 고정 · 양 끝이 기둥 머리의 잠금 핀 Ø10에 걸림', None, 'r')
    I.label((154, 110, 766), R, 180, '⑦ 위 열판 220°C + Ø49.6 플러그 3 + 안내 핀 2 · 속 시즈 히터 450W · NTC — 뚜껑 안', None, 'r')
    I.label((212, 110, 620), R, 260, '⑩ 몸체 · 흰 띠(뚜껑 밑 테) · 김 덕트 · 뒤 슬릿 · 뒤 경첩 · 앞 아래 서랍 구멍', None, 'r')
    I.label((248, 110, 620), R, 296, '⑪ 옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((150, 150, 442), R, 376, '⑥ 틀판 — 알루미늄 124 × 108 × 4 + Ø50 × 16 틀 3개(삼각 · 아래로) · 안내 핀 구멍 2 · 앞 탭', '세라믹 코팅 · 들어서 씻음 · 틀 바닥은 피스톤 윗면 · 한 번에 3장', 'r')
    I.label((153, 4, 448), L + 40, 420, '⑫ 펴개 숟가락 3g · 끝 폭 = 틀 Ø60 — 뚜껑 뒤 홈에 자석', None, 'l')
    I.label((182, 110, 348), R, 450, '⑧ 열 상자 144 × 132 — 강판 + 단열 5 · 위 열림 · 틀판 턱 · 뒤 벽 김 구멍 2', None, 'r')
    I.label((141, 88, 256), R, 520, '⑤ 아래 열판 = 받침 12t(속 히터 450W · 퓨즈) + 피스톤 Ø49.6 × 13 세 개 — 받침째 10 · 9 · 16mm · 스프링 2', None, 'r')
    I.label((160, 100, 192), R, 566, '② 부스러기 서랍 — 열 상자 바닥 · 앞 아래로 당김', None, 'r')
    I.label((15, 110, 190), L, 600, '⑨ 제어 보드', None, 'l')
    I.label((188, 106, 110), R, 630, '⑬ 강철 틀 — 바닥판 10t + 기둥 12 × 12 두 개(열 상자 밖) + 기둥 머리(잠금 핀 Ø10 × 2 · 솔레노이드)', '뚜껑 윗보와 함께 ㅁ자가 되어 누르는 힘 4.2~8.8kN이 여기서만 돎', 'r')
    I.label((130, 100, 72), R, 690, '④ 달팽이 캠 + 레버(1:2) + 푸시 로드 + 캠 위치 센서 — 한 바퀴 = 한 장', None, 'r')
    I.label((188, 90, 66), R, 730, '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결', None, 'r')
    I.label((206, 110, 3), R, 800, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.text(480, 962, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼어 씻는 것은 ⑥ 틀판(3칸) · ② 부스러기 서랍 둘뿐입니다. 부품 14개, 번호는 단면 · 동작 · 3D · 본문과 같습니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1250 980" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

# ---------------- 옆 단면(동작 순서 · 가열) ----------------
S = 1.1
def SX(y): return 60 + (176 - y) * S            # 앞(y 176) = x 60 · 뒤(y 44) = x 205
def SZ(z): return 238 - (z - 62) * S             # z 62 = y 238 · z 200 = y 86

def _rect(o, y0, y1, z0, z1, fill, extra=''):
    """mm 좌표(y 앞뒤 · z 높이)로 옆 단면 사각형"""
    x = SX(y1); w = (y1 - y0) * S; yy = SZ(z1); h = (z1 - z0) * S
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" %s/>' % (x, yy, w, h, fill, extra))

def _panel(o, i, lift, lid_up, cake=None, rice=True, lock=False, steam=False, press=False, spoon=False, heater_on=True, pop=False):
    """열 상자 옆 단면 한 칸. lift = 피스톤 올라간 mm(0~16) · lid_up = 뚜껑 들린 mm(0 닫힘 · 10 살짝 · 40 열림)
    고정: 열 상자 · ⑬ 기둥 · 머리 · 틀판(턱) · 레일 없음. 움직임: ⑤ 피스톤(lift) · 뚜껑(위 열판 · 플러그 · 윗보 · 단열 · 상판 전부 lid_up 만큼 위로)"""
    o.append('<rect x="52" y="62" width="160" height="176" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
    lk = '#d19a3c' if lock else '#9aa3ad'
    o.append('<rect x="190" y="50" width="22" height="16" rx="3" fill="%s"/><path d="M195 50 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lk, lk))
    o.append('<text x="46" y="236" font-size="9.5" fill="#6a6a70" text-anchor="middle">앞</text>')
    # ⑧ 열 상자 벽(앞 · 뒤 · 바닥) · 뒤 벽 김 구멍 · 기둥(y 98..110) · 턱 · 틀판 + 틀(고정)
    _rect(o, 170, 176, 62, 158, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"'); _rect(o, 44, 50, 62, 158, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 50, 170, 62, 68, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 44, 50, 124, 130, '#15151a')
    _rect(o, 100, 112, 68, 136, '#4f5864', 'opacity=".35"'); _rect(o, 94, 118, 136, 166, '#4f5864', 'opacity=".35"')   # 기둥 · 머리(열 상자 밖 · 뒤에 비침)
    o.append('<text x="%.1f" y="%.1f" font-size="8.5" fill="#fff" text-anchor="middle">틀</text>' % (SX(106), SZ(100)))
    _rect(o, 50, 56, 112, 116, '#4f5864'); _rect(o, 164, 170, 112, 116, '#4f5864')                   # 턱
    _rect(o, 56, 63, 116, 120, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"'); _rect(o, 113, 117, 116, 120, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"'); _rect(o, 167, 170, 116, 120, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')   # 틀판
    for (a, b) in ((63, 68), (108, 113), (117, 122), (162, 167)): _rect(o, a, b, 104, 116, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')   # 뒤 틀(68..108) · 앞 틀(122..162) 벽
    # ② 부스러기 서랍(바닥) · ⑤ 받침(히터) + 피스톤(lift) · 스프링
    _rect(o, 52, 172, 70, 72, '#b9bec4')
    zp = lift
    _rect(o, 56, 156, 80 + zp, 92 + zp, '#8a8f96', 'rx="2"'); _rect(o, 96, 116, 83 + zp, 89 + zp, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
    for (a, b) in ((68.2, 107.8), (122.2, 161.8)):
        _rect(o, a, b, 92 + zp, 105 + zp, '#8a8f96'); _rect(o, a, b, 104.5 + zp, 105.5 + zp, '#d19a3c')
    _rect(o, 66, 72, 82 + zp, 90 + zp, '#e06c5a')
    for yy in (60, 164):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="1.4" stroke-dasharray="2 2"/>' % (SX(yy), SZ(68), SX(yy), SZ(80 + zp)))
    # 쌀 · 떡뻥(피스톤 윗면 위)
    top = REST + zp
    for (a, b) in ((68.2, 107.8), (122.2, 161.8)):
        if cake == 'pressed':
            _rect(o, a, b, top, top + 1.5, '#e9dcc0', 'stroke="#d19a3c" stroke-width=".6"')
        elif cake in ('puffed', 'done'):
            _rect(o, a, b, top, top + DROP + 1.5, '#fff3dc', 'rx="4" stroke="#d19a3c"')
        elif rice:
            for k in range(5): o.append('<circle cx="%.1f" cy="%.1f" r="1.8" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (SX(b - 4 - k * 8), SZ(top + 1.5)))
    if spoon:
        o.append('<path d="M%.1f %.1f l-22 -30 l-10 0" fill="none" stroke="#9aa3ad" stroke-width="3" stroke-linecap="round"/>' % (SX(142), SZ(top + 6)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">⑫ 숟가락 3g × 3</text>' % (SX(176) - 2, SZ(150)))
    # ⑭ 뚜껑(lid_up 만큼 위로): 단열 · 껍데기 · 상판 · ⑦ 위 열판 + 플러그 · ⑬ 윗보 · 잠금 핀
    u = lid_up
    _rect(o, 44, 176, 166 + u, 176 + u, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 40, 180, 176 + u, 196 + u, '#2a2a2f', 'rx="3"'); _rect(o, 38, 182, 196 + u, 200 + u, '#101014', 'rx="2"')
    _rect(o, 50, 162, 122 + u, 136 + u, '#8a8f96', 'rx="2"'); _rect(o, 54, 158, 126 + u, 132 + u, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
    for (a, b) in ((68.2, 107.8), (122.2, 161.8)):
        _rect(o, a, b, 116.5 + u, 122 + u, '#8a8f96'); _rect(o, a, b, 116.5 + u, 117.5 + u, '#d19a3c')
    _rect(o, 58, 62, 110 + u, 122 + u, '#15151a')                                                   # 안내 핀(뒤)
    _rect(o, 164, 170, 130 + u, 135 + u, '#15151a')
    _rect(o, 86, 126, 136 + u, 166 + u, '#4f5864')                                                   # 윗보(옆에서 y 86..126)
    if lock: _rect(o, 82, 130, 146, 156, '#15151a')                                                  # 잠금 핀(머리 안 · 윗보 관통)
    o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#6a6a70">뚜껑</text>' % (SX(176) + 2, SZ(186 + u)))
    if u > 0: o.append('<text x="%.1f" y="%.1f" font-size="9.5" font-weight="800" fill="#8a5d12">열림 %s</text>' % (SX(44) + 4, SZ(186 + u), '10mm' if u < 20 else ''))
    # 열 · 압력 화살(누르는 중)
    if press:
        for k in range(6):
            x = SX((150 if k < 3 else 96) - (k % 3) * 12)
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(128), x, SZ(118)))
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(92 + zp), x, SZ(103 + zp)))
    if steam:
        o.append('<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" stroke="#d19a3c" stroke-width="1.6" stroke-dasharray="3 3" marker-end="url(#arr)"/>' % (SX(88), SZ(121), SX(76), SZ(128), SX(60), SZ(128), SX(51), SZ(127)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#8a5d12">김 → 뒤 구멍</text>' % (SX(100), SZ(142)))
    if pop: o.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="800" fill="#8a5d12">9mm 툭 · 뻥 × 3</text>' % (SX(176), SZ(96)))
    # ④ 캠 · 레버 · 푸시 로드 · ③ 모터(바닥 칸)
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(96), SZ(80 + zp), SX(96), SZ(50)))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="3.5" stroke-linecap="round"/>' % (SX(96), SZ(50), SX(96) + 40, SZ(50) - 2))   # 레버(옆에서 보면 x 방향이라 짧게)
    r = 10 + 8 * (lift / 16.0)
    o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#5a5e66" opacity=".9"/><circle cx="%.1f" cy="%.1f" r="2.2" fill="#15151a"/>' % (SX(96) + 20, SZ(40), r * S, SX(96) + 20, SZ(40)))
    o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">④ 캠</text>' % (SX(96) + 36, SZ(36)))
    o.append('<rect x="%.1f" y="276" width="%.1f" height="5" fill="#4f5864"/>' % (SX(176), 132 * S))   # 틀 바닥판
    o.append('<rect x="100" y="286" width="40" height="14" rx="4" fill="#5a5e66"/><text x="146" y="297" font-size="10" fill="#6a6a70">③ 모터</text>')

def sequence(only=None):
    """동작 순서 ①~⑥ 6칸 — 옆에서 본 열 상자(왼쪽 = 앞). 틀판 · 기둥 고정, 피스톤만 오르내리고 뚜껑은 사람이 여닫음"""
    pw = 252; gap = 16
    titles = [('① 뚜껑 열고 쌀 넣기', '예열 끝 · 5초', '예열 불빛 → 앞 홈 당겨 뚜껑 젖힘(히터 꺼짐)|⑫ 숟가락으로 마른 쌀 3g씩 세 칸에|틀에 쓸어 넣어 한 겹(바닥 2/3)|틀 바닥 = 피스톤 윗면 · 틀판은 고정'),
              ('② 뚜껑 닫고 시작', '220°C · 1초', '닫으면 안내 핀 2가 틀판에 먼저 들어가 정렬|잠금 핀 2 딸깍 → ㅁ자 틀 · 플러그 3이 틀 안 3.5mm|시작 터치 → 모터가 캠을 돌림'),
              ('③ 올려 누르기 8~10초', '220°C · 8~10초', '캠이 받침째 피스톤 3을 10mm 올림 → 쌀 1.5mm|열판 두 장이 위 · 아래에서 데움|세 틀이 플러그로 막혀 압력 ↑(8.8kN) · 캠은 멈춤'),
              ('④ 순간 하강 9mm', '220°C · 0.1초', '캠 절벽 → 압력 + 스프링이 받침을 9mm 툭|세 칸이 한꺼번에 「뻥」|두께 ≈ 10.5mm · 플러그는 아직 틀 안'),
              ('⑤ 완료 · 뚜껑 열림', '완료 불빛 · 3초', '잠금 핀 풀림 → 뚜껑이 10mm 들림|김은 뒤 구멍 · 뚜껑 틈으로|사람이 뚜껑을 젖히면 히터 꺼짐'),
              ('⑥ 올려서 꺼내기', '열림 확인 · 5초', '열림 스위치 → 캠이 피스톤 3을 16mm 올림|떡뻥 3장이 틀 위로 → 집게 · 손끝|제자리 → 다음 3장 · 3장 약 35초 · 10장 약 2분')]
    cfg = [dict(lift=0, lid_up=20, lock=False, rice=True, spoon=True, heater_on=False),
           dict(lift=0, lid_up=0, lock=True, rice=True),
           dict(lift=UP, lid_up=0, lock=True, cake='pressed', press=True),
           dict(lift=UP - DROP, lid_up=0, lock=True, cake='puffed', pop=True),
           dict(lift=UP - DROP, lid_up=10, lock=False, cake='done', steam=True),
           dict(lift=EJ, lid_up=20, lock=False, cake='done', heater_on=False)]
    idx = range(6) if only is None else [only]
    N = len(idx)
    o = ['<svg viewBox="0 0 %d 400" xmlns="http://www.w3.org/2000/svg" %s>%s' % (14 + N * (pw + gap), FONT, DEFS)]
    for n, i in enumerate(idx):
        x0 = 14 + n * (pw + gap)
        o.append('<g transform="translate(%d,0)">' % x0)
        o.append('<rect x="0" y="12" width="%d" height="376" rx="16" fill="#fff" stroke="#e6e1d7"/>' % pw)
        o.append('<text x="16" y="40" font-size="15" font-weight="800" fill="#15151a">%s</text>' % titles[i][0])
        o.append('<rect x="36" y="45" width="118" height="14" rx="7" fill="#fbe9e4"/><text x="95" y="55.5" font-size="10" font-weight="800" fill="#c8503c" text-anchor="middle">%s</text>' % titles[i][1])
        o.append('<g transform="translate(0,0)">'); _panel(o, i, **cfg[i]); o.append('</g>')
        if i == 2: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 10</text>' % (SX(176) - 10, SZ(84), SX(176) - 10, SZ(104), SX(176) - 8, SZ(92)))
        if i == 5: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 16</text>' % (SX(176) - 10, SZ(90), SX(176) - 10, SZ(116), SX(176) - 8, SZ(100)))
        for k, w in enumerate(titles[i][2].split('|')): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (318 + k * 16, w))
        o.append('</g>')
        if n < N - 1: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

def heating():
    """가열 방식 — 누르는 중(③) 옆 단면 1.7배 + 원리 3단 + 아래 띠(김 길 · 전기)"""
    o = ['<svg viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS)]
    o.append('<g transform="translate(30,50) scale(1.6) translate(-52,-62)">')
    _panel(o, 2, lift=UP, lid_up=0, lock=True, cake='pressed', press=True)
    o.append('</g>')
    o.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="800" fill="#15151a">누르는 중(③) · 옆 단면(앞 칸 + 뒤 칸, 3칸 중 2칸이 보임) · 왼쪽 = 앞 · 뚜껑 닫힘 · 잠김</text>' % (30, 22))
    def lab(py, pz, sx, sy, t, sub=None):
        px = 30 + 1.6 * (SX(py) - 52); pyy = 50 + 1.6 * (SZ(pz) - 62)
        o.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#d19a3c" stroke="#fff" stroke-width="1.2"/><polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (px, pyy, px, pyy, sx - 14, sy - 4, sx - 6, sy - 4))
        o.append('<text x="%d" y="%d" font-size="13.5" font-weight="800" fill="#15151a">%s</text>' % (sx, sy, t))
        if sub: o.append('<text x="%d" y="%d" font-size="11.5" font-weight="600" fill="#6a6a70">%s</text>' % (sx, sy + 15, sub))
    LX = 500
    lab(106, 151, LX, 72, '⑬ 뚜껑 윗보 40 × 30 + 잠금 핀 Ø10 × 2 — 누르는 힘 4.2~8.8kN이 핀 → 기둥 2 → 바닥판으로 닫힘', '핀 전단 약 28MPa · 윗보 굽힘 약 55MPa(기둥 사이 150mm) · 몸체 · 뚜껑 껍데기엔 힘이 걸리지 않음')
    lab(60, 129, LX, 128, '⑦ 위 열판 — 알루미늄 다이캐스트 · 속에 시즈 히터 450W(빨강) · NTC — 뚜껑 안', '220°C 유지 · 상한 230°C · 뚜껑 윗보에 볼트로 고정 · 뒤 안내 핀 2가 틀판에 먼저 들어감')
    lab(142, 119, LX, 184, '⑦ 플러그 Ø49.6 × 3 — 닫으면 틀 안으로 3.5mm · 틈 0.2mm · 입구 모따기 1mm', '쌀 1.5mm 두께로 눌림 · 물기가 끓어 0.5~1.5MPa(틀 안) · 세 칸 합 4.2~8.8kN')
    lab(56, 118, LX, 240, '⑥ 틀판 — Ø50 × 16 틀 3개 · 턱 위 · 뚜껑 안내 핀으로 플러그와 정렬', '마른 쌀 3g 한 겹씩 · 틀판은 움직이지 않음 · 들어서 씻음')
    lab(142, 100, LX, 296, '⑤ 피스톤 Ø49.6 × 3 + 받침 12t — 속에 시즈 히터 450W(빨강) · 온도 퓨즈 250°C', '받침째 10mm 올라간 상태 · 캠 멈춤(일정 반지름)이라 모터엔 힘이 안 걸림')
    steps = [('① 열 전달 · 8~10초', '220°C 판 두 장이 위 · 아래에서 바로 데움'), ('② 압력 ↑', '틀이 플러그로 막혀 물기가 끓어 0.5~1.5MPa'), ('③ 9mm 순간 하강', '캠 절벽 → 세 칸이 한꺼번에 「뻥」 · 두께 약 10.5mm')]
    for k, (t, d) in enumerate(steps):
        x = 500 + k * 230
        o.append('<rect x="%d" y="330" width="214" height="64" rx="12" fill="#fff" stroke="#e6e1d7"/>' % x)
        o.append('<text x="%d" y="356" font-size="13.5" font-weight="800" fill="#8a5d12">%s</text><text x="%d" y="378" font-size="11.5" fill="#6a6a70">%s</text>' % (x + 14, t, x + 14, d))
        if k < 2: o.append('<text x="%d" y="368" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x + 222))
    o.append('<rect x="30" y="424" width="560" height="72" rx="12" fill="#fbe9e4"/>')
    o.append('<text x="48" y="452" font-size="13.5" font-weight="800" fill="#c8503c">김 길 — 틀 → 틀판 위 → 뒤 벽 위 구멍 Ø8 × 2 → 덕트 → 뒤 김 슬릿 (+ 뚜껑 열 때 조금)</text>')
    o.append('<text x="48" y="474" font-size="11.5" fill="#6a6a70">순간 하강 때와 뚜껑이 10mm 들릴 때 김이 나옴(3장 1.35g) · 사람이 젖히기 전 3초 · 덕트 아래 물받이 홈</text>')
    o.append('<rect x="610" y="424" width="560" height="72" rx="12" fill="#f3efe6"/>')
    o.append('<text x="628" y="452" font-size="13.5" font-weight="800" fill="#15151a">전기 — 220V 직결 · 약 1kW = 시즈 히터 450W × 2 + 모터 · 제어</text>')
    o.append('<text x="628" y="474" font-size="11.5" fill="#6a6a70">켜고 약 4분 데우면 「예열 완료」 불빛 · 뚜껑 열리면 히터 꺼짐 · NTC 2 + 온도 퓨즈 250°C 2중 차단</text>')
    o.append('</svg>')
    return '\n'.join(o)

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence), ('iso_heat', heating)]:
        with open(os.path.join(here, name + '.svg'), 'w', encoding='utf-8') as f: f.write(fn())
        print('wrote', name)
    img = os.path.join(os.path.dirname(here), 'img')
    for n, i in [('step1', 0), ('step2', 2), ('step3', 5)]:
        with open(os.path.join(img, n + '.svg'), 'w', encoding='utf-8') as f: f.write(sequence(only=i))
        print('wrote', n)
