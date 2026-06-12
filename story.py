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
    # 1학기 엔딩 — 15주차 결과 (→ 2학기로 연결)
    # ══════════════════════════════════════════════
    {
        "id": "ending",
        "week": "15주차 — 1학기 결과",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "이렇게 길고도 길었던 1학기 마지막 시험이 끝났다."),
            (None, "수강신청부터 기말고사까지, 정신없이 달려온 한 학기였다."),
            (None, "[ 1학기 최종 결과 ]"),  # 실제 스탯은 엔딩 씬에서 별도 렌더
            (None, "여름방학이 순식간에 지나갔다."),
            (None, "그리고 다시, 2학기가 찾아왔다."),
        ],
        "choices": [],
        "next": "s2_title",
    },

    # ══════════════════════════════════════════════════════════
    # ■ 2학기 : 다시 시작된 서바이벌
    # ══════════════════════════════════════════════════════════

    # ── 2학기 타이틀 ──────────────────────────────────────────
    {
        "id": "s2_title",
        "week": "",
        "bg": "title.png",
        "character": None,
        "lines": [
            (None, "한성대학교 신입생 생존기"),
            (None, "1학년 2학기"),
            (None, "— 다시 시작된 서바이벌 —"),
        ],
        "choices": [],
        "next": "s2_w1_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 1주차 — 수강신청, 2회차의 여유?
    # ══════════════════════════════════════════════
    {
        "id": "s2_w1_intro",
        "week": "2학기 1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "여름방학이 순식간에 증발하고, 다시 찾아온 수강신청의 아침."),
            (None, "1학기의 뼈아픈 실패를 교훈 삼아, 이번엔 만반의 준비를 마쳤다."),
            (None, "화면에는 이번 학기 핵심 전공인 파이썬(Python) 프로그래밍과 선형대수학이 띄워져 있다."),
            ("나", "이번엔 다를 거다… 윈도우 데스크탑, 맥북, 아이패드까지 삼중 세팅 완료."),
            (None, "3… 2… 1… 클릭!"),
            (None, "어떤 전략으로 수강신청을 할까?"),
        ],
        "choices": [
            {
                "text": "① 올클리어를 향한 도박, 인기 교수님 픽",
                "condition": None,
                "effects": {"학점": 10, "멘탈": -5},
                "flags": {},
                "next": "s2_w1_a",
            },
            {
                "text": "② 안전제일, 비인기 시간대(아침 9시) 픽",
                "condition": None,
                "effects": {"학점": 5, "멘탈": -10},
                "flags": {},
                "next": "s2_w1_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w1_a",
        "week": "2학기 1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "가장 평점이 좋은 교수님의 강의들만 골라 담았다."),
            (None, "결과는… 한 과목 튕김! 하지만 나머지는 성공했다."),
            ("나", "아, 선형대수학 하나 놓쳤지만 이 정도면 선방이지. 시간표 나쁘지 않아!"),
        ],
        "choices": [],
        "next": "s2_w3_intro",
    },
    {
        "id": "s2_w1_b",
        "week": "2학기 1주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "클릭 전쟁을 피하기 위해 1교시 강의들로만 꽉꽉 채웠다."),
            (None, "결과는 완벽한 올클리어. 하지만 시간표를 보니 숨이 턱 막힌다."),
            ("나", "주 4일 1교시라니… 미래의 나, 아침에 일어날 수 있지?"),
        ],
        "choices": [],
        "next": "s2_w3_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 3주차 — 가을, 그리고 짝선후배 모임
    # ══════════════════════════════════════════════
    {
        "id": "s2_w3_intro",
        "week": "2학기 3주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "선선한 가을바람이 불어오는 9월 중순."),
            (None, "동아리방이나 과 단톡방이 다시 시끌벅적해지기 시작했다."),
            ("선배", "이번 주 금요일에 성북천 쪽에서 짝선배, 짝후배 다 같이 모여서 밥 먹고 노래방 갈 건데 올 사람?"),
            (None, "1학기 때 멘토링으로 친해졌던 선배의 연락이다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 기꺼이 참석한다 (소지금 15 이상)",
                "condition": lambda p: p.check("소지금", 15),
                "effects": {"인간관계": 15, "멘탈": 10, "소지금": -15},
                "flags": {},
                "next": "s2_w3_a",
            },
            {
                "text": "② 핑계를 대고 불참한다",
                "condition": None,
                "effects": {"멘탈": 15, "인간관계": -5, "소지금": -10},
                "flags": {},
                "next": "s2_w3_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w3_a",
        "week": "2학기 3주차",
        "bg": "restaurant.png",
        "character": "player_happy.png",
        "lines": [
            (None, "저녁 6시, 성북천 근처 고깃집."),
            ("선배", "오, 오랜만이다! 방학 잘 보냈어?"),
            (None, "오랜만에 만난 동기들과 선배들과 고기를 구워 먹으며 밀린 근황을 나눴다."),
            (None, "2차로 간 노래방에서는 목이 터져라 노래를 부르며 스트레스를 풀었다."),
            ("나", "역시 가끔은 이렇게 놀아줘야 학교 다닐 맛이 나지."),
        ],
        "choices": [],
        "next": "s2_w6_intro",
    },
    {
        "id": "s2_w3_b",
        "week": "2학기 3주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "아, 선배 죄송해요. 제가 오늘 꼭 처리해야 할 과제가 있어서요..."),
            (None, "사실 과제는 없었다. 그저 오늘은 혼자만의 시간이 필요했을 뿐."),
            (None, "컴퓨터를 켜고 익숙하게 토스 앱을 열어 발로란트 포인트를 충전한다."),
            (None, "새로 나온 스킨을 사고 게임을 돌리니 이것도 나름의 힐링이다."),
            ("나", "새 스킨 타격감 미쳤다... 이게 내 소확행이지."),
        ],
        "choices": [],
        "next": "s2_w6_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 6주차 — 전공 팀 프로젝트의 늪
    # ══════════════════════════════════════════════
    {
        "id": "s2_w6_intro",
        "week": "2학기 6주차",
        "bg": "classroom.png",
        "character": None,
        "lines": [
            (None, "파이썬 프로그래밍 시간."),
            ("교수", "자, 이번 중간고사는 대체 과제로 팀 프로젝트를 진행하겠습니다. 주제는 자유롭게 웹 크롤링이나 외부 API를 활용한 프로그램 제작입니다."),
            (None, "팀이 배정되고 첫 회의 시간. 모두가 모니터만 바라보며 침묵을 지키고 있다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 답답해서 내가 총대를 멘다 (멘탈 30 이상)",
                "condition": lambda p: p.check("멘탈", 30),
                "effects": {"학점": 15, "인간관계": 10, "멘탈": -15},
                "flags": {},
                "next": "s2_w6_a",
            },
            {
                "text": "② 조용히 묻어간다",
                "condition": None,
                "effects": {"멘탈": 5, "인간관계": -10, "학점": -5},
                "flags": {},
                "next": "s2_w6_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w6_a",
        "week": "2학기 6주차",
        "bg": "classroom.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "저기… 제가 대충 기획안 짜온 게 있는데, 뉴스 데이터 크롤링해서 키워드 뽑아주는 건 어떨까요?"),
            (None, "결국 내가 조장이 되었다. 역할 분담부터 일정 조율까지 신경 쓸 게 산더미다."),
            ("나", "내가 이러려고 대학 왔나... 하지만 완성 퀄리티는 보장되겠지."),
        ],
        "choices": [],
        "next": "s2_w8_intro",
    },
    {
        "id": "s2_w6_b",
        "week": "2학기 6주차",
        "bg": "classroom.png",
        "character": "player_sad.png",
        "lines": [
            ("나", "아 네, 저는 자료조사 쪽 맡겠습니다."),
            (None, "적당히 할 수 있는 최소한의 분량만 가져왔다. 팀장은 힘들어 보였지만, 내 알 바는 아니다."),
            ("나", "대학은 각자도생이야. 내 코가 석 자라고."),
        ],
        "choices": [],
        "next": "s2_w8_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 8주차 — 선형대수학 중간고사
    # ══════════════════════════════════════════════
    {
        "id": "s2_w8_intro",
        "week": "2학기 8주차",
        "bg": "library.png",
        "character": None,
        "lines": [
            (None, "프로젝트의 산을 넘자마자 중간고사 기간이 찾아왔다."),
            (None, "특히 선형대수학... 벡터와 행렬 연산이 칠판을 가득 채울 때마다 머리가 어지럽다."),
            (None, "어떻게 공부할까?"),
        ],
        "choices": [
            {
                "text": "① 손으로 풀고, 코드로 검증한다 (멘탈 40 이상)",
                "condition": lambda p: p.check("멘탈", 40),
                "effects": {"학점": 20, "멘탈": -20},
                "flags": {},
                "next": "s2_w8_a",
            },
            {
                "text": "② 굿노트 AI와 벼락치기의 콜라보",
                "condition": None,
                "effects": {"학점": 5, "멘탈": -10},
                "flags": {},
                "next": "s2_w8_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w8_a",
        "week": "2학기 8주차",
        "bg": "library.png",
        "character": "player_normal.png",
        "lines": [
            (None, "종이에 수식을 빽빽하게 적어가며 계산을 마친 뒤, 노트북을 열어 매트랩(MATLAB)으로 코드를 짜서 결괏값을 비교해 본다."),
            (None, "시간은 두 배로 걸리지만 완벽하게 이해하고 넘어갔다."),
            ("나", "행렬 곱셈... 이제 꿈에서도 할 수 있을 것 같아."),
        ],
        "choices": [],
        "next": "s2_w10_intro",
    },
    {
        "id": "s2_w8_b",
        "week": "2학기 8주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            ("나", "요즘은 툴을 잘 쓰는 게 실력이지!"),
            (None, "아이패드를 꺼내 굿노트 AI 기능으로 교수님의 필기를 요약하고 중요한 부분만 달달 외웠다."),
            (None, "하지만 시험지에 나온 응용문제를 보는 순간 펜이 멈췄다."),
            ("나", "아... 이 공식이 왜 여기서 나와..."),
        ],
        "choices": [],
        "next": "s2_w10_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 10주차 — 가을맞이 단장
    # ══════════════════════════════════════════════
    {
        "id": "s2_w10_intro",
        "week": "2학기 10주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "날씨가 부쩍 쌀쌀해졌다."),
            (None, "옷장을 열어보니 작년에 입던 옷들이 어딘가 촌스러워 보인다."),
            (None, "마침 주말에 사진 동아리 출사 일정 겸 동기들과의 약속도 있다."),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 나를 위한 투자, 쇼핑을 한다 (소지금 20 이상)",
                "condition": lambda p: p.check("소지금", 20),
                "effects": {"인간관계": 10, "멘탈": 10, "소지금": -20},
                "flags": {},
                "next": "s2_w10_a",
            },
            {
                "text": "② 있는 옷을 대충 입는다",
                "condition": None,
                "effects": {"멘탈": -5},
                "flags": {},
                "next": "s2_w10_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w10_a",
        "week": "2학기 10주차",
        "bg": "campus.png",
        "character": "player_happy.png",
        "lines": [
            (None, "무신사에 접속해 네이비색 오버핏 시그니처 후드티를 장바구니에 담았다."),
            (None, "내친김에 떨어져 가는 트러블 패치와 헤어 볼륨 컬크림도 같이 주문했다."),
            (None, "약속 당일, 꽤 맘에 드는 스타일링으로 나갔다."),
            ("동기", "오, 오늘 좀 꾸몄는데?"),
            ("나", "역시 돈 쓰는 게 제일 재밌어. 사진도 엄청 잘 나왔다."),
        ],
        "choices": [],
        "next": "s2_w13_intro",
    },
    {
        "id": "s2_w10_b",
        "week": "2학기 10주차",
        "bg": "campus.png",
        "character": "player_sad.png",
        "lines": [
            ("나", "어차피 학생인데 편한 게 최고지."),
            (None, "늘 입던 검은색 맨투맨을 걸치고 나갔다."),
            (None, "다들 예쁘게 입고 와서 사진을 찍는데 어쩐지 나만 조금 칙칙해 보인다."),
            ("나", "나도 후드티 하나 살 걸 그랬나..."),
        ],
        "choices": [],
        "next": "s2_w13_intro",
    },

    # ══════════════════════════════════════════════
    # 2학기 13주차 — 기말 프로젝트 D-2의 비극
    # ══════════════════════════════════════════════
    {
        "id": "s2_w13_intro",
        "week": "2학기 13주차",
        "bg": "room.png",
        "character": None,
        "lines": [
            (None, "기말 프로젝트로 '강의 요약 어시스턴트'를 만들기로 했다."),
            (None, "EasyOCR로 텍스트를 추출하고 LLM API를 붙여 요약본을 만드는 야심 찬 계획."),
            (None, "하지만 마감 이틀 전, 치명적인 오류가 발생했다."),
            ("나", "왜 맥북에서는 잘 되는데 윈도우 데스크탑으로 옮기면 파일 경로(os, shutil)에서 에러가 나는 거야!"),
            (None, "어떻게 해결할까?"),
        ],
        "choices": [
            {
                "text": "① 밤을 새워 직접 코드를 뜯어고친다 (멘탈 40 이상)",
                "condition": lambda p: p.check("멘탈", 40),
                "effects": {"학점": 20, "멘탈": -25},
                "flags": {},
                "next": "s2_w13_a",
            },
            {
                "text": "② 생성형 AI에게 구원을 요청한다",
                "condition": None,
                "effects": {"학점": 15, "멘탈": -5},
                "flags": {},
                "next": "s2_w13_b",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_w13_a",
        "week": "2학기 13주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "커피를 3캔째 들이켜며 스택오버플로우를 뒤진다."),
            (None, "운영체제별 파일 시스템의 차이를 완벽하게 이해하고 코드를 수정했다."),
            (None, "새벽 4시, 마침내 버그 없는 완벽한 실행 화면을 보았다."),
            ("나", "내가 해냈다... 내가 바로 휴먼 디버거다..."),
        ],
        "choices": [],
        "next": "s2_w13_event_check",
    },
    {
        "id": "s2_w13_b",
        "week": "2학기 13주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            ("나", "제발 살려줘..."),
            (None, "에러 로그를 통째로 복사해서 프롬프트창에 던져 넣었다."),
            (None, "몇 초 뒤, AI가 문제 원인과 수정된 코드를 뱉어냈다."),
            (None, "적용해 보니 귀신같이 해결되었다."),
            ("나", "기술 발전의 혜택은 누리라고 있는 거지. 압도적 감사!"),
        ],
        "choices": [],
        "next": "s2_w13_event_check",
    },

    # 2학기 특별이벤트 : 인간관계 70 이상
    {
        "id": "s2_w13_event_check",
        "week": "2학기 13주차",
        "bg": "campus.png",
        "character": None,
        "lines": [],
        "choices": [],
        "next": "s2_ending",
        "_special": "s2_w13_friend_event",
        "_condition": lambda p: p.check("인간관계", 70),
    },
    {
        "id": "s2_w13_friend_event",
        "week": "2학기 13주차 — 특별이벤트",
        "bg": "campus.png",
        "character": "player_happy.png",
        "lines": [
            (None, "기말고사가 모두 끝나고 학교를 나서는 길."),
            (None, "폰이 울린다."),
            ("친구", "야! 오늘 종강 파티 안 올 거냐? 너 안 오면 시작 안 함 ㅋㅋ"),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {
                "text": "① 당장 달려간다 (소지금 10 이상)",
                "condition": lambda p: p.check("소지금", 10),
                "effects": {"인간관계": 15, "멘탈": 20, "소지금": -10},
                "flags": {},
                "next": "s2_party_a",
            },
            {
                "text": "② 체력 방전으로 거절한다",
                "condition": None,
                "effects": {"멘탈": 10, "인간관계": -5},
                "flags": {},
                "next": "s2_ending",
            },
        ],
        "next": None,
    },
    {
        "id": "s2_party_a",
        "week": "2학기 13주차",
        "bg": "restaurant.png",
        "character": "player_happy.png",
        "lines": [
            ("나", "기다려라, 지금 간다!"),
            (None, "종강 파티는 그 어느 때보다 시끌벅적하고 즐거웠다."),
            (None, "1년간의 고생을 서로 위로하며 웃었다."),
        ],
        "choices": [],
        "next": "s2_ending",
    },

    # ══════════════════════════════════════════════
    # 2학기 엔딩 분기 체크 — 15주차
    # 우선순위: 빛나는별 → 핵인싸 → 자본주의 → 그래도괜찮아
    # ══════════════════════════════════════════════
    {
        "id": "s2_ending",
        "week": "2학기 15주차 — 최종 결과",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "다사다난했던 1학년이 끝났다. 2학년은… 조금 더 나은 내가 되어 있기를!"),
            (None, "[ 2학기 최종 결과 ]"),
        ],
        "choices": [],
        # 실제 분기는 게임 엔진이 ENDINGS_S2를 참조해 처리
        "next": "s2_end_star",          # 엔진이 조건 체크 후 덮어씀
        "_ending_branch": True,         # 엔딩 분기 씬임을 엔진에 알림
    },

    # ── 엔딩 1 : 빛나는 캠퍼스의 별 (학점 80↑ & 멘탈 50↑) ──
    {
        "id": "s2_end_star",
        "week": "2학기 — 엔딩",
        "bg": "campus.png",
        "character": "player_happy.png",
        "lines": [
            (None, "【 빛나는 캠퍼스의 별 】"),
            (None, "기말고사가 끝난 후, 당신은 우수한 성적으로 1학년을 마무리했다."),
            (None, "과제와 시험에 치이며 힘든 순간도 있었지만 끝까지 포기하지 않았다."),
            (None, "교수님들에게 좋은 평가를 받았고, 장학금 대상자로 선정되었다."),
            (None, "앞으로의 대학 생활도 기대되는 순간이다."),
        ],
        "choices": [],
        "next": None,
    },

    # ── 엔딩 2 : 한성대학교 핵인싸 (학점 70↓ & 인간관계 80↑ & 멘탈 60↑) ──
    {
        "id": "s2_end_inssa",
        "week": "2학기 — 엔딩",
        "bg": "festival.png",
        "character": "player_happy.png",
        "lines": [
            (None, "【 한성대학교 핵인싸 】"),
            (None, "축제, MT, 동아리 활동까지."),
            (None, "당신은 학교 곳곳에 친구가 있는 유명인이 되었다."),
            (None, "강의실에 들어가면 아는 사람이 한 명쯤은 꼭 있었고,"),
            (None, "힘든 일이 생겨도 함께 고민해 줄 친구들이 있었다."),
            (None, "학점은 조금 아쉬웠지만, 당신의 대학 생활은 누구보다 즐거웠다."),
        ],
        "choices": [],
        "next": None,
    },

    # ── 엔딩 3 : 자본주의의 승리자 (소지금 80↑) ──
    {
        "id": "s2_end_money",
        "week": "2학기 — 엔딩",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "【 자본주의의 승리자 】"),
            (None, "남들이 과제를 할 때 당신은 알바를 했다."),
            (None, "남들이 놀 때도 당신은 알바를 했다."),
            (None, "어느새 통장에는 꽤 많은 돈이 모여 있었다."),
            (None, "비록 체력은 조금 부족했지만, 등록금과 생활비 걱정을 덜 수 있게 되었다."),
            (None, "당신은 누구보다 현실적인 대학생이 되었다."),
        ],
        "choices": [],
        "next": None,
    },

    # ── 엔딩 4 : 그래도 괜찮은 1학년 (위 조건 모두 미달) ──
    {
        "id": "s2_end_okay",
        "week": "2학기 — 엔딩",
        "bg": "campus.png",
        "character": "player_normal.png",
        "lines": [
            (None, "【 그래도 괜찮은 1학년 】"),
            (None, "특별히 뛰어난 성적을 받지는 못했다."),
            (None, "엄청난 부자가 되지도 못했다."),
            (None, "학교에서 유명인이 된 것도 아니다."),
            (None, "하지만 당신은 무사히 1학년을 마쳤다."),
            (None, "좋은 기억도, 아쉬운 기억도 모두 대학 생활의 일부다."),
            (None, "내년에는 어떤 일이 기다리고 있을까?"),
        ],
        "choices": [],
        "next": None,
    },
]

# ─── 빠른 조회용 딕셔너리 ───────────────────────────────────
SCENE_MAP = {s["id"]: s for s in SCENES}

# ─── 2학기 엔딩 분기 조건 ────────────────────────────────────
# 게임 엔진에서 s2_ending의 "_ending_branch": True 를 감지하면
# 아래 리스트를 순서대로 검사해 첫 번째로 조건을 만족하는 씬으로 이동한다.
ENDINGS_S2 = [
    {
        "id":        "s2_end_star",
        "name":      "빛나는 캠퍼스의 별",
        "condition": lambda p: p.check("학점", 80) and p.check("멘탈", 50),
    },
    {
        "id":        "s2_end_inssa",
        "name":      "한성대학교 핵인싸",
        "condition": lambda p: (not p.check("학점", 70))
                               and p.check("인간관계", 80)
                               and p.check("멘탈", 60),
    },
    {
        "id":        "s2_end_money",
        "name":      "자본주의의 승리자",
        "condition": lambda p: p.check("소지금", 80),
    },
    {
        "id":        "s2_end_okay",
        "name":      "그래도 괜찮은 1학년",
        "condition": lambda p: True,   # 기본 엔딩 — 항상 참
    },
]