# story.py
# 1학기 + 2학기(1~15주차) 통합 대본 데이터

# ─── 빠른 조회용 딕셔너리 ───────────────────────────────────#  
SCENES = [

    # ══════════════════════════════════════════════
# ══════════════════════════════════════════════
    # 1학기 1주차 — 수강신청 (미니게임 전략 1 적용)
    # ══════════════════════════════════════════════
    {
        "id": "w1_intro",
        "week": "1학기 1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "아침 10시쯤, 나는 노트북 앞에 앉아 있다."),
            (None, "수강신청 오픈까지 앞으로 10초."),
            ("나", "제발 성공하자…"),
            (None, "3… 2… 1… 클릭!"),
            (None, "새로고침을 누르는 순간, 타이밍 맞추기 창이 떴다!"),
        ],
        "choices": [
            {
                "text": "① 자리가 남은 강의를 그냥 넣는다",
                "condition": None,
                "next": "w1_a",
                "minigame": {
                    "speed": 6,  # 1학기는 조금 느리게 (난이도 쉬움)
                    "base_effects": {"학점": 10, "멘탈": -10},
                    "success_bonus": {"학점": 5, "멘탈": 5},
                    "fail_penalty": {"멘탈": -10}
                }
            },
            {
                "text": "② 학점이 좀 모자라도 이대로 간다",
                "condition": None,
                "next": "w1_b",
                "minigame": {
                    "speed": 6,
                    "base_effects": {"학점": 5, "멘탈": 5},
                    "success_bonus": {"학점": 5},
                    "fail_penalty": {"멘탈": -5}
                }
            },
        ],
        "next": None,
    },


    {
        "id": "w2_intro",
        "week": "1학기 2주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "따스한 봄바람이 불어오는 3월 초. 오늘은 드디어 입학식 날이다."),
            (None, "빈자리를 찾아 앉으려던 순간, 옆자리에 앉은 학생이 말을 걸어왔다."),
            ("???", "저기… 안녕하세요?"),
            (None, "어색한 침묵이 흐른다. 어떻게 할까?"),
        ],
        "choices": [
            {"text": "① 먼저 웃으며 말을 건다", "condition": None, "effects": {"인간관계": 10, "멘탈": 5}, "flags": {}, "next": "w2_a"},
            {"text": "② 간단하게만 대답한다", "condition": None, "effects": {}, "flags": {}, "next": "w2_b"},
            {"text": "③ 못 들은 척 휴대폰을 본다", "condition": None, "effects": {"인간관계": -5, "멘탈": 5}, "flags": {}, "next": "w2_c"},
        ],
        "next": None,
    },
    {
        "id": "w2_a", "week": "1학기 2주차", "bg": "hall.png", "character": "player_happy.png",
        "lines": [("나", "네 안녕하세요! 저도 아는 사람이 아무도 없어서 긴장되네요."), ("???", "진짜요? 다행이다..."), (None, "생애 첫 대학 친구가 생겼다.")],
        "choices": [], "next": "w3_intro",
    },
    {
        "id": "w2_b", "week": "1학기 2주차", "bg": "hall.png", "character": "player_normal.png",
        "lines": [("나", "아... 네."), ("???", "아하..."), (None, "입학식은 무사히 끝났지만 특별한 일은 없었다.")],
        "choices": [], "next": "w3_intro",
    },
    {
        "id": "w2_c", "week": "1학기 2주차", "bg": "hall.png", "character": "player_sad.png",
        "lines": [("???", "...아."), (None, "괜히 조금 미안해졌다. 입학식이 끝난 후 곧바로 집으로 향했다.")],
        "choices": [], "next": "w3_intro",
    },
    {
        "id": "w3_intro",
        "week": "1학기 3주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "점심시간. 천막들이 길게 늘어서 있었고, 선배들이 홍보를 하고 있었다."),
            ("선배", "신입생이죠? 우리 동아리 한번 보고 가요!"),
        ],
        "choices": [
            {"text": "① 따라 간다 (밴드 동아리)", "condition": None, "effects": {"인간관계": 10, "멘탈": 5}, "flags": {"동아리_가입": True}, "next": "w3_a"},
            {"text": "② 그냥 지나친다", "condition": None, "effects": {"멘탈": 5, "인간관계": -10}, "flags": {}, "next": "w3_b"},
        ],
        "next": None,
    },
    {
        "id": "w3_a", "week": "1학기 3주차", "bg": "clubbooth.png", "character": "player_happy.png",
        "lines": [("선배", "안녕하세요! 음악 좋아하세요?"), (None, "생각보다 엄청 멋있어 보였다. 가입 신청서를 작성했다.")],
        "choices": [], "next": "w4_intro",
    },
    {
        "id": "w3_b", "week": "1학기 3주차", "bg": "campus.png", "character": "player_normal.png",
        "lines": [("나", "일단 대학 생활부터 적응하자.")],
        "choices": [], "next": "w4_intro",
    },
    {
        "id": "w4_intro",
        "week": "1학기 4주차",
        "bg": "classroom.png",
        "character": None,
        "lines": [
            ("교수", "이번주까지 보고서 작성 과제 있습니다. 분량은 A4 10페이지 이상입니다."),
            (None, "과제 현황: 교양 과제 1개 / 전공 과제 2개 / 발표 자료 제작 / 팀플 회의 준비"),
            (None, "마감까지 남은 시간은 일주일. 어떻게 할까?"),
        ],
        "choices": [
            {"text": "① 오늘부터 바로 시작한다", "condition": None, "effects": {"학점": 15, "멘탈": -10}, "flags": {}, "next": "w4_a"},
            {"text": "② 마감 전날 밤에 몰아서 한다", "condition": None, "effects": {"학점": 5, "멘탈": -20}, "flags": {}, "next": "w4_b"},
            {"text": "③ AI를 적극 활용한다", "condition": None, "effects": {}, "flags": {}, "next": "w4_c"},
        ],
        "next": None,
    },
    {
        "id": "w4_a", "week": "1학기 4주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [("나", "미래의 나를 믿지 말자. 지금 하는 게 맞다."), (None, "마감 하루 전 모든 과제를 끝냈다.")],
        "choices": [], "next": "w4_event_check",
    },
    {
        "id": "w4_b", "week": "1학기 4주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [("나", "...망했다."), (None, "새벽 2시… 겨우 제출에는 성공했다.")],
        "choices": [], "next": "w4_event_check",
    },
    {
        "id": "w4_c", "week": "1학기 4주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [(None, "과제 주제를 입력했다. 몇 초 만에 초안이 완성되었다. 어떻게 할까?")],
        "choices": [
            {"text": "① 직접 수정한다 (멘탈 35 이상)", "condition": lambda p: p.check("멘탈", 35), "effects": {"학점": 12, "멘탈": -3}, "flags": {}, "next": "w4_c1"},
            {"text": "② 그대로 제출한다", "condition": None, "effects": {"학점": -15, "멘탈": -10}, "flags": {}, "next": "w4_c2"},
        ],
        "next": None,
    },
    {
        "id": "w4_c1", "week": "1학기 4주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [(None, "AI가 만든 내용을 참고해 자신만의 내용으로 수정했다. 생각보다 더 좋은 평을 받았다!")],
        "choices": [], "next": "w4_event_check",
    },
    {
        "id": "w4_c2", "week": "1학기 4주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [(None, "며칠 후… 생각보다 좋지 않은 평가를 받았다…")],
        "choices": [], "next": "w4_event_check",
    },
    {
        "id": "w4_event_check",
        "week": "1학기 4주차",
        "bg": "room.png",
        "character": None,
        "lines": [],
        "choices": [],
        "next": "w4_event",
        "_special": "w4_friend_event",
        "_condition": lambda p: p.check("인간관계", 70),
    },
    {
        "id": "w4_friend_event", "week": "1학기 4주차 — 특별이벤트", "bg": "cafe.png", "character": "player_happy.png",
        "lines": [("친구", "나도 지금 하는 중인데 같이 할래?"), (None, "카페에서 함께 과제를 하며 자연스럽게 대화가 이어졌다.")],
        "choices": [], "effects_on_enter": {"인간관계": 5, "멘탈": 5}, "flags_on_enter": {"친구_찬스": 1}, "next": "w4_event",
    },
    {
        "id": "w4_event", "week": "1학기 4주차 결과", "bg": "room.png", "character": "player_normal.png",
        "lines": [(None, "한 달이 지났다. 슬슬 중간고사 준비를 생각해야 할 때다.")],
        "choices": [], "next": "w78_intro",
    },
    {
        "id": "w78_intro",
        "week": "1학기 7~8주차",
        "bg": "classroom.png",
        "character": None,
        "lines": [
            ("교수", "다음 주가 중간고사 기간입니다."),
            (None, "시험 일정: 교양 과목 3개 / 전공 과목 2개"),
            (None, "어떻게 할까?"),
        ],
        "choices": [
            {"text": "① 도서관에 틀어박혀 공부한다 (멘탈 50 이상)", "condition": lambda p: p.check("멘탈", 50), "effects": {"학점": 20, "멘탈": -15, "인간관계": -5}, "flags": {}, "next": "w78_a"},
            {"text": "② 친구들과 스터디를 한다 (인간관계 40 이상 또는 친구 찬스)", "condition": lambda p: p.check("인간관계", 40) or p.has_flag("친구_찬스"), "effects": {"학점": 10, "인간관계": 10, "멘탈": -5}, "flags": {}, "next": "w78_b"},
            {"text": "③ 벼락치기를 한다", "condition": None, "effects": {"학점": -10, "멘탈": -20}, "flags": {}, "next": "w78_c"},
        ],
        "next": None,
    },
    {
        "id": "w78_a", "week": "1학기 7~8주차", "bg": "library.png", "character": "player_normal.png",
        "lines": [("나", "어? 이거 어제 본 건데? 살았다...")], "choices": [], "next": "w9_intro",
    },
    {
        "id": "w78_b", "week": "1학기 7~8주차", "bg": "cafe.png", "character": "player_happy.png",
        "lines": [(None, "스터디는 생각보다 도움이 됐다. 혼자 하는 것보다 훨씬 낫네.")], "choices": [], "next": "w9_intro",
    },
    {
        "id": "w78_c", "week": "1학기 7~8주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [("나", "이거 어디서 본 것 같은데…"), (None, "결국 절반도 풀지 못했다.")], "choices": [], "next": "w9_intro",
    },
    {
        "id": "w9_intro",
        "week": "1학기 9주차",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "드디어 마지막 시험이 끝났다."),
            ("동기", "오늘 저녁에 다 같이 술 마시러 갈 건데?"),
            (None, "오늘은 뭘 할까?"),
        ],
        "choices": [
            {"text": "① 술자리에 참석한다 (소지금 30 이상)", "condition": lambda p: p.check("소지금", 30), "effects": {"인간관계": 15, "멘탈": -5, "소지금": -10}, "flags": {}, "next": "w9_a"},
            {"text": "② 혼자 휴식한다 (멘탈 20 이하 권장)", "condition": None, "effects": {"멘탈": 15}, "flags": {}, "next": "w9_b"},
            {"text": "③ 아르바이트를 시작한다", "condition": None, "effects": {"소지금": 20, "멘탈": -10}, "flags": {}, "next": "w9_c"},
        ],
        "next": None,
    },
    {
        "id": "w9_a", "week": "1학기 9주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [("나", "가끔은 이런 시간도 필요한 것 같다.")], "choices": [], "next": "w9_money_event",
    },
    {
        "id": "w9_b", "week": "1학기 9주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [("나", "이게 행복이지.")], "choices": [], "next": "w9_money_event",
    },
    {
        "id": "w9_c", "week": "1학기 9주차", "bg": "cafe.png", "character": "player_normal.png",
        "lines": [("나", "힘들긴 해도 지갑이 두툼해지는 느낌은 좋네.")], "choices": [], "next": "w9_money_event",
    },
    {
        "id": "w9_money_event",
        "week": "1학기 9주차",
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
        "week": "1학기 9주차 — 특별이벤트",
        "bg": "campus.png",
        "character": "player_normal.png",
        "lines": [("동기", "야. 너 요즘 돈 좀 있는 것 같던데. 그럼 오늘 밥은 네가 사는 거지?")],
        "choices": [
            {"text": "① 밥을 산다", "condition": None, "effects": {"인간관계": 10, "소지금": -5}, "flags": {}, "next": "w9_money_a"},
            {"text": "② 도망간다", "condition": None, "effects": {"인간관계": -5, "멘탈": 5}, "flags": {}, "next": "w9_money_b"},
        ],
        "next": None,
    },
    {
        "id": "w9_money_a", "week": "1학기 9주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [("나", "대학생의 지갑은 언제나 가볍다...")], "choices": [], "next": "w10_intro",
    },
    {
        "id": "w9_money_b", "week": "1학기 9주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [("나", "뭐라는거야… 나도 쓰기엔 부족하다고…")], "choices": [], "next": "w10_intro",
    },
    {
        "id": "w10_intro",
        "week": "1학기 10주차",
        "bg": "festival.png",
        "character": None,
        "lines": [
            (None, "한성대학교 대동제 D-3"),
            ("나", "그래서 오늘은 뭐를 할까?"),
        ],
        "choices": [
            {"text": "① 동기들과 축제를 마음껏 즐긴다 (인간관계 40 이상)", "condition": lambda p: p.check("인간관계", 40), "effects": {"인간관계": 15, "멘탈": 15, "소지금": -10}, "flags": {}, "next": "w10_a"},
            {"text": "② 동아리 사람들과 함께한다 (동아리 가입 시)", "condition": lambda p: p.has_flag("동아리_가입"), "effects": {"인간관계": 20, "멘탈": 10}, "flags": {}, "next": "w10_b"},
            {"text": "③ 그냥 집으로 간다", "condition": None, "effects": {"멘탈": -5, "인간관계": -5}, "flags": {}, "next": "w10_c"},
        ],
        "next": None,
    },
    {
        "id": "w10_a", "week": "1학기 10주차", "bg": "festival.png", "character": "player_happy.png",
        "lines": [("나", "오늘 진짜 재밌었다.")], "choices": [], "next": "w12_intro",
    },
    {
        "id": "w10_b", "week": "1학기 10주차", "bg": "festival.png", "character": "player_happy.png",
        "lines": [(None, "어느새 자연스럽게 대화에 섞여 있었다.")], "choices": [], "next": "w12_intro",
    },
    {
        "id": "w10_c", "week": "1학기 10주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [(None, "나는 너무 피곤해서 빨리 집으로 가고 싶었다.")], "choices": [], "next": "w12_intro",
    },
    {
        "id": "w12_intro",
        "week": "1학기 12주차",
        "bg": "room.png",
        "character": None,
        "lines": [
            (None, "기말고사가 2주 앞으로 다가온 어느 날."),
            (None, "과제 제출 D-3, 기말 프로젝트 발표 D-4, 전공 보고서 D-5"),
            ("나", "잠깐... 왜 다 이번 주야?"),
        ],
        "choices": [
            {"text": "① 밤샘해서 전부 끝낸다 (멘탈 30 이상)", "condition": lambda p: p.check("멘탈", 30), "effects": {"학점": 15, "멘탈": -20}, "flags": {}, "next": "w12_a"},
            {"text": "② 중요한 것만 챙긴다", "condition": None, "effects": {"학점": 10, "멘탈": -10}, "flags": {}, "next": "w12_b"},
            {"text": "③ 친구와 작업하기 (친구 찬스 보유 시)", "condition": lambda p: p.flags.get("친구_찬스", 0) > 0, "effects": {"학점": 10, "인간관계": 10, "멘탈": -5}, "flags": {}, "next": "w12_c"},
        ],
        "next": None,
    },
    {
        "id": "w12_a", "week": "1학기 12주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [("나", "이번 주만 버티자…")], "choices": [], "next": "w13_intro",
    },
    {
        "id": "w12_b", "week": "1학기 12주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [("나", "줄 건 줘야지…")], "choices": [], "next": "w13_intro",
    },
    {
        "id": "w12_c", "week": "1학기 12주차", "bg": "cafe.png", "character": "player_happy.png",
        "lines": [("나", "혼자하면 쓰러질지도 몰라.")], "choices": [], "next": "w13_intro",
    },
    {
        "id": "w13_intro",
        "week": "1학기 13주차",
        "bg": "library.png",
        "character": None,
        "lines": [
            (None, "기말고사 기간 시작."),
            ("나", "드디어 마지막 관문이다."),
        ],
        "choices": [
            {"text": "① 끝까지 최선을 다한다 (학점 30 이상 & 멘탈 40 이상)", "condition": lambda p: p.check("학점", 30) and p.check("멘탈", 40), "effects": {"학점": 20, "멘탈": -15}, "flags": {}, "next": "w13_a"},
            {"text": "② 벼락치기를 시도한다", "condition": None, "effects": {}, "flags": {}, "next": "w13_b"},
            {"text": "③ 한 과목을 포기하고 나머지에 집중한다", "condition": None, "effects": {"학점": 5, "멘탈": 5}, "flags": {}, "next": "w13_c"},
        ],
        "next": None,
    },
    {
        "id": "w13_a", "week": "1학기 13주차", "bg": "classroom.png", "character": "player_happy.png",
        "lines": [("나", "드디어 끝났다...")], "choices": [], "next": "w13_event_check",
    },
    {
        "id": "w13_b", "week": "1학기 13주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [("나", "다음 학기엔 진짜 미리 공부해야지.")], "choices": [],
        "effects_on_enter_cond": {
            "condition": lambda p: p.check("학점", 40),
            "true_effects": {"학점": 0, "멘탈": -20},
            "false_effects": {"학점": -10, "멘탈": -20},
        },
        "next": "w13_event_check",
    },
    {
        "id": "w13_c", "week": "1학기 13주차", "bg": "library.png", "character": "player_normal.png",
        "lines": [("나", "모든 걸 다 잘할 수는 없어.")], "choices": [], "next": "w13_event_check",
    },
    {
        "id": "w13_event_check",
        "week": "1학기 13주차",
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
        "week": "1학기 13주차 — 특별이벤트",
        "bg": "campus.png",
        "character": "player_happy.png",
        "lines": [
            ("동기", "입학한 게 엊그제 같은데 벌써 한 학기가 끝났네. 고생 많았어."),
        ],
        "choices": [
            {"text": "① 같이 밥 먹으러 간다 (소지금 10 이상)", "condition": lambda p: p.check("소지금", 10), "effects": {"인간관계": 10, "멘탈": 10, "소지금": -10}, "flags": {}, "next": "w13_f_a"},
            {"text": "② 집으로 간다", "condition": None, "effects": {"멘탈": 5}, "flags": {}, "next": "ending"},
        ],
        "next": None,
    },
    {
        "id": "w13_f_a", "week": "1학기 13주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [(None, "어쩌면 서로 더 각별한 사이가 된 것 같다.")], "choices": [], "next": "ending",
    },
    {
        "id": "ending",
        "week": "15주차 — 1학기 결과",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "이렇게 길고도 길었던 1학기 마지막 시험이 끝났다."),
            (None, "여름방학이 순식간에 지나갔다."),
            (None, "그리고 다시, 2학기가 찾아왔다."),
        ],
        "choices": [],
        "next": "s2_title",
    },

    # ══════════════════════════════════════════════════════════
    # ■ 2학기 (1~15주차) : 다시 시작된 서바이벌
    # ══════════════════════════════════════════════════════════
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
        "next": "s2_w1",
    },
    # ── 2학기 1주차 ──
    # 2학기 1주차 — 수강신청 (미니게임 전략 1 적용)
    # ══════════════════════════════════════════════
    {
        "id": "s2_w1",
        "week": "2학기 1주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "여름방학이 순식간에 증발하고, 다시 찾아온 수강신청의 아침."),
            (None, "1학기의 뼈아픈 실패를 교훈 삼아, 이번엔 만반의 준비를 마쳤다."),
            ("나", '"이번엔 다를 거다…"'),
            (None, "PC방에 와서 수강 신청 페이지에 들어가 모든 준비를 마쳤다."),
            (None, "3... 2... 1... 클릭!"),
            ("나", "이번에는 운이 좀 따라줄까?")
        ],
        "choices": [
            {
                "text": "1. 올클리어를 향한 도박, 인기 교수님 픽",
                "condition": None,
                "next": "s2_w1_ch1_res",
                "minigame": {
                    "speed": 12,  # 2학기 도박 픽은 엄청 빠르게! (하이리스크)
                    "base_effects": {"학점": 10, "멘탈": -5},
                    "success_bonus": {"학점": 10, "멘탈": 5},
                    "fail_penalty": {"학점": -5, "멘탈": -15}
                }
            },
            {
                "text": "2. 안전제일, 비인기 시간대(아침 9시) 픽",
                "condition": None,
                "next": "s2_w1_ch2_res",
                "minigame": {
                    "speed": 7,   # 안전 픽은 무난한 속도로
                    "base_effects": {"학점": 5, "멘탈": -10},
                    "success_bonus": {"학점": 5},
                    "fail_penalty": {"멘탈": -5}
                }
            },
            {
                "text": "3. 정공법은 버린다, '우주 공강' 메우기 픽",
                "condition": None,
                "next": "s2_w1_ch3_res",
                "minigame": {
                    "speed": 8,
                    "base_effects": {"학점": -5, "멘탈": 15},
                    "success_bonus": {"멘탈": 10},
                    "fail_penalty": {"멘탈": -10}
                }
            }
        ]
    },

    # ── 2학기 2주차 ──
    {
        "id": "s2_w2",
        "week": "2학기 2주차",
        "bg": "campus.png",
        "character": "player_sad.png",
        "lines": [
            (None, "2학기가 시작되자마자 어김없이 찾아온 삼선교의 아침."),
            (None, "하필 오늘따라 늦잠을 잤다."),
            (None, "한성대입구역 2번 출구에 내리니 수업 시작까지 남은 시간은 단 7분."),
            (None, "상상관 언덕 위를 올려다보니 한숨이 나온다. 어떻게 할까?")
        ],
        "choices": [
            {"text": "1. 성북 02번 마을버스 줄에 몸을 구겨 넣는다.", "condition": None, "effects": {"학점": -2, "멘탈": -15}, "next": "s2_w2_ch1_res"},
            {"text": "2. AI 응용학과의 기상으로 걸어 올라간다. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"멘탈": -10}, "next": "s2_w2_ch2_res"},
            {"text": "3. 중간에 편의점으로 새서 유유자적 등교한다.", "condition": None, "effects": {"학점": -5, "멘탈": 10, "소지금": -3}, "next": "s2_w2_ch3_res"}
        ]
    },
    {
        "id": "s2_w2_ch1_res", "week": "2학기 2주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [
            (None, "야속하게도 상상관 앞 고갯길 정체 구간에서 차가 멈춰 서서 움직이지 않는다."),
            ("나", '"아, 마을버스 샌드위치 지옥이다… 결국 첫 주부터 지각이네."')
        ],
        "choices": [], "next": "s2_w3"
    },
    {
        "id": "s2_w2_ch2_res", "week": "2학기 2주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [
            (None, "허벅지가 터질 것 같고 허리가 끊어질 것 같지만 오직 강의실을 향해 돌진했다."),
            ("나", '"상상관은 캠퍼스가 아니라 에베레스트다… 수업 시작 전부터 기가 다 빨렸어."')
        ],
        "choices": [], "next": "s2_w3"
    },
    {
        "id": "s2_w2_ch3_res", "week": "2학기 2주차", "bg": "campus.png", "character": "player_normal.png",
        "lines": [
            (None, "강의실 뒷문을 슬쩍 열고 들어가니 이미 수업은 중반을 달리고 있고, 교수님의 매서운 눈총이 이마에 꽂힌다."),
            ("나", '"F만 안 나오면 돼. 일단 배는 채웠으니 만족한다."')
        ],
        "choices": [], "next": "s2_w3"
    },

    # ── 2학기 3주차 ──
    {
        "id": "s2_w3",
        "week": "2학기 3주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "학과 공지방에 1학년 학우들을 위한 '인공지능 분야 커리어 탐색 특강' 안내가 올라왔다."),
            (None, "전공 학점을 잘 받으려면 유익하겠지만, 하필 토요일 아침 10시 상상관 대강당이다."),
            ("나", '"주말 아침 10시라니..."'),
            (None, "어떻게 할까?")
        ],
        "choices": [
            {"text": "1. 잠을 포기하고 전공 역량을 쌓는다. (멘탈 40 이상)", "condition": lambda p: p.get("멘탈") >= 40, "effects": {"학점": 10, "멘탈": -15}, "next": "s2_w3_ch1_res"},
            {"text": "2. 집에서 침대와 물아일체가 된다.", "condition": None, "effects": {"학점": -3, "멘탈": 20}, "next": "s2_w3_ch2_res"},
            {"text": "3. 뒤풀이만 참석하는 영리한(?) 선택을 한다. (소지금 15 이상)", "condition": lambda p: p.get("소지금") >= 15, "effects": {"인간관계": 15, "멘탈": -5, "소지금": -15}, "next": "s2_w3_ch3_res"}
        ]
    },
    {
        "id": "s2_w3_ch1_res", "week": "2학기 3주차", "bg": "hall.png", "character": "player_sad.png",
        "lines": [
            (None, "대강당 차가운 의자에 앉아 교수님들의 설명과 파이썬 코딩 팁을 열심히 필기한다."),
            ("나", '"주말 반납은 쓰지만, 2학기 학점 방어엔 도움 되겠지."')
        ],
        "choices": [], "next": "s2_w3_event_check"
    },
    {
        "id": "s2_w3_ch2_res", "week": "2학기 3주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "단톡방 특강 공지를 못 본 척 다시 따뜻한 이불을 덮었다."),
            ("나", '"대학생에게 주말 특강을 권하는 건 유죄야. 역시 쉬는 게 최고지!"')
        ],
        "choices": [], "next": "s2_w3_event_check"
    },
    {
        "id": "s2_w3_ch3_res", "week": "2학기 3주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "저녁에 열린 학과 특강 뒤풀이 술자리에만 슬쩍 숟가락을 얹었다."),
            ("나", '"인생은 타이밍과 인맥이지. 알짜배기 정보는 다 얻었다."')
        ],
        "choices": [], "next": "s2_w3_event_check"
    },
    {
        "id": "s2_w3_event_check",
        "week": "2학기 3주차",
        "bg": "campus.png",
        "lines": [],
        "choices": [],
        "next": "s2_w4",
        "_special": "s2_w3_special",
        "_condition": lambda p: p.get("인간관계") >= 70
    },
    {
        "id": "s2_w3_special", "week": "2학기 3주차 — 특별이벤트", "bg": "cafe.png", "character": "player_happy.png",
        "lines": [
            (None, "갑자기 휴대폰 알림이 울렸다."),
            ("동기", '"오늘 특강 들었어? 카페에서 같이 복습할래?"'),
            (None, "카페에서 함께 과제를 하며 꿀팁을 공유했다.")
        ],
        "choices": [],
        "effects_on_enter": {"인간관계": 5, "멘탈": 5},
        "flags_on_enter": {"친구_찬스": 1},
        "next": "s2_w4"
    },

    # ── 2학기 4주차 ──
    {
        "id": "s2_w4",
        "week": "2학기 4주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "2학기 전공 파이썬 과제를 하던 중, 치명적인 런타임 에러가 발생했다."),
            ("나", '"아무리 봐도 코드엔 문제가 없는데 왜 안 돌아가는 거야!"'),
            (None, "마침 내일 오후는 교수님의 학생 면담 시간(Office Hour)이다. 어떻게 할까?")
        ],
        "choices": [
            {"text": "1. 노트북을 들고 교수님 연구실을 두드린다. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"학점": 12, "인간관계": 10, "멘탈": -10}, "next": "s2_w4_ch1_res"},
            {"text": "2. 동기 단톡방에 조공을 바치며 헬프 미를 외친다. (소지금 10 이상)", "condition": lambda p: p.get("소지금") >= 10, "effects": {"학점": 5, "인간관계": 5, "소지금": -5}, "next": "s2_w4_ch2_res"},
            {
                "text": "3. 에라 모르겠다, AI에게 통째로 맡긴다. [성공 50% / 실패 50%]",
                "condition": None,
                "random_branches": [
                    {"next": "s2_w4_ch3_success", "effects": {"학점": 5, "멘탈": -20}},
                    {"next": "s2_w4_ch3_fail", "effects": {"학점": -20, "멘탈": -20}}
                ]
            }
        ]
    },
    {
        "id": "s2_w4_ch1_res", "week": "2학기 4주차", "bg": "classroom.png", "character": "player_happy.png",
        "lines": [
            (None, "긴장감에 침을 삼키는 나를 보며 교수님은 허허 웃으시더니, 코드 한 줄을 슥 고쳐주셨다."),
            ("나", '"진작 찾아올 걸! 코딩 막힌 게 뚫리니까 속이 다 시원하다."')
        ],
        "choices": [], "next": "s2_w5"
    },
    {
        "id": "s2_w4_ch2_res", "week": "2학기 4주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "귀신같이 톡을 확인한 과탑 동기가 5분 만에 배열 인덱스 오류를 찾아냈다."),
            ("나", '"돈으로 해결하는 코딩이 제일 편하다. 고마워, 과탑아!"')
        ],
        "choices": [], "next": "s2_w5"
    },
    {
        "id": "s2_w4_ch3_success", "week": "2학기 4주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "다행히 복사 붙여넣기 한 코드가 유사도 검사망을 교묘하게 피해 갔다."),
            ("나", '"와, 진짜 조마조마했다... 모르면 어때, 돌아가면 장땡이지!"')
        ],
        "choices": [], "next": "s2_w5"
    },
    {
        "id": "s2_w4_ch3_fail", "week": "2학기 4주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "[공지] AI 코드 유사도 90% 이상 적발자 명단... 뇌정지가 온다."),
            ("나", '"아... 망했다. 교수님이 코드 직접 설명해 보라는데 어떡하지?"')
        ],
        "choices": [], "next": "s2_w5"
    },

    # ── 2학기 5주차 ──
    {
        "id": "s2_w5",
        "week": "2학기 5주차",
        "bg": "campus.png",
        "character": "player_normal.png",
        "lines": [
            (None, "개강 한 달 차. 지옥 같은 연속 강의 사이에 무려 4시간이라는 '우주 공강'이 발생했다."),
            (None, "1주차에 맛보았던 수강신청 실패의 나비효과가 현실이 되었다."),
            (None, "이 기나긴 시간을 어떻게 때울까?")
        ],
        "choices": [
            {"text": "1. 상상큐브를 대여해 과제를 달린다.", "condition": None, "effects": {"학점": 8, "인간관계": 5, "멘탈": -10}, "next": "s2_w5_ch1_res"},
            {"text": "2. 삼선교 골목 맛집 투어를 간다. (소지금 20 이상)", "condition": lambda p: p.get("소지금") >= 20, "effects": {"인간관계": 15, "멘탈": 15, "소지금": -20}, "next": "s2_w5_ch2_res"},
            {"text": "3. 상상파크 구석에서 좀비처럼 버틴다.", "condition": None, "effects": {"멘탈": -5}, "next": "s2_w5_ch3_res"}
        ]
    },
    {
        "id": "s2_w5_ch1_res", "week": "2학기 5주차", "bg": "library.png", "character": "player_normal.png",
        "lines": [
            (None, "마커로 알고리즘을 적어가며 미뤄둔 파이썬 실습을 미리 끝내두었다."),
            ("나", '"공강을 생산적으로 쓰다니, 나 완전 갓생 살고 있네."')
        ],
        "choices": [], "next": "s2_w6"
    },
    {
        "id": "s2_w5_ch2_res", "week": "2학기 5주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "맛집에서 기름진 고기를 흡입하고 감성 카페에서 디저트까지 클리어했다."),
            ("나", '"학교 주변 맛집 가려고 등교하는 거지. 행복하다!"')
        ],
        "choices": [], "next": "s2_w6"
    },
    {
        "id": "s2_w5_ch3_res", "week": "2학기 5주차", "bg": "hall.png", "character": "player_sad.png",
        "lines": [
            (None, "소파에 묻혀 유튜브 영상을 보며 멍을 때렸다. 시간이 느리게 흐른다."),
            ("나", '"지루하긴 한데... 돈 아꼈으니 됐다. 집에 가고 싶다."')
        ],
        "choices": [], "next": "s2_w6"
    },

    # ── 2학기 6주차 ──
    {
        "id": "s2_w6",
        "week": "2학기 6주차",
        "bg": "classroom.png",
        "character": "player_normal.png",
        "lines": [
            (None, "어느덧 10월, 교수님이 빔프로젝터를 띄우며 의미심장하게 웃으셨다."),
            ("교수", '"이번 중간고사는 대체 과제로 팀 프로젝트를 진행하겠습니다."'),
            (None, "조가 무작위로 배정되고 어색하게 첫 회의가 시작되었다. 누군가는 말을 꺼내야 한다.")
        ],
        "choices": [
            {"text": "1. 답답해서 내가 총대를 멘다. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"학점": 15, "인간관계": 10, "멘탈": -15}, "next": "s2_w6_ch1_res"},
            {"text": "2. 조용히 묻어간다.", "condition": None, "effects": {"멘탈": 5, "학점": -5, "인간관계": -10}, "next": "s2_w6_ch2_res"},
            {"text": "3. 무임승차는 차단한다, '철혈의 총무'가 된다. (인간관계 50 이상)", "condition": lambda p: p.get("인간관계") >= 50, "effects": {"학점": 10, "인간관계": -5, "멘탈": -5}, "next": "s2_w6_ch3_res"}
        ]
    },
    {
        "id": "s2_w6_ch1_res", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_sad.png",
        "lines": [
            (None, "정신을 차려보니 내가 조장이 되어 있었다. 역할 분담, 일정 조율 등 산더미다."),
            ("나", '"내가 이러려고 대학 왔나... 하지만 완성 퀄리티는 보장되겠지."')
        ],
        "choices": [], "next": "s2_w7"
    },
    {
        "id": "s2_w6_ch2_res", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_normal.png",
        "lines": [
            (None, "최대한 무난한 파트를 선점했다. 조장의 한숨 소리가 들리지만 몸은 편하다."),
            ("나", '"대학은 각자도생이야. 내 코가 석 자라고."')
        ],
        "choices": [], "next": "s2_w7"
    },
    {
        "id": "s2_w6_ch3_res", "week": "2학기 6주차", "bg": "classroom.png", "character": "player_happy.png",
        "lines": [
            (None, "조장은 피하되 냉철한 감시자 역할을 자처하며 팀의 기강을 잡았다."),
            ("나", '"악역을 자처했지만, 잔혹한 대학 사회에서 조별과제를 살려내는 방법이다."')
        ],
        "choices": [], "next": "s2_w7"
    },

    # ── 2학기 7주차 ──
    {
        "id": "s2_w7",
        "week": "2학기 7주차",
        "bg": "campus.png",
        "character": "player_sad.png",
        "lines": [
            (None, "가을비가 억수같이 쏟아지는 화요일 오후. 수업을 마치고 나와보니..."),
            (None, "우산꽂이에 예쁘게 꽂아두었던 내 소중한 3단 우산이 감쪽같이 사라졌다."),
            ("나", '"어떤 녀석이 내 우산 가져갔어..."'),
            (None, "어떻게 할까?")
        ],
        "choices": [
            {"text": "1. 비를 맞으며 당당하게 낭만을 즐긴다.", "condition": None, "effects": {"멘탈": -25}, "next": "s2_w7_ch1_res"},
            {"text": "2. 남은 우산 중 가장 좋아 보이는 걸 픽한다.", "condition": None, "effects": {"멘탈": -5}, "next": "s2_w7_ch2_res"},
            {"text": "3. 에타에 분노의 저격 글을 올리고 존버한다.", "condition": None, "effects": {"인간관계": 5, "멘탈": -10}, "next": "s2_w7_ch3_res"}
        ]
    },
    {
        "id": "s2_w7_ch1_res", "week": "2학기 7주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [
            (None, "악순환을 끊기 위해 빗속으로 뛰어들었지만 3초 만에 생쥐 꼴이 되었다."),
            ("나", '"도대체 내 우산 가져간 놈 누구냐? 감기 걸리겠네 진짜..."')
        ],
        "choices": [], "next": "s2_w7_event_check"
    },
    {
        "id": "s2_w7_ch2_res", "week": "2학기 7주차", "bg": "campus.png", "character": "player_normal.png",
        "lines": [
            (None, "양심의 가책이 찌르지만 튼튼한 장우산을 슬쩍 집어 쾌적하게 하교했다."),
            ("나", '"미안합니다 이름 모를 학우여... 이것이 낙산벌의 생존 법칙입니다."')
        ],
        "choices": [], "next": "s2_w7_event_check"
    },
    {
        "id": "s2_w7_ch3_res", "week": "2학기 7주차", "bg": "hall.png", "character": "player_normal.png",
        "lines": [
            (None, "에타에 저격 글을 올리자 실시간으로 동조 댓글이 달리며 기묘한 연대감을 느낀다."),
            ("나", '"익명의 동지들아, 힘을 줘... 비 그칠 때까지 절대 안 나간다."')
        ],
        "choices": [], "next": "s2_w7_event_check"
    },
    {
        "id": "s2_w7_event_check",
        "week": "2학기 7주차",
        "bg": "campus.png",
        "lines": [], "choices": [], "next": "s2_w8",
        "_special": "s2_w7_special",
        "_condition": lambda p: p.get("인간관계") >= 70
    },
    {
        "id": "s2_w7_special", "week": "2학기 7주차 — 특별이벤트", "bg": "campus.png", "character": "player_happy.png",
        "lines": [
            (None, "갑자기 휴대폰이 울렸다."),
            ("동기", '"너 우산 털렸다며? 나 상상관 1층인데 같이 쓰고 갈래?"'),
            (None, "하나의 우산을 쓰고 역까지 함께 걸어갔다.")
        ],
        "choices": [],
        "effects_on_enter": {"인간관계": 5, "멘탈": 5},
        "flags_on_enter": {"친구_찬스": 1},
        "next": "s2_w8"
    },

    # ── 2학기 8주차 ──
    {
        "id": "s2_w8",
        "week": "2학기 8주차",
        "bg": "library.png",
        "character": "player_sad.png",
        "lines": [
            (None, "비가 그치고 어김없이 중간고사 기간이 코앞으로 다가왔다."),
            (None, "이번 선형대수학 시험 범위는 기가 질릴 정도로 심상치 않다. 벡터공간부터 역행렬까지..."),
            (None, "어떻게 공부를 시작할까?")
        ],
        "choices": [
            {"text": "1. 손으로 풀고 옥타브(Octave)로 검증한다. (멘탈 40 이상)", "condition": lambda p: p.get("멘탈") >= 40, "effects": {"학점": 20, "멘탈": -15}, "next": "s2_w8_ch1_res"},
            {"text": "2. 친구들과 스터디룸을 잡는다. (인간관계 40 이상 or 친구찬스)", "condition": lambda p: p.get("인간관계") >= 40 or p.has_flag("친구_찬스"), "effects": {"학점": 10, "인간관계": 10, "멘탈": -5}, "next": "s2_w8_ch2_res"},
            {"text": "3. 예시 문제만 달달 외운다.", "condition": None, "effects": {"학점": -10, "멘탈": -20}, "next": "s2_w8_ch3_res"}
        ]
    },
    {
        "id": "s2_w8_ch1_res", "week": "2학기 8주차", "bg": "library.png", "character": "player_normal.png",
        "lines": [
            (None, "시간은 두 배로 걸렸지만 어느 순간 수식의 원리가 머릿속에 완벽하게 복사되었다."),
            ("나", '"행렬 곱셈과 고윳값 구하기, 이제 눈 감고도 하겠다."')
        ],
        "choices": [], "next": "s2_w9"
    },
    {
        "id": "s2_w8_ch2_res", "week": "2학기 8주차", "bg": "library.png", "character": "player_happy.png",
        "lines": [
            (None, "칠판을 수식으로 가득 채워나가니 혼자 끙끙 앓을 때보다 이해가 훨씬 빠르다."),
            ("나", '"혼자 앓는 것보다 백배 낫네. 같이 하니까 든든하다."')
        ],
        "choices": [], "next": "s2_w9"
    },
    {
        "id": "s2_w8_ch3_res", "week": "2학기 8주차", "bg": "library.png", "character": "player_sad.png",
        "lines": [
            (None, "개념을 꼬아버린 낯선 응용문제들이 튀어나왔고, 머릿속이 하얗게 지워졌다."),
            ("나", '"망했다... 아는 게 하나도 없잖아..."')
        ],
        "choices": [], "next": "s2_w9"
    },

    # ── 2학기 9주차 ──
    {
        "id": "s2_w9",
        "week": "2학기 9주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "중간고사가 끝나고 과방에서 동기들과 배달 앱으로 야식을 시키려 한다."),
            (None, "학교 언덕 때문인지 배달 팁이 무려 6,000원이나 찍힌다."),
            (None, "어떻게 할까?")
        ],
        "choices": [
            {"text": "1. \"내가 그냥 뛰어 갔다 올게!\" 직접 포장.", "condition": None, "effects": {"인간관계": 10, "멘탈": -10}, "next": "s2_w9_ch1_res"},
            {"text": "2. \"나 통장에 돈이 없는데...\" 눈치 싸움 승리.", "condition": None, "effects": {"멘탈": -5, "인간관계": -15}, "next": "s2_w9_ch2_res"},
            {"text": "3. \"시간이 돈이다.\" 풀 결제 쏜다. (소지금 25 이상)", "condition": lambda p: p.get("소지금") >= 25, "effects": {"학점": 5, "인간관계": 20, "소지금": -25}, "next": "s2_w9_ch3_res"}
        ]
    },
    {
        "id": "s2_w9_ch1_res", "week": "2학기 9주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [
            (None, "무거운 떡볶이를 들고 언덕을 올라오는데 다리가 후들거린다."),
            ("나", '"돈은 아꼈는데... 내 영혼이 먼저 가출했어."')
        ],
        "choices": [], "next": "s2_w10"
    },
    {
        "id": "s2_w9_ch2_res", "week": "2학기 9주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "공짜로 야식을 먹었지만 동기들의 싸늘한 시선이 느껴진다."),
            ("나", '"일단 배는 채웠는데... 과방 분위기가 왜 이리 차갑지?"')
        ],
        "choices": [], "next": "s2_w10"
    },
    {
        "id": "s2_w9_ch3_res", "week": "2학기 9주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "동기들은 나를 구원자라 부르며 고마웠는지 팀 과제 코딩 검토를 일사천리로 도와준다."),
            ("나", '"역시 자본주의가 최고야. 과제 깔끔하게 진도 뺀 걸로 만족하자."')
        ],
        "choices": [], "next": "s2_w10"
    },

    # ── 2학기 10주차 ──
    {
        "id": "s2_w10",
        "week": "2학기 10주차",
        "bg": "room.png",
        "character": "player_normal.png",
        "lines": [
            (None, "바람이 부쩍 쌀쌀해졌다. 작년 옷들은 촌스러워 보이고 외투가 마땅치 않다."),
            (None, "주말에 학과 동기들과 중요한 약속이 있다. 어떻게 스타일링 할까?")
        ],
        "choices": [
            {"text": "1. 나를 위한 투자, 쇼핑을 한다. (소지금 20 이상)", "condition": lambda p: p.get("소지금") >= 20, "effects": {"인간관계": 10, "멘탈": 10, "소지금": -20}, "next": "s2_w10_ch1_res"},
            {"text": "2. 있는 옷을 대충 입는다.", "condition": None, "effects": {"멘탈": -5}, "next": "s2_w10_ch2_res"},
            {"text": "3. 에타 중고장터와 빈티지를 턴다. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"인간관계": 10, "멘탈": 5, "소지금": -10}, "next": "s2_w10_ch3_res"}
        ]
    },
    {
        "id": "s2_w10_ch1_res", "week": "2학기 10주차", "bg": "campus.png", "character": "player_happy.png",
        "lines": [
            (None, "깔끔한 네이비색 오버핏 시그니처 후드티로 코디했다."),
            ("나", '"역시 돈 쓰는 게 젤 재밌어. 인스타 업로드용 사진 잘 나왔다."')
        ],
        "choices": [], "next": "s2_w10_event_check"
    },
    {
        "id": "s2_w10_ch2_res", "week": "2학기 10주차", "bg": "campus.png", "character": "player_sad.png",
        "lines": [
            (None, "단체 사진을 찍는데 거울 속 어쩐지 나만 후줄근해 보인다."),
            ("나", '"무리해서라도 새로 살 걸 그랬나... 괜히 신경 쓰이네."')
        ],
        "choices": [], "next": "s2_w10_event_check"
    },
    {
        "id": "s2_w10_ch3_res", "week": "2학기 10주차", "bg": "campus.png", "character": "player_happy.png",
        "lines": [
            (None, "카키색 워크 재킷을 직거래로 건져 빈티지 룩을 완성했다."),
            ("나", '"발품을 팔면 되지! 가성비와 스타일을 모두 잡은 승리다."')
        ],
        "choices": [], "next": "s2_w10_event_check"
    },
    {
        "id": "s2_w10_event_check",
        "week": "2학기 10주차",
        "bg": "campus.png",
        "lines": [], "choices": [], "next": "s2_w11",
        "_special": "s2_w10_special",
        "_condition": lambda p: p.get("인간관계") >= 70
    },
    {
        "id": "s2_w10_special", "week": "2학기 10주차 — 특별이벤트", "bg": "cafe.png", "character": "player_happy.png",
        "lines": [
            (None, "문자가 왔다."),
            ("동기", '"나도 옷 고르는 중인데 카페에서 같이 무신사 볼래?"'),
            (None, "카페에서 함께 쇼핑몰을 보며 즐겁게 대화했다.")
        ],
        "choices": [],
        "effects_on_enter": {"인간관계": 5, "멘탈": 5},
        "flags_on_enter": {"친구_찬스": 1},
        "next": "s2_w11"
    },

    # ── 2학기 11주차 ──
    {
        "id": "s2_w11",
        "week": "2학기 11주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "에타 핫게시물 제목: [익명] AI실습실 키보드 빌런 본 사람?"),
            (None, "읽어보니 내 기계식 키보드 소음과 한숨 버릇이 적나라하게 박제되어 있다."),
            (None, "댓글들이 실시간으로 달리며 심장이 쿵쾅거린다. 어떻게 할까?")
        ],
        "choices": [
            {"text": "1. 깔끔한 사과 글로 진화 시도. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"인간관계": 10, "멘탈": -15}, "next": "s2_w11_ch1_res"},
            {"text": "2. 익명의 키보드 워리어로 정면 돌파.", "condition": None, "effects": {"학점": -5, "인간관계": -5, "멘탈": -30}, "next": "s2_w11_ch2_res"},
            {"text": "3. 철저하게 모르는 척 에타 앱을 봉인한다.", "condition": None, "effects": {"학점": 8, "멘탈": 10}, "next": "s2_w11_ch3_res"}
        ]
    },
    {
        "id": "s2_w11_ch1_res", "week": "2학기 11주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [
            (None, "정중한 사과를 남기자 작성자가 글을 내렸고 동기들도 대처가 깔끔했다며 다독여 주었다."),
            ("나", '"앞으론 실습실에서 숨도 살살 쉬어야겠다."')
        ],
        "choices": [], "next": "s2_w12"
    },
    {
        "id": "s2_w11_ch2_res", "week": "2학기 11주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "대댓글로 거친 난타전이 벌어졌고, 과 단톡방에까지 링크가 돌아 얼굴이 시빨개졌다."),
            ("나", '"얼굴도 모르는 녀석 때문에 멘탈 다 갈아 넣었네."')
        ],
        "choices": [], "next": "s2_w12"
    },
    {
        "id": "s2_w11_ch3_res", "week": "2학기 11주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [
            (None, "애써 현실을 부정하며 앱을 지우고 무선 이어폰 볼륨을 높였다."),
            ("나", '"내 학점이 먼저지, 가상 세계 인터넷 싸움이 뭐가 중요해."')
        ],
        "choices": [], "next": "s2_w12"
    },

    # ── 2학기 12주차 ──
    {
        "id": "s2_w12",
        "week": "2학기 12주차",
        "bg": "library.png",
        "character": "player_sad.png",
        "lines": [
            (None, "기말고사가 다가왔다. 장학금을 받으려면 무조건 A를 받아야 한다."),
            (None, "하지만 과제 폭탄 때문에 3일 연속 잠을 자지 못했다. 어떻게 밤을 지새울까?")
        ],
        "choices": [
            {"text": "1. 각성 드링크 제조. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"학점": 15, "멘탈": -25}, "next": "s2_w12_ch1_res"},
            {"text": "2. 상상관 수면실에서 딥슬립을 택한다.", "condition": None, "effects": {"학점": -8, "멘탈": 15}, "next": "s2_w12_ch2_res"},
            {"text": "3. 야간 PC방 밤샘 공부를 택한다. (소지금 10 이상)", "condition": lambda p: p.get("소지금") >= 10, "effects": {"학점": -15, "인간관계": 10, "멘탈": -10, "소지금": -8}, "next": "s2_w12_ch3_res"}
        ]
    },
    {
        "id": "s2_w12_ch1_res", "week": "2학기 12주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "엄청난 인위적 각성 효과로 알고리즘 소스코드를 뇌에 쑤셔 넣었다."),
            ("나", '"뇌가 강제로 풀가동되는 기분이다. 졸음이 완전히 달아났어."')
        ],
        "choices": [], "next": "s2_w13"
    },
    {
        "id": "s2_w12_ch2_res", "week": "2학기 12주차", "bg": "hall.png", "character": "player_normal.png",
        "lines": [
            (None, "눈을 뜨니 정신은 맑지만, 보지 못한 뒷부분이 머리를 스친다."),
            ("나", '"시험지 뒷장에 안 배운 알고리즘 나오면 어떡하지?"')
        ],
        "choices": [], "next": "s2_w13"
    },
    {
        "id": "s2_w12_ch3_res", "week": "2학기 12주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "PC방에서 시작은 좋았으나 옆자리 동기의 유혹에 마우스를 쥐고 말았다."),
            ("나", '"창밖으로 해가 뜨고 있네... 내 학점도 하늘로 뜨는구나."')
        ],
        "choices": [], "next": "s2_w13"
    },

    # ── 2학기 13주차 ──
    {
        "id": "s2_w13",
        "week": "2학기 13주차",
        "bg": "restaurant.png",
        "character": "player_normal.png",
        "lines": [
            (None, "고대하던 종강일! 동기들과 맥주를 마시는데 랩실 선배에게 전화가 왔다."),
            ("선배", '"지금 당장 3일만 라벨링 알바 대타 뛰어주면 40만 원 꽂아줄게! 할래?"'),
            (None, "어떻게 대답할까?")
        ],
        "choices": [
            {"text": "1. \"종강이고 뭐고 돈이 최고다!\" (소지금 10 이하)", "condition": lambda p: p.get("소지금") <= 10, "effects": {"멘탈": -15, "인간관계": -10, "소지금": 40}, "next": "s2_w13_ch1_res"},
            {"text": "2. \"1년 동안 구른 나에게 휴식을!\"", "condition": None, "effects": {"인간관계": 25, "멘탈": 20, "소지금": -10}, "next": "s2_w13_ch2_res"},
            {"text": "3. 동기에게 알바를 토스하고 얻어먹는다. (인간관계 50 이상)", "condition": lambda p: p.get("인간관계") >= 50, "effects": {"인간관계": 20, "멘탈": 10}, "next": "s2_w13_ch3_res"}
        ]
    },
    {
        "id": "s2_w13_ch1_res", "week": "2학기 13주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "피로를 참아가며 밤새 데이터와 코드를 만지고 40만 원을 손에 넣었다."),
            ("나", '"남들 놀 때 난 노예였지만... 지갑이 두툼하니 이게 행복이다."')
        ],
        "choices": [], "next": "s2_w14"
    },
    {
        "id": "s2_w13_ch2_res", "week": "2학기 13주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "제안을 단칼에 거절하고 동기들과 밤새도록 달렸다."),
            ("나", '"돈은 언제든 벌 수 있지! 다 같이 종강 축배 드는 게 진짜 대학 생활이야."')
        ],
        "choices": [], "next": "s2_w14"
    },
    {
        "id": "s2_w13_ch3_res", "week": "2학기 13주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "급전이 필요한 동기에게 토스했고, 동기는 고맙다며 1차 술값을 전액 결제했다."),
            ("나", '"이게 바로 상생 네트워크지. 도랑 치고 가재 잡고!"')
        ],
        "choices": [], "next": "s2_w14"
    },

    # ── 2학기 14주차 ──
    {
        "id": "s2_w14",
        "week": "2학기 14주차",
        "bg": "restaurant.png",
        "character": "player_normal.png",
        "lines": [
            (None, "드디어 1학년 2학기 공식 종강 총회! 술잔이 거침없이 오간다."),
            (None, "오늘 밤 나는 어떤 모습을 보여줄까?")
        ],
        "choices": [
            {"text": "1. 동기들과 찐하게 의리를 다진다. (멘탈 30 이상)", "condition": lambda p: p.get("멘탈") >= 30, "effects": {"인간관계": 25, "멘탈": 10, "소지금": -15}, "next": "s2_w14_ch1_res"},
            {"text": "2. 얌전히 도망친다.", "condition": None, "effects": {"학점": 3, "인간관계": 5, "멘탈": 5}, "next": "s2_w14_ch2_res"},
            {
                "text": "3. 분위기에 취해 교수님 어깨에 팔을 두른다?! (멘탈 50 이상)",
                "condition": lambda p: p.get("멘탈") >= 50,
                "random_branches": [
                    {"next": "s2_w14_ch3_success", "effects": {"인간관계": 30, "학점": 15}},
                    {"next": "s2_w14_ch3_fail", "effects": {"인간관계": 30, "학점": -25}}
                ]
            }
        ]
    },
    {
        "id": "s2_w14_ch1_res", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "1년 동안의 에피소드를 털어놓으며 동기들과 뜨겁게 다짐했다."),
            ("나", '"이 맛에 대학 다니지. 한 학기 스트레스가 싹 씻겨 내려간다!"')
        ],
        "choices": [], "next": "s2_w15"
    },
    {
        "id": "s2_w14_ch2_res", "week": "2학기 14주차", "bg": "campus.png", "character": "player_normal.png",
        "lines": [
            (None, "교수님과 선배들에게 폴더 인사를 남기고 깔끔하게 탈출했다."),
            ("나", '"술김에 실수하기 전에 먼저 튀길 진짜 잘했다."')
        ],
        "choices": [], "next": "s2_w15"
    },
    {
        "id": "s2_w14_ch3_success", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_happy.png",
        "lines": [
            (None, "교수님이 유쾌하게 껄껄 웃으시며 받아주셨고, 성적 창에는 기적의 최고 등급이 떴다."),
            ("나", '"형님 같은 교수님을 만나 제 새내기 라이프가... 읍읍" (동기들이 끌고 나감)')
        ],
        "choices": [], "next": "s2_w15"
    },
    {
        "id": "s2_w14_ch3_fail", "week": "2학기 14주차", "bg": "restaurant.png", "character": "player_sad.png",
        "lines": [
            (None, "교수님이 정색하며 손을 쳐내셨고, 며칠 뒤 성적표엔 자비 없는 F학점이 찍혔다."),
            ("나", '"다음 학기 재수강 라이프가 확정되었습니다..." (동기들이 입을 막고 끌고 나감)')
        ],
        "choices": [], "next": "s2_w15"
    },

    # ── 2학기 15주차 ──
    {
        "id": "s2_w15",
        "week": "2학기 15주차",
        "bg": "room.png",
        "character": "player_sad.png",
        "lines": [
            (None, "종합정보시스템에 성적 공람 창이 열렸다."),
            (None, "가장 공들였던 핵심 전공 과목 성적이 잔인한 'D+'로 찍혀 있다."),
            (None, "성적 정정 기간 마감 시계가 다가온다. 어떻게 이 위기를 돌파할까?")
        ],
        "choices": [
            {
                "text": "1. 눈물의 반성문 메일을 쏜다. (멘탈 25 이상) [성공 50% / 실패 50%]",
                "condition": lambda p: p.get("멘탈") >= 25,
                "random_branches": [
                    {"next": "s2_w15_ch1_success", "effects": {"학점": 5, "멘탈": -10}},
                    {"next": "s2_w15_ch1_fail", "effects": {"멘탈": -30}}
                ]
            },
            {"text": "2. 깨끗하게 패배를 인정하고 앱을 지운다.", "condition": None, "effects": {"학점": -5, "멘탈": 35}, "next": "s2_w15_ch2_res"},
            {"text": "3. 과탑 동기와 비교하며 이의신청 증거를 잡는다. (학점 50 이상)", "condition": lambda p: p.get("학점") >= 50, "effects": {"학점": 10, "멘탈": -15}, "next": "s2_w15_ch3_res"}
        ]
    },
    {
        "id": "s2_w15_ch1_success", "week": "2학기 15주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "절박한 서사와 감성 호소 메일을 보냈다."),
            (None, "기적적으로 교수님이 자비를 베풀어 성적을 C로 올려주셨다!")
        ],
        "choices": [], "next": "s2_w15_result"
    },
    {
        "id": "s2_w15_ch1_fail", "week": "2학기 15주차", "bg": "room.png", "character": "player_sad.png",
        "lines": [
            (None, "새로고침을 연타했지만 교수님의 답장은 오지 않았고 D+로 굳어졌다."),
            ("나", '"깊은 자괴감과 거절감이 파도처럼 밀려온다..."')
        ],
        "choices": [], "next": "s2_w15_result"
    },
    {
        "id": "s2_w15_ch2_res", "week": "2학기 15주차", "bg": "room.png", "character": "player_happy.png",
        "lines": [
            (None, "깔끔하게 재수강을 결심하며 앱을 통째로 삭제했다."),
            ("나", '"신나는 겨울방학인데 일단 놀고 보자!"')
        ],
        "choices": [], "next": "s2_w15_result"
    },
    {
        "id": "s2_w15_ch3_res", "week": "2학기 15주차", "bg": "room.png", "character": "player_normal.png",
        "lines": [
            (None, "논리 정연한 증거를 수집해 정식으로 이의신청을 제기했다."),
            ("나", '"오직 팩트와 논리, 코드로 내 정당한 학점을 받아내겠다."')
        ],
        "choices": [], "next": "s2_w15_result"
    },
    {
        "id": "s2_w15_result", "week": "2학기 15주차", "bg": "campus.png", "character": None,
        "lines": [
            (None, "이렇게 눈물과 웃음, 밤샘 코딩으로 가득했던 1학년 2학기 마지막 성적 공람이 끝났다.")
        ],
        "choices": [], "next": "s2_ending"
    },

    # ── 2학기 최종 엔딩 (조건 분기) ──
    {
        "id": "s2_ending",
        "week": "2학기 15주차 — 최종 결과",
        "bg": "campus.png",
        "character": None,
        "lines": [
            (None, "다사다난했던 1학년이 끝났다. 2학년은… 조금 더 나은 내가 되어 있기를!"),
            (None, "[ 1학년 최종 종합 결과 ]"),
        ],
        "choices": [],
        "next": "s2_end_star",
        "_ending_branch": True,
    },
    {
        "id": "s2_end_star", "week": "2학기 — 엔딩", "bg": "campus.png", "character": "player_happy.png",
        "lines": [
            (None, "【 빛나는 캠퍼스의 별 】"),
            (None, "우수한 성적으로 1학년을 마무리했다."),
            (None, "과제와 시험에 치이며 힘든 순간도 있었지만 끝까지 포기하지 않았다."),
            (None, "장학금 대상자로 선정되며 완벽한 새내기 라이프를 완성했다.")
        ],
        "choices": [], "next": None,
    },
    {
        "id": "s2_end_inssa", "week": "2학기 — 엔딩", "bg": "festival.png", "character": "player_happy.png",
        "lines": [
            (None, "【 한성대학교 핵인싸 】"),
            (None, "당신은 학교 곳곳에 친구가 있는 유명인이 되었다."),
            (None, "힘든 일이 생겨도 함께 고민해 줄 친구들이 곁에 있었다."),
            (None, "학점은 조금 아쉬웠지만, 누구보다 즐거운 1학년을 보냈다.")
        ],
        "choices": [], "next": None,
    },
    {
        "id": "s2_end_money", "week": "2학기 — 엔딩", "bg": "room.png", "character": "player_normal.png",
        "lines": [
            (None, "【 자본주의의 승리자 】"),
            (None, "남들이 놀 때도, 과제할 때도 당신은 알바를 했다."),
            (None, "어느새 통장에는 꽤 많은 돈이 모여 있었다."),
            (None, "누구보다 현실적이고 든든한 지갑을 가진 대학생이 되었다.")
        ],
        "choices": [], "next": None,
    },
    {
        "id": "s2_end_okay", "week": "2학기 — 엔딩", "bg": "campus.png", "character": "player_normal.png",
        "lines": [
            (None, "【 그래도 괜찮은 1학년 】"),
            (None, "특별히 뛰어난 성적을 받지도, 부자가 되지도 않았지만,"),
            (None, "좋은 기억도, 아쉬운 기억도 모두 훌륭한 자양분이 되었다."),
            (None, "내년 2학년에는 어떤 일이 기다리고 있을까?")
        ],
        "choices": [], "next": None,
    },
]

# ─── 빠른 조회용 딕셔너리 ───────────────────────────────────
SCENE_MAP = {s["id"]: s for s in SCENES}

# ─── 2학기 엔딩 분기 조건 ────────────────────────────────────
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
        "condition": lambda p: True,
    },
]

# ─── 빠른 조회용 딕셔너리 (반드시 대본이 끝