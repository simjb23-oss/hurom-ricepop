# -*- coding: utf-8 -*-
"""쌀참 r12a (2026-11-25) — 「설계도 · 티어다운」 칸 추가: 3면도 · 단면 B-B / A-A · 칸 상세 · 2.5D 분해도(구조 칸에서 옮김) · 부품표 · 조립 순서 · 분해 · 수리
준보 「단면도 2D설계도 2.5D분해도 티어다운 등등 널어주라」 msg_5fae3925. 무게는 부품표 합(약 7kg)으로 맞춤."""
import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(root)
sys.path.insert(0, os.path.join(root, 'test'))
import gen_2d_v12 as D2
import gen_iso_v12 as G
P = 'index.html'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, ('count', c, old[:90]); s = s.replace(old, new)

# ---- 부품표(티어다운) — (번호, 이름, 재질 · 공정, 수량, g, 식품 접촉, 원 낮음, 원 높음)
BOM = [
 ('①', '바닥 무게판 · 고무발 · 기울기 센서', 'SPCC 2t 프레스 · 고무발 4 · 기울기 스위치', '1식', 420, '', 2000, 3500),
 ('②', '코드 보관함 덮개', 'PP 사출', '1', 60, '', 600, 1200),
 ('③', '모터', '웜 기어드 DC 24V 8W · 자기 잠금', '1', 180, '', 4500, 7500),
 ('④', '캠 모듈', '달팽이 캠 S45C 가공 · 레버 SPCC 프레스 · 푸시 로드 SUS304 · 실리콘 벨로즈 · 되돌림 스프링 2 · 캠 위치 센서', '1식', 240, '', 5000, 8500),
 ('⑤', '받침(아래 열판)', 'ADC12 다이캐스트 + 윗면 CNC · 시즈 히터 450W 매립 · 온도 퓨즈 250°C · 판 감지 자석 스위치', '1식', 520, '', 7500, 12000),
 ('⑥', '아래 판(얕은 칸 3)', 'A6061 CNC · PFAS 없는 세라믹 코팅', '1', 510, '●', 6000, 10000),
 ('⑦', '위 열판', 'ADC12 다이캐스트 · 시즈 히터 450W · NTC', '1식', 470, '', 7000, 11000),
 ('⑧', '열 상자 · 단열', 'SPCC 0.8 프레스 · 세라믹 섬유 단열 6(상자) · 5(뚜껑)', '1식', 380, '', 3000, 5000),
 ('⑨', '제어 보드', 'MCU · 트라이악 2 · 숫자 2자리 · 주황 LED · 단추 · 솔레노이드 드라이버', '1', 60, '', 8000, 13000),
 ('⑩', '몸체 · 흰 띠 · 앞면 · 김 덕트', 'PP-GF 내열 사출 · 흰 띠 PBT · 덕트 PPS', '1식', 620, '', 5000, 8500),
 ('⑪', '옆 패널 4장', 'ABS 사출 + 도장(5색)', '4', 300, '', 3000, 5000),
 ('⑫', '위 판(얕은 볼록 3)', 'A6061 CNC · 세라믹 코팅 · 실리콘 손잡이 2 · SUS 스프링 걸쇠', '1식', 260, '●', 5000, 8500),
 ('⑬', '바닥판 10t', 'SS400 레이저 절단 · 가운데 비움 · 전착 도장', '1', 700, '', 3000, 5000),
 ('⑬', 'C자 틀 8t × 2 · 경첩 축', 'SS400 레이저 절단 · 축 SUS304', '2', 600, '', 3500, 6000),
 ('⑬', '뚜껑 보 11t · 앞 갈고리 2', 'SS400 레이저(리브 비움) · 갈고리 SUS304 프레스', '1식', 550, '', 3500, 6000),
 ('⑬', '잠금 막대 · 솔레노이드', 'SUS 막대 · 솔레노이드 12V · 스프링', '1식', 90, '', 2500, 4000),
 ('⑭', '검은 유리 윗면', '강화유리 4t · 뒷면 인쇄', '1', 520, '', 3500, 6000),
 ('⑭', '뚜껑 껍데기 · 위 판 떼는 단추', 'PBT 사출 · 단추 POM · 스프링', '1식', 160, '', 2500, 4000),
 ('⑭', '떠 있는 경첩 팔 2 · 댐퍼', '팔 ADC12 · 세로 홈 · 회전 댐퍼 · 들림 스프링', '1식', 120, '', 3000, 5000),
 ('—', '전원 코드 · 내열 배선 · 커넥터 · 나사', '220V 코드 1.2m · 실리콘 배선', '1식', 180, '', 3000, 5000),
 ('—', '계량 숟가락 3g', 'PP 사출', '1', 15, '●', 300, 700),
]
tw = sum(r[4] for r in BOM); lo = sum(r[6] for r in BOM); hi = sum(r[7] for r in BOM)
def won(v): return '{:,}'.format(v)
rows = '\n'.join('      <tr><td><b>%s</b></td><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s~%s</td></tr>' % (n, name, mat, q, won(g), fc, won(a), won(b)) for (n, name, mat, q, g, fc, a, b) in BOM)
rows += '\n      <tr><td></td><td><b>합계</b></td><td>부품 21줄 · 움직이는 부품 2(캠 모듈 · 받침 덩어리)</td><td></td><td><b>%s</b></td><td>3</td><td><b>%s~%s</b></td></tr>' % (won(tw), won(lo), won(hi))
print('BOM', tw, 'g', lo, hi)

