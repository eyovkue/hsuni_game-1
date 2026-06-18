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
                "use_friend_chance": True,
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
                "text": "① 술자리에 참석한다 (소지금 30↑)",
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
            (None, "첫날. 카페 알바를 시작했다."),
            (None, "손님들이 주문을 시작한다."),
        ],
        "choices": [],
        "next": "w9_cafe_minigame",
    },
    {
        "id": "w9_cafe_minigame",
        "week": "9주차 — 카페 알바 미니게임",
        "bg": "cafe.png",
        "character": None,
        "lines": [
            (None, "【 카페 주문 미니게임 】"),
            (None, "손님의 주문을 정확히 기억해서 메뉴를 맞춰보세요!"),
            (None, "주문: 아이스 아메리카노, 카페라떼, 바닐라라떼, 카라멜마키아토"),
        ],
        "choices": [
            {
                "text": "① 아이스 아메리카노",
                "condition": None,
                "effects": {"소지금": 5, "멘탈": -5},
                "flags": {},
                "next": "w9_cafe_correct",
            },
            {
                "text": "② 카페라떼",
                "condition": None,
                "effects": {"소지금": 3, "멘탈": -3},
                "flags": {},
                "next": "w9_cafe_wrong",
            },
            {
                "text": "③ 바닐라라떼",
                "condition": None,
                "effects": {"소지금": 3, "멘탈": -3},
                "flags": {},
                "next": "w9_cafe_wrong",
            },
            {
                "text": "④ 카라멜마키아토",
                "condition": None,
                "effects": {"소지금": 3, "멘탈": -3},
                "flags": {},
                "next": "w9_cafe_wrong",
            },
        ],
        "next": None,
    },
    {
        "id": "w9_cafe_correct",
        "week": "9주차",
        "bg": "cafe.png",
        "character": "player_happy.png",
        "lines": [
            (None, "정답! 손님이 만족스럽게 마시고 갔다."),
            ("사장", "잘했어요. 계속 이렇게만 하면 돼요."),
            (None, "생각보다 쉽지 않았다. 하지만 퇴근 후 받은 첫 월급 일부를 보니 기분이 좋아졌다."),
            ("나", "내가 번 돈이다..."),
            ("나", "힘들긴 해도 지갑이 두툼해지는 느낌은 좋네."),
        ],
        "choices": [],
        "next": "w9_money_event",
    },
    {
        "id": "w9_cafe_wrong",
        "week": "9주차",
        "bg": "cafe.png",
        "character": "player_sad.png",
        "lines": [
            (None, "틀렸다! 손님이 실망한 표정으로 다시 주문했다."),
            ("사장", "괜찮아요. 처음엔 다 그래요."),
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
                "text": "① 동기들과 축제를 마음껏 즐긴다 (인간관계 40↑)",
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
                "use_friend_chance": True,
                "force_friend_chance": True,
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
        "next": "s1_result",
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
                "text": "① 같이 밥 먹으러 간다 (소지금 10↑)",
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
                "next": "s1_result",
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
        "next": "s1_result",
    },

    # ══════════════════════════════════════════════
    # 1학기 결과 — 15주차 (→ 2학기로 연결)
    # ══════════════════════════════════════════════
    {
        "id": "s1_result",
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
    # 2학기 1주차 — 수강신청
    # ══════════════════════════════════════════════
    {
        "id": "s2_w1_intro",
        "week": "2학기 1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "여름방학이 순식간에 증발하고, 다시 찾아온 수강신청의 아침."),
            (None, "1학기의 뼈아픈 실패를 교훈 삼아, 이번엔 만반의 준비를 마쳤다."),
            (None, "화면에는 파이썬 프로그래밍과 선형대수학이 띄워져 있다."),
            ("나", "이번엔 다를 거다… 삼중 세팅 완료."),
            (None, "3… 2… 1… 클릭!"),
            (None, "어떤 전략으로 수강신청을 할까?"),
        ],
        "choices": [
            {"text": "① 인기 교수님 픽 (올클리어 도박)", "condition": None,
             "effects": {"학점": 10, "멘탈": -5}, "flags": {}, "next": "s2_w1_a"},
            {"text": "② 아침 9시 비인기 시간대 픽", "condition": None,
             "effects": {"학점": 5, "멘탈": -10}, "flags": {}, "next": "s2_w1_b"},
            {"text": "③ 우주 공강 웰빙 시간표", "condition": None,
             "effects": {"학점": -5, "멘탈": 15}, "flags": {}, "next": "s2_w1_c"},
        ],
        "next": None,
    },
    {"id": "s2_w1_a", "week": "2학기 1주차", "bg": "room.png", "character": "player_normal.png",
     "lines": [(None, "한 과목 튕김! 나머지는 성공."), ("나", "선형대수 하나 놓쳤지만 선방이지!")],
     "choices": [], "next": "s2_w2_intro"},
    {"id": "s2_w1_b", "week": "2학기 1주차", "bg": "room.png", "character": "player_sad.png",
     "lines": [(None, "완벽한 올클리어. 시간표는 숨 막힌다."), ("나", "주 4일 1교시… 일어날 수 있지?")],
     "choices": [], "next": "s2_w2_intro"},
    {"id": "s2_w1_c", "week": "2학기 1주차", "bg": "room.png", "character": "player_happy.png",
     "lines": [(None, "점심 앞뒤 황금 시간표 완성."), ("나", "성적은 포기! 밥은 편하게 먹자!")],
     "choices": [], "next": "s2_w2_intro"},

    # 2학기 2주차 — 등교 지옥
    {"id": "s2_w2_intro", "week": "2학기 2주차", "bg": "sangsang.png", "character": None,
     "lines": [
         (None, "2학기 시작. 오늘따라 늦잠."),
         (None, "한성대입구역 2번 출구. 수업까지 7분. 상상관 언덕이 보인다."),
         (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 마을버스 줄에 선다", "condition": None,
          "effects": {"학점": -2, "멘탈": -15}, "flags": {}, "next": "s2_w2_a"},
         {"text": "② 걸어 올라간다 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"멘탈": -10}, "flags": {}, "next": "s2_w2_b"},
         {"text": "③ 편의점 들러 여유 등교", "condition": None,
          "effects": {"학점": -5, "멘탈": 10, "소지금": -3}, "flags": {}, "next": "s2_w2_c"},
     ], "next": None},
    {"id": "s2_w2_a", "week": "2학기 2주차", "bg": "sangsang.png", "character": "player_sad.png",
     "lines": [(None, "만차 버스 정체."), ("나", "마을버스 샌드위치… 결국 지각.")],
     "choices": [], "next": "s2_w3_intro"},
    {"id": "s2_w2_b", "week": "2학기 2주차", "bg": "sangsang.png", "character": "player_normal.png",
     "lines": [(None, "죽음의 계단을 뛰어 올랐다."), ("나", "상상관은 에베레스트다…")],
     "choices": [], "next": "s2_w3_intro"},
    {"id": "s2_w2_c", "week": "2학기 2주차", "bg": "cafe.png", "character": "player_normal.png",
     "lines": [(None, "편의점에서 간식 사 들고 늦게 입장."), ("나", "F만 안 나오면 돼.")],
     "choices": [], "next": "s2_w3_intro"},

    # 2학기 3주차 — AI 특강
    {"id": "s2_w3_intro", "week": "2학기 3주차", "bg": "campus.png", "character": None,
     "lines": [
         (None, "학과 공지: 토요일 아침 10시 AI 워크숍 특강."),
         ("나", "주말 아침 10시라니…"),
         (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 특강에 참석 (멘탈 40↑)", "condition": lambda p: p.check("멘탈", 40),
          "effects": {"학점": 10, "멘탈": -15}, "flags": {}, "next": "s2_w3_a"},
         {"text": "② 침대와 물아일체", "condition": None,
          "effects": {"학점": -3, "멘탈": 20}, "flags": {}, "next": "s2_w3_b"},
         {"text": "③ 뒤풀이만 참석 (소지금 15↑)", "condition": lambda p: p.check("소지금", 15),
          "effects": {"인간관계": 15, "멘탈": -5, "소지금": -15}, "flags": {}, "next": "s2_w3_c"},
     ], "next": None},
    {"id": "s2_w3_a", "week": "2학기 3주차", "bg": "hall.png", "character": "player_normal.png",
     "lines": [(None, "토요일 아침, AI 트랙 설명을 필기했다."), ("나", "주말 반납은 쓰지만 도움 되겠지.")],
     "choices": [], "next": "s2_w3_event_check"},
    {"id": "s2_w3_b", "week": "2학기 3주차", "bg": "room.png", "character": "player_happy.png",
     "lines": [(None, "이불 속에서 게임."), ("나", "쉬는 게 최고지!")],
     "choices": [], "next": "s2_w3_event_check"},
    {"id": "s2_w3_c", "week": "2학기 3주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "삼선교 포차 뒤풀이에서 족보 정보를 캤다."), ("나", "인생은 타이밍과 인맥!")],
     "choices": [], "next": "s2_w3_event_check"},
    {"id": "s2_w3_event_check", "week": "2학기 3주차", "bg": "campus.png", "character": None,
     "lines": [], "choices": [], "next": "s2_w4_intro",
     "_special": "s2_w3_friend_event", "_condition": lambda p: p.check("인간관계", 70)},
    {"id": "s2_w3_friend_event", "week": "2학기 3주차 — 특별", "bg": "cafe.png", "character": "player_happy.png",
     "lines": [
         ("친구", "특강 들었어?"), ("나", "완전 기절…"),
         ("친구", "같이 복습할래? 역 앞 투썸."),
         (None, "카페에서 함께 공부하며 대화가 이어졌다."),
     ],
     "effects_on_enter": {"인간관계": 5, "멘탈": 5},
     "flags_on_enter": {"친구_찬스": 1},
     "choices": [], "next": "s2_w4_intro"},

    # 4주차 — 오피스아워
    {"id": "s2_w4_intro", "week": "2학기 4주차", "bg": "lab.png", "character": None,
     "lines": [
         (None, "파이썬 과제 중 치명적 런타임 에러."),
         ("나", "왜 안 돌아가는 거야!"),
         (None, "내일 오피스아워. 어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 교수님 연구실 방문 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"학점": 12, "인간관계": 10, "멘탈": -10}, "flags": {}, "next": "s2_w4_a"},
         {"text": "② 단톡방에 헬프 (소지금 10↑)", "condition": lambda p: p.check("소지금", 10),
          "effects": {"학점": 5, "인간관계": 5, "소지금": -5}, "flags": {}, "next": "s2_w4_b"},
         {"text": "③ AI에게 통째로 맡긴다 [50/50]", "condition": None, "effects": {}, "flags": {},
          "random_outcomes": [
              {"weight": 0.5, "next": "s2_w4_c_ok", "effects": {"학점": 5, "멘탈": -20}},
              {"weight": 0.5, "next": "s2_w4_c_fail", "effects": {"학점": -20, "멘탈": -20}},
          ]},
     ], "next": None},
    {"id": "s2_w4_a", "week": "2학기 4주차", "bg": "lab.png", "character": "player_happy.png",
     "lines": [(None, "교수님이 코드 한 줄로 에러 해결."), ("나", "진작 올 걸!")],
     "choices": [], "next": "s2_w5_intro"},
    {"id": "s2_w4_b", "week": "2학기 4주차", "bg": "cafe.png", "character": "player_normal.png",
     "lines": [(None, "과탑 동기가 5분 만에 해결."), ("나", "돈으로 해결하는 코딩!")],
     "choices": [], "next": "s2_w5_intro"},
    {"id": "s2_w4_c_ok", "week": "2학기 4주차", "bg": "room.png", "character": "player_normal.png",
     "lines": [(None, "유사도 검사 통과."), ("나", "조마조마했지만 장땡!")],
     "choices": [], "next": "s2_w5_intro"},
    {"id": "s2_w4_c_fail", "week": "2학기 4주차", "bg": "lab.png", "character": "player_sad.png",
     "lines": [(None, "AI 유사도 90% 적발."), ("나", "망했다… 교수님이 부르셨어…")],
     "choices": [], "next": "s2_w5_intro"},

    # 5주차 — 우주 공강
    {"id": "s2_w5_intro", "week": "2학기 5주차", "bg": "campus.png", "character": None,
     "lines": [
         (None, "4시간짜리 우주 공강. 1학기 수강신청 나비효과."),
         (None, "이 시간을 어떻게 보낼까?"),
     ],
     "choices": [
         {"text": "① 상상큐브에서 과제", "condition": None,
          "effects": {"학점": 8, "인간관계": 5, "멘탈": -10}, "flags": {}, "next": "s2_w5_a"},
         {"text": "② 맛집 투어 (소지금 20↑)", "condition": lambda p: p.check("소지금", 20),
          "effects": {"인간관계": 15, "멘탈": 15, "소지금": -20}, "flags": {}, "next": "s2_w5_b"},
         {"text": "③ 상상파크에서 멍", "condition": None,
          "effects": {"멘탈": -5}, "flags": {}, "next": "s2_w5_c"},
     ], "next": None},
    {"id": "s2_w5_a", "week": "2학기 5주차", "bg": "library.png", "character": "player_normal.png",
     "lines": [(None, "상상큐브에서 과제 완료."), ("나", "갓생 산다!")],
     "choices": [], "next": "s2_w6_intro"},
    {"id": "s2_w5_b", "week": "2학기 5주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "돈가스·카페·웃음."), ("나", "맛집 때문에 등교!")],
     "choices": [], "next": "s2_w6_intro"},
    {"id": "s2_w5_c", "week": "2학기 5주차", "bg": "campus.png", "character": "player_sad.png",
     "lines": [(None, "소파에서 유튜브."), ("나", "지루하지만 돈은 아꼈다.")],
     "choices": [], "next": "s2_w6_intro"},

    # 6주차 — 팀플
    {"id": "s2_w6_intro", "week": "2학기 6주차", "bg": "classroom.png", "character": None,
     "lines": [
         ("교수", "중간고사 대체: 팀 프로젝트입니다."),
         (None, "첫 회의, 침묵."), (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 내가 총대 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"학점": 15, "인간관계": 10, "멘탈": -15}, "flags": {}, "next": "s2_w6_a"},
         {"text": "② 조용히 묻어간다", "condition": None,
          "effects": {"멘탈": 5, "학점": -5, "인간관계": -10}, "flags": {}, "next": "s2_w6_b"},
         {"text": "③ 철혈 총무 (인간관계 50↑)", "condition": lambda p: p.check("인간관계", 50),
          "effects": {"학점": 10, "인간관계": -5, "멘탈": -5}, "flags": {}, "next": "s2_w6_c"},
     ], "next": None},
    {"id": "s2_w6_a", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_normal.png",
     "lines": [(None, "조장이 되었다."), ("나", "퀄리티는 보장되겠지.")],
     "choices": [], "next": "s2_w7_intro"},
    {"id": "s2_w6_b", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_sad.png",
     "lines": [(None, "최소 분량만."), ("나", "각자도생.")],
     "choices": [], "next": "s2_w7_intro"},
    {"id": "s2_w6_c", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_normal.png",
     "lines": [(None, "진행 상황 투명 공유."), ("나", "악역이지만 팀을 살린다.")],
     "choices": [], "next": "s2_w7_intro"},

    # 7주차 — 우산
    {"id": "s2_w7_intro", "week": "2학기 7주차", "bg": "sangsang.png", "character": None,
     "lines": [
         (None, "폭우. 상상관에서 우산이 사라졌다."),
         ("나", "누가 가져갔어…"), (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 비 맞으며 걸어간다", "condition": None,
          "effects": {"멘탈": -25}, "flags": {}, "next": "s2_w7_a"},
         {"text": "② 남은 우산 하나 집어든다", "condition": None,
          "effects": {"멘탈": -5}, "flags": {}, "next": "s2_w7_b"},
         {"text": "③ 에타 저격글", "condition": None,
          "effects": {"인간관계": 5, "멘탈": -10}, "flags": {}, "next": "s2_w7_c"},
     ], "next": None},
    {"id": "s2_w7_a", "week": "2학기 7주차", "bg": "sangsang.png", "character": "player_sad.png",
     "lines": [(None, "생쥐 꼴."), ("나", "감기 걸리겠네…")],
     "choices": [], "next": "s2_w7_event_check"},
    {"id": "s2_w7_b", "week": "2학기 7주차", "bg": "campus.png", "character": "player_normal.png",
     "lines": [(None, "양심의 가책."), ("나", "낙산벌 생존 법칙…")],
     "choices": [], "next": "s2_w7_event_check"},
    {"id": "s2_w7_c", "week": "2학기 7주차", "bg": "campus.png", "character": "player_normal.png",
     "lines": [(None, "익명 동지들의 연대."), ("나", "비 그칠 때까지 버틴다.")],
     "choices": [], "next": "s2_w7_event_check"},
    {"id": "s2_w7_event_check", "week": "2학기 7주차", "bg": "campus.png", "character": None,
     "lines": [], "choices": [], "next": "s2_w8_intro",
     "_special": "s2_w7_friend_event", "_condition": lambda p: p.check("인간관계", 70)},
    {"id": "s2_w7_friend_event", "week": "2학기 7주차 — 특별", "bg": "sangsang.png", "character": "player_happy.png",
     "lines": [
         ("친구", "우산 털렸다며?"), ("나", "진짜 황당…"),
         ("친구", "같이 쓰고 갈래?"),
     ],
     "effects_on_enter": {"인간관계": 5, "멘탈": 5},
     "flags_on_enter": {"친구_찬스": 1},
     "choices": [], "next": "s2_w8_intro"},

    # 8주차 — 선형대수
    {"id": "s2_w8_intro", "week": "2학기 8주차", "bg": "library.png", "character": None,
     "lines": [
         (None, "선형대수학 중간고사. 벡터·행렬의 지옥."),
         (None, "어떻게 공부할까?"),
     ],
     "choices": [
         {"text": "① 손풀이 + Octave 검증 (멘탈 40↑)", "condition": lambda p: p.check("멘탈", 40),
          "effects": {"학점": 20, "멘탈": -15}, "flags": {}, "next": "s2_w8_a"},
         {"text": "② 스터디룸 (인간관계 40↑ or 친구찬스)", "condition": lambda p: p.check("인간관계", 40) or p.has_flag("친구_찬스"),
          "effects": {"학점": 10, "인간관계": 10, "멘탈": -5}, "flags": {}, "use_friend_chance": True, "next": "s2_w8_b"},
         {"text": "③ 예시문제 암기", "condition": None,
          "effects": {"학점": -10, "멘탈": -20}, "flags": {}, "next": "s2_w8_c"},
     ], "next": None},
    {"id": "s2_w8_a", "week": "2학기 8주차", "bg": "library.png", "character": "player_normal.png",
     "lines": [(None, "원리 완벽 이해."), ("나", "눈 감고도 행렬 곱셈!")],
     "choices": [], "next": "s2_w9_intro"},
    {"id": "s2_w8_b", "week": "2학기 8주차", "bg": "library.png", "character": "player_happy.png",
     "lines": [(None, "화이트보드 스터디."), ("나", "혼자보다 백배 낫다!")],
     "choices": [], "next": "s2_w9_intro"},
    {"id": "s2_w8_c", "week": "2학기 8주차", "bg": "room.png", "character": "player_sad.png",
     "lines": [(None, "응용문제에 멘붕."), ("나", "망했다…")],
     "choices": [], "next": "s2_w9_intro"},

    # 9주차 — 야식
    {"id": "s2_w9_intro", "week": "2학기 9주차", "bg": "lab.png", "character": None,
     "lines": [
         (None, "과제 중. 배달 팁 6,000원."),
         (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 직접 포장해 온다", "condition": None,
          "effects": {"인간관계": 10, "멘탈": -10}, "flags": {}, "next": "s2_w9_a"},
         {"text": "② 눈치 싸움 승리", "condition": None,
          "effects": {"멘탈": -5, "인간관계": -15}, "flags": {}, "next": "s2_w9_b"},
         {"text": "③ 풀 결제 (소지금 25↑)", "condition": lambda p: p.check("소지금", 25),
          "effects": {"학점": 5, "인간관계": 20, "소지금": -25}, "flags": {}, "next": "s2_w9_c"},
     ], "next": None},
    {"id": "s2_w9_a", "week": "2학기 9주차", "bg": "sangsang.png", "character": "player_sad.png",
     "lines": [(None, "언덕 왕복 대시."), ("나", "영혼이 먼저 가출…")],
     "choices": [], "next": "s2_w10_intro"},
    {"id": "s2_w9_b", "week": "2학기 9주차", "bg": "lab.png", "character": "player_sad.png",
     "lines": [(None, "공짜 야식."), ("나", "단톡방 분위기 싸늘…")],
     "choices": [], "next": "s2_w10_intro"},
    {"id": "s2_w9_c", "week": "2학기 9주차", "bg": "lab.png", "character": "player_happy.png",
     "lines": [(None, "구원자 대접."), ("나", "자본주의 최고!")],
     "choices": [], "next": "s2_w10_intro"},

    # 10주차 — 쇼핑
    {"id": "s2_w10_intro", "week": "2학기 10주차", "bg": "campus.png", "character": None,
     "lines": [
         (None, "쌀쌀해진 날씨. 입을 옷이 없다."),
         (None, "주말 동기 약속. 어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 쇼핑 (소지금 20↑)", "condition": lambda p: p.check("소지금", 20),
          "effects": {"인간관계": 10, "멘탈": 10, "소지금": -20}, "flags": {}, "next": "s2_w10_a"},
         {"text": "② 맨투맨 대충", "condition": None,
          "effects": {"멘탈": -5}, "flags": {}, "next": "s2_w10_b"},
         {"text": "③ 에타 중고장터 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"인간관계": 10, "멘탈": 5, "소지금": -10}, "flags": {}, "next": "s2_w10_c"},
     ], "next": None},
    {"id": "s2_w10_a", "week": "2학기 10주차", "bg": "campus.png", "character": "player_happy.png",
     "lines": [(None, "후드티·사진 대성공."), ("나", "돈 쓰는 게 최고!")],
     "choices": [], "next": "s2_w10_event_check"},
    {"id": "s2_w10_b", "week": "2학기 10주차", "bg": "campus.png", "character": "player_sad.png",
     "lines": [(None, "칙칙한 단체 사진."), ("나", "후드티 살 걸…")],
     "choices": [], "next": "s2_w10_event_check"},
    {"id": "s2_w10_c", "week": "2학기 10주차", "bg": "campus.png", "character": "player_happy.png",
     "lines": [(None, "1만 원 빈티지 재킷."), ("나", "가성비·스타일 모두 잡았다!")],
     "choices": [], "next": "s2_w10_event_check"},
    {"id": "s2_w10_event_check", "week": "2학기 10주차", "bg": "campus.png", "character": None,
     "lines": [], "choices": [], "next": "s2_w11_intro",
     "_special": "s2_w10_friend_event", "_condition": lambda p: p.check("인간관계", 70)},
    {"id": "s2_w10_friend_event", "week": "2학기 10주차 — 특별", "bg": "cafe.png", "character": "player_happy.png",
     "lines": [
         ("친구", "뭐 입고 올 거야?"), ("나", "입을 옷이 없네…"),
         ("친구", "카페에서 무신사 같이 볼래?"),
     ],
     "effects_on_enter": {"인간관계": 5, "멘탈": 5},
     "flags_on_enter": {"친구_찬스": 1},
     "choices": [], "next": "s2_w11_intro"},

    # 11주차 — 에타 키보드
    {"id": "s2_w11_intro", "week": "2학기 11주차", "bg": "lab.png", "character": None,
     "lines": [
         (None, "[익명] 실습실 키보드 빌런 누구냐"),
         (None, "내 타건 습관이 적나라하게…"),
         (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 사과 댓글 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"인간관계": 10, "멘탈": -15}, "flags": {}, "next": "s2_w11_a"},
         {"text": "② 정면 키보드 배틀", "condition": None,
          "effects": {"학점": -5, "인간관계": -5, "멘탈": -30}, "flags": {}, "next": "s2_w11_b"},
         {"text": "③ 모르는 척", "condition": None,
          "effects": {"학점": 8, "멘탈": 10}, "flags": {}, "next": "s2_w11_c"},
     ], "next": None},
    {"id": "s2_w11_a", "week": "2학기 11주차", "bg": "lab.png", "character": "player_normal.png",
     "lines": [(None, "진심 사과."), ("나", "앞으론 무소음 스킨!")],
     "choices": [], "next": "s2_w12_intro"},
    {"id": "s2_w11_b", "week": "2학기 11주차", "bg": "lab.png", "character": "player_sad.png",
     "lines": [(None, "댓글 난타전."), ("나", "과제도 못 했다…")],
     "choices": [], "next": "s2_w12_intro"},
    {"id": "s2_w11_c", "week": "2학기 11주차", "bg": "lab.png", "character": "player_normal.png",
     "lines": [(None, "에타 로그아웃."), ("나", "학점이 먼저!")],
     "choices": [], "next": "s2_w12_intro"},

    # 12주차 — 기말 대비
    {"id": "s2_w12_intro", "week": "2학기 12주차", "bg": "room.png", "character": None,
     "lines": [
         (None, "12월. 기말·프로젝트·보고서 삼중주."),
         (None, "3일째 잠 못 잤다. 밤을 어떻게 보낼까?"),
     ],
     "choices": [
         {"text": "① 각성 드링크 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"학점": 15, "멘탈": -25}, "flags": {}, "next": "s2_w12_a"},
         {"text": "② 상상관 수면실", "condition": None,
          "effects": {"학점": -8, "멘탈": 15}, "flags": {}, "next": "s2_w12_b"},
         {"text": "③ PC방 밤샘 (소지금 10↑)", "condition": lambda p: p.check("소지금", 10),
          "effects": {"학점": -15, "인간관계": 10, "멘탈": -10, "소지금": -8}, "flags": {}, "next": "s2_w12_c"},
     ], "next": None},
    {"id": "s2_w12_a", "week": "2학기 12주차", "bg": "room.png", "character": "player_sad.png",
     "lines": [(None, "심장 쿵쾅."), ("나", "졸음은 저 세상으로…")],
     "choices": [], "next": "s2_w13_intro"},
    {"id": "s2_w12_b", "week": "2학기 12주차", "bg": "campus.png", "character": "player_normal.png",
     "lines": [(None, "3시간 딥슬립."), ("나", "맨 뒷장 나오면 어쩌지…")],
     "choices": [], "next": "s2_w13_intro"},
    {"id": "s2_w12_c", "week": "2학기 12주차", "bg": "pcbang.png", "character": "player_sad.png",
     "lines": [(None, "게임 한 판… 해가 뜬다."), ("나", "학점도 하늘로…")],
     "choices": [], "next": "s2_w13_intro"},

    # 13주차 — 랩 알바
    {"id": "s2_w13_intro", "week": "2학기 13주차", "bg": "restaurant.png", "character": None,
     "lines": [
         (None, "종강 포차. 선배 전화: 3일 단기 알바 40만 원."),
         ("나", "방학 시작하자마자 또 상상관…?"),
         (None, "어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 돈이 최고! (소지금 10↓)", "condition": lambda p: not p.check("소지금", 11),
          "effects": {"멘탈": -15, "인간관계": -10, "소지금": 40}, "flags": {}, "next": "s2_w13_a"},
         {"text": "② 1년 고생, 휴식!", "condition": None,
          "effects": {"인간관계": 25, "멘탈": 20, "소지금": -10}, "flags": {}, "next": "s2_w13_b"},
         {"text": "③ 동기에게 토스 (인간관계 50↑)", "condition": lambda p: p.check("인간관계", 50),
          "effects": {"인간관계": 20, "멘탈": 10}, "flags": {}, "next": "s2_w13_c"},
     ], "next": None},
    {"id": "s2_w13_a", "week": "2학기 13주차", "bg": "lab.png", "character": "player_sad.png",
     "lines": [(None, "3일간 랩실 노예."), ("나", "지갑은 두툼!")],
     "choices": [], "next": "s2_w14_intro"},
    {"id": "s2_w13_b", "week": "2학기 13주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "종강 파티 밤새."), ("나", "이게 진짜 대학!")],
     "choices": [], "next": "s2_w14_intro"},
    {"id": "s2_w13_c", "week": "2학기 13주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "동기가 술값 전액."), ("나", "꿩·알 모두!")],
     "choices": [], "next": "s2_w14_intro"},

    # 14주차 — 종강 총회
    {"id": "s2_w14_intro", "week": "2학기 14주차", "bg": "restaurant.png", "character": None,
     "lines": [
         (None, "삼선교 종강 총회."),
         (None, "오늘 밤 어떤 모습?"),
     ],
     "choices": [
         {"text": "① 찐하게 의리 (멘탈 30↑)", "condition": lambda p: p.check("멘탈", 30),
          "effects": {"인간관계": 25, "멘탈": 10, "소지금": -15}, "flags": {}, "next": "s2_w14_a"},
         {"text": "② 교수님께 인사 후 퇴장", "condition": None,
          "effects": {"학점": 3, "인간관계": 5, "멘탈": 5}, "flags": {}, "next": "s2_w14_b"},
         {"text": "③ 교수님 어깨 [50/50] (멘탈 50↑)", "condition": lambda p: p.check("멘탈", 50),
          "effects": {}, "flags": {},
          "random_outcomes": [
              {"weight": 0.5, "next": "s2_w14_c_ok", "effects": {"인간관계": 30, "학점": 15}},
              {"weight": 0.5, "next": "s2_w14_c_fail", "effects": {"인간관계": -10, "학점": -25}},
          ]},
     ], "next": None},
    {"id": "s2_w14_a", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "1년 에피소드 토크."), ("나", "스트레스 싹!")],
     "choices": [], "next": "s2_w15_intro"},
    {"id": "s2_w14_b", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_normal.png",
     "lines": [(None, "막차 전 탈출."), ("나", "처세술 성공!")],
     "choices": [], "next": "s2_w15_intro"},
    {"id": "s2_w14_c_ok", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_happy.png",
     "lines": [(None, "교수님이 웃으시며 잔을 채워주셨다."), ("나", "형님 같은 교수님!")],
     "choices": [], "next": "s2_w15_intro"},
    {"id": "s2_w14_c_fail", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_sad.png",
     "lines": [(None, "교수님 정색."), ("나", "재수강 확정…")],
     "choices": [], "next": "s2_w15_intro"},

    # 15주차 — 성적 정정
    {"id": "s2_w15_intro", "week": "2학기 15주차", "bg": "room.png", "character": None,
     "lines": [
         (None, "성적 공람. 핵심 전공 D+."),
         (None, "정정 마감 오늘 자정. 어떻게 할까?"),
     ],
     "choices": [
         {"text": "① 눈물의 반성문 [50/50] (멘탈 25↑)", "condition": lambda p: p.check("멘탈", 25),
          "effects": {}, "flags": {},
          "random_outcomes": [
              {"weight": 0.5, "next": "s2_w15_a_ok", "effects": {"학점": 5, "멘탈": -10}},
              {"weight": 0.5, "next": "s2_w15_a_fail", "effects": {"멘탈": -30}},
          ]},
         {"text": "② 깔끔하게 포기", "condition": None,
          "effects": {"학점": -5, "멘탈": 35}, "flags": {}, "next": "s2_ending"},
         {"text": "③ 이의신청 (학점 50↑)", "condition": lambda p: p.check("학점", 50),
          "effects": {"학점": 10, "멘탈": -15}, "flags": {}, "next": "s2_w15_c"},
     ], "next": None},
    {"id": "s2_w15_a_ok", "week": "2학기 15주차", "bg": "room.png", "character": "player_happy.png",
     "lines": [(None, "D+ → C 기적."), ("나", "교수님 감사합니다!")],
     "choices": [], "next": "s2_ending"},
    {"id": "s2_w15_a_fail", "week": "2학기 15주차", "bg": "room.png", "character": "player_sad.png",
     "lines": [(None, "읽씹."), ("나", "D+ 확정…")],
     "choices": [], "next": "s2_ending"},
    {"id": "s2_w15_c", "week": "2학기 15주차", "bg": "room.png", "character": "player_normal.png",
     "lines": [(None, "팩트 기반 이의신청."), ("나", "논리로 정당한 학점!")],
     "choices": [], "next": "s2_ending"},

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