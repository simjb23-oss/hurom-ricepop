# 휴롬 쌀참 — 신제품 기획 제안서

쌀 한 칸, 버튼 하나, 첨가물 없는 간식. 쌀참 = 쌀로 만드는 새참. 곡물 떡뻥 + 휴롬 원액기 찌꺼기 칩 두 모드.

- 페이지: https://simjb23-oss.github.io/hurom-ricepop/
- 디자인 보드(Figma): https://www.figma.com/design/JeHF6ltyqlQTJdEbAcmmjv
- `index.html` 기획서 · `explode.js` 구조 3D(three.js) · `test/gen_iso.py` 2.5D 구조도(SVG) 생성기 · `img/` 실사 컨셉(AI 생성) · `test/shot.py` 캡처 스크립트
- 3D 쿼리: `?p=0~1`(분해 진행) · `?ang=<도>` · `?color=black|white|cream|sage|lavender` · `?nolabel`


## 기준 구조 (r5 · 2026-11-24)
- r5: 쌀 길(⓪ 쌀 넣기 — 카세트 → 계량 컵 3g → 슬라이드 전진 → 가운데 낙하 → 후진) · 밀대 없음(⑫ 계량 슬라이드가 밀어내기 겸용) · 가열 방식 칸(위 · 아래 열판 속 시즈 히터 450W × 2 · 떡뻥 220°C · 센서 상한 230 · 퓨즈 250 · 칩 170~180°C · 220V 약 1kW). 2.5D는 test/gen_iso.py(iso_cut · iso_seq 6칸 · iso_explode · iso_heat), 본문 편집 test/edit_v5.py.
- r6: 칩 모드 넣는 길을 떡뻥과 같게 — 반죽은 칩 카세트(짜는 통 + 넓은 컵 8g, ⑫ 자리에 갈아 끼움) → 계량 슬라이드 → 같은 몰드 링 가운데 → 같은 슬롯 배출. 「칩 몰드(접시)」 삭제 · 앞문은 씻을 때만 · 「열선」 → 「히터」. 본문 편집 test/edit_v6.py.
- r7(2026-11-25): 몰드 서랍 구조 — 카세트 · 깔때기 · 계량 컵 · 슬라이드 · 배출 슬롯 · 플랩 · 트레이 · 앞문 삭제. 마른 쌀 3g을 ⑫ 계량 숟가락으로 ⑥ 서랍 트레이(Ø6 오목 틀 15mm)에 넣고 밀어 넣음 → ⑤ 피스톤이 트레이째 20mm 올려 ⑦ 플러그(Ø59)가 13.5mm 들어가 누름 → 8~10mm 순간 하강(두께 8~10mm) → 천천히 → 서랍 잠금 해제 → 빼서 꺼냄. ⑬ ㅁ자 강철 틀(힘 길) · ⑧ 뒤 벽 김 구멍 → ⑩ 덕트 → 슬릿(김 길) · 칩 모드는 다음 단계. 2.5D test/gen_iso_v7.py · 본문 test/body_v7.html + edit_v7.py · 3D explode.js v7. 실사는 서랍 구조로 3장 새로(Figma 세션 7b255e22 노드 5:2~5:4 · img/photo_{hero,open,family}.jpg · 원본 out/v7/), 옛 8장 삭제.
- r7(2026-11-25): 몰드 서랍 구조 — 카세트 · 깔때기 · 계량 컵 · 슬라이드 · 배출 슬롯 · 플랩 · 트레이 · 앞문 삭제. 마른 쌀 3g을 ⑫ 계량 숟가락으로 ⑥ 서랍 트레이(Ø6 오목 틀 15mm)에 넣고 밀어 넣음 → ⑤ 피스톤이 트레이째 20mm 올려 ⑦ 플러그(Ø59)가 13.5mm 들어가 누름 → 8~10mm 순간 하강(두께 8~10mm) → 천천히 → 서랍 잠금 해제 → 빼서 꺼냄. ⑬ ㅁ자 강철 틀(힘 길) · ⑧ 뒤 벽 김 구멍 → ⑩ 덕트 → 슬릿(김 길) · 칩 모드는 다음 단계. 2.5D test/gen_iso_v7.py · 본문 test/body_v7.html + edit_v7.py · 3D explode.js v7. 실사는 서랍 구조로 3장 새로(Figma 세션 7b255e22 노드 5:2~5:4 · img/photo_{hero,open,family}.jpg · 원본 out/v7/), 옛 8장 삭제.
- r4: 창 없음(위 · 앞) · 불투명 내열 상판 · 앞문으로 몰드 링 분리 · 피스톤 + 고정 몰드 링.
- 유리 상판 · 위 열판 고정, 아래 열판(몰드)만 바닥 모터 + 토글 링크로 25mm 오르내림(사점 잠금 → 2~3mm 순간 하강 → 천천히). 물통 없음(쌀을 10분 불려 넣음).
- 부품 번호 ①~⑭ 는 2.5D(test/gen_iso.py → test/iso_*.svg) · 3D(explode.js) 공통. 실사 컨셉 8장은 Figma 보드 JeHF6ltyqlQTJdEbAcmmjv 에서 생성(out/v3/ 원본).
- 본문 편집은 test/edit_v3.py, 칸 캡처는 test/shot_v3.py.