# ---- 2.5D 분해도: 구조 칸에서 떼어 옮김(구조 칸이 덜 빽빽해짐)
m = re.search(r'\n    <div class="cut rv">\n      <h3>층 분해 — .*?</svg>\n    </div>', s, re.S)
assert m, 'explode block'
explode_block = m.group(0); s = s.replace(explode_block, '', 1)
explode_block = explode_block.replace('층 분해 — 아래에서 위로 쌓는 순서', '2.5D 분해도 — 아래에서 위로 쌓는 순서 = 조립 순서')

SEC = '''
<section id="drawings" class="light2">
  <div class="wrap">
    <div class="rv"><div class="kicker">11 · 설계도 · 티어다운</div>
    <h2>밖에서 안까지, <b>부품 하나하나</b>.</h2>
    <p class="lead">3면도로 겉 치수를, 두 단면으로 안의 쌓임을, 상세도로 칸 하나가 「쉼 → 누름 → 뻥」 하는 틈을 봅니다. 번호 ①~⑭는 2.5D · 3D · 본문과 같습니다. 맨 아래 부품표는 뜯어 놓은 순서 그대로입니다.</p></div>
    <div class="cut rv">
      <h3>3면도 — 평면 · 정면 · 우측면 (3각법 · 점선 = 숨은선)</h3>
      %(three)s
    </div>
    <div class="cut rv">
      <h3>단면 B-B — 앞 두 칸 중심을 좌우로 자름 (③ 누르는 상태)</h3>
      %(bb)s
    </div>
    <div class="cut rv">
      <h3>단면 A-A — 앞 왼쪽 칸 중심을 앞뒤로 자름 (③ 누르는 상태 · 왼쪽 = 앞)</h3>
      %(aa)s
    </div>
    <div class="cut rv">
      <h3>상세 — 칸 하나의 세 상태 (볼록 끝은 고정 · 받침과 아래 판만 움직임)</h3>
      %(det)s
    </div>
%(explode)s
    <div class="rv" style="margin-top:56px"><h3 style="font-size:22px;font-weight:800">티어다운 — 부품표</h3>
    <p class="lead" style="margin-top:10px">뜯으면 나오는 순서대로. 단가는 1만 대 기준 부품 단가 범위(원)이고, 조립 · 검사 · 포장 · 물류는 뺐습니다. ● = 쌀이 닿는 부품.</p></div>
    <div class="tblwrap"><table class="rv bom">
      <tr><th>번호</th><th>부품</th><th>재질 · 공정</th><th>수량</th><th>무게 g</th><th>닿음</th><th>단가 원</th></tr>
%(rows)s
    </table></div>
    <div class="grid2">
      <div class="card rv"><small>조립 순서</small><strong>아래에서 위로, 열 번</strong><ol style="padding-left:20px;font-size:15px;line-height:1.75;color:var(--sub)">
        <li>① 무게판 위에 ⑬ 바닥판 · ② 코드 보관함</li>
        <li>③ 모터 · ④ 캠 모듈을 바닥판에 · 캠 위치 맞춤</li>
        <li>⑬ C자 틀 2장 세움 · 잠금 막대 · 솔레노이드</li>
        <li>⑧ 열 상자 얹고 푸시 로드 벨로즈 끼움</li>
        <li>⑤ 받침(히터 · 퓨즈 · 판 감지) 로드에 물림</li>
        <li>⑨ 보드 · 배선 · 앞면 단추 · 숫자 연결</li>
        <li>⑩ 몸체 · 흰 띠 · 덕트 → ⑪ 옆 패널 4장 끼움</li>
        <li>⑭ 뚜껑: 유리 + 뚜껑 보 + 단열 + ⑦ 위 열판 + 갈고리</li>
        <li>뚜껑을 경첩 팔 축에 걸고 댐퍼 · 들림 스프링</li>
        <li>⑥ 아래 판 · ⑫ 위 판 끼우고 내압 · 온도 · 잠금 검사</li>
      </ol></div>
      <div class="card rv"><small>분해 · 수리</small><strong>사람은 판 두 장, 서비스는 세 덩어리</strong><ul>
        <li><b>사람이 떼는 것</b>: ⑥ 아래 판(손가락 홈) · ⑫ 위 판(단추 + 손잡이). 도구 없음.</li>
        <li><b>뚜껑 히터</b>: 유리 아래 나사 4개 → ⑦ 위 열판을 커넥터째 교체. 뚜껑을 몸체에서 떼지 않음.</li>
        <li><b>캠 모듈</b>: 바닥 무게판을 떼면 ③ 모터 + ④ 캠이 한 덩어리로 빠짐(나사 4).</li>
        <li><b>보드</b>: 왼쪽 옆 패널을 밀어 빼면 ⑨ 보드가 바로 보임.</li>
        <li>열 상자 · 강철 틀은 수리하지 않는 부품(수명 내내).</li>
      </ul></div>
    </div>
  </div>
</section>
''' % {'three': D2.three_view(), 'bb': D2.section('B'), 'aa': D2.section('A'), 'det': D2.detail(), 'explode': explode_block, 'rows': rows}

