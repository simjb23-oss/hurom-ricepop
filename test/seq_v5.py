def _panel_common(o, i, yF, pw):
    """열 상자 옆 단면 공통(왼쪽 = 앞). 위 열판 · 몰드 링 고정, 아래 피스톤만 움직임. 히터 2개(빨강) · 배출 턱 · 슬라이드 틈"""
    o.append('<rect x="36" y="62" width="180" height="176" rx="6" fill="#f7f2e8" stroke="#b9b2a2" stroke-width="1.5"/>')
    lock = '#d19a3c' if i in (1, 2, 3) else '#9aa3ad'
    o.append('<rect x="192" y="50" width="22" height="16" rx="3" fill="%s"/><path d="M197 50 v-6 a6 6 0 0 1 12 0 v6" fill="none" stroke="%s" stroke-width="2.4"/>' % (lock, lock))
    # 앞문(왼 벽) · 슬롯 · 트레이
    o.append('<rect x="30" y="62" width="8" height="176" rx="2" fill="#e7d9c2" stroke="#b9b2a2"/>')
    o.append('<rect x="29" y="150" width="10" height="20" fill="#fff" stroke="#8a5d12" stroke-width="1" stroke-dasharray="3 2"/>')
    o.append('<rect x="2" y="170" width="30" height="4" rx="1" fill="#dfe3e6" stroke="#9aa3ad"/>')
    o.append('<text x="22" y="86" font-size="9.5" fill="#6a6a70" text-anchor="middle">앞</text><text x="22" y="126" font-size="9" fill="#6a6a70" text-anchor="middle">문</text>')
    # 위 열판(고정) · 기둥 2 · 속 히터 · 히터 면 · 몰드 링
    o.append('<rect x="80" y="62" width="6" height="42" fill="#b9bec4"/><rect x="168" y="62" width="6" height="42" fill="#b9bec4"/>')
    o.append('<rect x="70" y="102" width="112" height="16" rx="3" fill="#8a8f96"/><rect x="76" y="107" width="100" height="6" rx="3" fill="#c8503c"/><rect x="70" y="118" width="112" height="3" fill="#d19a3c"/>')
    o.append('<rect x="96" y="121" width="6" height="9" fill="#dfe3e6" stroke="#9aa3ad" stroke-width=".8"/><rect x="150" y="121" width="6" height="9" fill="#dfe3e6" stroke="#9aa3ad" stroke-width=".8"/>')
    o.append('<text x="188" y="113" font-size="9.5" fill="#6a6a70">고정</text>')
    # 뒤 벽 슬라이드 틈(y 145..153)
    o.append('<rect x="200" y="145" width="17" height="8" fill="#fff" stroke="#8a8f96" stroke-width=".6" stroke-dasharray="2 2"/>')
    # 아래 피스톤 + 받침(속 히터) + 배출 턱 + 퓨즈
    o.append('<rect x="70" y="%d" width="112" height="12" rx="3" fill="#8a8f96"/><rect x="76" y="%d" width="100" height="6" rx="3" fill="#c8503c"/>' % (yF + 12, yF + 15))
    o.append('<rect x="102" y="%d" width="48" height="12" fill="#8a8f96"/><rect x="102" y="%d" width="48" height="3" fill="#d19a3c"/>' % (yF, yF - 1))
    o.append('<rect x="40" y="%d" width="56" height="3" fill="#8a8f96"/>' % (yF - 1))                        # 배출 턱(받침 앞 · 피스톤 면 높이)
    o.append('<rect x="176" y="%d" width="4" height="6" fill="#e06c5a"/>' % (yF + 3))                        # 온도 퓨즈
    # 토글 · 푸시 로드 · 모터
    o.append('<line x1="126" y1="%d" x2="126" y2="252" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>' % (yF + 24))
    if i in (1, 2, 3): o.append('<path d="M126 252 v8 M126 260 l-14 14 M126 260 l14 14" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
    else: o.append('<path d="M126 252 l-16 8 l16 8 M126 252 l16 8 l-16 8" fill="none" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
    o.append('<line x1="126" y1="276" x2="126" y2="288" stroke="#55585e" stroke-width="4" stroke-linecap="round"/>')
    o.append('<rect x="106" y="286" width="40" height="14" rx="4" fill="#5a5e66"/><text x="152" y="297" font-size="10" fill="#6a6a70">모터(바닥)</text>')

def _slide_in(o, yF, with_cake):
    """⑫ 계량 슬라이드가 들어온 상태(앞머리 x 92) · 컵이 가운데(x 116..136)에서 3g 낙하 · 떡뻥은 앞머리에 밀려 배출 턱 → 슬롯"""
    o.append('<rect x="92" y="146" width="125" height="6" fill="#b9bec4" stroke="#8a8f96" stroke-width=".6"/>')
    o.append('<rect x="116" y="143" width="20" height="9" fill="none" stroke="#4a4e55" stroke-width="1.2"/><rect x="118" y="144" width="16" height="4" fill="#f3eedf"/>')   # 컵(바닥 열림)
    for k in range(3): o.append('<circle cx="%d" cy="%d" r="2" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (124 + (k % 2) * 4, 156 + k * 3))
    o.append('<line x1="126" y1="154" x2="126" y2="%d" stroke="#d19a3c" stroke-width="1.4" stroke-dasharray="2 2" marker-end="url(#arr)"/>' % (yF - 6))
    o.append('<line x1="216" y1="139" x2="150" y2="139" stroke="#55585e" stroke-width="1.6" marker-end="url(#arrg)"/><text x="196" y="135" font-size="9.5" fill="#6a6a70" text-anchor="end">슬라이드 →</text>')
    if with_cake:
        o.append('<rect x="40" y="%d" width="52" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 11))      # 배출 턱 위 · 슬롯 지나는 떡뻥
        o.append('<rect x="8" y="160" width="22" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c" opacity=".6"/>')     # 트레이 위
        o.append('<line x1="100" y1="%d" x2="60" y2="%d" stroke="#55585e" stroke-width="2" marker-end="url(#arrg)"/>' % (yF - 16, yF - 16))

def sequence():
    """동작 순서 ⓪~⑤ 6칸 — 옆에서 본 열 상자(왼쪽 = 앞). 위 열판 · 몰드 링 고정, 아래 피스톤만 움직임. ⑫ 슬라이드가 쌀 넣기 + 밀어내기"""
    o = []
    pw = 252; gap = 16; N = 6
    o.append('<svg viewBox="0 0 %d 400" xmlns="http://www.w3.org/2000/svg" %s>%s' % (14 + N * (pw + gap), FONT, DEFS))
    titles = [('⓪ 쌀 넣기 3g', '220°C 예열 뒤 · 1초', '카세트 → 깔때기 → 슬라이드 앞머리 컵 · 피스톤 내려간 25mm 틈으로 들어옴 · 컵이 가운데서 바닥 열려 3g 낙하 · 슬라이드 후진 → ①'),
              ('① 올려서 잠금', '220°C · 0.5초', '모터가 피스톤을 올려 링 안으로 6mm · 토글 사점에서 잠김 · 쌀 3g은 링 안 · 위 열판 · 링은 제자리'),
              ('② 누르기 8~10초', '220°C · 8~10초', '히터 450W 판 두 장이 바로 닿아 데움 · 링 안이 막혀 물기가 끓어 압력 ↑ · 위 열판 · 링은 제자리 · 증기 · 바람 없음'),
              ('③ 2~3mm 순간 하강', '220°C · 0.1초', '래치 해제 · 스프링이 피스톤을 2~3mm 툭 · 압력이 한순간에 풀려 「뻥」 · 잠긴 열 상자 안'),
              ('④ 천천히 내리기', '220°C · 0.5~1초', '모터가 0.5~1초에 걸쳐 끝까지 · 떡뻥은 피스톤 위에 얹혀 링 밖으로 · 배출 턱과 같은 높이 · 리밋 스위치 확인'),
              ('⑤ 배출 · 다음 장', '1초 · 떡뻥 100°C+', '슬라이드 앞머리가 떡뻥을 배출 턱 → 슬롯으로 · 플랩 밀고 트레이로 · 같은 움직임으로 컵 3g 가운데 낙하 · 후진 → ①')]
    downs = [40, 0, 0, 4, 40, 40]
    for i in range(N):
        x0 = 14 + i * (pw + gap); yF = 124 + downs[i]
        o.append('<g transform="translate(%d,0)">' % x0)
        o.append('<rect x="0" y="12" width="%d" height="376" rx="16" fill="#fff" stroke="#e6e1d7"/>' % pw)
        o.append('<text x="16" y="40" font-size="15" font-weight="800" fill="#15151a">%s</text>' % titles[i][0])
        o.append('<rect x="36" y="45" width="118" height="14" rx="7" fill="#fbe9e4"/><text x="95" y="55.5" font-size="10" font-weight="800" fill="#c8503c" text-anchor="middle">%s</text>' % titles[i][1])
        _panel_common(o, i, yF, pw)
        if i == 0:
            # 뒤 벽 안 깔때기(카세트 → 틈) + 낟알
            o.append('<rect x="204" y="62" width="10" height="84" fill="#fff" stroke="#8a8f96" stroke-width=".6" stroke-dasharray="2 2"/>')
            for k in range(5): o.append('<circle cx="%d" cy="%d" r="2" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (207 + (k % 2) * 4, 70 + k * 14))
            o.append('<text x="200" y="76" font-size="9.5" fill="#6a6a70" text-anchor="end">카세트에서 ↓</text>')
            _slide_in(o, yF, False)
        elif i == 1:
            o.append('<rect x="204" y="146" width="13" height="6" fill="#b9bec4"/>')
            for k in range(6): o.append('<circle cx="%d" cy="%d" r="2.2" fill="#f3eedf" stroke="#b9b2a2" stroke-width=".6"/>' % (108 + k * 7, yF - 4))
        elif i == 2:
            o.append('<rect x="204" y="146" width="13" height="6" fill="#b9bec4"/>')
            o.append('<rect x="104" y="%d" width="44" height="3" fill="#e9dcc0" stroke="#d19a3c" stroke-width=".6"/>' % (yF - 4))
            for k in range(4): o.append('<path d="M%d %d q3 -6 0 -12" fill="none" stroke="#d19a3c" stroke-width="1.6" opacity=".8"/>' % (110 + k * 10, yF - 6))
            for k in range(3): o.append('<line x1="%d" y1="99" x2="%d" y2="%d" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (112 + k * 14, 112 + k * 14, 120))
            for k in range(3): o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c8503c" stroke-width="1.4" marker-end="url(#arrh)"/>' % (112 + k * 14, yF + 22, 112 + k * 14, yF + 1))
        elif i == 3:
            o.append('<rect x="204" y="146" width="13" height="6" fill="#b9bec4"/>')
            o.append('<rect x="103" y="%d" width="46" height="8" rx="4" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 9))
            for a in range(0, 360, 40):
                r = math.radians(a); o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#d19a3c" stroke-width="2"/>' % (126 + 36 * math.cos(r), yF - 5 + 12 * math.sin(r), 126 + 46 * math.cos(r), yF - 5 + 20 * math.sin(r)))
            o.append('<text x="60" y="%d" font-size="13" font-weight="800" fill="#8a5d12">2~3mm · 뻥</text>' % (yF + 44))
        elif i == 4:
            o.append('<rect x="204" y="146" width="13" height="6" fill="#b9bec4"/>')
            o.append('<rect x="100" y="%d" width="52" height="10" rx="5" fill="#fff3dc" stroke="#d19a3c"/>' % (yF - 11))
        else:
            _slide_in(o, yF, True)
        if i == 1: o.append('<text x="152" y="268" font-size="10.5" fill="#6a6a70">사점 잠금</text><line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">올림</text>' % (yF + 60, yF + 26, yF + 46))
        if i == 2: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">누름</text>' % (yF + 50, yF + 26, yF + 42))
        if i == 3: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">스프링</text>' % (yF + 10, yF + 34, yF + 26))
        if i == 4: o.append('<line x1="200" y1="%d" x2="200" y2="%d" stroke="#d19a3c" stroke-width="2" marker-end="url(#arr)"/><text x="206" y="%d" font-size="11" fill="#8a5d12">천천히</text>' % (yF - 30, yF + 10, yF - 8))
        words = titles[i][2].split(' · ')
        for k, w in enumerate(words): o.append('<text x="16" y="%d" font-size="11.5" fill="#6a6a70">%s</text>' % (318 + k * 16, w))
        o.append('</g>')
        if i < N - 1: o.append('<text x="%d" y="170" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x0 + pw + gap / 2))
    o.append('</svg>')
    return '\n'.join(o)

def heating():
    """가열 방식 — 열판 직접 접촉 · 눌렀다가 한 번에 풀기. 왼쪽: 누르는 중(②) 열 상자 옆 단면 2배 · 오른쪽: 원리 3단 · 아래: 칩 모드 · 전기"""
    o = ['<svg viewBox="0 0 1200 520" xmlns="http://www.w3.org/2000/svg" %s>%s' % (FONT, DEFS)]
    S = 2.0; OX, OY = 30, 50
    def X(x): return OX + S * x
    def Y(y): return OY + S * (y - 62)
    def rect(x, y, w, h, fill, extra=''):
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" %s/>' % (X(x), Y(y), S * w, S * h, fill, extra))
    yF = 124
    rect(36, 62, 180, 176, '#f7f2e8', 'rx="10" stroke="#b9b2a2" stroke-width="2"')
    rect(30, 62, 8, 176, '#e7d9c2', 'rx="3" stroke="#b9b2a2"')
    rect(29, 150, 10, 20, '#fff', 'stroke="#8a5d12" stroke-dasharray="4 3"')
    rect(80, 62, 6, 42, '#b9bec4'); rect(168, 62, 6, 42, '#b9bec4')
    rect(70, 102, 112, 16, '#8a8f96', 'rx="5"'); rect(76, 107, 100, 6, '#c8503c', 'rx="6"'); rect(70, 118, 112, 3, '#d19a3c')
    rect(96, 121, 6, 9, '#dfe3e6', 'stroke="#9aa3ad"'); rect(150, 121, 6, 9, '#dfe3e6', 'stroke="#9aa3ad"')
    rect(70, yF + 12, 112, 12, '#8a8f96', 'rx="5"'); rect(76, yF + 15, 100, 6, '#c8503c', 'rx="6"')
    rect(102, yF, 48, 12, '#8a8f96'); rect(102, yF - 1, 48, 3, '#d19a3c'); rect(40, yF - 1, 56, 3, '#8a8f96'); rect(176, yF + 3, 4, 6, '#e06c5a')
    rect(104, yF - 4, 44, 3, '#e9dcc0', 'stroke="#d19a3c"')
    rect(200, 145, 17, 8, '#fff', 'stroke="#8a8f96" stroke-dasharray="3 3"'); rect(204, 146, 13, 6, '#b9bec4')
    # NTC 센서(위 열판 속) · 열 화살(빨강) · 압력 화살(회색, 링 안 밀봉)
    rect(160, 105, 6, 6, '#15151a')
    for k in range(4):
        x = X(108 + k * 12); o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="2.4" marker-end="url(#arrh)"/>' % (x, Y(100), x, Y(119)))
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#c8503c" stroke-width="2.4" marker-end="url(#arrh)"/>' % (x, Y(yF + 21), x, Y(yF + 1)))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="2" marker-end="url(#arrg)"/>' % (X(126), Y(122.5), X(103), Y(122.5)))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="2" marker-end="url(#arrg)"/>' % (X(126), Y(122.5), X(149), Y(122.5)))
    # 토글 · 모터
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#55585e" stroke-width="7" stroke-linecap="round"/>' % (X(126), Y(yF + 24), X(126), Y(240)))
    o.append('<path d="M%.1f %.1f v14 M%.1f %.1f l-26 26 M%.1f %.1f l26 26" fill="none" stroke="#55585e" stroke-width="7" stroke-linecap="round"/>' % (X(126), Y(240), X(126), Y(247), X(126), Y(247)))
    o.append('<text x="%.1f" y="%.1f" font-size="11.5" fill="#6a6a70">④ 토글 사점 잠금 — 내압 0.5~1.5MPa를 버팀</text>' % (X(136), Y(262)))
    o.append('<text x="%.1f" y="%.1f" font-size="10" fill="#6a6a70" text-anchor="middle">앞문</text>' % (X(34), Y(90)))
    o.append('<text x="%.1f" y="%.1f" font-size="12" font-weight="800" fill="#15151a">누르는 중(②) · 열 상자 옆 단면 · 왼쪽 = 앞</text>' % (X(36), Y(50)))
    # 라벨(오른쪽)
    def lab(px, py, sx, sy, t, sub=None):
        o.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="#d19a3c" stroke="#fff" stroke-width="1.2"/><polyline points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" stroke="#9a948a" stroke-width="1"/>' % (X(px), Y(py), X(px), Y(py), sx - 14, sy - 4, sx - 6, sy - 4))
        o.append('<text x="%d" y="%d" font-size="13.5" font-weight="800" fill="#15151a">%s</text>' % (sx, sy, t))
        if sub: o.append('<text x="%d" y="%d" font-size="11.5" font-weight="600" fill="#6a6a70">%s</text>' % (sx, sy + 15, sub))
    LX = 500
    lab(176, 110, LX, 72, '⑦ 위 열판 — 알루미늄 다이캐스트 · 속에 시즈 히터 450W(빨강)', 'NTC 센서가 220°C 유지 · 상한 230°C(넘으면 끊음) · 고정')
    lab(153, 125, LX, 128, '⑥ 몰드 링 Ø6 — 피스톤이 6mm 들어가 밀봉', '링 안이 막혀 압력이 오름(회색 화살) · 위 열판 아래 고정')
    lab(126, 122, LX, 184, '불린 쌀 3g — 판이 바로 닿아 데움(빨간 화살)', '증기 · 뜨거운 바람 없음 · 수분 20% 안팎이 끓으며 압력 ↑')
    lab(150, 133, LX, 240, '⑤ 피스톤 Ø6 + 받침 — 속에 시즈 히터 450W(빨강) · 온도 퓨즈 250°C', '이것만 25mm 오르내림 · 받침 앞 배출 턱(피스톤 면 높이)')
    lab(210, 149, LX, 296, '⑫ 계량 슬라이드 틈 — 피스톤이 내려간 뒤에만 들어옴', '쌀 넣기 + 밀어내기 겸용 · 가열 중엔 뒤 벽 안에 물러나 있음')
    # 원리 3단(오른쪽 아래)
    steps = [('① 열 전달 · 8~10초', '220°C 판 두 장이 위 · 아래에서 바로 데움'), ('② 압력 ↑', '링 안이 막혀 물기가 끓어 0.5~1.5MPa'), ('③ 2~3mm 순간 하강', '압력이 한꺼번에 빠지며 「뻥」 · 부피 5~8배')]
    for k, (t, d) in enumerate(steps):
        x = 500 + k * 230
        o.append('<rect x="%d" y="330" width="214" height="64" rx="12" fill="#fff" stroke="#e6e1d7"/>' % x)
        o.append('<text x="%d" y="356" font-size="13.5" font-weight="800" fill="#8a5d12">%s</text><text x="%d" y="378" font-size="11.5" fill="#6a6a70">%s</text>' % (x + 14, t, x + 14, d))
        if k < 2: o.append('<text x="%d" y="368" font-size="22" fill="#d19a3c" text-anchor="middle">›</text>' % (x + 222))
    # 아래 띠: 칩 모드 · 전기
    o.append('<rect x="30" y="424" width="560" height="72" rx="12" fill="#fbe9e4"/>')
    o.append('<text x="48" y="452" font-size="13.5" font-weight="800" fill="#c8503c">칩 모드 — 같은 열판 170~180°C · 60~80초 · 순간 하강 없음</text>')
    o.append('<text x="48" y="474" font-size="11.5" fill="#6a6a70">곡물가루 70~80% + 찌꺼기 20~30% 반죽을 접시 몰드(피스톤 위)에 얹어 얇게 눌러 굽기 · 전병 원리</text>')
    o.append('<rect x="610" y="424" width="560" height="72" rx="12" fill="#f3efe6"/>')
    o.append('<text x="628" y="452" font-size="13.5" font-weight="800" fill="#15151a">전기 — 220V 직결 · 약 1kW = 시즈 히터 450W × 2 + 모터 · 제어</text>')
    o.append('<text x="628" y="474" font-size="11.5" fill="#6a6a70">켜고 약 3분 데우면 「예열 완료」 불빛 · 온도 제어 NTC 2 + 온도 퓨즈 250°C 2중 차단</text>')
    o.append('</svg>')
    return '\n'.join(o)
