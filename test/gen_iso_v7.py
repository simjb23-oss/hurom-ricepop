# -*- coding: utf-8 -*-
"""쌀참 2.5D 구조도 생성기 v7 (2026-11-25) — 몰드 서랍 구조
두팔 검토(msg_de2e0e1d · msg_b5aa8dec) 반영: 카세트 · 깔때기 · 계량 컵 · 슬라이드 · 배출 슬롯 · 플랩 · 트레이 · 앞문 삭제.
마른 쌀 3g을 계량 숟가락으로 서랍의 몰드 트레이(Ø6 오목)에 넣고 밀어 넣음 → 피스톤이 트레이를 들어 올려 위 열판의 플러그(Ø59)가
틀 안으로 13.5mm 들어가며 누름(쌀 1.5mm) → 래치가 8~10mm 순간 하강(떡뻥 두께 = 틈 + 쌀 층 ≈ 9~11mm) → 모터가 천천히 내림 → 서랍 잠금 해제 → 빼서 꺼냄.
힘: 플러그 ← 위 열판 ← 윗보 ← 기둥 2 ← 바닥판 ← 토글 고정 핀 ↔ 토글 → 푸시 로드 → 피스톤 → 트레이 → 쌀 (ㅁ자 강철 틀 ⑬ 안에서 닫힘, 몸체엔 힘 없음)
김: 틀 안 → (순간 하강 · 플러그가 빠질 때) 열 상자 안 → 뒤 벽 위 김 구멍 2 → 덕트(공기층 뒤) → 몸체 뒤 김 슬릿
쌀: 계량 숟가락 3g → 트레이 틀(한 겹으로 펴짐) → 서랍 밀어 넣기 → 누르기 · 뻥 → 트레이 안 떡뻥 → 서랍 빼서 집기

좌표(mm): x 0..220 왼→오, y 0..220 뒤→앞, z 0..200 아래→위. 보는 방향 = 앞·오른쪽·위.
부품 번호(모든 그림 · 3D · 본문 공통):
 ① 바닥 무게판 · 고무발 · 기울기 센서  ② 부스러기 받침(열 상자 바닥 · 앞으로 당김)  ③ 승강 모터(웜 · 바닥 오른쪽)
 ④ 토글 링크 · 래치 스프링 · 리밋 2 · 푸시 로드(바닥 칸, 틀 바닥판에 핀)  ⑤ 아래 열판 = 받침(속 시즈 히터 450W · 퓨즈 250°C) + 피스톤 Ø70(오르내림 20mm)
 ⑥ 몰드 서랍 = 단열 손잡이 앞판 + 레일 프레임 + 몰드 트레이(Ø6 오목 틀 · 세라믹 코팅 · 들어서 분리) + 서랍 잠금(완료 뒤 해제)
 ⑦ 위 열판 + Ø59 플러그(고정 · 틀 윗보에 볼트) · 속 시즈 히터 450W · NTC  ⑧ 열 상자(강판 1.5 + 단열 5mm) · 뒤 벽 위 김 구멍 2
 ⑨ 제어 보드  ⑩ 몸체 · 흰 띠 · 공기층 10mm · 김 덕트 · 뒤 김 슬릿  ⑪ 옆 패널 4장 · 비스포크  ⑫ 계량 숟가락 3g(서랍 앞판 안쪽 클립)
 ⑬ ㅁ자 강철 틀 = 바닥판 8t + 기둥 12×12 두 개 + 윗보 12×80 눕힌 강판(위 열판 고정 · 굽힘 약 52MPa)  ⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛
높이(z): 고무발 6 · 무게판 8..14 · 틀 바닥판 14..22 · 토글 · 모터 칸 22..44 · 열 상자 44..150(안 50..144) · 공기층 150..196 · 상판 196..200
열 상자 안: 부스러기 받침 52..54 · 받침 60..72(히터 63..69) · 피스톤 72..80(쉴 때 면 80) · 트레이 82..100(틀 안 85..100 · 바닥 82..85 · 플랜지 94..100)
 · 서랍 프레임 88..94 · 플러그 104.5..118 · 위 열판 118..132(히터 122..128) · 윗보 132..144 · 기둥 22..132 · 김 구멍 134..140(뒤 벽)
행정: 쉼 80 → +2 트레이에 닿음 → +20 누름(트레이 윗면 118 = 위 열판 밑면, 플러그 13.5 들어감, 쌀 1.5mm) → 8~10 순간 하강 → 천천히 쉼으로
"""
import sys, os, math
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_iso import Iso, shade, DEFS, FONT, PANEL, BODY, BAND, GLASS, STEEL, PLATE, HEAT, MOLD, CRACK, DARK, MOTOR, BOARD, RICE, INSUL, RED, HTR, hollow

FRAME = '#4f5864'   # 강철 틀(짙은 청회색)
CX, CY = 110, 110
UP = 20            # 피스톤 행정
DROP = 9           # 순간 하강(8~10)

def frame_cut(I):
    """⑬ ㅁ자 틀 — 바닥판(z 14..22) · 기둥 2(x 50..62 · 158..170, y 98..110, z 22..132) · 윗보(z 132..144, y 70..150)"""
    I.box(50, 64, 14, 120, 92, 8, FRAME)
def frame_cols(I):
    I.box(50, 98, 22, 12, 12, 110, FRAME); I.box(158, 98, 22, 12, 12, 110, FRAME)

