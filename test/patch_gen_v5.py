# -*- coding: utf-8 -*-
"""gen_iso.py v4 → v5 패치: 밀대 삭제 → ⑫ 계량 슬라이드(밀어내기 겸용) · 히터 2개 표시 · 쌀 길 화살표 · ⓪ 쌀 넣기 칸 · 온도 220/230/250 · 가열 방식 그림(heating) 추가"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'gen_iso.py'); s = open(p, encoding='utf-8').read()
def R(a, b, count=1):
    global s
    assert a in s, 'MISSING: ' + a[:90]
    s = s.replace(a, b, count)

# ---------- 머리말 ----------
R('''"""쌀참 2.5D 구조도 생성기 v4 — 아이소메트릭 단면 · 층 분해 · 동작 순서 5단계 (SVG)''',
  '''"""쌀참 2.5D 구조도 생성기 v5 — 아이소메트릭 단면 · 층 분해 · 동작 순서 ⓪~⑤ 6칸 · 가열 방식 (SVG)
v5(2026-11-24): 밀대 삭제 → ⑫ 계량 슬라이드가 밀어내기 겸용(앞머리로 떡뻥을 슬롯으로 밀고, 같은 움직임으로 컵 3g을 가운데 떨어뜨림) · 위 · 아래 열판 속 시즈 히터 450W × 2 표시 · 떡뻥 220°C(센서 상한 230 · 퓨즈 250) · 칩 170~180°C''')
R(''' ① 바닥 무게판 · 고무발 · 기울기 센서  ② 부스러기 서랍(앞 아래)  ③ 승강 모터(웜 · 바닥 오른쪽) · 밀대 모터  ④''', ''' ① 바닥 무게판 · 고무발 · 기울기 센서  ② 부스러기 서랍(앞 아래)  ③ 승강 모터(웜 · 바닥 오른쪽) · 슬라이드 모터  ④''')
R(''' ⑤ 아래 열판 = 피스톤 Ø6(오르내림 25mm) · 온도 퓨즈 · 밀대  ⑥''', ''' ⑤ 아래 열판 = 받침 + 피스톤 Ø6(오르내림 25mm) + 시즈 히터 450W(속) · 온도 퓨즈 250°C · 배출 턱  ⑥''')
R(''' ⑦ 위 열판(고정 · 천장 기둥 2) · 온도 센서''', ''' ⑦ 위 열판(고정 · 천장 기둥 2) + 시즈 히터 450W(속) · NTC 220°C(상한 230)''')
R(''' ⑫ 곡물 카세트 200g · 계량 슬라이드 3g(뒤에서 몰드 위로 들어와 떨어뜨리고 돌아감)''', ''' ⑫ 곡물 카세트 200g · 계량 슬라이드 3g(밀어내기 겸용 — 뒤 벽 틈 z 80..86 으로 들어와 앞머리로 떡뻥을 슬롯으로 밀고 컵 3g을 가운데 떨어뜨린 뒤 돌아감)''')
R('''# 계량 슬라이드 ⑫: 뒤 벽 틈(z 86..96)으로 들어와 몰드 위(y 110)에서 3g 떨어뜨리고 돌아감''',
  '''# 계량 슬라이드 ⑫: 뒤 벽 틈(z 80..86)으로 들어와 열린 피스톤 면(z 77) 위 25mm 틈을 지나며 앞머리로 떡뻥(z 77..87)을 앞 슬롯으로 밀고, 컵이 가운데(y 110)에 오면 바닥이 열려 3g 낙하 → 후진
# 히터: 위 열판 ⑦ 속 시즈 히터 450W(z 108..112) · 아래 받침 ⑤ 속 시즈 히터 450W(받침 z 80..92 → 83..89) — 둘 다 x 방향 막대, 절단면에 단면이 보임
# 배출 턱: 받침 앞에 붙은 얇은 판(x 80..140 · y 143..154 · 피스톤 면 높이) — 떡뻥이 피스톤에서 슬롯까지 미끄러짐''')

# ---------- cutaway ----------
R('''    I.box(104, 34, 96, 30, 24, 26, STEEL, op=.9)                                # 깔때기(카세트 → 슬라이드)
    I.box(95, 40, 88, 30, 70, 6, STEEL)                                         # 계량 슬라이드(들어온 상태 · y 40..110)
    I.line([(110, 108, 88), (110, 108, 78)], HEAT, 1.6, '2 2', .9, marker='marker-end="url(#arr)"')   # 낟알 떨어짐
    # ---- ⑤ 아래 열판(내려간 상태): 받침 + 피스톤 Ø60 + 히터 면 + 퓨즈 · 밀대 · 떡뻥
    I.box(62, 70, 80 - DOWN, 96, 80, 12, PLATE)
    I.cylz(CX, CY, 92 - DOWN, 30, 8, PLATE); I.cylz(CX, CY, 100 - DOWN, 30, 2, HEAT)
    I.box(158, 84, 82 - DOWN, 6, 8, 8, RED, hatch_cut=False)
    I.box(66, 72, 92 - DOWN, 88, 4, 14, DARK)                                   # 밀대(받침 뒤, 앞으로 쓸어냄)
    I.cylz(CX, CY, 102 - DOWN, 34, 10, CRACK, op=.92)                           # 부푼 떡뻥 Ø7 × 10''',
  '''    I.box(104, 34, 86, 30, 24, 36, STEEL, op=.9)                                # 깔때기(카세트 → 슬라이드 컵)
    # ---- ⑤ 아래 열판(내려간 상태): 받침(속 히터) + 피스톤 Ø60 + 히터 면 + 퓨즈 · 떡뻥
    I.box(62, 70, 80 - DOWN, 96, 80, 12, PLATE)
    I.box(66, 100, 83 - DOWN, 88, 20, 6, HTR, hatch_cut=False, faces='l')                  # 받침 속 시즈 히터 450W(절단면에 단면)
    I.cylz(CX, CY, 92 - DOWN, 30, 8, PLATE); I.cylz(CX, CY, 100 - DOWN, 30, 2, HEAT)
    I.box(158, 84, 82 - DOWN, 6, 8, 8, RED, hatch_cut=False)
    I.cylz(CX, CY, 102 - DOWN, 34, 10, CRACK, op=.92)                           # 부푼 떡뻥 Ø7 × 10 — 피스톤 위
    # ---- ⑫ 계량 슬라이드(밀어내기 겸용 · 들어온 상태 · y 40..110 · z 80..86) + 앞머리 컵
    I.box(95, 40, 80, 30, 70, 6, STEEL)
    I.box(98, 98, 80, 24, 14, 6, DARK, hatch_cut=False)                         # 계량 컵 3g(바닥 열림)
    I.line([(110, 106, 80), (110, 106, 78)], HEAT, 1.6, '2 2', .9, marker='marker-end="url(#arr)"')
    # 쌀 길(화살표): 카세트 → 깔때기 → 슬라이드 컵 → 가운데 낙하
    I.line([(168, 30, 124), (168, 30, 106), (134, 46, 100)], HEAT, 2, '5 3', .95, marker='marker-end="url(#arr)"')
    I.line([(119, 46, 90), (110, 60, 83), (110, 104, 83)], HEAT, 2, '5 3', .95, marker='marker-end="url(#arr)"')''')
R('''    I.box(62, 70, 102, 96, 80, 2, HEAT, hatch_cut=False); I.box(62, 70, 104, 96, 80, 14, PLATE)
    I.box(158, 84, 108, 6, 8, 8, HEAT, hatch_cut=False)''',
  '''    I.box(62, 70, 102, 96, 80, 2, HEAT, hatch_cut=False); I.box(62, 70, 104, 96, 80, 14, PLATE)
    I.box(66, 100, 108, 88, 20, 6, HTR, hatch_cut=False, faces='l')                        # 위 열판 속 시즈 히터 450W(절단면에 단면)
    I.box(158, 84, 108, 6, 8, 8, HEAT, hatch_cut=False)''')
R('''    I.label((168, 20, 160), R, 104, '⑫ 곡물 카세트 200g · 계량 슬라이드 3g', '뒤 벽 틈으로 몰드 위까지 들어와 떨어뜨리고 돌아감', 'r')''',
  '''    I.label((168, 20, 160), R, 104, '⑫ 곡물 카세트 200g → 깔때기 → 계량 컵 3g', '점선 화살 = 쌀 길 · 카세트에서 슬라이드 컵으로', 'r')''')
R('''    I.label((161, 88, 112), R, 198, '⑦ 위 열판 200~230°C · 센서 — 고정(천장 기둥 2)', None, 'r')''',
  '''    I.label((161, 88, 112), R, 198, '⑦ 위 열판 220°C — 고정(천장 기둥 2)', '속에 시즈 히터 450W(빨간 단면) · NTC 센서 상한 230°C', 'r')''')
R('''    I.label((140, 118, 102 - DOWN), R, 290, '⑤ 아래 열판 = 피스톤 Ø6 · 퓨즈 — 이것만 25mm 오르내림', '그림은 내려간(열린) 상태 · 닫히면 링 안으로 6mm', 'r')
    I.label((70, 74, 100 - DOWN), R, 338, '⑤ 밀대 — 받침 뒤에서 앞으로, 떡뻥을 슬롯으로', None, 'r')''',
  '''    I.label((140, 118, 102 - DOWN), R, 290, '⑤ 아래 열판 = 피스톤 Ø6 · 퓨즈 250°C — 이것만 25mm 오르내림', '그림은 내려간(열린) 상태 · 닫히면 링 안으로 6mm · 받침 속 시즈 히터 450W', 'r')
    I.label((110, 105, 86), R, 338, '⑫ 계량 슬라이드 — 밀어내기 겸용(들어온 상태)', '앞머리로 떡뻥을 앞 슬롯으로 밀고, 컵이 가운데서 3g을 떨어뜨리고 돌아감', 'r')''')
R('''    I.text(600, 732, '220V 900W~1kW · 바닥부터:''', '''    I.text(600, 732, '220V 약 1kW(시즈 히터 450W × 2 + 모터 · 제어) · 바닥부터:''')

# ---------- exploded ----------
R('''    # L3 ⑤ 아래 열판 = 받침 + 피스톤 + 히터 면 + 퓨즈 + 밀대
    z = 170; I.box(62, 70, z, 96, 80, 12, PLATE); I.cylz(CX, CY, z + 12, 30, 8, PLATE); I.cylz(CX, CY, z + 20, 30, 2, HEAT)
    I.box(158, 84, z + 2, 6, 8, 8, RED); I.box(66, 72, z + 12, 88, 4, 14, DARK)''',
  '''    # L3 ⑤ 아래 열판 = 받침(속 히터 450W) + 피스톤 + 히터 면 + 퓨즈 + 배출 턱(앞)
    z = 170; I.box(62, 70, z, 96, 80, 12, PLATE); I.box(66, 100, z + 12, 88, 6, 3, HTR); I.cylz(CX, CY, z + 12, 30, 8, PLATE); I.cylz(CX, CY, z + 20, 30, 2, HEAT)
    I.box(158, 84, z + 2, 6, 8, 8, RED); I.box(80, 143, z + 20, 60, 11, 2, PLATE)''')
R('''    z = 268; I.box(62, 70, z, 96, 80, 2, HEAT); I.box(62, 70, z + 2, 96, 80, 14, PLATE); I.box(158, 84, z + 4, 6, 8, 8, HEAT)''',
  '''    z = 268; I.box(62, 70, z, 96, 80, 2, HEAT); I.box(62, 70, z + 2, 96, 80, 14, PLATE); I.box(66, 100, z + 16, 88, 6, 3, HTR); I.box(158, 84, z + 4, 6, 8, 8, HEAT)''')
R('''I.box(104, 34, z - 24, 30, 24, 26, STEEL, op=.9); I.box(95, 40, z - 32, 30, 70, 6, STEEL)''',
  '''I.box(104, 34, z - 34, 30, 24, 36, STEEL, op=.9); I.box(95, 40, z - 40, 30, 70, 6, STEEL); I.box(98, 98, z - 40, 24, 14, 6, DARK)''')
R('''    I.label((168, 20, 740), R, 112, '⑫ 곡물 카세트 · 깔때기 · 계량 슬라이드 3g', None, 'r')''',
  '''    I.label((168, 20, 740), R, 112, '⑫ 곡물 카세트 · 깔때기 · 계량 슬라이드 3g(밀어내기 겸용 · 앞머리 컵)', None, 'r')''')
R('''    I.label((158, 110, 276), R, 490, '⑦ 위 열판 · 히터 · 센서 — 고정(기둥 2)', None, 'r')''',
  '''    I.label((158, 110, 276), R, 490, '⑦ 위 열판 220°C · 속 시즈 히터 450W(빨강) · NTC — 고정(기둥 2)', None, 'r')''')
R('''    I.label((140, 118, 192), R, 600, '⑤ 아래 열판 = 피스톤 Ø6 · 퓨즈 · 밀대 — 오르내림', None, 'r')''',
  '''    I.label((140, 118, 192), R, 600, '⑤ 아래 열판 = 피스톤 Ø6 · 속 시즈 히터 450W · 퓨즈 · 배출 턱(앞) — 오르내림', None, 'r')''')

R('''<marker id="arrg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6a6a70"/></marker>''', '''<marker id="arrg" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6a6a70"/></marker>
<marker id="arrh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#c8503c"/></marker>''')

# ---------- 색 ----------
R('''RICE = '#f3eedf'; INSUL = '#e7d9c2'; RED = '#e06c5a'; SMOKE = '#3a3f47\'''', '''RICE = '#f3eedf'; INSUL = '#e7d9c2'; RED = '#e06c5a'; SMOKE = '#3a3f47'; HTR = '#c8503c\'''')

# ---------- sequence: 6칸 ----------
i0 = s.index('def sequence():'); i1 = s.index("if __name__ == '__main__':")
s = s[:i0] + open(os.path.join(here, 'seq_v5.py'), encoding='utf-8').read() + '\n' + s[i1:]
R('''    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence)]:''',
  '''    for name, fn in [('iso_cut', cutaway), ('iso_explode', exploded), ('iso_seq', sequence), ('iso_heat', heating)]:''')
open(p, 'w', encoding='utf-8').write(s); print('patched gen_iso.py')
