# story.py
# 대본 전체 씬 데이터

# ─────────────────────────────────────────────────────────────
# 씬 형식
# {
#   "id": str,            ← 씬 식별자
#   "week": str,          ← 화면 상단에 표시할 주차 레이블
#   "bg": str,            ← assets/backgrounds/ 안의 파일명 (확장자 포함)
#   "character": str|None ← assets/characters/ 안의 파일명 (없으면 None)
#   "lines": [            ← 순서대로 보여줄 대사 목록
#       ("화자", "대사"),  ← 화자가 None 이면 나레이션 박스
#   ],
#   "choices": [          ← 없으면 자동으로 다음 씬으로
#       {
#           "text": str,
#           "condition": callable(player)|None,  ← None = 항상 활성
#           "effects": dict,   ← apply(**effects) 에 전달
#           "flags": dict,     ← flags 직접 갱신
#           "next": str,       ← 다음 씬 id
#       },
#   ],
#   "next": str|None      ← choices 없을 때 다음 씬
# }
# ─────────────────────────────────────────────────────────────

SCENES = [

    # ══════════════════════════════════════════════
    # 타이틀
    # ══════════════════════════════════════════════
    {
        "id": "title",
        "week": "",
        "bg": "title.png",
        "character": None,
        "lines": [
            (None, "한성대학교 신입생 생존기"),
            (None, "1학년 1학기"),
        ],
        "choices": [],
        "next": "w1_intro",
    },

    # ══════════════════════════════════════════════
    # 1주차 — 수강신청
    # ══════════════════════════════════════════════
    {
        "id": "w1_intro",
        "week": "1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "아침 10시쯤, 나는 노트북 앞에 앉아 있다."),
            (None, "수강신청 오픈까지 앞으로 10초."),
            ("나", "제발 성공하자…"),
            (None, "3… 2… 1… 클릭!"),
            (None, "재빠르게 새로고침을 눌렀지만, 원하던 강의 대부분을 놓치고 말았다."),
        ],
        "choices": [
            {
                "text": "① 자리가 남은 강의를 그냥 넣는다",
                "condition": None,
                "effects": {"학점": 10, "멘탈": -10},
                "flags": {},
                "next": "w1_a",
            },
            {
                "text": "② 학점이 좀 모자라도 이대로 간다",
                "condition": None,
                "effects": {"학점": 5, "멘탈": 5},
                "flags": {},
                "next": "w1_b",
            },
        ],
        "next": None,
    },
    {
        "id": "w1_a",
        "week": "1주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            ("나", "어쩔 수 없지… 강의 사이에 우주 공강이 되어버렸지만 이미 벌어진 일이니까..."),
        ],
        "choices": [],
        "next": "w2_intro",
    },
    {
        "id": "w1_b",
        "week": "1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "어쩔 수 없지! 미래의 나에게 맡긴다!"),
        ],
        "choices": [],
        "next": "w2_intro",
    },

    # ══════════════════════════════════════════════
    # 2주차 — 입학식
    # ══════════════════════════════════════════════
    {
        "id": "w2_intro",
        "week": "2주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "따스한 봄바람이 불어오는 3월 초."),
            (None, "오늘은 드디어 한성대학교 입학식 날이다."),
            (None, "정문 앞에는 새내기들이 삼삼오오 모여 사진을 찍고 있었고,"),
            (None, "교내 곳곳에는 신입생을 환영하는 현수막이 걸려 있었다."),
            (None, "강당 안은 이미 많은 신입생들로 가득 차 있었다."),
            (None, "빈자리를 찾아 앉으려던 순간, 옆자리에 앉은 학생이 말을 걸어왔다."),
            ("???", "저기… 안녕하세요?"),
            (None, "조금 긴장한 표정의 학생이었다. 나도 아는 사람이 한 명도 없었다."),
            (None, "어색한 침묵이 흐른다. 어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 먼저 웃으며 말을 건다",
                "condition": None,
                "effects": {"인간관계": 10, "멘탈": 5},
                "flags": {},
                "next": "w2_a",
            },
            {
                "text": "② 간단하게만 대답한다",
                "condition": None,
                "effects": {},
                "flags": {},
                "next": "w2_b",
            },
            {
                "text": "③ 못 들은 척 휴대폰을 본다",
                "condition": None,
                "effects": {"인간관계": -5, "멘탈": 5},
                "flags": {},
                "next": "w2_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w2_a",
        "week": "2주차",
        "bg": "hall.png",
        "character": "player_happy.png",
        "lines": [
            ("나", "네 안녕하세요! 저도 아는 사람이 아무도 없어서 긴장되네요."),
            ("???", "진짜요? 다행이다..."),
            (None, "서로 이름을 소개하고 이런저런 이야기를 나누기 시작했다."),
            (None, "입학식이 끝난 후."),
            ("???", "혹시 괜찮으면 연락처 교환할래요?"),
            (None, "생애 첫 대학 친구가 생겼다."),
            ("나", "생각보다 대학 생활도 나쁘지 않을지도?"),
        ],
        "choices": [],
        "next": "w3_intro",
    },
    {
        "id": "w2_b",
        "week": "2주차",
        "bg": "hall.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "아... 네."),
            ("???", "아하..."),
            (None, "짧은 대화가 끝나고 어색한 침묵이 이어진다."),
            (None, "입학식은 무사히 끝났지만 특별한 일은 없었다."),
            ("나", "뭐... 아직 학기 시작도 안 했으니까."),
        ],
        "choices": [],
        "next": "w3_intro",
    },
    {
        "id": "w2_c",
        "week": "2주차",
        "bg": "hall.png",
        "character": "player_sad.png",
        "lines": [
            (None, "학생은 잠시 머뭇거리더니 고개를 돌렸다."),
            ("???", "...아."),
            (None, "괜히 조금 미안해졌다. 입학식이 끝난 후 곧바로 집으로 향했다."),
        ],
        "choices": [],
        "next": "w3_intro",
    },

    # ══════════════════════════════════════════════
    # 3주차 — 동아리
    # ══════════════════════════════════════════════
    {
        "id": "w3_intro",
        "week": "3주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "입학식이 끝난 지도 어느덧 일주일."),
            (None, "점심시간. 천막들이 길게 늘어서 있었고, 선배들이 목이 터져라 홍보를 하고 있었다."),
            ("선배", "동아리 구경하고 가세요!"),
            ("선배", "신입생 무료 간식 증정!"),
            (None, "나는 전단지 몇 장을 들고 광장을 천천히 걸었다."),
            ("나", "대학교 하면 역시 동아리지..."),
            ("나", "근데 괜히 가입했다가 시간만 뺏기는 거 아닐까?"),
            (None, "한 선배가 다가왔다."),
            ("선배", "신입생이죠? 우리 동아리 한번 보고 가요!"),
            (None, "어떤 선택을 할까?"),
        ],
        "choices": [
            {
                "text": "① 따라 간다 (밴드 동아리)",
                "condition": None,
                "effects": {"인간관계": 10, "멘탈": 5},
                "flags": {"동아리_가입": True},
                "next": "w3_a",
            },
            {
                "text": "② 그냥 지나친다",
                "condition": None,
                "effects": {"멘탈": 5, "인간관계": -10},
                "flags": {},
                "next": "w3_b",
            },
        ],
        "next": None,
    },
    {
        "id": "w3_a",
        "week": "3주차",
        "bg": "clubbooth.png",
        "character": "player_happy.png",
        "lines": [
            (None, "커다란 스피커에서 밴드 음악이 흘러나오고 있었다."),
            ("선배", "안녕하세요! 음악 좋아하세요?"),
            ("나", "좋아하긴 하는데… 악기는 할 줄 모르는데요."),
            ("선배", "괜찮아요. 잘 할 줄 몰라도 가입할 수 있어요."),
            (None, "축제 무대 위에서 연주하는 모습, 관객들의 함성. 생각보다 엄청 멋있어 보였다."),
            (None, "나도 모르게 가입 신청서를 작성했다."),
        ],
        "choices": [],
        "next": "w4_intro",
    },
    {
        "id": "w3_b",
        "week": "3주차",
        "bg": "campus.png",
        "character": "player_normal.png",
        "lines": [
            (None, "나는 한참 동안 광장을 둘러봤지만 결국 어느 부스에도 가입하지 않았다."),
            ("나", "일단 대학 생활부터 적응하자."),
            ("나", "괜히 이것저것 했다가 감당 못 하면 어떡해."),
        ],
        "choices": [],
        "next": "w4_intro",
    },

    # ══════════════════════════════════════════════
    # 4주차 — 과제 폭탄
    # ══════════════════════════════════════════════
    {
        "id": "w4_intro",
        "week": "4주차",
        "bg": "classroom.png",
        "character": None,
        "lines": [
            (None, "입학한 지 어느덧 한 달."),
            (None, "슬슬 대학 생활의 현실이 모습을 드러내기 시작했다."),
            ("교수", "자, 다음 주까지 과제 하나 제출해 주세요."),
            ("교수", "그리고 여러분은 이번 주부터 프로젝트를 진행합니다."),
            ("교수", "이번주까지 보고서 작성 과제 있습니다. 분량은 A4 10페이지 이상입니다."),
            ("나", "또인가…"),
            (None, "과제 현황: 교양 과제 1개 / 전공 과제 2개 / 발표 자료 제작 / 팀플 회의 준비"),
            (None, "마감까지 남은 시간은 일주일. 어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 오늘부터 바로 시작한다",
                "condition": None,
                "effects": {"학점": 15, "멘탈": -10},
                "flags": {},
                "next": "w4_a",
            },
            {
                "text": "② 마감 전날 밤에 몰아서 한다",
                "condition": None,
                "effects": {"학점": 5, "멘탈": -20},
                "flags": {},
                "next": "w4_b",
            },
            {
                "text": "③ AI를 적극 활용한다",
                "condition": None,
                "effects": {},
                "flags": {},
                "next": "w4_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w4_a",
        "week": "4주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "미래의 나를 믿지 말자. 지금 하는 게 맞다."),
            (None, "친구들이 게임하자는 연락을 보냈지만 전부 거절했다."),
            ("친구", "롤 ㄱ?"),
            ("나", "과제해야 함."),
            ("친구", "벌써 해?"),
            (None, "며칠 동안 꾸준히 과제를 진행했다. 마감 하루 전 모든 과제를 끝냈다."),
            ("나", "힘들긴 했지만... 역시 미리 하길 잘했어."),
        ],
        "choices": [],
        "next": "w4_event_check",
    },
    {
        "id": "w4_b",
        "week": "4주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "과제는 미래의 나에게 맡겼다."),
            (None, "월요일. '아직 많이 남았네.'  수요일. '괜찮아.'  금요일. '내일 하면 되지.'"),
            (None, "마감 전날 밤. 현재 시간 오후 11시 43분."),
            ("나", "...망했다."),
            (None, "분량은 절반도 못 채웠다. 새벽 2시… 4시… 아침 8시… 겨우 제출에는 성공했다."),
            ("나", "다음부터는 진짜 미리 해야지."),
        ],
        "choices": [],
        "next": "w4_event_check",
    },
    {
        "id": "w4_c",
        "week": "4주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "요즘은 AI 시대잖아."),
            (None, "과제 주제를 입력했다. 몇 초 만에 초안이 완성되었다."),
            (None, "하지만 그대로 제출하기엔 조금 부족했다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① AI 내용을 직접 수정한다 (멘탈 35 이상)",
                "condition": lambda p: p.check("멘탈", 35),
                "effects": {"학점": 12, "멘탈": -3},
                "flags": {},
                "next": "w4_c1",
            },
            {
                "text": "② 그대로 제출한다",
                "condition": None,
                "effects": {"학점": -15, "멘탈": -10},
                "flags": {},
                "next": "w4_c2",
            },
        ],
        "next": None,
    },
    {
        "id": "w4_c1",
        "week": "4주차",
        "bg": "room.png",
        "character": "player_happy.png",
        "lines": [
            (None, "AI가 만든 내용을 참고해 자신만의 내용으로 수정했다."),
            (None, "생각보다 더 좋은 평을 받았다!"),
        ],
        "choices": [],
        "next": "w4_event_check",
    },
    {
        "id": "w4_c2",
        "week": "4주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            ("나", "그래 그냥 제출해버리자."),
            (None, "며칠 후… 생각보다 좋지 않은 평가를 받았다…"),
            (None, "가장 중요한 내용을 빠뜨린 것 같다…"),
        ],
        "choices": [],
        "next": "w4_event_check",
    },
    # 특별이벤트 체크 (인간관계 70 이상)
    {
        "id": "w4_event_check",
        "week": "4주차",
        "bg": "room.png",
        "character": None,
        "lines": [],
        "choices": [],
        "next": "w4_event",   # story engine에서 조건 분기
        "_special": "w4_friend_event",  # 인간관계 70이상이면 이 씬으로
        "_condition": lambda p: p.check("인간관계", 70),
    },
    {
        "id": "w4_friend_event",
        "week": "4주차 — 특별이벤트",
        "bg": "cafe.png",
        "character": "player_happy.png",
        "lines": [
            (None, "갑자기 휴대폰 문자 알림음이 울려왔다."),
            ("친구", "과제 다 했어?"),
            ("나", "아직..."),
            ("친구", "나도 지금 하는 중인데 같이 할래?"),
            (None, "카페에서 함께 과제를 하며 자연스럽게 대화가 이어졌다."),
        ],
        "choices": [],
        "effects_on_enter": {"인간관계": 5, "멘탈": 5},
        "flags_on_enter": {"친구_찬스": 1},
        "next": "w4_event",
    },
    {
        "id": "w4_event",
        "week": "4주차 결과",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "한 달이 지났다. 슬슬 중간고사 준비를 생각해야 할 때다."),
        ],
        "choices": [],
        "next": "w78_intro",
    },

    # ══════════════════════════════════════════════
    # 7~8주차 — 중간고사
    # ══════════════════════════════════════════════
    {
        "id": "w78_intro",
        "week": "7~8주차",
        "bg": "classroom.png",
        "character": None,
        "lines": [
            (None, "입학한 지 한 달 반. 벚꽃은 어느새 지고, 캠퍼스에는 초록빛이 가득해졌다."),
            ("교수", "다음 주가 중간고사 기간입니다."),
            (None, "시험 일정: 교양 과목 3개 / 전공 과목 2개"),
            (None, "지금부터 어떻게 공부하느냐에 따라 첫 대학 성적이 결정될 것이다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 도서관에 틀어박혀 공부한다 (멘탈 50 이상)",
                "condition": lambda p: p.check("멘탈", 50),
                "effects": {"학점": 20, "멘탈": -15, "인간관계": -5},
                "flags": {},
                "next": "w78_a",
            },
            {
                "text": "② 친구들과 스터디를 한다 (인간관계 40 이상 또는 친구 찬스)",
                "condition": lambda p: p.check("인간관계", 40) or p.has_flag("친구_찬스"),
                "effects": {"학점": 10, "인간관계": 10, "멘탈": -5},
                "flags": {},
                "next": "w78_b",
            },
            {
                "text": "③ 벼락치기를 한다",
                "condition": None,
                "effects": {"학점": -10, "멘탈": -20},
                "flags": {},
                "next": "w78_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w78_a",
        "week": "7~8주차",
        "bg": "library.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "제발 자리 있어라..."),
            (None, "다행히 구석 자리를 하나 발견했다."),
            (None, "수업이 끝나면 도서관. 밥 먹고 도서관. 집 가서 도서관."),
            (None, "시험 당일, 문제를 보는 순간."),
            ("나", "어? 이거 어제 본 건데?"),
            ("나", "살았다..."),
        ],
        "choices": [],
        "next": "w9_intro",
    },
    {
        "id": "w78_b",
        "week": "7~8주차",
        "bg": "cafe.png",
        "character": "player_happy.png",
        "lines": [
            ("동기", "야 이거 이해한 사람?"),
            ("나", "나도 모르겠음."),
            ("동기", "수업 시간에 잤냐?"),
            (None, "스터디는 생각보다 도움이 됐다. 내가 모르는 부분은 친구들이 알려주고."),
            (None, "시험 당일, 몇몇 문제는 생각보다 쉽게 풀렸다."),
            ("나", "혼자 하는 것보다 훨씬 낫네."),
        ],
        "choices": [],
        "next": "w9_intro",
    },
    {
        "id": "w78_c",
        "week": "7~8주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "일요일 밤. 현재 시각 오후 11시 57분."),
            (None, "교재를 펼쳐보니 처음 보는 내용이 절반이었다."),
            (None, "새벽 3시… 새벽 5시… '잠깐만 눈만 감자…'"),
            (None, "시험장. 첫 문제를 읽었다."),
            ("나", "이거 어디서 본 것 같은데… 어 다시 보니까 아닌 것 같기도..."),
            (None, "결국 절반도 풀지 못했다."),
            ("나", "다음 시험부터는 진짜 미리 공부한다."),
        ],
        "choices": [],
        "next": "w9_intro",
    },

    # ══════════════════════════════════════════════
    # 9주차 — 시험 후 선택
    # ══════════════════════════════════════════════
    {
        "id": "w9_intro",
        "week": "9주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "드디어 마지막 시험이 끝났다."),
            (None, "엄청난 해방감. 하지만 통장 잔고도 조금 신경 쓰였다."),
            ("동기", "오늘 저녁에 다 같이 술 마시러 갈 건데?"),
            ("동기", "시험 끝났는데 이 정도는 해야지."),
            (None, "오늘은 뭘 할까?"),
        ],
        "choices": [
            {
                "text": "① 술자리에 참석한다 (소지금 30 이상)",
                "condition": lambda p: p.check("소지금", 30),
                "effects": {"인간관계": 15, "멘탈": -5, "소지금": -10},
                "flags": {},
                "next": "w9_a",
            },
            {
                "text": "② 혼자 휴식한다 (멘탈 20 이하 권장)",
                "condition": None,
                "effects": {"멘탈": 15},
                "flags": {},
                "next": "w9_b",
            },
            {
                "text": "③ 아르바이트를 시작한다",
                "condition": None,
                "effects": {"소지금": 20, "멘탈": -10},
                "flags": {},
                "next": "w9_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w9_a",
        "week": "9주차",
        "bg": "restaurant.png",
        "character": "player_happy.png",
        "lines": [
            (None, "저녁 7시. 학교 근처 술집. 동기들이 여러 명 모여 있었다."),
            (None, "술자리는 생각보다 즐거웠다. 입학 후 처음으로 편하게 이야기하는 시간이었다."),
            (None, "집에 돌아온 시간은 밤 12시가 넘어서였다."),
            ("나", "가끔은 이런 시간도 필요한 것 같다."),
        ],
        "choices": [],
        "next": "w9_money_event",
    },
    {
        "id": "w9_b",
        "week": "9주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "오늘은 좀 쉬고 싶다."),
            (None, "알람도 끄고, 과제도 생각하지 않고. 유튜브를 보다가 잠들었다."),
            (None, "눈을 뜨니 저녁이었다."),
            ("나", "이게 행복이지."),
        ],
        "choices": [],
        "next": "w9_money_event",
    },
    {
        "id": "w9_c",
        "week": "9주차",
        "bg": "cafe.png",
        "character": "player_normal.png",
        "lines": [
            ("사장", "경력은 없죠?"),
            ("나", "네."),
            ("사장", "괜찮아요. 배우면 돼요."),
            (None, "첫날. '아이스 아메리카노 두 잔이요.'"),
            ("나", "네!"),
            ("사장", "그쪽 말고 저쪽 손님 거."),
            ("나", "...아."),
            (None, "생각보다 쉽지 않았다. 하지만 퇴근 후 받은 첫 월급 일부를 보니 기분이 좋아졌다."),
            ("나", "내가 번 돈이다..."),
            ("나", "힘들긴 해도 지갑이 두툼해지는 느낌은 좋네."),
        ],
        "choices": [],
        "next": "w9_money_event",
    },
    # 소지금 50 이상 이벤트
    {
        "id": "w9_money_event",
        "week": "9주차",
        "bg": "campus.png",
        "character": None,
        "lines": [],
        "choices": [],
        "next": "w10_intro",
        "_special": "w9_money_scene",
        "_condition": lambda p: p.check("소지금", 50),
    },
    {
        "id": "w9_money_scene",
        "week": "9주차 — 특별이벤트",
        "bg": "campus.png",
        "character": "player_normal.png",
        "lines": [
            ("동기", "야. 너 요즘 돈 좀 있는 것 같던데."),
            ("동기", "그럼 오늘 밥은 네가 사는 거지?"),
        ],
        "choices": [
            {
                "text": "① 밥을 산다",
                "condition": None,
                "effects": {"인간관계": 10, "소지금": -5},
                "flags": {},
                "next": "w9_money_a",
            },
            {
                "text": "② 도망간다",
                "condition": None,
                "effects": {"인간관계": -5, "멘탈": 5},
                "flags": {},
                "next": "w9_money_b",
            },
        ],
        "next": None,
    },
    {
        "id": "w9_money_a",
        "week": "9주차",
        "bg": "restaurant.png",
        "character": "player_happy.png",
        "lines": [("나", "대학생의 지갑은 언제나 가볍다...")],
        "choices": [],
        "next": "w10_intro",
    },
    {
        "id": "w9_money_b",
        "week": "9주차",
        "bg": "campus.png",
        "character": "player_sad.png",
        "lines": [("나", "뭐라는거야… 나도 쓰기엔 부족하다고…")],
        "choices": [],
        "next": "w10_intro",
    },

    # ══════════════════════════════════════════════
    # 10주차 — 대동제 축제
    # ══════════════════════════════════════════════
    {
        "id": "w10_intro",
        "week": "10주차",
        "bg": "festival.png",
        "character": None,
        "lines": [
            (None, "중간고사가 끝난 후. 캠퍼스 분위기가 갑자기 달라지기 시작했다."),
            (None, "한성대학교 대동제 D-3"),
            (None, "축제가 시작되는 날. 학교는 평소와 완전히 다른 모습이었다."),
            (None, "푸드트럭, 주점, 체험 부스, 공연 준비 중인 사람들, 수많은 학생들."),
            ("나", "그래서 오늘은 뭐를 할까?"),
        ],
        "choices": [
            {
                "text": "① 동기들과 축제를 마음껏 즐긴다 (인간관계 40 이상)",
                "condition": lambda p: p.check("인간관계", 40),
                "effects": {"인간관계": 15, "멘탈": 15, "소지금": -10},
                "flags": {},
                "next": "w10_a",
            },
            {
                "text": "② 동아리 사람들과 함께한다 (동아리 가입 시)",
                "condition": lambda p: p.has_flag("동아리_가입"),
                "effects": {"인간관계": 20, "멘탈": 10},
                "flags": {},
                "next": "w10_b",
            },
            {
                "text": "③ 그냥 집으로 간다",
                "condition": None,
                "effects": {"멘탈": -5, "인간관계": -5},
                "flags": {},
                "next": "w10_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w10_a",
        "week": "10주차",
        "bg": "festival.png",
        "character": "player_happy.png",
        "lines": [
            ("나", "오늘은 놀자."),
            (None, "동기들과 함께 부스를 돌아다니고, 푸드트럭 음식도 먹었다."),
            (None, "무대 앞에는 이미 수많은 학생들이 모여 있었다."),
            (None, "공연이 시작되고 관객들의 함성이 울려 퍼졌다."),
            ("나", "와..."),
            (None, "나는 어느새 친구들과 함께 노래를 따라 부르고 있었다."),
            ("나", "오늘 진짜 재밌었다."),
        ],
        "choices": [],
        "next": "w12_intro",
    },
    {
        "id": "w10_b",
        "week": "10주차",
        "bg": "festival.png",
        "character": "player_happy.png",
        "lines": [
            (None, "동아리 단톡방. '오늘 다 같이 축제 보러 갈 사람?'"),
            (None, "나는 동아리 사람들과 합류했다."),
            ("선배", "신입생 적응은 잘 하고 있어?"),
            ("나", "생각보다 힘들어요."),
            ("선배", "원래 다 그래. 괜찮아, 차차 익숙해지겠지."),
            (None, "어느새 자연스럽게 대화에 섞여 있었다."),
        ],
        "choices": [],
        "next": "w12_intro",
    },
    {
        "id": "w10_c",
        "week": "10주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "밖에서는 축제 음악이 들려왔다."),
            (None, "하지만 나는 너무 피곤해서 빨리 집으로 가고 싶었다."),
        ],
        "choices": [],
        "next": "w12_intro",
    },

    # ══════════════════════════════════════════════
    # 12주차 — 기말 과제 폭탄
    # ══════════════════════════════════════════════
    {
        "id": "w12_intro",
        "week": "12주차",
        "bg": "room.png",
        "character": None,
        "lines": [
            (None, "기말고사가 2주 앞으로 다가온 어느 날."),
            (None, "띠링— 과제 제출 D-3  띠링— 기말 프로젝트 발표 D-4  띠링— 전공 보고서 D-5"),
            ("나", "잠깐... 왜 다 이번 주야?"),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 밤샘해서 전부 끝낸다 (멘탈 30 이상)",
                "condition": lambda p: p.check("멘탈", 30),
                "effects": {"학점": 15, "멘탈": -20},
                "flags": {},
                "next": "w12_a",
            },
            {
                "text": "② 중요한 것만 챙긴다",
                "condition": None,
                "effects": {"학점": 10, "멘탈": -10},
                "flags": {},
                "next": "w12_b",
            },
            {
                "text": "③ 친구와 작업하기 (친구 찬스 보유 시)",
                "condition": lambda p: p.flags.get("친구_찬스", 0) > 0,
                "effects": {"학점": 10, "인간관계": 10, "멘탈": -5},
                "flags": {},
                "next": "w12_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w12_a",
        "week": "12주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [("나", "이번 주만 버티자…")],
        "choices": [],
        "next": "w13_intro",
    },
    {
        "id": "w12_b",
        "week": "12주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [("나", "줄 건 줘야지…")],
        "choices": [],
        "next": "w13_intro",
    },
    {
        "id": "w12_c",
        "week": "12주차",
        "bg": "cafe.png",
        "character": "player_happy.png",
        "lines": [("나", "혼자하면 쓰러질지도 몰라.")],
        "choices": [],
        "next": "w13_intro",
    },

    # ══════════════════════════════════════════════
    # 13주차 — 기말고사
    # ══════════════════════════════════════════════
    {
        "id": "w13_intro",
        "week": "13주차",
        "bg": "library.png",
        "character": None,
        "lines": [
            (None, "기말고사 기간 시작."),
            (None, "캠퍼스는 조용했다. 도서관도, 카페도. 전부 시험 공부를 하는 학생들로 가득 차 있었다."),
            (None, "지난 3개월 동안 들었던 강의. 수십 장의 PPT. 끝없이 쌓인 전공 내용."),
            ("나", "드디어 마지막 관문이다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 끝까지 최선을 다한다 (학점 30 이상 & 멘탈 40 이상)",
                "condition": lambda p: p.check("학점", 30) and p.check("멘탈", 40),
                "effects": {"학점": 20, "멘탈": -15},
                "flags": {},
                "next": "w13_a",
            },
            {
                "text": "② 벼락치기를 시도한다",
                "condition": None,
                "effects": {},  # 학점에 따라 씬에서 분기
                "flags": {},
                "next": "w13_b",
            },
            {
                "text": "③ 한 과목을 포기하고 나머지에 집중한다",
                "condition": None,
                "effects": {"학점": 5, "멘탈": 5},
                "flags": {},
                "next": "w13_c",
            },
        ],
        "next": None,
    },
    {
        "id": "w13_a",
        "week": "13주차",
        "bg": "classroom.png",
        "character": "player_happy.png",
        "lines": [
            (None, "시험 전날. 나는 밤늦게까지 공부했다."),
            ("나", "이 부분은 꼭 나온다. 이 공식도 외워야 하고..."),
            (None, "시험 당일. 시험지를 펼쳤다."),
            ("나", "어? 생각보다 문제가 잘 풀렸다. 할 만한데?"),
            (None, "강의실을 나오는 순간. 묘한 성취감이 밀려왔다."),
            ("나", "드디어 끝났다..."),
        ],
        "choices": [],
        "next": "w13_event_check",
    },
    {
        "id": "w13_b",
        "week": "13주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "시험 하루 전. 현재 시각 오후 8시."),
            ("나", "왜 이렇게 범위가 많지?"),
            (None, "새벽 2시… '큰일 났는데.'  새벽 5시… '이제 자면 안 되는 거 아니야?'"),
            (None, "시험장. 첫 문제를 읽었다."),
            ("나", "처음 보는 건데?  두 번째 문제. 이것도?"),
            (None, "시험은 끝났지만 영혼도 함께 끝난 것 같았다."),
            ("나", "다음 학기엔 진짜 미리 공부해야지."),
        ],
        "choices": [],
        "effects_on_enter_cond": {
            "condition": lambda p: p.check("학점", 40),
            "true_effects": {"학점": 0, "멘탈": -20},
            "false_effects": {"학점": -10, "멘탈": -20},
        },
        "next": "w13_event_check",
    },
    {
        "id": "w13_c",
        "week": "13주차",
        "bg": "library.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "모든 걸 다 잘할 수는 없어."),
            (None, "가장 자신 없는 과목 하나를 과감하게 포기했다."),
            (None, "시험은 예상보다 괜찮게 끝났다. 하지만 포기한 과목은 처참했다."),
        ],
        "choices": [],
        "next": "w13_event_check",
    },
    # 인간관계 80 이상 특별이벤트
    {
        "id": "w13_event_check",
        "week": "13주차",
        "bg": "campus.png",
        "character": None,
        "lines": [],
        "choices": [],
        "next": "ending",
        "_special": "w13_friend_event",
        "_condition": lambda p: p.check("인간관계", 80),
    },
    {
        "id": "w13_friend_event",
        "week": "13주차 — 특별이벤트",
        "bg": "campus.png",
        "character": "player_happy.png",
        "lines": [
            (None, "시험 종료. 강의실 밖."),
            ("동기", "끝났다."),
            ("나", "그러게."),
            ("동기", "입학한 게 엊그제 같은데 벌써 한 학기가 끝났네."),
            ("동기", "고생 많았어."),
        ],
        "choices": [
            {
                "text": "① 같이 밥 먹으러 간다 (소지금 10 이상)",
                "condition": lambda p: p.check("소지금", 10),
                "effects": {"인간관계": 10, "멘탈": 10, "소지금": -10},
                "flags": {},
                "next": "w13_f_a",
            },
            {
                "text": "② 집으로 간다",
                "condition": None,
                "effects": {"멘탈": 5},
                "flags": {},
                "next": "ending",
            },
        ],
        "next": None,
    },
    {
        "id": "w13_f_a",
        "week": "13주차",
        "bg": "restaurant.png",
        "character": "player_happy.png",
        "lines": [
            (None, "나는 동기와 함께 밥을 먹으러 갔다."),
            (None, "어쩌면 서로 더 각별한 사이가 된 것 같다."),
        ],
        "choices": [],
        "next": "ending",
    },

    # ══════════════════════════════════════════════
    # 엔딩 — 15주차 결과
    # ══════════════════════════════════════════════
    {
        "id": "ending",
        "week": "15주차 — 1학기 결과",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "이렇게 길고도 길었던 1학기 마지막 시험이 끝났다."),
            (None, "수강신청부터 기말고사까지, 정신없이 달려온 한 학기였다."),
            (None, "[ 최종 결과 ]"),  # 실제 스탯은 엔딩 씬에서 별도 렌더
        ],
        "choices": [],
        "next": None,  # 게임 종료
    },
]

# ─── 빠른 조회용 딕셔너리 ───────────────────────────────────
SCENE_MAP = {s["id"]: s for s in SCENES}