# ---- 칸 번호 11~18 → 12~19 (뒤에서부터)
for n in range(18, 10, -1):
    s = s.replace('class="kicker">%02d · ' % n, 'class="kicker">%02d · ' % (n + 1))
# ---- 새 칸은 3D 칸 뒤 · 세척 칸 앞
rep('\n<section id="clean" class="dark">', SEC + '\n<section id="clean" class="dark">')
rep('<li><a href="#structure">3D</a></li>', '<li><a href="#structure">3D</a></li><li><a href="#drawings">설계도</a></li>')
rep('.cut+.cut{margin-top:24px}', '.cut+.cut{margin-top:24px}\n.bom td,.bom th{font-size:13.5px;vertical-align:top}.bom td:nth-child(5),.bom td:nth-child(7){white-space:nowrap;text-align:right}.bom td:nth-child(6){text-align:center;color:var(--acc)}')
# ---- 무게는 부품표 합으로
kg = round(tw / 1000, 1)
rep('약 4.8kg(강철 틀 · 바닥 무게판 포함)', '약 %.0fkg(부품표 합 %s g · 강철 틀 2.4kg 포함)' % (kg, won(tw)))
rep('바닥 230 × 230, 4.8kg(강철 틀 포함), 무게중심 높이 약 85mm → 전도각 약 53°. 뚜껑(약 1.1kg)을 젖혀도 무게중심은 뒤로 25mm 가는 정도라 바닥 안.',
    '바닥 230 × 230, 약 7kg(강철 틀 포함), 무게중심 높이 약 85mm → 전도각 약 53°. 뚜껑(약 2kg)을 70° 젖혀도 전체 무게중심은 뒤로 약 18mm 가는 정도라 바닥 안.')
rep('<span class="ver">r12 · 2026-11-25</span>', '<span class="ver">r12a · 2026-11-25</span>')

# ---- 구조 칸 2.5D 단면: 오른쪽 라벨 바탕(흰 판) 빼서 덜 답답하게
src = open('test/gen_iso_v12.py', encoding='utf-8').read()
bg = "    I.out.append('<rect x=\"790\" y=\"34\" width=\"470\" height=\"300\" rx=\"12\" fill=\"#fff\" opacity=\".86\"/>')\n"
if bg in src:
    open('test/gen_iso_v12.py', 'w', encoding='utf-8').write(src.replace(bg, ''))
import importlib; importlib.reload(G)
pat = re.compile(r'<svg viewBox="0 0 1260 750"[^>]*>.*?</svg>', re.S)
assert len(pat.findall(s)) == 1; s = pat.sub(lambda _: G.cutaway(), s, count=1)
open(P, 'w', encoding='utf-8').write(s)
print('ok', s.count('id="drawings"'), s.count('층 분해'))
