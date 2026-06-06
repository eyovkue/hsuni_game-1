# 프롬프트 기록 (prompt_history.md)

본 파일은 Claude AI를 활용한 개발 과정에서 주고받은 주요 프롬프트를 기록합니다.

---

## 1. 대본 분석 및 게임 기획

**사용 모델:** Claude Sonnet 4.6  
**날짜:** 2025년

### 프롬프트 1
> 이 대본을 바탕으로 한성대학교 비주얼 노벨 게임을 만들거야 파이썬으로 코드를 작성해줘

**AI 응답 요약:**
- `대본.odt` 파일을 읽어 전체 스토리 구조(1주차~15주차) 파악
- `player.py`, `story.py`, `main.py` 세 파일로 분리된 구조 제안
- Pygame 기반 비주얼 노벨 엔진 초안 생성

---

### 프롬프트 2
> 아, 참고로 현재 폴더 명을 HANSUNGFRESHMANSURVIVAL이라는 큰 폴더와 그 안에 main.py, player.py, prompt_history.md, README.md, story.py, 그리고 assets가 있는데 assets는 폴더고 여기에는 audio, backgrounds, characters가 있어. 과제 제출방식은 Github 레포지토리 (팀원간 협업 필수) ...

**AI 응답 요약:**
- 폴더 구조에 맞게 파일 경로 정리
- `player.py`: Player 클래스 (스탯 관리, 조건 체크, 학점 등급 계산)
- `story.py`: 전체 씬 데이터 (SCENES 리스트 + SCENE_MAP 딕셔너리)
- `main.py`: Pygame 게임 엔진 (배경, 캐릭터, HUD, 대화창, 선택지, 타이핑 애니메이션, 엔딩)
- `README.md`: 설치 방법, 실행 방법, 팀원 역할, 스크린샷 섹션 포함

---

## 2. 개발 메모

### 설계 결정 사항
- **스탯 시스템:** 학점(0~100), 멘탈(0~100), 인간관계(0~100), 소지금(0~100)
- **분기 조건:** 각 선택지에 `condition: lambda p: ...` 형태로 조건 부여
- **특별이벤트:** `_special`, `_condition` 키로 조건부 씬 전환 구현
- **폰트:** 한국어 지원을 위해 OS별 폰트 경로 자동 탐색

### 아직 개선할 점
- [ ] 실제 배경 이미지 추가 (assets/backgrounds/)
- [ ] 캐릭터 스프라이트 추가 (assets/characters/)
- [ ] BGM 추가 (assets/audio/)
- [ ] 저장/불러오기 기능
- [ ] 타이틀 화면 개선
- [ ] 효과음 추가

---

*이 파일은 지속적으로 업데이트됩니다.*
