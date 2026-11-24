# 휴롬 쌀참 — 신제품 기획 제안서

쌀 한 칸, 버튼 하나, 첨가물 없는 간식. 쌀참 = 쌀로 만드는 새참. 곡물 떡뻥 + 휴롬 원액기 찌꺼기 칩 두 모드.

- 페이지: https://simjb23-oss.github.io/hurom-ricepop/
- 디자인 보드(Figma): https://www.figma.com/design/JeHF6ltyqlQTJdEbAcmmjv
- `index.html` 기획서 · `explode.js` 구조 3D(three.js) · `test/gen_iso.py` 2.5D 구조도(SVG) 생성기 · `img/` 실사 컨셉(AI 생성) · `test/shot.py` 캡처 스크립트
- 3D 쿼리: `?p=0~1`(분해 진행) · `?ang=<도>` · `?color=black|white|cream|sage|lavender` · `?nolabel`


## 기준 구조 (r3 · 2026-11-24)
- 유리 상판 · 위 열판 고정, 아래 열판(몰드)만 바닥 모터 + 토글 링크로 25mm 오르내림(사점 잠금 → 2~3mm 순간 하강 → 천천히). 물통 없음(쌀을 10분 불려 넣음).
- 부품 번호 ①~⑭ 는 2.5D(test/gen_iso.py → test/iso_*.svg) · 3D(explode.js) 공통. 실사 컨셉 8장은 Figma 보드 JeHF6ltyqlQTJdEbAcmmjv 에서 생성(out/v3/ 원본).
- 본문 편집은 test/edit_v3.py, 칸 캡처는 test/shot_v3.py.
