# main.py — 한성대학교 신입생 생존기 (Pygame 비주얼 노벨)
import os
import random
import sys

import pygame

from player import Player
from story import ENDINGS_S2, SCENE_MAP


SCREEN_W, SCREEN_H = 1280, 720
FPS = 60
WEEK_TRANSITION_DURATION_MS = 2000

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BG_DIR = os.path.join(BASE_DIR, "assets", "backgrounds")
CHAR_DIR = os.path.join(BASE_DIR, "assets", "characters")

C_BG_FALLBACK = (30, 34, 50)
C_DIALOG_BG = (15, 18, 35, 220)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 220, 80)
C_GRAY = (160, 160, 175)
C_DARK = (20, 20, 35)
C_CHOICE_IDLE = (30, 38, 70, 200)
C_CHOICE_HOV = (60, 90, 160, 230)
C_CHOICE_DIS = (30, 30, 45, 140)
C_STAT_BAR_BG = (40, 40, 60)
C_ACCENT = (80, 160, 255)

FINAL_ENDING_IDS = {"s2_end_star", "s2_end_inssa", "s2_end_money", "s2_end_okay"}

LOCATION_LABELS = {
    "campus.png": "한성대학교 캠퍼스",
    "room.png": "자취방",
    "hall.png": "입학식 강당",
    "clubbooth.png": "동아리 박람회",
    "classroom.png": "강의실",
    "library.png": "도서관",
    "cafe.png": "카페",
    "restaurant.png": "삼선교 포차",
    "festival.png": "한성대학교 대동제",
    "sangsang.png": "상상관 앞",
    "lab.png": "전공 실습실",
    "pcbang.png": "PC방",
}

KOR_FONT_CANDIDATES = [
    "C:/Windows/Fonts/malgun.ttf",
    "C:/Windows/Fonts/gulim.ttc",
    "/Library/Fonts/AppleGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
]


def find_kor_font():
    for path in KOR_FONT_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def load_font(size, bold=False):
    path = find_kor_font()
    if path:
        try:
            return pygame.font.Font(path, size)
        except Exception:
            pass
    return pygame.font.SysFont("malgungothic,applegothic,nanumgothic,sans", size, bold=bold)


def load_image(folder, filename, size=None):
    if not filename:
        return None
    path = os.path.join(folder, filename)
    if not os.path.exists(path):
        return None
    try:
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        return img
    except Exception:
        return None


def draw_rect_alpha(surface, color, rect, radius=0):
    temp = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    if radius > 0:
        pygame.draw.rect(temp, color, (0, 0, rect[2], rect[3]), border_radius=radius)
    else:
        temp.fill(color)
    surface.blit(temp, (rect[0], rect[1]))