def cutaway():
    I = Iso(1.5, 560, 268, cut_y=110)
    W, D, H = 220, 220, 200
    # ---- 껍데기(뒤 벽 · 바닥 · 왼 벽) · 뒤 김 슬릿 · 김 덕트(뒤 벽과 열 상자 사이)
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 0, z0, W, 8, h, col, left=BODY if col == PANEL else col)
    I.box(8, 8, 0, 204, 212, 8, BODY, top=shade(BODY, -.05))
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(0, 8, z0, 8, 212, h, col, right=BODY if col == PANEL else col)
    I.poly([(70, 8, 172), (150, 8, 172), (150, 8, 180), (70, 8, 180)], '#2b2b30', 'none', 0, .85)   # 뒤 김 슬릿
    I.box(96, 48, 136, 28, 12, 40, STEEL, op=.9)                                                     # 김 덕트(뒤 벽 → 슬릿)
    # ---- 바닥 칸: 무게판 · 틀 바닥판 · 보드 · 모터 · 토글(틀 바닥판 핀)
    I.box(14, 14, 8, 192, 192, 6, STEEL)                                        # ① 무게판
    frame_cut(I)                                                                # ⑬ 바닥판 + 기둥
    I.box(14, 60, 60, 3, 100, 80, BOARD)                                        # ⑨ 제어 보드(왼 벽)
    I.box(170, 70, 22, 36, 40, 20, MOTOR)                                       # ③ 승강 모터(바닥 오른쪽)
    I.line([(170, 90, 32), (130, 100, 32)], MOTOR, 5)                           # 크랭크 → 푸시 로드(가로)
    I.line([(130, 100, 32), (110, 100, 24), (110, 100, 40)], MOTOR, 4.2)        # ④ 토글(접힘) — 아래 핀은 틀 바닥판
    I.line([(96, 100, 30), (110, 100, 24), (124, 100, 30), (110, 100, 40)], MOTOR, 4.2)
    I.box(140, 96, 24, 8, 8, 6, DARK); I.box(140, 96, 38, 8, 8, 6, DARK)         # 리밋 2
    I.line([(150, 100, 24), (150, 100, 42)], HEAT, 2.4, '3 2')                  # 래치 스프링
    # ---- 열 상자 뒤 · 왼 · 바닥(푸시 로드 관통) · 김 구멍 2
    I.box(44, 60, 44, 132, 6, 106, INSUL)
    I.poly([(100, 66.2, 134), (108, 66.2, 134), (108, 66.2, 140), (100, 66.2, 140)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 66.2, 134), (120, 66.2, 134), (120, 66.2, 140), (112, 66.2, 140)], '#2b2b30', 'none', 0, .9)
    I.box(44, 66, 44, 6, 94, 106, INSUL)
    I.box(50, 66, 44, 120, 94, 6, INSUL, top=shade(INSUL, -.08))
    frame_cols(I)                                                               # ⑬ 기둥 2(바닥 관통) — 왼 벽 · 바닥 뒤에 그림
    I.line([(110, 100, 40), (110, 100, 60)], MOTOR, 5)                          # 푸시 로드(바닥 관통 · 벨로즈)
    I.box(50, 66, 52, 120, 94, 2, STEEL, op=.9)                                 # ② 부스러기 받침(얇은 판)
    # ---- ⑤ 아래 열판(쉴 때): 받침(속 히터) + 피스톤 Ø70 + 퓨즈
    I.box(70, 74, 60, 80, 72, 12, PLATE)
    I.box(74, 100, 63, 72, 20, 6, HTR, hatch_cut=False, faces='l')
    I.cylz(CX, CY, 72, 35, 8, PLATE); I.cylz(CX, CY, 79.5, 35, 0.5, HEAT)
    I.box(150, 84, 62, 6, 8, 8, RED, hatch_cut=False)
    # ---- ⑥ 몰드 서랍: 레일(옆 벽) · 프레임 바 2 · 몰드 트레이(틀 안 마른 쌀 한 겹)
    I.box(50, 66, 88, 6, 88, 6, STEEL); I.box(164, 66, 88, 6, 88, 6, STEEL)       # 레일
    I.box(62, 66, 88, 6, 88, 6, DARK); I.box(152, 66, 88, 6, 88, 6, DARK)         # 서랍 프레임 바(앞판까지)
    I.box(62, 66, 88, 96, 6, 6, DARK)                                             # 뒤 가로 바
    I.ringz(CX, CY, 82, 39, 30, 18, MOLD)                                         # 트레이 Ø78 · 틀 Ø60
    I.ringz(CX, CY, 94, 44, 39, 6, MOLD)                                          # 플랜지 Ø88
    for k in range(7): I.out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="%s" stroke="#b9b2a2" stroke-width=".6"/>' % (I.P(92 + k * 6, 104 - (k % 2) * 4, 86) + (RICE,)))
    # ---- ⑦ 위 열판 + 플러그 · 히터 · NTC · ⑬ 윗보
    I.cylz(CX, CY, 104.5, 29.5, 13.5, PLATE)
    I.box(66, 72, 118, 88, 76, 14, PLATE)
    I.box(74, 100, 122, 72, 20, 6, HTR, hatch_cut=False, faces='l')
    I.box(150, 84, 122, 6, 8, 8, HEAT, hatch_cut=False)
    I.box(50, 70, 132, 120, 80, 12, FRAME)                                        # 윗보(기둥 위)
    # ---- 열 상자 오른 벽 · 천장
    I.box(170, 66, 44, 6, 94, 106, INSUL)
    I.box(44, 60, 144, 132, 100, 6, INSUL)
    # ---- 김 길(점선 화살): 틀 → 열 상자 안 → 뒤 벽 김 구멍 → 덕트 → 슬릿 → 밖
    I.line([(110, 110, 101), (110, 90, 128), (110, 68, 137)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    I.line([(110, 60, 140), (110, 54, 172), (110, 10, 176), (110, -14, 190)], HEAT, 1.8, '4 4', .95, marker='marker-end="url(#arr)"')
    # ---- 힘 길(굵은 회색 화살): 토글 → 로드 → 피스톤 → 트레이 → 플러그 → 윗보 → 기둥 → 바닥판 → 토글
    I.line([(136, 100, 46), (136, 100, 78)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(136, 100, 120), (136, 100, 134)], FRAME, 2.6, None, .9, marker='marker-end="url(#arrg)"')
    I.line([(164, 104, 134), (164, 104, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    I.line([(56, 104, 134), (56, 104, 24)], FRAME, 2.6, '6 3', .9, marker='marker-end="url(#arrg)"')
    # 움직임 화살(↕ 20mm)
    I.line([(80, 108, 80), (80, 108, 100)], HEAT, 1.8, None, 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')
    # ---- 오른 벽
    for (z0, h, col) in [(0, 180, PANEL), (180, 10, BAND), (190, 6, BODY)]:
        I.box(212, 8, z0, 8, 212, h, col)
    # ---- ⑭ 상판(창 없음) · 터치
    I.box(-2, -2, 196, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    # ---- 앞 절반 고스트: 서랍 앞판(겉) · 손잡이 · 부스러기 받침 손잡이 · 터치
    I.ghost_box(0, 110, 0, 220, 110, 200)
    I.ghost_box(58, 154, 76, 104, 6, 32, '#9a948a', 1, '3 3')                                          # 열 상자 앞 벽의 서랍 구멍(안쪽 단열판 자리)
    I.line([(56, 220, 74), (164, 220, 74), (164, 220, 118), (56, 220, 118), (56, 220, 74)], '#8a5d12', 1.2, '4 3')   # 서랍 겉 앞판
    I.line([(76, 222, 96), (144, 222, 96)], '#8a5d12', 3.2)                                           # 손잡이(단열)
    I.line([(66, 220, 52), (154, 220, 52), (154, 220, 58), (66, 220, 58), (66, 220, 52)], '#8a8a90', 1, '3 3')   # 부스러기 받침 앞턱
    for x in (38, 54): sx, sy = I.P(x, 196, 200); I.out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="none" stroke="#8a8a90" stroke-dasharray="2 2"/>' % (sx, sy))
    I.line([(66, 196, 200), (88, 196, 200)], '#8a8a90', 2, '2 2')
    I.line([(110, 160, 96), (110, 206, 96)], HEAT, 1.6, '4 3', 1, marker='marker-start="url(#arr)" marker-end="url(#arr)"')   # 서랍 앞뒤
    I.line([(176, 100, 100), (212, 100, 100)], '#6a6a70', 1, None, 1, marker='marker-start="url(#arrg)" marker-end="url(#arrg)"')
    # ---- 라벨
    R = 850; L = 330
    I.label((110, 110, 200), R, 56, '⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛', '창 없음 · 유리 아님 · 카세트 덮개 없음', 'r')
    I.label((110, 54, 160), R, 104, '⑩ 김 덕트 → 뒤 김 슬릿', '점선 주황 화살 = 김 길 · 틀 → 열 상자 → 뒤 벽 구멍 → 덕트 → 슬릿', 'r')
    I.label((194, 100, 100), R, 152, '⑩ 이중벽 공기층 10mm + ⑧ 단열 5mm', '겉면 60°C 이하 · 몸체엔 힘이 걸리지 않음', 'r')
    I.label((150, 110, 138), R, 198, '⑬ ㅁ자 강철 틀 — 윗보 12 × 80 · 기둥 12 × 12 두 개 · 바닥판 8t', '누르는 힘 1.4~4.2kN이 이 틀 안에서 닫힘(회색 화살) · 윗보 굽힘 약 52MPa', 'r')
    I.label((150, 88, 125), R, 240, '⑦ 위 열판 220°C + Ø59 플러그 — 윗보에 고정', '속 시즈 히터 450W(빨간 단면) · NTC 상한 230°C', 'r')
    I.label((146, 110, 97), R, 282, '⑥ 몰드 트레이 — Ø6 오목 틀 15mm · 서랍 프레임에 얹힘', '마른 쌀 3g 한 겹 · 세라믹 코팅 · 들어서 씻음', 'r')
    I.label((144, 118, 76), R, 324, '⑤ 피스톤 Ø70 · 받침 속 시즈 히터 450W · 퓨즈 250°C', '쉴 땐 트레이 2mm 아래 · 올라가 트레이째 20mm 밀어 올림', 'r')
    I.label((160, 100, 53), R, 366, '② 부스러기 받침 — 열 상자 바닥 · 앞으로 당겨 비움', None, 'r')
    I.label((110, 100, 50), R, 400, '푸시 로드 — 열 상자 바닥 관통(벨로즈)', None, 'r')
    I.label((110, 100, 30), R, 436, '④ 토글 링크 — 사점 잠금 · 래치 스프링 8~10mm · 리밋 2', '핀은 ⑬ 틀 바닥판에 · 그 뒤 모터가 천천히', 'r')
    I.label((200, 90, 42), R, 478, '③ 승강 모터(웜) — 바닥 오른쪽 · 정전에도 자기 잠금', None, 'r')
    I.label((206, 110, 11), R, 518, '① 바닥 무게판 + 고무발 · 기울기 센서', None, 'r')
    I.label((110, 8, 176), L, 150, '⑩ 뒤 김 슬릿(위) — 김은 뒤로만', None, 'l')
    I.label((15, 110, 100), L, 226, '⑨ 제어 보드 — 온도 · 기울기 · 서랍 잠금', None, 'l')
    I.label((104, 66.2, 137), L, 190, '⑧ 뒤 벽 위 김 구멍 Ø8 × 2', None, 'l')
    I.label((110, 220, 96), L, 300, '⑥ 서랍 겉 앞판 + 단열 손잡이', '점선 = 잘라낸 앞 절반 · 완료 뒤에만 열림(잠금)', 'l')
    I.label((110, 183, 96), L, 356, '서랍 앞뒤 ↔ — 사람이 당김', '안쪽 단열판 + 테두리 실리콘 개스킷이 앞 구멍을 막음', 'l')
    I.label((80, 108, 90), L, 410, '움직임 ↕ 20mm — 피스톤만', None, 'l')
    I.label((110, 220, 55), L, 456, '② 부스러기 받침 앞턱', None, 'l')
    I.label((46, 196, 200), L, 520, '터치 · 상태 불빛(예열 · 굽는 중 · 완료) · 숫자 2', None, 'l')
    I.text(600, 712, '바깥 220 × 220 × 200mm · 열 상자 132 × 100 × 106mm(단열 포함) · 절단면은 앞뒤 가운데(y = 110) · 빗금 = 잘린 면 · 그림은 쉬는 상태(서랍 닫힘)', 12.5, 600, '#6a6a70', 'middle')
    I.text(600, 732, '220V 약 1kW(시즈 히터 450W × 2 + 모터 · 제어) · 바닥부터: 고무발 6 · 무게판 8 · 틀 바닥판 8 · 토글 · 모터 칸 22 · 열 상자 106 · 공기층 46 · 상판 4 = 200mm', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1260 750" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

def exploded():
    I = Iso(0.86, 480, 760)
    W, D, H = 220, 220, 200
    # L0 ① 무게판 · 고무발
    for (x, y) in [(20, 20), (180, 20), (20, 180), (180, 180)]: I.box(x, y, -8, 20, 20, 8, '#333338')
    I.box(14, 14, 0, 192, 192, 6, STEEL)
    # L1 ⑬ ㅁ자 틀(바닥판 + 기둥 2 + 윗보 — 한 몸) + ③ 모터 + ④ 토글
    z = 44; I.box(50, 64, z, 120, 92, 8, FRAME)
    I.box(170, 70, z + 8, 36, 40, 20, MOTOR); I.line([(170, 90, z + 18), (130, 100, z + 18), (110, 100, z + 10), (110, 100, z + 26)], MOTOR, 4.5)
    I.line([(96, 100, z + 16), (110, 100, z + 10), (124, 100, z + 16), (110, 100, z + 26)], MOTOR, 4.2)
    I.line([(150, 100, z + 10), (150, 100, z + 30)], HEAT, 2.6, '3 2'); I.box(140, 96, z + 8, 8, 8, 6, DARK); I.box(140, 96, z + 24, 8, 8, 6, DARK)
    I.line([(110, 100, z + 26), (110, 100, z + 62)], MOTOR, 4.5)
    I.box(50, 98, z + 8, 12, 12, 70, FRAME); I.box(158, 98, z + 8, 12, 12, 70, FRAME)
    I.box(50, 70, z + 78, 120, 80, 12, FRAME)                                   # 윗보(분해도에선 기둥을 짧게 그림)
    # L2 ⑨ 보드(왼 벽)
    I.box(14, 60, 120, 3, 100, 80, BOARD)
    # L3 ② 부스러기 받침
    z = 150; I.box(50, 66, z, 120, 94, 2, STEEL, op=.95); I.box(60, 160, z - 2, 100, 8, 6, STEEL)
    # L4 ⑤ 아래 열판 = 받침(속 히터) + 피스톤 Ø70 + 퓨즈
    z = 178; I.box(70, 74, z, 80, 72, 12, PLATE); I.box(74, 100, z + 12, 72, 6, 3, HTR); I.cylz(CX, CY, z + 12, 35, 8, PLATE); I.cylz(CX, CY, z + 19.5, 35, 0.5, HEAT)
    I.box(150, 84, z + 2, 6, 8, 8, RED)
    # L5 ⑥ 몰드 서랍(앞으로 반쯤 뺀 모양): 프레임 바 2 + 뒤 바 + 트레이 + 안쪽 단열판 + 겉 앞판 + 손잡이 + ⑫ 숟가락
    z = 240; dy = 40
    I.box(62, 66 + dy, z, 6, 88, 6, DARK); I.box(152, 66 + dy, z, 6, 88, 6, DARK); I.box(62, 66 + dy, z, 96, 6, 6, DARK)
    I.ringz(CX, CY + dy, z - 6, 39, 30, 18, MOLD); I.ringz(CX, CY + dy, z + 6, 44, 39, 6, MOLD)
    I.box(58, 154 + dy, z - 12, 104, 6, 32, INSUL)                                       # 안쪽 단열판
    I.box(56, 212 + dy - 40, z - 14, 108, 8, 44, PANEL)                                  # 겉 앞판(공기층 46 건너)
    I.line([(76, 222 + dy - 40, z + 8), (144, 222 + dy - 40, z + 8)], '#8a5d12', 3.2)    # 손잡이
    I.box(70, 170, z + 2, 6, 40, 3, STEEL); I.box(55, 208, z + 2, 36, 18, 3, STEEL)        # ⑫ 계량 겸 펴개 숟가락(납작한 끝 · 클립)
    # L6 ⑦ 위 열판 + 플러그 · 히터 · NTC
    z = 330; I.cylz(CX, CY, z - 13.5, 29.5, 13.5, PLATE); I.box(66, 72, z, 88, 76, 14, PLATE); I.box(74, 100, z + 14, 72, 6, 3, HTR); I.box(150, 84, z + 4, 6, 8, 8, HEAT)
    # L7 ⑧ 열 상자(앞 벽에 서랍 구멍 · 받침 구멍) · 뒤 벽 위 김 구멍 2
    z = 392; hollow(I, 44, 60, z, 132, 100, 106, 6, INSUL, front=False); I.box(44, 60, z + 100, 132, 100, 6, INSUL)
    I.box(44, 154, z, 132, 6, 32, INSUL); I.box(44, 154, z + 64, 132, 6, 42, INSUL)     # 앞 벽(서랍 구멍 z 76..108 · 받침 구멍)
    I.box(44, 154, z + 8, 14, 6, 24, INSUL); I.box(162, 154, z + 8, 14, 6, 24, INSUL)
    I.poly([(100, 60, z + 90), (108, 60, z + 90), (108, 60, z + 96), (100, 60, z + 96)], '#2b2b30', 'none', 0, .9)
    I.poly([(112, 60, z + 90), (120, 60, z + 90), (120, 60, z + 96), (112, 60, z + 96)], '#2b2b30', 'none', 0, .9)
    # L8 ⑩ 몸체(흰 띠 · 김 덕트 · 뒤 슬릿 · 앞면 서랍 구멍) + ⑪ 옆 패널 4장
    z = 560; hollow(I, 8, 8, z, 204, 204, 182, 4, BODY)
    I.box(0, 0, z + 180, 220, 220, 10, BAND); I.box(2, 2, z + 190, 216, 216, 6, BODY)
    I.poly([(70, 8, z + 172), (150, 8, z + 172), (150, 8, z + 180), (70, 8, z + 180)], '#2b2b30', 'none', 0, .85)
    I.box(96, 10, z + 136, 28, 10, 40, STEEL, op=.9)
    for (x0, y0, w, d) in [(-30, 8, 4, 204), (246, 8, 4, 204), (8, -30, 204, 4), (8, 246, 204, 4)]:
        I.box(x0, y0, z, w, d, 180, PANEL)
    I.line([(56, 250, z + 74), (164, 250, z + 74), (164, 250, z + 118), (56, 250, z + 118), (56, 250, z + 74)], '#8a5d12', 1.2, '4 3')
    I.line([(66, 250, z + 52), (154, 250, z + 52), (154, 250, z + 58), (66, 250, z + 58), (66, 250, z + 52)], '#8a8a90', 1, '3 3')
    # L9 ⑭ 상판 · 터치
    z = 790; I.box(-2, -2, z, 224, 224, 4, GLASS, top='url(#glassT)', left='#303036', right='#0c0c0f')
    for x in (38, 54): sx, sy = I.P(x, 196, z + 4); I.out.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/>' % (sx, sy))
    I.poly([(66, 192, z + 4.2), (88, 192, z + 4.2), (88, 200, z + 4.2), (66, 200, z + 4.2)], '#fff', 'none', 0)
    I.line([(110, 110, 0), (110, 110, 800)], '#b8b2a6', 1, '3 6', .8)
    # 라벨
    R = 700; L = 280
    I.label((110, 110, 794), R, 48, '⑭ 검은 불투명 내열 상판 · 터치 · 상태 불빛', None, 'r')
    I.label((212, 110, 650), R, 150, '⑩ 몸체 · 흰 띠 · 김 덕트 · 뒤 김 슬릿 · 앞면 서랍 구멍(점선)', None, 'r')
    I.label((248, 110, 650), R, 186, '⑪ 옆 패널 4장 — 비스포크(갈아 끼움)', None, 'r')
    I.label((176, 110, 440), R, 300, '⑧ 열 상자 — 강판 + 단열 5mm · 앞 벽에 서랍 구멍 · 뒤 벽 위 김 구멍 2', None, 'r')
    I.label((154, 110, 338), R, 380, '⑦ 위 열판 220°C + Ø59 플러그 · 속 시즈 히터 450W(빨강) · NTC — 틀 윗보에 고정', None, 'r')
    I.label((150, 150, 246), R, 450, '⑥ 몰드 서랍 — 프레임 + 트레이(Ø6 틀) + 단열판(실리콘 개스킷) + 앞판 · 손잡이', '트레이는 들어서 씻음 · 개스킷이 김을 앞으로 안 내보냄 · 서랍을 반쯤 뺀 모습 · ⑫ 숟가락은 앞판 안쪽 클립', 'r')
    I.label((73, 214, 244), L + 60, 500, '⑫ 펴개 숟가락 3g · 끝 폭 = 틀 Ø60', None, 'l')
    I.label((144, 118, 198), R, 540, '⑤ 아래 열판 = 받침(속 히터 450W · 퓨즈) + 피스톤 Ø70 — 20mm 오르내림', None, 'r')
    I.label((160, 100, 152), R, 590, '② 부스러기 받침 — 열 상자 바닥 · 앞으로 당김', None, 'r')
    I.label((15, 110, 160), L, 640, '⑨ 제어 보드', None, 'l')
    I.label((164, 104, 100), R, 640, '⑬ ㅁ자 강철 틀 — 바닥판 8t + 기둥 12 × 12 두 개 + 윗보 12 × 80 (한 몸)', '누르는 힘이 여기서만 돎 · 토글 핀도 바닥판에', 'r')
    I.label((110, 100, 70), R, 700, '④ 토글 링크 · 래치 스프링 8~10mm · 리밋 2 · 푸시 로드', None, 'r')
    I.label((188, 90, 62), R, 740, '③ 승강 모터(웜) — 바닥 오른쪽', None, 'r')
    I.label((206, 110, 3), R, 800, '① 바닥 무게판 · 고무발 4', None, 'r')
    I.text(480, 962, '아래에서 위로 쌓는 순서 = 조립 순서. 사람이 떼어 씻는 것은 ⑥ 몰드 트레이 · ② 부스러기 받침 둘뿐입니다. 부품 14개, 번호는 단면 · 동작 · 3D · 본문과 같습니다.', 12.5, 600, '#6a6a70', 'middle')
    return '<svg viewBox="0 0 1250 980" xmlns="http://www.w3.org/2000/svg" %s>%s\n%s</svg>' % (FONT, DEFS, I.svg())

# ---------------- 옆 단면(동작 순서 · 가열) ----------------
def SX(y): return 66 + (160 - y) * 1.5          # 앞(y 160) = x 66 · 뒤(y 60) = x 216 · 서랍 뺀 자리 x 12~66
def SZ(z): return 238 - (z - 44) * 1.66          # z 44 = y 238 · z 150 = y 62

def _rect(o, y0, y1, z0, z1, fill, extra=''):
    """mm 좌표(y 앞뒤 · z 높이)로 옆 단면 사각형"""
    x = SX(y1); w = (y1 - y0) * 1.5; yy = SZ(z1); h = (z1 - z0) * 1.66
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" %s/>' % (x, yy, w, h, fill, extra))

def _panel(o, i, lift, drawer_out, cake=None, rice=True, lock=False, steam=False, press=False, pull_arrow=None):
    """열 상자 옆 단면 한 칸. lift = 피스톤 올라간 mm(0~20) · drawer_out = 서랍 빼낸 mm(0~60)
    고정: 열 상자 · ⑬ 틀(기둥 · 윗보) · ⑦ 위 열판 + 플러그 · 레일. 움직임: ⑤ 피스톤(lift) · 트레이(lift > 2 이면 lift − 2 만큼 위로) · 서랍(drawer_out 만큼 앞으로)"""
    o.append('<rect x="66" y="62" width="150" height="176" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
    lk = '#d19a3c' if lock else '#9aa3ad'
    o.append('<rect x="192" y="50" width="22" height="16" rx="3" fill="%s"/><path d="M197 50 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lk, lk))
    o.append('<text x="56" y="74" font-size="9.5" fill="#6a6a70" text-anchor="middle">앞</text>')
    # ⑧ 앞 벽(서랍 구멍 z 76..108 · 받침 구멍 50..58) · 뒤 벽 김 구멍
    _rect(o, 154, 160, 108, 144, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"'); _rect(o, 154, 160, 58, 76, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".6"')
    _rect(o, 60, 66, 134, 140, '#15151a')
    # ⑬ 틀: 기둥(옆에서 보면 y 98..110 한 줄) · 윗보 · 바닥판(아래 밖)
    _rect(o, 98, 110, 44, 132, '#4f5864'); _rect(o, 70, 150, 132, 144, '#4f5864')
    o.append('<text x="%.1f" y="%.1f" font-size="8.5" fill="#fff" text-anchor="middle">틀</text>' % (SX(104), SZ(80)))
    # ⑦ 위 열판 + 플러그(고정) · 히터 · NTC
    _rect(o, 72, 148, 118, 132, '#8a8f96', 'rx="2"'); _rect(o, 76, 144, 122, 128, '#c8503c', 'rx="3"'); _rect(o, 80.5, 139.5, 104.5, 118, '#8a8f96')
    _rect(o, 80.5, 139.5, 104.5, 105.5, '#d19a3c'); _rect(o, 136, 142, 126, 131, '#15151a')
    o.append('<text x="%.1f" y="%.1f" font-size="9" fill="#6a6a70">고정</text>' % (SX(70) + 2, SZ(126)))
    # 레일(고정)
    _rect(o, 66, 154, 88, 94, '#b9bec4')
    # ⑤ 피스톤(lift)
    zp = lift
    _rect(o, 74, 146, 60 + zp, 72 + zp, '#8a8f96', 'rx="2"'); _rect(o, 100, 120, 63 + zp, 69 + zp, '#c8503c', 'rx="3"')
    _rect(o, 75, 145, 72 + zp, 80 + zp, '#8a8f96'); _rect(o, 75, 145, 79.5 + zp, 80.5 + zp, '#d19a3c'); _rect(o, 84, 92, 62 + zp, 70 + zp, '#e06c5a')
    # ⑥ 서랍: 프레임 바(y 66..154 + 앞판) · 트레이(틀 단면 U자) · 안쪽 단열판 · 겉 앞판
    d = drawer_out; zt = max(0, lift - 2)
    _rect(o, 66 + d, 154 + d, 88, 94, '#4a4e55')                                  # 프레임 바
    _rect(o, 154 + d, 160 + d, 76, 108, '#e7d9c2', 'stroke="#b9b2a2" stroke-width=".8"')   # 안쪽 단열판(앞 벽 구멍 막음)
    _rect(o, 154 + d, 160 + d, 106, 108, '#e06c5a'); _rect(o, 154 + d, 160 + d, 76, 78, '#e06c5a')   # 테두리 실리콘 개스킷(위 · 아래)
    o.append('<rect x="%.1f" y="%.1f" width="8" height="%.1f" rx="2" fill="#ebe4d6" stroke="#b9b2a2"/>' % (SX(160 + d) - 10, SZ(118), 44 * 1.66))   # 겉 앞판(공기층 건너 · 그림에선 바로 옆)
    o.append('<rect x="%.1f" y="%.1f" width="10" height="4" rx="2" fill="#8a5d12"/>' % (SX(160 + d) - 14, SZ(97)))                                  # 손잡이
    # 트레이 U자: 바닥 82..85 · 벽 Ø78 바깥 ~ Ø60 안(y 71..80 · 140..149) · 플랜지
    ty = zt
    _rect(o, 71 + d, 149 + d, 82 + ty, 85 + ty, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')
    _rect(o, 71 + d, 80 + d, 85 + ty, 100 + ty, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"'); _rect(o, 140 + d, 149 + d, 85 + ty, 100 + ty, '#dfe3e6', 'stroke="#9aa3ad" stroke-width=".6"')
    _rect(o, 66 + d, 71 + d, 94 + ty, 100 + ty, '#dfe3e6'); _rect(o, 149 + d, 154 + d, 94 + ty, 100 + ty, '#dfe3e6')
    # 쌀 · 떡뻥
    if cake == 'pressed':
        _rect(o, 80.5 + d, 139.5 + d, 85 + ty, 86.5 + ty, '#e9dcc0', 'stroke="#d19a3c" stroke-width=".6"')
    elif cake == 'puffed':
        _rect(o, 80.5 + d, 139.5 + d, 85 + ty, 85 + ty + DROP, '#fff3dc', 'rx="4" stroke="#d19a3c"')
    elif cake == 'done':
        _rect(o, 80.5 + d, 139.5 + d, 85 + ty, 85 + ty + DROP, '#fff3dc', 'rx="4" stroke="#d19a3c"')
    elif rice:
        for k in range(7): o.append('<circle cx="%.1f" cy="%.1f" r="1.8" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (SX(136 + d - k * 8), SZ(86 + ty)))
    # 열 · 압력 화살(누르는 중)
    if press:
        for k in range(3):
            x = SX(126 - k * 12)
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(100), x, SZ(89)))
            o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (x, SZ(72 + zp), x, SZ(83 + zp)))
    if steam:
        o.append('<path d="M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f" fill="none" stroke="#d19a3c" stroke-width="1.6" stroke-dasharray="3 3" marker-end="url(#arr)"/>' % (SX(110), SZ(101 + ty), SX(100), SZ(118), SX(80), SZ(130), SX(67), SZ(137)))
        o.append('<text x="%.1f" y="%.1f" font-size="9.5" fill="#8a5d12">김 → 뒤 구멍</text>' % (SX(118), SZ(128)))
    if pull_arrow:
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/>' % (SX(160 + d) - 12, SZ(70), SX(160 + d) - 12 + (-22 if pull_arrow == 'out' else 22), SZ(70)))
    # 토글 · 푸시 로드 · 모터(바닥) — 틀 바닥판 위
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="252" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(104), SZ(60 + zp), SX(104)))
    if lift > 10: o.append('<path d="M%.1f 252 v8 M%.1f 260 l-14 14 M%.1f 260 l14 14" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(104), SX(104), SX(104)))
    else: o.append('<path d="M%.1f 252 l-16 8 l16 8 M%.1f 252 l16 8 l-16 8" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (SX(104), SX(104)))
    o.append('<rect x="%.1f" y="276" width="%.1f" height="5" fill="#4f5864"/>' % (SX(150), 90 * 1.5))   # 틀 바닥판
    o.append('<rect x="106" y="286" width="40" height="14" rx="4" fill="#5a5e66"/><text x="152" y="297" font-size="10" fill="#6a6a70">모터(바닥)</text>')

def sequence(only=None):
    """동작 순서 ①~⑥ 6칸 — 옆에서 본 열 상자(왼쪽 = 앞). 위 열판 · 플러그 · 틀 고정, 피스톤만 오르내리고 서랍은 사람이 당김"""
    pw = 252; gap = 16
    titles = [('① 서랍 빼서 쌀 넣기', '220°C 예열 뒤 · 5초', '완료 · 예열 불빛에서만 서랍이 빠짐|⑫ 펴개 숟가락에 마른 쌀 3g(불리지 않음)|넓적한 끝으로 쓸어 넣어 한 겹(바닥 2/3)|트레이는 서랍 프레임에 얹혀 있음'),
              ('② 밀어 넣고 시작', '220°C · 1초', '서랍이 끝까지 들어가면 잠김(솔레노이드)|단열판 + 실리콘 개스킷이 앞 구멍을 막음|시작 터치 → 피스톤이 올라감'),
              ('③ 올려 누르기 8~10초', '220°C · 8~10초', '피스톤이 트레이째 20mm 밀어 올림|플러그가 틀 안으로 13.5mm → 쌀 1.5mm|히터 판 두 장이 닿아 데움 · 압력 ↑ · 틀 밀봉'),
              ('④ 순간 하강 8~10mm', '220°C · 0.1초', '래치 해제 · 스프링이 피스톤을 8~10mm 툭|압력이 한순간에 풀려 「뻥」|두께 = 틈 8~10 + 쌀 층 ≈ 9~11mm · 틀 안'),
              ('⑤ 천천히 내리기', '220°C · 1초', '모터가 1초에 걸쳐 쉬는 자리까지|트레이는 서랍 프레임에 내려앉음|김은 플러그가 빠질 때 뒤 구멍 → 덕트 → 슬릿'),
              ('⑥ 서랍 빼서 꺼내기', '완료 불빛 · 5초', '「완료」 불빛 → 서랍 잠금 해제|서랍을 빼면 틀 안에 떡뻥 Ø6 × 9~11|집게로 집기 · 틀은 뜨거움(손잡이만 잡기)')]
    cfg = [dict(lift=0, drawer_out=36, lock=False, rice=True, pull_arrow='out'),
           dict(lift=0, drawer_out=0, lock=True, rice=True, pull_arrow='in'),
           dict(lift=UP, drawer_out=0, lock=True, cake='pressed', press=True),
           dict(lift=UP - DROP, drawer_out=0, lock=True, cake='puffed'),
           dict(lift=0, drawer_out=0, lock=True, cake='done', steam=True),
           dict(lift=0, drawer_out=36, lock=False, cake='done', pull_arrow='out')]
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
        if i == 2: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">올림 20</text>' % (SX(64), SZ(60), SX(64), SZ(84), SX(64) + 4, SZ(70)))
        if i == 3: o.append('<text x="%.1f" y="%.1f" font-size="13" font-weight="800" fill="#8a5d12">8~10mm · 뻥</text>' % (SX(158), SZ(66)))
        if i == 4: o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="%.1f" y="%.1f" font-size="11" fill="#8a5d12">천천히</text>' % (SX(64), SZ(84), SX(64), SZ(62), SX(64) + 4, SZ(72)))
        for k, w in enumerate(titles[i][2].split('|')): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (318 + k * 16, w))
        o.append('</g>')
        if n < N - 1: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

def heating():
    """가열 방식 — 누르는 중(③) 옆 단면 2배 + 원리 3단 + 아래 띠(김 길 · 전기)"""
    o = ['<svg viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS)]
    o.append('<g transform="translate(30,50) scale(1.7) translate(-66,-62)">')
    _panel(o, 2, lift=UP, drawer_out=0, lock=True, cake='pressed', press=True)
    o.append('</g>')
    o.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="800" fill="#15151a">누르는 중(③) · 열 상자 옆 단면 · 왼쪽 = 앞</text>' % (30, 22))
    def lab(py, pz, sx, sy, t, sub=None):
        px = 30 + 1.7 * (SX(py) - 66); pyy = 50 + 1.7 * (SZ(pz) - 62)
        o.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#d19a3c" stroke="#fff" stroke-width="1.2"/><polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (px, pyy, px, pyy, sx - 14, sy - 4, sx - 6, sy - 4))
        o.append('<text x="%d" y="%d" font-size="13.5" font-weight="800" fill="#15151a">%s</text>' % (sx, sy, t))
        if sub: o.append('<text x="%d" y="%d" font-size="11.5" font-weight="600" fill="#6a6a70">%s</text>' % (sx, sy + 15, sub))
    LX = 500
    lab(100, 138, LX, 72, '⑬ 윗보 — 위 열판을 받침 · 누르는 힘 1.4~4.2kN이 기둥 2로 내려가 바닥판에서 닫힘', '몸체 · 열 상자 벽엔 힘이 걸리지 않음')
    lab(76, 125, LX, 128, '⑦ 위 열판 — 알루미늄 다이캐스트 · 속에 시즈 히터 450W(빨강) · NTC', '220°C 유지 · 상한 230°C · 틀 윗보에 볼트로 고정')
    lab(100, 110, LX, 184, '⑦ 플러그 Ø59 — 틀 안으로 13.5mm 들어가 밀봉(틈 0.1~0.2mm)', '쌀 1.5mm 두께로 눌림 · 물기가 끓어 0.5~1.5MPa(틀 안)')
    lab(72, 103, LX, 240, '⑥ 몰드 트레이 — Ø6 오목 틀 15mm · 피스톤이 트레이째 밀어 올림', '마른 쌀 3g 한 겹 · 서랍 프레임에서 18mm 떠 있음')
    lab(76, 86, LX, 296, '⑤ 피스톤 Ø70 + 받침 — 속에 시즈 히터 450W(빨강) · 온도 퓨즈 250°C', '20mm 올라간 상태 · 토글 사점 잠금')
    steps = [('① 열 전달 · 8~10초', '220°C 판 두 장이 위 · 아래에서 바로 데움'), ('② 압력 ↑', '틀이 플러그로 막혀 물기가 끓어 0.5~1.5MPa'), ('③ 8~10mm 순간 하강', '압력이 한꺼번에 빠지며 「뻥」 · 두께 9~11mm')]
    for k, (t, d) in enumerate(steps):
        x = 500 + k * 230
        o.append('<rect x="%d" y="330" width="214" height="64" rx="12" fill="#fff" stroke="#e6e1d7"/>' % x)
        o.append('<text x="%d" y="356" font-size="13.5" font-weight="800" fill="#8a5d12">%s</text><text x="%d" y="378" font-size="11.5" fill="#6a6a70">%s</text>' % (x + 14, t, x + 14, d))
        if k < 2: o.append('<text x="%d" y="368" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x + 222))
    o.append('<rect x="30" y="424" width="560" height="72" rx="12" fill="#fbe9e4"/>')
    o.append('<text x="48" y="452" font-size="13.5" font-weight="800" fill="#c8503c">김 길 — 틀 → 열 상자 안 → 뒤 벽 위 구멍 Ø8 × 2 → 덕트 → 뒤 김 슬릿</text>')
    o.append('<text x="48" y="474" font-size="11.5" fill="#6a6a70">순간 하강과 플러그가 빠질 때 김이 나옴(한 장 0.45g) · 앞(서랍 · 사람 쪽)으로는 길이 없음 · 덕트 아래 물받이 홈</text>')
    o.append('<rect x="610" y="424" width="560" height="72" rx="12" fill="#f3efe6"/>')
    o.append('<text x="628" y="452" font-size="13.5" font-weight="800" fill="#15151a">전기 — 220V 직결 · 약 1kW = 시즈 히터 450W × 2 + 모터 · 제어</text>')
    o.append('<text x="628" y="474" font-size="11.5" fill="#6a6a70">켜고 약 3분 데우면 「예열 완료」 불빛 · 온도 제어 NTC 2 + 온도 퓨즈 250°C 2중 차단</text>')
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
