# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 v9 (2026-11-25) — 「뚜껑형 1칸 · 틀 고정」 구조 (준보 「가자」 msg_a055c8ce · 「외부 구조도 바뀌어도 된다 · 새롭게」 msg_c91ce084 · msg_492e8e2c)
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
    I.box(50, 64, 12, 120, 92, 10, FRAME)
def frame_cols(I):
    """⑬ 기둥 2(x 50..62 · 158..170, y 98..110, z 22..136)"""
    I.box(50, 98, 22, 12, 12, 114, FRAME); I.box(158, 98, 22, 12, 12, 114, FRAME)
def frame_heads(I, locked=True):
    """⑬ 기둥 머리(z 136..158 · 윗보 끝을 감쌈) + 잠금 핀 Ø8(x 방향 · z 147)"""
    for x0 in (44, 152):
        I.box(x0, 92, 136, 24, 24, 22, FRAME, op=.92)
        if locked: I.box(x0 - 4, 105, 143, 32, 8, 8, DARK)

def cutaway():
    I = Iso(1.5, 560, 268, cut_y=110)
    W, D, H = 220, 220, 200
    # ---- 껍데기 뒤 벽 · 바닥 · 왼 벽 (몸체 0..150 · 흰 띠 150..158 · 뚜껑 158..196 · 상판 196..200) · 뒤 김 슬릿 · 덕트
    for (z0, h, col) in [(0, 150, PANEL), (150, 8, BAND), (158, 38, LID)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))
    for (z0, h, col) in [(0, 150, PANEL), (150, 8, BAND), (158, 38, LID)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col)
    I.poly([(70, 8, 138), (150, 8, 138), (150, 8, 146), (70, 8, 146)], '#2b2b30', 'none', 0, .85)   # 뒤 김 슬릿
    I.box(96, 48, 122, 28, 12, 22, STEEL, op=.9)                                                     # 김 덕트(뒤 벽 구멍 → 슬릿)
    I.box(60, 2, 150, 100, 10, 10, DARK)                                                             # ⑭ 경첩(뒤 · x 60..160)
    # ---- 바닥 칸: 무게판 · 틀 바닥판 · 보드 · 모터 · 캠 축 · 레버 · 푸시 로드
    I.box(14, 14, 6, 192, 192, 6, STEEL)                                        # ① 무게판
    frame_base(I)
    I.box(14, 60, 60, 3, 100, 70, BOARD)                                        # ⑨ 제어 보드(왼 벽)
    I.box(172, 78, 26, 34, 44, 24, MOTOR)                                       # ③ 모터(바닥 오른쪽 · 캠 축 직결)
    I.line([(172, 100, 40), (138, 100, 40)], MOTOR, 5)                          # 캠 축(x 방향)
    I.poly(cam_pts(130, 100, 40, 0.3), MOTOR, '#2b2b30', 0.9, .95)              # ④ 달팽이 캠(절단면 가까이 · 그림은 쉼 자리)
    I.box(148, 96, 22, 8, 8, 30, FRAME)                                         # 레버 받침(바닥판에)
    I.line([(152, 100, 50), (110, 100, 50)], MOTOR, 4.5)                        # 레버(받침 → 푸시 로드 · 1:2)
    I.line([(110, 100, 50), (110, 100, 80)], MOTOR, 5)                          # 푸시 로드(바닥 관통 · 벨로즈)
    I.box(100, 96, 26, 8, 8, 6, DARK)                                           # 캠 위치 센서
    # ---- 열 상자 뒤 · 왼 · 바닥(위 열림) · 김 구멍 2
    I.box(44, 60, 62, 132, 6, 96, INSUL)
    I.poly([(100, 66.2, 124), (108, 66.2, 124), (108, 66.2, 130), (100, 66.2, 130)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 66.2, 124), (120, 66.2, 124), (120, 66.2, 130), (112, 66.2, 130)], '#2b2b30', 'none', 0, .9)
    I.box(44, 66, 62, 6, 94, 96, INSUL)
    I.box(50, 66, 62, 120, 94, 6, INSUL, top=shade(INSUL, -.08))
    frame_cols(I)                                                               # ⑬ 기둥 2(바닥 관통)
    I.box(60, 66, 70, 100, 90, 2, STEEL, op=.9)                                 # ② 부스러기 서랍 바닥판(얇은 판 · 앞으로 당김)
    # ---- ⑤ 아래 열판(쉴 때): 받침(속 히터) + 피스톤 Ø59.6 + 퓨즈 + 되돌림 스프링 2
    I.box(70, 74, 80, 80, 72, 12, PLATE)
    I.box(74, 100, 83, 72, 20, 6, HTR, hatch_cut=False, faces='l')
    I.line([(92, 104, 68), (92, 104, 80)], HEAT, 2.4, '3 2'); I.line([(128, 104, 68), (128, 104, 80)], HEAT, 2.4, '3 2')
    I.cylz(CX, CY, 92, 29.8, REST - 92, PLATE); I.cylz(CX, CY, REST - 0.5, 29.8, 0.5, HEAT)
    I.box(150, 84, 82, 6, 8, 8, RED, hatch_cut=False)
    # ---- ⑥ 틀판: 턱(뒤 · 왼 · 오른) · 자리 핀 2 · 판 + Ø60 틀(아래로 16) · 마른 쌀 한 겹(피스톤 윗면)
    I.box(50, 66, 112, 120, 6, 4, FRAME); I.box(50, 66, 112, 6, 94, 4, FRAME)
    I.box(58, 102, 116, 3, 3, 4, DARK); I.box(159, 102, 116, 3, 3, 4, DARK)
    I.ringz(CX, CY, RING_Z0, 36, 30, RING_Z1 - RING_Z0, MOLD)                    # 틀 Ø72 바깥 · Ø60 안
    for k in range(7): I.out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="%s" stroke="#b9b2a2" stroke-width=".6"/>' % (I.P(92 + k * 6, 104 - (k % 2) * 4, REST + 1) + (RICE,)))
    I.box(56, 72, 116, 18, 82, 4, MOLD); I.box(146, 72, 116, 18, 82, 4, MOLD)     # 틀판 좌 · 우(틀 둘레는 링)
    I.box(74, 72, 116, 72, 2, 4, MOLD)                                           # 틀판 뒤 띠
    I.box(164, 66, 112, 6, 94, 4, FRAME)                                         # 턱 오른쪽
    # ---- ⑦ 위 열판 + 플러그(뚜껑 안) · 히터 · NTC · ⑬ 윗보 · 기둥 머리 · 잠금 핀 · 솔레노이드
    I.cylz(CX, CY, 116.5, 29.8, 5.5, PLATE)
    I.box(66, 72, 122, 88, 76, 14, PLATE)
    I.box(74, 100, 126, 72, 20, 6, HTR, hatch_cut=False, faces='l')
    I.box(150, 84, 126, 6, 8, 8, HEAT, hatch_cut=False)
    I.box(46, 90, 136, 128, 40, 22, FRAME)                                       # 윗보 40 × 22(뚜껑 안 · 양 끝이 기둥 머리에)
    frame_heads(I, locked=True)
    I.box(30, 96, 140, 12, 12, 10, MOTOR)                                        # 잠금 솔레노이드(핀 2를 당김)
    # ---- 열 상자 오른 벽 · 뚜껑 안 단열(위 덮개) · 뚜껑 열림 스위치
    I.box(170, 66, 62, 6, 94, 96, INSUL)
    I.box(44, 60, 158, 132, 100, 10, INSUL)
    I.box(100, 60, 150, 10, 6, 8, DARK)
    # ---- 김 길(점선 화살): 틀 → 틀판 위 → 뒤 벽 김 구멍 → 덕트 → 슬릿 → 밖
    I.line([(110, 110, 121), (110, 90, 128), (110, 68, 127)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    I.line([(110, 60, 128), (110, 54, 142), (110, 10, 142), (110, -14, 150)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    # ---- 힘 길(굵은 회색 화살): 캠 → 레버 → 로드 → 피스톤 → 쌀 → 플러그 → 위 열판 → 윗보 → 잠금 핀 → 기둥 → 바닥판 → 캠 축
    I.line([(136, 100, 84), (136, 100, 104)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(136, 100, 124), (136, 100, 138)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(164, 104, 150), (164, 104, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    I.line([(56, 104, 150), (56, 104, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    # 움직임 화살(피스톤 ↕)
    I.line([(80, 108, 105), (80, 108, 121)], HEAT, 1.8, None, 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')
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
    I.line([(100, 156, 116), (120, 156, 116), (120, 156, 122), (100, 156, 122), (100, 156, 116)], '#9aa3ad', 1, '3 3')   # ⑥ 틀판 앞 탭
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
    I.label((150, 110, 147), R, 148, '⑬ 뚜껑 윗보 40 × 22 + 기둥 머리 + 잠금 핀 Ø8 × 2', '닫으면 핀이 걸려 ㅁ자 틀 · 힘 1.4~4.2kN이 이 안에서만(회색 화살)', 'r')
    I.label((150, 88, 129), R, 194, '⑦ 위 열판 220°C + Ø59.6 플러그 6mm — 뚜껑 윗보에', '속 시즈 히터 450W(빨간 단면) · NTC 230°C · 닫으면 틀 안 3.5mm', 'r')
    I.label((146, 110, 118), R, 240, '⑥ 틀판 — 알루미늄 4t + Ø60 × 16 틀 · 턱 + 자리 핀 2', '세라믹 코팅 · 앞 탭 잡고 들어 씻음 · 틀 바닥 = 피스톤 윗면', 'r')
    I.label((140, 118, 100), R, 286, '⑤ 피스톤 Ø59.6(틈 0.2) + 받침 속 히터 450W · 퓨즈', '+10 누름 → −9 뻥 → +16 꺼내기 · 되돌림 스프링 2(주황 점선)', 'r')
    I.label((160, 100, 71), R, 330, '② 부스러기 서랍 — 열 상자 바닥 · 앞 아래로 당겨 비움', None, 'r')
    I.label((110, 100, 66), R, 366, '푸시 로드 — 열 상자 바닥 관통(벨로즈)', None, 'r')
    I.label((131, 100, 50), R, 402, '④ 레버(1:2) + 달팽이 캠 — 한 바퀴 = 한 장', '올림 10 → 멈춤 8~10초 → 절벽(뻥 9) → 올림 16 → 제자리 · 위치 센서', 'r')
    I.label((200, 90, 44), R, 448, '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결 · 자기 잠금', None, 'r')
    I.label((206, 110, 11), R, 488, '① 바닥 무게판 + 고무발 · 기울기 센서', None, 'r')
    I.label((110, 6, 155), L, 130, '⑭ 경첩(뒤) — 뚜껑이 뒤로 젖혀짐', None, 'l')
    I.label((110, 8, 142), L, 166, '⑩ 뒤 김 슬릿 — 김은 뒤로', None, 'l')
    I.label((104, 66.2, 127), L, 202, '⑧ 뒤 벽 위 김 구멍 Ø8 × 2 → 덕트', None, 'l')
    I.label((36, 102, 145), L, 238, '잠금 솔레노이드 — 완료 뒤 핀 2를 당김', None, 'l')
    I.label((15, 110, 95), L, 290, '⑨ 제어 보드 — 온도 · 기울기 · 뚜껑 잠금 · 캠 위치', None, 'l')
    I.label((110, 220, 168), L, 330, '⑭ 열림 단추(앞) — 점선 = 잘라낸 앞 절반', '완료 뒤 눌러 열기 · 뚜껑이 10mm 들려 김이 빠진 뒤 젖힘', 'l')
    I.label((110, 156, 119), L, 378, '⑥ 틀판 앞 탭 — 식은 뒤 들어 올림', None, 'l')
    I.label((80, 108, 113), L, 420, '움직임 ↕ — 피스톤만(10 · 9 · 16)', None, 'l')
    I.label((110, 220, 73), L, 464, '② 부스러기 서랍 앞판 — 앞 아래 작은 서랍', None, 'l')
    I.label((46, 196, 200), L, 520, '터치 · 상태 불빛(예열 · 굽는 중 · 완료 · 열어도 돼요) · 숫자 2', None, 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm(몸체 158 + 뚜껑 42) · 열 상자 132 × 100 × 96mm(단열 포함 · 위 열림) · 절단면은 앞뒤 가운데(y = 110) · 빗금 = 잘린 면 · 그림은 쉬는 상태(뚜껑 닫힘 · 잠김)', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 약 1kW(시즈 히터 450W × 2 + 모터 · 제어) · 바닥부터: 고무발 6 · 무게판 6 · 틀 바닥판 10 · 캠 · 모터 칸 40 · 열 상자 96 · 뚜껑 42 = 200mm', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1260 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def exploded():
    I = Iso(0.86, 480, 760)
    W, D, H = 220, 220, 200
    # L0 ① 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 ⑬ 바닥판 + 기둥 2 + ③ 모터 + ④ 캠 · 레버 · 푸시 로드
    z = 44; I.box(50, 64, z, 120, 92, 10, FRAME)
    I.box(172, 78, z + 14, 34, 44, 24, MOTOR); I.line([(172, 100, z + 28), (138, 100, z + 28)], MOTOR, 5)
    I.poly(cam_pts(130, 100, z + 28, 0.3), MOTOR, '#2b2b30', 0.9, .95)
    I.box(148, 96, z + 10, 8, 8, 30, FRAME); I.line([(152, 100, z + 38), (110, 100, z + 38)], MOTOR, 4.5); I.line([(110, 100, z + 38), (110, 100, z + 66)], MOTOR, 5)
    I.box(100, 96, z + 14, 8, 8, 6, DARK)
    I.box(50, 98, z + 10, 12, 12, 80, FRAME); I.box(158, 98, z + 10, 12, 12, 80, FRAME)
    for x0 in (44, 152): I.box(x0, 92, z + 90, 24, 24, 22, FRAME, op=.92); I.box(x0 - 4, 105, z + 97, 32, 8, 8, DARK)   # 기둥 머리 + 잠금 핀(분해도에선 기둥 위에)
    I.box(30, 96, z + 94, 12, 12, 10, MOTOR)
    # L2 ⑨ 보드(왼 벽)
    I.box(14, 60, 150, 3, 100, 70, BOARD)
    # L3 ② 부스러기 서랍(얇은 판 + 앞판)
    z = 190; I.box(60, 66, z, 100, 90, 2, STEEL, op=.95); I.box(56, 156, z - 6, 108, 8, 18, PANEL); I.line([(96, 165, z + 3), (124, 165, z + 3)], '#8a8a90', 2.4)
    # L4 ⑤ 아래 열판 = 받침(속 히터) + 피스톤 Ø59.6 + 퓨즈 + 스프링 2
    z = 232; I.box(70, 74, z, 80, 72, 12, PLATE); I.box(74, 100, z + 12, 72, 6, 3, HTR); I.cylz(CX, CY, z + 12, 29.8, 13, PLATE); I.cylz(CX, CY, z + 24.5, 29.8, 0.5, HEAT)
    I.box(150, 84, z + 2, 6, 8, 8, RED); I.line([(92, 104, z - 14), (92, 104, z)], HEAT, 2.4, '3 2'); I.line([(128, 104, z - 14), (128, 104, z)], HEAT, 2.4, '3 2')
    # L5 ⑧ 열 상자(위 열림 · 앞 벽 아래 부스러기 서랍 구멍 · 뒤 벽 위 김 구멍 2) + 턱(틀판 자리) + 자리 핀 2
    z = 300; hollow(I, 44, 60, z, 132, 100, 96, 6, INSUL, front=False)
    I.box(44, 154, z + 22, 132, 6, 74, INSUL); I.box(44, 154, z, 14, 6, 22, INSUL); I.box(162, 154, z, 14, 6, 22, INSUL)   # 앞 벽(아래 서랍 구멍)
    I.poly([(100, 60, z + 62), (108, 60, z + 62), (108, 60, z + 68), (100, 60, z + 68)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 60, z + 62), (120, 60, z + 62), (120, 60, z + 68), (112, 60, z + 68)], '#2b2b30', 'none', 0, .9)
    for (x0, y0, w, d) in [(50, 66, 120, 6), (50, 66, 6, 94), (164, 66, 6, 94), (50, 154, 120, 6)]: I.box(x0, y0, z + 50, w, d, 4, FRAME)
    I.box(58, 102, z + 54, 3, 3, 4, DARK); I.box(159, 102, z + 54, 3, 3, 4, DARK)
    # L6 ⑥ 틀판(판 + Ø60 틀 아래로 + 앞 탭 + 자리 핀 구멍 2) · ⑫ 숟가락
    z = 440; I.ringz(CX, CY, z - 16, 36, 30, 16, MOLD)
    I.box(56, 72, z, 18, 82, 4, MOLD); I.box(146, 72, z, 18, 82, 4, MOLD); I.box(74, 72, z, 72, 2, 4, MOLD); I.box(74, 146, z, 72, 8, 4, MOLD)
    I.ringz(CX, CY, z, 36, 30, 4, MOLD)
    I.box(100, 154, z, 20, 8, 4, '#9aa3ad')                                                          # 앞 탭
    for x0 in (58, 159): I.out.append('<circle cx="%.1f" cy="%.1f" r="2.2" fill="#55585e"/>' % I.P(x0 + 1.5, 103.5, z + 4))
    I.box(150, 30, z + 4, 6, 40, 3, STEEL); I.box(140, 10, z + 4, 26, 20, 3, STEEL)                   # ⑫ 계량 겸 펴개 숟가락(뚜껑 뒤 홈에 자석)
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
    z = 760; I.cylz(CX, CY, z - 5.5, 29.8, 5.5, PLATE); I.box(66, 72, z, 88, 76, 14, PLATE); I.box(74, 100, z + 14, 72, 6, 3, HTR); I.box(150, 84, z + 4, 6, 8, 8, HEAT)
    I.box(46, 90, z + 14, 128, 40, 22, FRAME)
    z = 830; I.box(44, 60, z, 132, 100, 10, INSUL)
    I.box(8, 8, z + 10, 204, 204, 28, LID, top=shade(LID, .1))
    I.box(-2, -2, z + 38, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    for x in (38, 54): sx, sy = I.P(x, 196, z + 42); I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/>' % (sx, sy))
    I.poly([(66, 192, z + 42.2), (88, 192, z + 42.2), (88, 200, z + 42.2), (66, 200, z + 42.2)], '#fff', 'none', 0)
    I.box(96, 212, z + 16, 28, 8, 8, DARK)                                                           # 열림 단추(앞)
    I.line([(110, 110, 0), (110, 110, 880)], '#b8b2a6', 1, '3 6', .8)
    # 라벨
    R = 690; L = 280
    I.label((110, 110, 874), R, 48, '⑭ 뚜껑 — 검은 내열 상판 · 터치 · 상태 불빛 · 앞 열림 단추 · 열림 스위치', None, 'r')
    I.label((176, 110, 836), R, 94, '⑧ 뚜껑 안 단열 10 — 열 상자 위를 덮음', None, 'r')
    I.label((160, 110, 786), R, 140, '⑬ 뚜껑 윗보 40 × 22 — 위 열판 고정 · 양 끝이 기둥 머리의 잠금 핀에 걸림', None, 'r')
    I.label((154, 110, 766), R, 180, '⑦ 위 열판 220°C + Ø59.6 플러그 6mm · 속 시즈 히터 450W · NTC — 뚜껑 안', None, 'r')
    I.label((212, 110, 620), R, 260, '⑩ 몸체 · 흰 띠(뚜껑 밑 테) · 김 덕트 · 뒤 슬릿 · 뒤 경첩 · 앞 아래 서랍 구멍', None, 'r')
    I.label((248, 110, 620), R, 296, '⑪ 옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((150, 150, 442), R, 376, '⑥ 틀판 — 알루미늄 108 × 82 × 4 + Ø60 × 16 틀(아래로) · 자리 핀 구멍 2 · 앞 탭', '세라믹 코팅 · 들어서 씻음 · 틀 바닥은 피스톤 윗면', 'r')
    I.label((153, 20, 448), L + 40, 420, '⑫ 펴개 숟가락 3g · 끝 폭 = 틀 Ø60 — 뚜껑 뒤 홈에 자석', None, 'l')
    I.label((176, 110, 348), R, 450, '⑧ 열 상자 — 강판 + 단열 5 · 위 열림 · 틀판 턱 + 자리 핀 2 · 뒤 벽 김 구멍 2', None, 'r')
    I.label((140, 118, 256), R, 520, '⑤ 아래 열판 = 받침(속 히터 450W · 퓨즈) + 피스톤 Ø59.6 × 13 — 10 · 9 · 16mm · 스프링 2', None, 'r')
    I.label((160, 100, 192), R, 566, '② 부스러기 서랍 — 열 상자 바닥 · 앞 아래로 당김', None, 'r')
    I.label((15, 110, 190), L, 600, '⑨ 제어 보드', None, 'l')
    I.label((164, 104, 110), R, 630, '⑬ 강철 틀 — 바닥판 10t + 기둥 12 × 12 두 개 + 기둥 머리(잠금 핀 2 · 솔레노이드)', '뚜껑 윗보와 함께 ㅁ자가 되어 누르는 힘이 여기서만 돎', 'r')
    I.label((130, 100, 72), R, 690, '④ 달팽이 캠 + 레버(1:2) + 푸시 로드 + 캠 위치 센서 — 한 바퀴 = 한 장', None, 'r')
    I.label((188, 90, 66), R, 730, '③ 모터(웜 기어드) — 바닥 오른쪽 · 캠 축 직결', None, 'r')
    I.label((206, 110, 3), R, 800, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.text(480, 962, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼어 씻는 것은 ⑥ 틀판 · ② 부스러기 서랍 둘뿐입니다. 부품 14개, 번호는 단면 · 동작 · 3D · 본문과 같습니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1250 980" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

# ---------------- 옆 단면(동작 순서 · 가열) ----------------
S = 1.1
def SX(y): return 66 + (166 - y) * S            # 앞(y 166) = x 66 · 뒤(y 60) = x 183
def SZ(z): return 238 - (z - 62) * S             # z 62 = y 238 · z 200 = y 86

def _rect(o, y0, y1, z0, z1, fill, extra=''):
    """mm 좌표(y 앞뒤 · z 높이)로 옆 단면 사각형"""
    x = SX(y1); w = (y1 - y0) * S; yy = SZ(z1); h = (z1 - z0) * S
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" %s/>' % (x, yy, w, h, fill, extra))

def _panel(o, i, lift, lid_up, cake=None, rice=True, lock=False, steam=False, press=False, spoon=False, heater_on=True, pop=False):
    """열 상자 옆 단면 한 칸. lift = 피스톤 올라간 mm(0~16) · lid_up = 뚜껑 들린 mm(0 닫힘 · 10 살짝 · 40 열림)
    고정: 열 상자 · ⑬ 기둥 · 머리 · 틀판(턱) · 레일 없음. 움직임: ⑤ 피스톤(lift) · 뚜껑(위 열판 · 플러그 · 윗보 · 단열 · 상판 전부 lid_up 만큼 위로)"""
    o.append('<rect x="58" y="62" width="134" height="176" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
    lk = '#d19a3c' if lock else '#9aa3ad'
    o.append('<rect x="170" y="50" width="22" height="16" rx="3" fill="%s"/><path d="M175 50 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lk, lk))
    o.append('<text x="52" y="236" font-size="9.5" fill="#6a6a70" text-anchor="middle">앞</text>')
    # ⑧ 열 상자 벽(앞 · 뒤 · 바닥) · 뒤 벽 김 구멍 · 기둥(y 98..110) · 턱 · 틀판 + 틀(고정)
    _rect(o, 160, 166, 62, 158, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"'); _rect(o, 60, 66, 62, 158, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 66, 160, 62, 68, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 60, 66, 124, 130, '#15151a')
    _rect(o, 98, 110, 68, 136, '#4f5864'); _rect(o, 92, 116, 136, 158, '#4f5864', 'opacity=".9"')
    o.append('<text x="%.1f" y="%.1f" font-size="8.5" fill="#fff" text-anchor="middle">틀</text>' % (SX(104), SZ(100)))
    _rect(o, 66, 72, 112, 116, '#4f5864'); _rect(o, 154, 160, 112, 116, '#4f5864')                   # 턱
    _rect(o, 72, 80, 116, 120, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"'); _rect(o, 140, 154, 116, 120, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')   # 틀판
    _rect(o, 74, 80, 104, 116, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"'); _rect(o, 140, 146, 104, 116, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')   # 틀 Ø60(안 80..140)
    # ② 부스러기 서랍(바닥) · ⑤ 받침(히터) + 피스톤(lift) · 스프링
    _rect(o, 66, 156, 70, 72, '#b9bec4')
    zp = lift
    _rect(o, 74, 146, 80 + zp, 92 + zp, '#8a8f96', 'rx="2"'); _rect(o, 100, 120, 83 + zp, 89 + zp, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
    _rect(o, 80.2, 139.8, 92 + zp, 105 + zp, '#8a8f96'); _rect(o, 80.2, 139.8, 104.5 + zp, 105.5 + zp, '#d19a3c')
    _rect(o, 84, 92, 82 + zp, 90 + zp, '#e06c5a')
    for yy in (90, 130):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="1.4" stroke-dasharray="2 2"/>' % (SX(yy), SZ(68), SX(yy), SZ(80 + zp)))
    # 쌀 · 떡뻥(피스톤 윗면 위)
    top = REST + zp
    if cake == 'pressed':
        _rect(o, 80.2, 139.8, top, top + 1.5, '#e9dcc0', 'stroke="#d19a3c" stroke-width=".6"')
    elif cake in ('puffed', 'done'):
        _rect(o, 80.2, 139.8, top, top + DROP + 1.5, '#fff3dc', 'rx="4" stroke="#d19a3c"')
    elif rice:
        for k in range(7): o.append('<circle cx="%.1f" cy="%.1f" r="1.8" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (SX(136 - k * 8), SZ(top + 1.5)))
    if spoon:
        o.append('<path d="M%.1f %.1f l-22 -30 l-10 0" fill="none" stroke="#9aa3ad" stroke-width="3" stroke-linecap="round"/>' % (SX(118), SZ(top + 6)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">⑫ 숟가락 3g</text>' % (SX(166) - 2, SZ(150)))
    # ⑭ 뚜껑(lid_up 만큼 위로): 단열 · 껍데기 · 상판 · ⑦ 위 열판 + 플러그 · ⑬ 윗보 · 잠금 핀
    u = lid_up
    _rect(o, 60, 166, 158 + u, 168 + u, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 56, 170, 168 + u, 196 + u, '#2a2a2f', 'rx="3"'); _rect(o, 54, 172, 196 + u, 200 + u, '#101014', 'rx="2"')
    _rect(o, 72, 148, 122 + u, 136 + u, '#8a8f96', 'rx="2"'); _rect(o, 76, 144, 126 + u, 132 + u, '#c8503c' if heater_on else '#9a9a9e', 'rx="3"')
    _rect(o, 80.2, 139.8, 116.5 + u, 122 + u, '#8a8f96'); _rect(o, 80.2, 139.8, 116.5 + u, 117.5 + u, '#d19a3c')
    _rect(o, 136, 142, 130 + u, 135 + u, '#15151a')
    _rect(o, 90, 130, 136 + u, 158 + u, '#4f5864')                                                   # 윗보(옆에서 y 90..130)
    if lock: _rect(o, 86, 134, 145, 149, '#15151a')                                                  # 잠금 핀(머리 안 · 윗보 관통)
    o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#6a6a70">뚜껑</text>' % (SX(166) + 2, SZ(184 + u)))
    if u > 0: o.append('<text x="%.1f" y="%.1f" font-size="9.5" font-weight="800" fill="#8a5d12">열림 %s</text>' % (SX(60) + 4, SZ(176 + u), '10mm' if u < 20 else ''))
    # 열 · 압력 화살(누르는 중)
    if press:
        for k in range(3):
            x = SX(126 - k * 12)
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(128), x, SZ(118)))
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(92 + zp), x, SZ(103 + zp)))
    if steam:
        o.append('<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" stroke="#d19a3c" stroke-width="1.6" stroke-dasharray="3 3" marker-end="url(#arr)"/>' % (SX(110), SZ(121), SX(96), SZ(128), SX(76), SZ(128), SX(67), SZ(127)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#8a5d12">김 → 뒤 구멍</text>' % (SX(112), SZ(140)))
    if pop: o.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="800" fill="#8a5d12">9mm 툭 · 뻥</text>' % (SX(164), SZ(96)))
    # ④ 캠 · 레버 · 푸시 로드 · ③ 모터(바닥 칸)
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(100), SZ(80 + zp), SX(100), SZ(50)))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="3.5" stroke-linecap="round"/>' % (SX(100), SZ(50), SX(100) + 40, SZ(50) - 2))   # 레버(옆에서 보면 x 방향이라 짧게)
    r = 10 + 8 * (lift / 16.0)
    o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#5a5e66" opacity=".9"/><circle cx="%.1f" cy="%.1f" r="2.2" fill="#15151a"/>' % (SX(100) + 20, SZ(40), r * S, SX(100) + 20, SZ(40)))
    o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#6a6a70">④ 캠</text>' % (SX(100) + 36, SZ(36)))
    o.append('<rect x="%.1f" y="276" width="%.1f" height="5" fill="#4f5864"/>' % (SX(156), 92 * S))   # 틀 바닥판
    o.append('<rect x="100" y="286" width="40" height="14" rx="4" fill="#5a5e66"/><text x="146" y="297" font-size="10" fill="#6a6a70">③ 모터</text>')

def sequence(only=None):
    """동작 순서 ①~⑥ 6칸 — 옆에서 본 열 상자(왼쪽 = 앞). 틀판 · 기둥 고정, 피스톤만 오르내리고 뚜껑은 사람이 여닫음"""
    pw = 252; gap = 16
    titles = [('① 뚜껑 열고 쌀 넣기', '예열 끝 · 5초', '예열 불빛 → 열림 단추 → 뚜껑 젖힘(히터 꺼짐)|⑫ 숟가락에 마른 쌀 3g(불리지 않음)|틀에 쓸어 넣어 한 겹(바닥 2/3)|틀 바닥 = 피스톤 윗면 · 틀판은 고정'),
              ('② 뚜껑 닫고 시작', '220°C · 1초', '뚜껑을 닫으면 잠금 핀 2가 딸깍 → ㅁ자 틀 닫힘|플러그가 틀 안으로 3.5mm(쌀엔 안 닿음)|시작 터치 → 모터가 캠을 돌림'),
              ('③ 올려 누르기 8~10초', '220°C · 8~10초', '캠이 피스톤을 10mm 올림 → 쌀 1.5mm|열판 두 장이 위 · 아래에서 데움|틀이 플러그로 막혀 압력 ↑ · 캠은 멈춤'),
              ('④ 순간 하강 9mm', '220°C · 0.1초', '캠 절벽 → 압력 + 스프링이 피스톤을 9mm 툭|압력이 한순간에 풀려 「뻥」|두께 ≈ 10.5mm · 플러그는 아직 틀 안'),
              ('⑤ 완료 · 뚜껑 열림', '완료 불빛 · 3초', '잠금 핀 풀림 → 뚜껑이 10mm 들림|김은 뒤 구멍 · 뚜껑 틈으로|사람이 뚜껑을 젖히면 히터 꺼짐'),
              ('⑥ 올려서 꺼내기', '열림 확인 · 5초', '열림 스위치 → 캠이 피스톤을 16mm 올림|떡뻥이 틀 위로 나옴 → 집게 · 손끝|피스톤 제자리 → 다음 장 · 한 장 약 25초')]
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
        if i == 2: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 10</text>' % (SX(166) - 10, SZ(84), SX(166) - 10, SZ(104), SX(166) - 8, SZ(92)))
        if i == 5: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 16</text>' % (SX(166) - 10, SZ(90), SX(166) - 10, SZ(116), SX(166) - 8, SZ(100)))
        for k, w in enumerate(titles[i][2].split('|')): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (318 + k * 16, w))
        o.append('</g>')
        if n < N - 1: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

def heating():
    """가열 방식 — 누르는 중(③) 옆 단면 1.7배 + 원리 3단 + 아래 띠(김 길 · 전기)"""
    o = ['<svg viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS)]
    o.append('<g transform="translate(30,50) scale(1.75) translate(-58,-62)">')
    _panel(o, 2, lift=UP, lid_up=0, lock=True, cake='pressed', press=True)
    o.append('</g>')
    o.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="800" fill="#15151a">누르는 중(③) · 열 상자 옆 단면 · 왼쪽 = 앞 · 뚜껑 닫힘 · 잠김</text>' % (30, 22))
    def lab(py, pz, sx, sy, t, sub=None):
        px = 30 + 1.75 * (SX(py) - 58); pyy = 50 + 1.75 * (SZ(pz) - 62)
        o.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#d19a3c" stroke="#fff" stroke-width="1.2"/><polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (px, pyy, px, pyy, sx - 14, sy - 4, sx - 6, sy - 4))
        o.append('<text x="%d" y="%d" font-size="13.5" font-weight="800" fill="#15151a">%s</text>' % (sx, sy, t))
        if sub: o.append('<text x="%d" y="%d" font-size="11.5" font-weight="600" fill="#6a6a70">%s</text>' % (sx, sy + 15, sub))
    LX = 500
    lab(100, 147, LX, 72, '⑬ 뚜껑 윗보 40 × 22 + 잠금 핀 Ø8 × 2 — 누르는 힘 1.4~4.2kN이 핀 → 기둥 2 → 바닥판으로 닫힘', '핀 전단 약 42MPa · 윗보 굽힘 약 31MPa · 몸체 · 뚜껑 껍데기엔 힘이 걸리지 않음')
    lab(76, 129, LX, 128, '⑦ 위 열판 — 알루미늄 다이캐스트 · 속에 시즈 히터 450W(빨강) · NTC — 뚜껑 안', '220°C 유지 · 상한 230°C · 뚜껑 윗보에 볼트로 고정')
    lab(100, 119, LX, 184, '⑦ 플러그 Ø59.6 — 닫으면 틀 안으로 3.5mm · 틈 0.2mm · 입구 모따기 1mm', '쌀 1.5mm 두께로 눌림 · 물기가 끓어 0.5~1.5MPa(틀 안)')
    lab(72, 118, LX, 240, '⑥ 틀판 — Ø60 × 16 틀 · 턱 + 자리 핀 2로 피스톤과 같은 강철 틀에 정렬', '마른 쌀 3g 한 겹 · 틀판은 움직이지 않음 · 들어서 씻음')
    lab(76, 100, LX, 296, '⑤ 피스톤 Ø59.6 + 받침 — 속에 시즈 히터 450W(빨강) · 온도 퓨즈 250°C', '10mm 올라간 상태 · 캠 멈춤(일정 반지름)이라 모터엔 힘이 안 걸림')
    steps = [('① 열 전달 · 8~10초', '220°C 판 두 장이 위 · 아래에서 바로 데움'), ('② 압력 ↑', '틀이 플러그로 막혀 물기가 끓어 0.5~1.5MPa'), ('③ 9mm 순간 하강', '캠 절벽 → 압력이 한꺼번에 빠지며 「뻥」 · 두께 약 10.5mm')]
    for k, (t, d) in enumerate(steps):
        x = 500 + k * 230
        o.append('<rect x="%d" y="330" width="214" height="64" rx="12" fill="#fff" stroke="#e6e1d7"/>' % x)
        o.append('<text x="%d" y="356" font-size="13.5" font-weight="800" fill="#8a5d12">%s</text><text x="%d" y="378" font-size="11.5" fill="#6a6a70">%s</text>' % (x + 14, t, x + 14, d))
        if k < 2: o.append('<text x="%d" y="368" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x + 222))
    o.append('<rect x="30" y="424" width="560" height="72" rx="12" fill="#fbe9e4"/>')
    o.append('<text x="48" y="452" font-size="13.5" font-weight="800" fill="#c8503c">김 길 — 틀 → 틀판 위 → 뒤 벽 위 구멍 Ø8 × 2 → 덕트 → 뒤 김 슬릿 (+ 뚜껑 열 때 조금)</text>')
    o.append('<text x="48" y="474" font-size="11.5" fill="#6a6a70">순간 하강 때와 뚜껑이 10mm 들릴 때 김이 나옴(한 장 0.45g) · 사람이 젖히기 전 3초 · 덕트 아래 물받이 홈</text>')
    o.append('<rect x="610" y="424" width="560" height="72" rx="12" fill="#f3efe6"/>')
    o.append('<text x="628" y="452" font-size="13.5" font-weight="800" fill="#15151a">전기 — 220V 직결 · 약 1kW = 시즈 히터 450W × 2 + 모터 · 제어</text>')
    o.append('<text x="628" y="474" font-size="11.5" fill="#6a6a70">켜고 약 3분 데우면 「예열 완료」 불빛 · 뚜껑 열리면 히터 꺼짐 · NTC 2 + 온도 퓨즈 250°C 2중 차단</text>')
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