def wrap_text(text, font, max_width):
    lines = []
    current = ""
    for ch in text:
        test = current + ch
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def draw_hud(surface, player, fonts):
    stat_order = ["학점", "멘탈", "인간관계", "소지금"]
    colors = {
        "학점": (80, 180, 255),
        "멘탈": (120, 220, 100),
        "인간관계": (255, 160, 80),
        "소지금": (255, 220, 60),
    }
    x, y = SCREEN_W - 210, 16
    bar_w, bar_h = 160, 12
    gap = 44
    sm = fonts["sm"]

    for name in stat_order:
        val = player.get(name)
        surface.blit(sm.render(name, True, C_GRAY), (x, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (x, y + 14, bar_w, bar_h), border_radius=4)
        fill_w = int(bar_w * val / 100)
        if fill_w > 0:
            pygame.draw.rect(surface, colors[name], (x, y + 14, fill_w, bar_h), border_radius=4)
        surface.blit(sm.render(str(val), True, C_WHITE), (x + bar_w + 6, y + 12))
        y += gap

    if player.has_flag("동아리_가입"):
        surface.blit(sm.render("동아리", True, (180, 130, 255)), (x, y + 4))
        y += gap
    friend_chance = player.flags.get("친구_찬스", 0)
    if friend_chance > 0:
        surface.blit(sm.render(f"친구찬스 x{friend_chance}", True, (100, 220, 180)), (x, y + 4))


DIALOG_H = 200
DIALOG_Y = SCREEN_H - DIALOG_H - 10
DIALOG_X = 30
DIALOG_W = SCREEN_W - 250


def draw_dialog(surface, speaker, text, fonts, anim_chars):
    draw_rect_alpha(surface, C_DIALOG_BG, (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H), radius=12)
    pygame.draw.rect(surface, C_ACCENT, (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H), 2, border_radius=12)

    pad = 20
    inner_w = DIALOG_W - pad * 2
    text_y = DIALOG_Y + 50 if speaker else DIALOG_Y + 20

    if speaker:
        surface.blit(fonts["md"].render(f"【 {speaker} 】", True, C_YELLOW), (DIALOG_X + pad, DIALOG_Y + 12))

    visible = text[:anim_chars]
    for line in wrap_text(visible, fonts["body"], inner_w)[:4]:
        surface.blit(fonts["body"].render(line, True, C_WHITE), (DIALOG_X + pad, text_y))
        text_y += fonts["body"].get_linesize() + 4

    if anim_chars >= len(text):
        hint = fonts["sm"].render("▶ 클릭 또는 Space", True, C_GRAY)
        surface.blit(hint, (DIALOG_X + DIALOG_W - hint.get_width() - pad, DIALOG_Y + DIALOG_H - 28))


CHOICE_X = 60
CHOICE_W = SCREEN_W - 120
CHOICE_H = 56
CHOICE_GAP = 10


def draw_choices(surface, choices, player, fonts, mouse_pos):
    total = len(choices)
    start_y = SCREEN_H // 2 - (total * (CHOICE_H + CHOICE_GAP)) // 2
    draw_rect_alpha(surface, (0, 0, 0, 160), (0, 0, SCREEN_W, SCREEN_H))

    hovered = -1
    for i, choice in enumerate(choices):
        ry = start_y + i * (CHOICE_H + CHOICE_GAP)
        rect = pygame.Rect(CHOICE_X, ry, CHOICE_W, CHOICE_H)
        cond = choice.get("condition")
        enabled = cond is None or cond(player)

        if not enabled:
            col, text_col = C_CHOICE_DIS, C_GRAY
        elif rect.collidepoint(mouse_pos):
            col, text_col = C_CHOICE_HOV, C_WHITE
            hovered = i
        else:
            col, text_col = C_CHOICE_IDLE, C_WHITE

        draw_rect_alpha(surface, col, (rect.x, rect.y, rect.w, rect.h), radius=10)
        pygame.draw.rect(surface, C_ACCENT if enabled else C_GRAY, rect, 2, border_radius=10)

        label = fonts["body"].render(choice["text"], True, text_col)
        surface.blit(label, (rect.x + (rect.w - label.get_width()) // 2, rect.y + (rect.h - label.get_height()) // 2))

        if not enabled:
            lock = fonts["sm"].render("(조건 미충족)", True, (160, 80, 80))
            surface.blit(lock, (rect.x + rect.w - lock.get_width() - 12, rect.y + (rect.h - lock.get_height()) // 2))

    return hovered


def get_ending_title(scene_id):
    for ending in ENDINGS_S2:
        if ending["id"] == scene_id:
            return ending["name"]
    return "1학년 마무리"


def draw_ending(surface, player, fonts, ending_id=None):
    surface.fill(C_DARK)
    title_text = get_ending_title(ending_id) if ending_id else "1학기 종료"
    title = fonts["title"].render(f"【 {title_text} 】", True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 60))

    grade = player.grade()
    grade_col = {
        "A+": (255, 215, 0),
        "A": (200, 255, 100),
        "B+": (100, 200, 255),
        "B": (120, 200, 220),
        "C+": (200, 160, 80),
        "C": (180, 100, 80),
    }.get(grade, C_WHITE)
    g_surf = fonts["title"].render(f"최종 학점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 140))

    stat_names = ["학점", "멘탈", "인간관계", "소지금"]
    colors = [(80, 180, 255), (120, 220, 100), (255, 160, 80), (255, 220, 60)]
    y = 230
    bar_w = 400
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        surface.blit(fonts["md"].render(f"{name}  {val}/100", True, C_WHITE), (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        fill_w = int(bar_w * val / 100)
        if fill_w > 0:
            pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, fill_w, 18), border_radius=6)
        y += 70

    msgs = []
    if player.get("학점") >= 80:
        msgs.append("학업을 성실하게 해낸 한 학년이었다!")
    elif player.get("학점") < 50:
        msgs.append("학점이 아쉽다. 다음엔 더 노력하자.")
    if player.get("멘탈") < 30:
        msgs.append("멘탈이 많이 닳았다. 스스로를 돌봐야 해.")
    if player.get("인간관계") >= 70:
        msgs.append("사람들과 좋은 관계를 쌓은 한 해!")
    if player.get("소지금") >= 80:
        msgs.append("통장이 꽤 두툼해졌다.")
    if not msgs:
        msgs.append("평범하지만 나쁘지 않은 1학년이었다.")

    for i, msg in enumerate(msgs):
        msg_surf = fonts["sm"].render(msg, True, C_GRAY)
        surface.blit(msg_surf, (SCREEN_W // 2 - msg_surf.get_width() // 2, y + i * 28))

    hint = fonts["sm"].render("[ 클릭 또는 Space 로 종료 ]", True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))


def draw_semester_result(surface, player, fonts, semester_title="1학기 결과"):
    surface.fill(C_DARK)
    title = fonts["title"].render(f"【 {semester_title} 】", True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 50))

    grade = player.grade()
    grade_col = {
        "A+": (255, 215, 0),
        "A": (200, 255, 100),
        "B+": (100, 200, 255),
        "B": (120, 200, 220),
        "C+": (200, 160, 80),
        "C": (180, 100, 80),
    }.get(grade, C_WHITE)

    g_surf = fonts["title"].render(f"학점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 130))

    g_detail = fonts["md"].render(f"({player.get('학점')}/100)", True, C_WHITE)
    surface.blit(g_detail, (SCREEN_W // 2 - g_detail.get_width() // 2, 180))

    stat_names = ["멘탈", "인간관계", "소지금"]
    colors = [(120, 220, 100), (255, 160, 80), (255, 220, 60)]
    y = 240
    bar_w = 450
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        surface.blit(fonts["md"].render(f"{name}  {val}/100", True, C_WHITE), (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 22), border_radius=6)
        fill_w = int(bar_w * val / 100)
        if fill_w > 0:
            pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, fill_w, 22), border_radius=6)
        y += 75

    msgs = []
    if player.get("학점") >= 80:
        msgs.append("학업을 성실하게 해낸 한 학기였다!")
    elif player.get("학점") < 50:
        msgs.append("학점이 아쉽다. 다음엔 더 노력하자.")
    if player.get("멘탈") < 30:
        msgs.append("멘탈이 많이 닳았다. 스스로를 돌봐야 해.")
    if player.get("인간관계") >= 70:
        msgs.append("사람들과 좋은 관계를 쌓은 한 학기!")
    if player.get("소지금") >= 80:
        msgs.append("통장이 꽤 두툼해졌다.")
    if not msgs:
        msgs.append("평범하지만 나쁘지 않은 한 학기였다.")

    for i, msg in enumerate(msgs):
        msg_surf = fonts["sm"].render(msg, True, C_GRAY)
        surface.blit(msg_surf, (SCREEN_W // 2 - msg_surf.get_width() // 2, y + i * 28))

    hint = fonts["sm"].render("[ 클릭 또는 Space 로 계속 ]", True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))


def split_week_label(week_str, scene_id=None):
    if not week_str:
        return ""

    base_week = week_str.split("—", 1)[0].strip()

    if base_week.startswith("1학기 ") or base_week.startswith("2학기 "):
        return base_week

    if scene_id and scene_id.startswith("s2_"):
        return f"2학기 {base_week}"

    return f"1학기 {base_week}"


def draw_week_label(surface, week_str, fonts, scene_id=None, bg_name=""):
    if not week_str:
        return

    display_text = split_week_label(week_str, scene_id)

    week_lbl = fonts["md"].render(display_text, True, C_YELLOW)
    draw_rect_alpha(surface, (0, 0, 0, 160), (10, 10, week_lbl.get_width() + 20, week_lbl.get_height() + 10), radius=6)
    surface.blit(week_lbl, (20, 14))

    location_text = LOCATION_LABELS.get(bg_name, "")
    if location_text:
        location_lbl = fonts["sm"].render(location_text, True, (200, 200, 220))
        location_x = week_lbl.get_width() + 40
        draw_rect_alpha(
            surface,
            (0, 0, 0, 160),
            (location_x, 10, location_lbl.get_width() + 20, location_lbl.get_height() + 10),
            radius=6,
        )
        surface.blit(location_lbl, (location_x + 10, 14))


def pick_random_outcome(outcomes):
    r = random.random()
    acc = 0.0
    for outcome in outcomes:
        acc += outcome.get("weight", 1.0 / len(outcomes))
        if r <= acc:
            return outcome
    return outcomes[-1]


def apply_scene_enter_effects(scene, player):
    if "effects_on_enter" in scene:
        player.apply(**scene["effects_on_enter"])

    if "flags_on_enter" in scene:
        for key, value in scene["flags_on_enter"].items():
            if key == "친구_찬스":
                player.add_friend_chance(value)
            else:
                player.flags[key] = value

    if "effects_on_enter_cond" in scene:
        cond_data = scene["effects_on_enter_cond"]
        effects = cond_data["true_effects"] if cond_data["condition"](player) else cond_data["false_effects"]
        player.apply(**effects)


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("한성대학교 신입생 생존기")
    clock = pygame.time.Clock()

    fonts = {
        "title": load_font(48, bold=True),
        "md": load_font(26, bold=True),
        "body": load_font(22),
        "sm": load_font(17),
    }

    bg_cache = {}
    char_cache = {}

    def get_bg(name):
        if name not in bg_cache:
            bg_cache[name] = load_image(BG_DIR, name, (SCREEN_W, SCREEN_H))
        return bg_cache[name]

    def get_char(name):
        if name not in char_cache:
            char_cache[name] = load_image(CHAR_DIR, name, (360, 540))
        return char_cache[name]

    player = Player()
    scene_id = "title"
    state = "dialog"
    ending_id = None
    last_week = ""

    week_transition_active = False
    week_transition_alpha = 0
    week_transition_text = ""
    week_transition_start_time = 0

    result_screen_start_time = 0
    result_screen_wait_duration = 3000

    scene = SCENE_MAP[scene_id]
    line_idx = 0
    anim_chars = 0
    anim_speed = 2
    anim_done = False

    def apply_week_decay(week_str):
        nonlocal last_week, week_transition_active, week_transition_text
        nonlocal week_transition_alpha, week_transition_start_time

        if not week_str or week_str == last_week:
            return

        if last_week:
            player.apply(멘탈=-5)
            week_transition_active = True
            week_transition_alpha = 255
            week_transition_text = split_week_label(week_str, scene_id)
            week_transition_start_time = pygame.time.get_ticks()

        last_week = week_str

    def resolve_next_scene_id():
        special = scene.get("_special")
        cond = scene.get("_condition")
        if special and cond and cond(player):
            return special
        return scene.get("next")

    def load_scene(sid):
        nonlocal scene, line_idx, anim_chars, anim_done, state, scene_id
        nonlocal ending_id, result_screen_start_time

        scene_id = sid
        scene = SCENE_MAP[sid]
        apply_scene_enter_effects(scene, player)
        apply_week_decay(scene.get("week", ""))

        line_idx = 0
        anim_chars = 0
        anim_done = False

        if scene["id"] == "s1_result":
            state = "semester_result"
            result_screen_start_time = pygame.time.get_ticks()
            return

        if scene.get("_ending_branch"):
            for ending in ENDINGS_S2:
                if ending["condition"](player):
                    load_scene(ending["id"])
                    return
            load_scene("s2_end_okay")
            return

        if not scene.get("lines") and not scene.get("choices"):
            advance_scene()
            return

        if scene["id"] in FINAL_ENDING_IDS:
            state = "dialog"
        elif scene.get("choices") and not scene.get("lines"):
            state = "choices"
        else:
            state = "dialog"

    def advance_scene():
        nonlocal state, ending_id

        next_id = resolve_next_scene_id()
        if next_id is None:
            if scene["id"] in FINAL_ENDING_IDS:
                ending_id = scene["id"]
                state = "ending"
                return
            pygame.quit()
            sys.exit()

        load_scene(next_id)

    def apply_choice(choice):
        if choice.get("force_friend_chance"):
            player.use_friend_chance()
        elif choice.get("use_friend_chance") and not player.check("인간관계", 40):
            player.use_friend_chance()

        player.apply(**choice.get("effects", {}))

        for key, value in choice.get("flags", {}).items():
            if key == "친구_찬스":
                player.add_friend_chance(value)
            else:
                player.flags[key] = value

        if choice.get("random_outcomes"):
            outcome = pick_random_outcome(choice["random_outcomes"])
            player.apply(**outcome.get("effects", {}))
            load_scene(outcome["next"])
        else:
            load_scene(choice["next"])

    def next_line_or_advance():
        nonlocal line_idx, anim_chars, anim_done, state

        if scene.get("lines") and line_idx < len(scene["lines"]) - 1:
            line_idx += 1
            anim_chars = 0
            anim_done = False
            return

        if scene.get("choices"):
            state = "choices"
        else:
            advance_scene()

    hovered_choice = -1
    load_scene(scene_id)

    while True:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if state == "ending":
                    pygame.quit()
                    sys.exit()
                if state == "semester_result":
                    current_time = pygame.time.get_ticks()
                    if current_time - result_screen_start_time >= result_screen_wait_duration:
                        advance_scene()
                elif state == "dialog":
                    if not anim_done:
                        anim_chars = 9999
                        anim_done = True
                    else:
                        next_line_or_advance()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "ending":
                    pygame.quit()
                    sys.exit()
                elif state == "semester_result":
                    current_time = pygame.time.get_ticks()
                    if current_time - result_screen_start_time >= result_screen_wait_duration:
                        advance_scene()
                elif state == "dialog":
                    if not anim_done:
                        anim_chars = 9999
                        anim_done = True
                    else:
                        next_line_or_advance()
                elif state == "choices" and hovered_choice >= 0:
                    choice = scene["choices"][hovered_choice]
                    cond = choice.get("condition")
                    if cond is None or cond(player):
                        apply_choice(choice)

        if state == "dialog" and scene.get("lines") and not anim_done:
            _, text = scene["lines"][line_idx]
            anim_chars += anim_speed
            if anim_chars >= len(text):
                anim_chars = len(text)
                anim_done = True

        if week_transition_active:
            elapsed = pygame.time.get_ticks() - week_transition_start_time
            fade_start = int(WEEK_TRANSITION_DURATION_MS * 0.8)
            if elapsed >= WEEK_TRANSITION_DURATION_MS:
                week_transition_active = False
                week_transition_alpha = 0
            elif elapsed >= fade_start:
                fade_progress = (elapsed - fade_start) / (WEEK_TRANSITION_DURATION_MS - fade_start)
                week_transition_alpha = int(220 * (1 - fade_progress))
            else:
                week_transition_alpha = 220

        bg = get_bg(scene.get("bg", ""))
        screen.blit(bg, (0, 0)) if bg else screen.fill(C_BG_FALLBACK)

        char_name = scene.get("character")
        if char_name:
            char_img = get_char(char_name)
            if char_img:
                cx = SCREEN_W // 2 - char_img.get_width() // 2
                cy = SCREEN_H - char_img.get_height() - DIALOG_H - 20
                screen.blit(char_img, (cx, cy))

        draw_hud(screen, player, fonts)
        draw_week_label(screen, scene.get("week", ""), fonts, scene_id, scene.get("bg", ""))

        if week_transition_active:
            transition_surface = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            transition_surface.fill((0, 0, 0, week_transition_alpha))
            screen.blit(transition_surface, (0, 0))

            trans_text = fonts["title"].render(week_transition_text, True, C_YELLOW)
            trans_text.set_alpha(min(255, week_transition_alpha + 35))
            screen.blit(trans_text, (SCREEN_W // 2 - trans_text.get_width() // 2, SCREEN_H // 2 - trans_text.get_height() // 2))

        if state == "dialog" and scene.get("lines"):
            speaker, text = scene["lines"][line_idx]
            if scene["id"] == "s1_result" and "[ 1학기 최종 결과 ]" in text:
                text = (
                    f"[ 1학기 최종 결과 ]\n"
                    f"학점 {player.grade()} ({player.get('학점')}/100) · "
                    f"멘탈 {player.get('멘탈')} · "
                    f"인간관계 {player.get('인간관계')} · "
                    f"소지금 {player.get('소지금')}"
                )
            if scene["id"] == "s2_ending" and "[ 2학기 최종 결과 ]" in text:
                text = (
                    f"[ 1학년 최종 결과 ]\n"
                    f"학점 {player.grade()} ({player.get('학점')}/100) · "
                    f"멘탈 {player.get('멘탈')} · "
                    f"인간관계 {player.get('인간관계')} · "
                    f"소지금 {player.get('소지금')}"
                )
            draw_dialog(screen, speaker, text, fonts, anim_chars)
        elif state == "choices":
            if scene.get("lines"):
                speaker, text = scene["lines"][-1]
                draw_dialog(screen, speaker, text, fonts, len(text))
            hovered_choice = draw_choices(screen, scene["choices"], player, fonts, mouse_pos)
        elif state == "semester_result":
            draw_semester_result(screen, player, fonts, "1학기 결과")
            current_time = pygame.time.get_ticks()
            wait_remaining = max(0, result_screen_wait_duration - (current_time - result_screen_start_time))
            if wait_remaining > 0:
                wait_text = fonts["sm"].render(f"결과 확인까지 {wait_remaining // 100 + 1}초...", True, (255, 100, 100))
                screen.blit(wait_text, (SCREEN_W // 2 - wait_text.get_width() // 2, SCREEN_H - 90))
        elif state == "ending":
            draw_ending(screen, player, fonts, ending_id)

        pygame.display.flip()


if __name__ == "__main__":
    main()