# main.py — 한성대학교 신입생 생존기 (UI/UX 완성형 마스터 마운트)
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
SOUND_DIR = os.path.join(BASE_DIR, "assets", "sound")

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
BGM_FILENAME = "main_bgm.mp3"

# ─────────────────────────────────────────────────────────────
DIALOG_H = 200
DIALOG_Y = SCREEN_H - DIALOG_H - 10
DIALOG_X = 30
DIALOG_W = SCREEN_W - 250
# ─────────────────────────────────────────────────────────────

CHOICE_X = 60
CHOICE_W = SCREEN_W - 120
CHOICE_H = 56
CHOICE_GAP = 10

LOCATION_LABELS = {
    "title_bg.jpg": "한성대학교 전경",
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
    raw_paragraphs = text.split("\n")
    for paragraph in raw_paragraphs:
        current = ""
        for ch in paragraph:
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


def get_average_brightness(surface, rect):
    try:
        sub_surf = surface.subsurface(rect)
        avg_col = pygame.transform.average_color(sub_surf)
        brightness = 0.299 * avg_col[0] + 0.587 * avg_col[1] + 0.114 * avg_col[2]
        return brightness
    except Exception:
        return 120


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
    if not week_str or scene_id == "title":  
        return
    display_text = split_week_label(week_str, scene_id)
    
    lbl_brightness = get_average_brightness(surface, (10, 10, 200, 40))
    is_light = lbl_brightness >= 135
    
    txt_col = (20, 25, 35) if is_light else C_YELLOW
    loc_col = (70, 75, 90) if is_light else (200, 200, 220)
    box_col = (220, 220, 230, 160) if is_light else (0, 0, 0, 160)

    week_lbl = fonts["md"].render(display_text, True, txt_col)
    draw_rect_alpha(surface, box_col, (10, 10, week_lbl.get_width() + 20, week_lbl.get_height() + 10), radius=6)
    surface.blit(week_lbl, (20, 14))

    location_text = LOCATION_LABELS.get(bg_name, "")
    if location_text:
        location_lbl = fonts["sm"].render(location_text, True, loc_col)
        location_x = week_lbl.get_width() + 40
        draw_rect_alpha(surface, box_col, (location_x, 10, location_lbl.get_width() + 20, location_lbl.get_height() + 10), radius=6)
        surface.blit(location_lbl, (location_x + 10, 14))


def draw_hud(surface, player, fonts):
    stat_order = ["학점", "멘탈", "인간관계", "소지금"]
    colors = {
        "학점": (50, 150, 255),
        "멘탈": (40, 200, 100),
        "인간관계": (255, 130, 50),
        "소지금": (255, 210, 40)
    }
    
    x, y = SCREEN_W - 220, 20
    bar_w, bar_h = 160, 10
    gap = 58 
    sm = fonts["sm"]

    hud_brightness = get_average_brightness(surface, (x - 10, y - 10, bar_w + 30, 240))
    is_light_bg = hud_brightness >= 135
    
    txt_main_color = (25, 28, 40) if is_light_bg else C_WHITE
    txt_sub_color = (80, 85, 105) if is_light_bg else C_GRAY

    draw_rect_alpha(surface, (20, 25, 40, 60 if is_light_bg else 140), (x - 12, y - 10, bar_w + 24, 245), radius=8)

    # 250ms 주기로 깜빡임 플래그 연산
    blink_state = (pygame.time.get_ticks() // 250) % 2 == 0

    for name in stat_order:
        val = player.get(name)
        
        # 스탯이 20 이하일 때 실시간 깜빡임 컬러 동적 스와이프
        if val <= 20 and blink_state:
            current_main_color = (255, 50, 50)
            current_bar_color = (255, 30, 30)
        else:
            current_main_color = txt_main_color
            current_bar_color = colors[name]

        surface.blit(sm.render(name, True, txt_sub_color), (x, y))
        
        if name == "소지금":
            val_surf = sm.render(f"{val * 1000:,}원", True, current_main_color)
            surface.blit(val_surf, (x + bar_w - val_surf.get_width(), y))
            pygame.draw.rect(surface, (180, 180, 195) if is_light_bg else C_STAT_BAR_BG, (x, y + 20, bar_w, bar_h), border_radius=4)
            pygame.draw.rect(surface, current_bar_color, (x, y + 20, bar_w, bar_h), border_radius=4)
        else:
            val_surf = sm.render(str(val), True, current_main_color)
            surface.blit(val_surf, (x + bar_w - val_surf.get_width(), y))
            pygame.draw.rect(surface, (180, 180, 195) if is_light_bg else C_STAT_BAR_BG, (x, y + 20, bar_w, bar_h), border_radius=4)
            fill_w = int(bar_w * val / 100)
            if fill_w > 0:
                pygame.draw.rect(surface, current_bar_color, (x, y + 20, fill_w, bar_h), border_radius=4)
                
        y += gap

    if player.has_flag("동아리_가입"):
        surface.blit(sm.render("동아리 가입됨", True, (120, 60, 220) if is_light_bg else (190, 160, 255)), (x, y))
        y += 24
    friend_chance = player.flags.get("friend_chance", 0) or player.flags.get("친구_찬스", 0)
    if friend_chance > 0:
        surface.blit(sm.render(f"친구찬스 x{friend_chance}", True, (10, 140, 100) if is_light_bg else (100, 220, 180)), (x, y))


def draw_dialog(surface, speaker, text, fonts, anim_chars):
    bg_brightness = get_average_brightness(surface, (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H))
    box_alpha = 245 if bg_brightness >= 140 else 200
    draw_rect_alpha(surface, (12, 14, 28, box_alpha), (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H), radius=12)
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


def draw_ending(surface, player, fonts, ending_id=None):
    surface.fill(C_DARK)
    title_text = get_ending_title(ending_id) if ending_id else "1학년 종료"
    title = fonts["title"].render(f"【 엔딩: {title_text} 】", True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 60))

    grade = player.grade()
    grade_col = {
        "A+": (255, 215, 0), "A": (200, 255, 100), "B+": (100, 200, 255),
        "B": (120, 200, 220), "C+": (200, 160, 80), "C": (180, 100, 80),
    }.get(grade, C_WHITE)
    g_surf = fonts["title"].render(f"최종 학점 평점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 140))

    stat_names = ["학점", "멘탈", "인간관계", "소지금"]
    colors = [(80, 180, 255), (120, 220, 100), (255, 160, 80), (255, 210, 40)]
    y = 230
    bar_w = 400
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        surface.blit(fonts["md"].render(f"{name}  {val}/100" if name != "소지금" else f"{name}  {val*1000:,}원", True, C_WHITE), (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        
        if name == "소지금":
            pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        else:
            fill_w = int(bar_w * val / 100)
            if fill_w > 0:
                pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, fill_w, 18), border_radius=6)
        y += 70

    msgs = []
    if player.get("학점") >= 80:
        msgs.append("학업을 대단히 성실하게 해낸 보람찬 한 해였다!")
    elif player.get("학점") < 50:
        msgs.append("학점이 아쉽다. 학사경고를 피하기 위해 다음 학기엔 힘내자.")
    if player.get("멘탈") < 30:
        msgs.append("낙산벌의 지옥 경사로에 심신이 완전히 닳았다. 가출한 멘탈을 치유하자.")
    if player.get("인간관계") >= 70:
        msgs.append("삼선교 포차 거리의 전설이 되었다. 든든한 동기들과 함께한 한 해!")
    if player.get("소지금") >= 80:
        msgs.append("통장이 꽤 두툼해졌다. 방학 알바 40만 원의 위력일까?")
    if not msgs:
        msgs.append("평범하지만 무난하게 보낸 1학년 신입생 라이프였다.")

    for i, msg in enumerate(msgs):
        msg_surf = fonts["sm"].render(msg, True, C_GRAY)
        surface.blit(msg_surf, (SCREEN_W // 2 - msg_surf.get_width() // 2, y + i * 28))

    hint = fonts["sm"].render("[ 클릭 또는 Space 로 종료 ]", True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))


def draw_semester_result(surface, player, fonts, semester_title="1학기 결과"):
    surface.fill(C_DARK)
    title = fonts["title"].render(f"【 {semester_title} 】", True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 60))

    grade = player.grade()
    grade_col = {
        "A+": (255, 215, 0), "A": (200, 255, 100), "B+": (100, 200, 255),
        "B": (120, 200, 220), "C+": (200, 160, 80), "C": (180, 100, 80),
    }.get(grade, C_WHITE)
    g_surf = fonts["title"].render(f"현재 학점 평점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 140))

    stat_names = ["학점", "멘탈", "인간관계", "소지금"]
    colors = [(80, 180, 255), (120, 220, 100), (255, 160, 80), (255, 210, 40)]
    y = 230
    bar_w = 400
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        surface.blit(fonts["md"].render(f"{name}  {val}/100" if name != "소지금" else f"{name}  {val*1000:,}원", True, C_WHITE), (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        
        if name == "소지금":
            pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        else:
            fill_w = int(bar_w * val / 100)
            if fill_w > 0:
                pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, fill_w, 18), border_radius=6)
        y += 70

    msgs = []
    if player.get("학점") >= 80:
        msgs.append("학업을 대단히 성실하게 해낸 1학기였다!")
    elif player.get("학점") < 50:
        msgs.append("학점이 아쉽다. 2학기엔 학점을 반드시 복구하자.")
    if player.get("멘탈") < 30:
        msgs.append("멘탈이 많이 닳았다. 방학 동안 치유가 필요해.")
    if player.get("인간관계") >= 70:
        msgs.append("사람들과 좋은 관계를 쌓은 1학기!")
    if player.get("소지금") >= 80:
        msgs.append("통장이 꽤 두툼해졌다.")
    if not msgs:
        msgs.append("평범하지만 나쁘지 않은 1학기였다.")

    for i, msg in enumerate(msgs):
        msg_surf = fonts["sm"].render(msg, True, C_GRAY)
        surface.blit(msg_surf, (SCREEN_W // 2 - msg_surf.get_width() // 2, y + i * 28))

    hint = fonts["sm"].render("[ 클릭 또는 Space 로 계속 ]", True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))


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
    try:
        pygame.mixer.pre_init(44100, -16, 2, 512)
    except Exception:
        pass
    pygame.init()
    
    bgm_volume = 0.4

    try:
        pygame.mixer.init()
        bgm_path = os.path.join(SOUND_DIR, BGM_FILENAME)
        if os.path.exists(bgm_path):
            pygame.mixer.music.load(bgm_path)
            pygame.mixer.music.set_volume(bgm_volume)
            pygame.mixer.music.play(-1)
        else:
            print(f"[경고] BGM 파일을 찾을 수 없습니다: {bgm_path}")
    except Exception as e:
        print(f"오디오 가동 불능: {e}")

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
    result_screen_wait_duration = 1500

    show_help = False

    scene = SCENE_MAP[scene_id]
    line_idx = 0
    anim_chars = 0
    anim_speed = 3
    anim_done = False

    floating_texts = []

    def spawn_floating_texts(effects):
        """[고도화] 스탯 팝업의 명료성을 높이고 유지시간을 1초 더 연장하여 정밀 바인딩합니다."""
        if not effects: return
        
        stat_indices = {"학점": 0, "멘탈": 1, "인간관계": 2, "소지금": 3}
        
        for stat, val in effects.items():
            if val == 0 or stat not in stat_indices: continue
            
            idx = stat_indices[stat]
            bind_x = SCREEN_W - 245 # 게이지 바 왼쪽 한계선에 극도로 밀착 바인딩
            bind_y = 20 + (idx * 58) 
            
            color = (120, 255, 120) if val > 0 else (255, 100, 100)
            sign = "+" if val > 0 else ""
            
            # [수정 사안] 무엇이 오르고 내렸는지 정확하게 스탯 이름 접두사 빌드 결합
            if stat == "소지금":
                txt_str = f"소지금 {sign}{val * 1000:,}원"
            else:
                txt_str = f"{stat} {sign}{val}"
            
            floating_texts.append({
                "text": txt_str, "color": color, "x": bind_x, "y": bind_y,
                "alpha": 255, "target_x": bind_x - 20, 
                "life": 150, # 90프레임에서 150프레임(2.5초)으로 표기 유지 시간 1초 연장 처리
                "delay": 0
            })

    def apply_week_decay(week_str):
        nonlocal last_week, week_transition_active, week_transition_text
        nonlocal week_transition_alpha, week_transition_text

        if not week_str or week_str == last_week:
            return
        if last_week:
            # --- 수정된 부분: 매주 멘탈 차감 및 팝업 기능 제거 ---
            # player.apply(멘탈=-5)
            # spawn_floating_texts({"멘탈": -5})
            # ----------------------------------------------------
            
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

        if scene.get("_ending_branch"):
            for ending in ENDINGS_S2:
                if ending["condition"](player):
                    load_scene(ending["id"])
                    return
            load_scene("s2_end_okay")
            return

        next_id = resolve_next_scene_id()
        if next_id is None:
            if scene["id"] in FINAL_ENDING_IDS:
                ending_id = scene["id"]
                state = "ending"
                return
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        load_scene(next_id)

    def apply_choice(choice):
        if choice.get("force_friend_chance"):
            player.use_friend_chance()
        elif choice.get("use_friend_chance") and not player.check("인간관계", 40):
            player.use_friend_chance()

        for key, value in choice.get("flags", {}).items():
            if key == "친구_찬스":
                player.add_friend_chance(value)
            else:
                player.flags[key] = value

        if choice.get("random_outcomes"):
            outcome = pick_random_outcome(choice["random_outcomes"])
            spawn_floating_texts(outcome.get("effects", {}))
            player.apply(**outcome.get("effects", {}))
            load_scene(outcome["next"])
        else:
            spawn_floating_texts(choice.get("effects", {}))
            player.apply(**choice.get("effects", {}))
            load_scene(choice["next"])
            
        pygame.time.wait(150)

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

    btn_vol_down = pygame.Rect(400, 615, 40, 40)
    btn_vol_up = pygame.Rect(590, 615, 40, 40)
    btn_help = pygame.Rect(720, 615, 180, 40)
    btn_help_close = pygame.Rect(540, 520, 200, 45)

    while True:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if show_help:
                    show_help = False 
                    continue
                if state == "ending":
                    pygame.mixer.music.stop()
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
                if show_help:
                    if btn_help_close.collidepoint(mouse_pos):
                        show_help = False
                    continue

                if scene_id == "title":
                    if btn_vol_down.collidepoint(mouse_pos):
                        bgm_volume = max(0.0, bgm_volume - 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                        continue
                    elif btn_vol_up.collidepoint(mouse_pos):
                        bgm_volume = min(1.0, bgm_volume + 0.1)
                        pygame.mixer.music.set_volume(bgm_volume)
                        continue
                    elif btn_help.collidepoint(mouse_pos):
                        show_help = True
                        continue
                    elif mouse_pos[1] < 600:
                        next_line_or_advance()
                        continue
                    else:
                        continue

                if state == "ending":
                    pygame.mixer.music.stop()
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

        if scene_id == "title":
            overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 90)) 
            screen.blit(overlay, (0, 0))

            title_font = load_font(84, bold=True)
            title_text = "한성대 신입생으로 살아남기"
            shadow_surf = title_font.render(title_text, True, (15, 15, 25))
            screen.blit(shadow_surf, (SCREEN_W // 2 - shadow_surf.get_width() // 2 + 5, 175))
            main_surf = title_font.render(title_text, True, (255, 255, 255))
            screen.blit(main_surf, (SCREEN_W // 2 - main_surf.get_width() // 2, 170))

            blink_alpha = abs((pygame.time.get_ticks() % 1800) - 900) / 900.0
            start_font = load_font(28, bold=True)
            start_surf = start_font.render("Space 키 또는 화면을 클릭하여 시작", True, C_YELLOW)
            start_surf.set_alpha(int(255 * blink_alpha))
            screen.blit(start_surf, (SCREEN_W // 2 - start_surf.get_width() // 2, 450))

            draw_rect_alpha(screen, (20, 24, 45, 200), (370, 610, 550, 50), radius=10)
            pygame.draw.rect(screen, C_ACCENT, (370, 610, 550, 50), 2, border_radius=10)

            v_down_col = C_CHOICE_HOV if btn_vol_down.collidepoint(mouse_pos) else C_CHOICE_IDLE
            draw_rect_alpha(screen, v_down_col, btn_vol_down, radius=5)
            screen.blit(fonts["body"].render("-", True, C_WHITE), (413, 622))

            v_up_col = C_CHOICE_HOV if btn_vol_up.collidepoint(mouse_pos) else C_CHOICE_IDLE
            draw_rect_alpha(screen, v_up_col, btn_vol_up, radius=5)
            screen.blit(fonts["body"].render("+", True, C_WHITE), (602, 622))

            vol_percent = int(bgm_volume * 100)
            vol_surf = fonts["sm"].render(f"BGM 볼륨: {vol_percent}%", True, C_WHITE)
            screen.blit(vol_surf, (455, 624))

            h_col = C_CHOICE_HOV if btn_help.collidepoint(mouse_pos) else C_CHOICE_IDLE
            draw_rect_alpha(screen, h_col, btn_help, radius=5)
            pygame.draw.rect(screen, C_YELLOW, btn_help, 1, border_radius=5)
            help_title_surf = fonts["sm"].render("❓ 게임 도움말", True, C_YELLOW)
            screen.blit(help_title_surf, (btn_help.x + (btn_help.w - help_title_surf.get_width()) // 2, 624))

        else:
            draw_hud(screen, player, fonts)
            draw_week_label(screen, scene.get("week", ""), fonts, scene_id, scene.get("bg", ""))

        if week_transition_active:
            transition_surface = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
            transition_surface.fill((0, 0, 0, week_transition_alpha))
            screen.blit(transition_surface, (0, 0))

        if state == "dialog" and scene.get("lines"):
            speaker, text = scene["lines"][line_idx]
            if scene["id"] == "s1_result" and "[ 1학기 최종 결과 ]" in text:
                text = (
                    f"[ 1학기 최종 결과 ]\n"
                    f"학점 {player.grade()} ({player.get('학점')}/100) · "
                    f"멘탈 {player.get('멘탈')} · "
                    f"인간관계 {player.get('인간관계')} · "
                    f"소지금 {player.get('소지금') * 1000:,}원"
                )
            if scene["id"] == "s2_ending" and "[ 2학기 최종 결과 ]" in text:
                text = (
                    f"[ 1학년 최종 결과 ]\n"
                    f"학점 {player.grade()} ({player.get('학점')}/100) · "
                    f"멘탈 {player.get('멘탈')} · "
                    f"인간관계 {player.get('인간관계')} · "
                    f"소지금 {player.get('소지금') * 1000:,}원"
                )
            if scene_id != "title":
                draw_dialog(screen, speaker, text, fonts, anim_chars)
                
        elif state == "choices":
            if scene.get("lines"):
                speaker, text = scene["lines"][-1]
                draw_dialog(screen, speaker, text, fonts, len(text))
            hovered_choice = draw_choices(screen, scene["choices"], player, fonts, mouse_pos)
        elif state == "semester_result":
            draw_semester_result(screen, player, fonts, "1학기 결과")
        elif state == "ending":
            draw_ending(screen, player, fonts, ending_id)

        # 애니메이션 플로팅 스탯 효과 렌더링 레이어
        for ft in floating_texts[:]:
            if ft["delay"] > 0:
                ft["delay"] -= 1
                continue
            ft["life"] -= 1
            if ft["life"] <= 0:
                floating_texts.remove(ft)
                continue
            
            ft["x"] += (ft["target_x"] - ft["x"]) * 0.05
            ft["alpha"] = max(0, int(255 * (ft["life"] / 150)))
            
            txt_surf = fonts["md"].render(ft["text"], True, ft["color"])
            txt_surf.set_alpha(ft["alpha"])
            outline_surf = fonts["md"].render(ft["text"], True, (0, 0, 0))
            outline_surf.set_alpha(ft["alpha"])
            ox, oy = ft["x"] - txt_surf.get_width(), ft["y"] 
            
            # 아웃라인 렌더링으로 가독성 최대로 보장
            screen.blit(outline_surf, (ox - 2, oy))
            screen.blit(outline_surf, (ox + 2, oy))
            screen.blit(outline_surf, (ox, oy - 2))
            screen.blit(outline_surf, (ox, oy + 2))
            screen.blit(txt_surf, (ox, oy))

        if show_help:
            draw_rect_alpha(screen, (0, 0, 0, 200), (0, 0, SCREEN_W, SCREEN_H))
            draw_rect_alpha(screen, (15, 18, 32, 245), (340, 100, 600, 500), radius=15)
            pygame.draw.rect(screen, C_YELLOW, (340, 100, 600, 500), 2, border_radius=15)
            
            h_title = fonts["md"].render("🏫 한성대 새내기 생존 가이드", True, C_YELLOW)
            screen.blit(h_title, (SCREEN_W // 2 - h_title.get_width() // 2, 130))
            
            help_lines = [
                "▪ 낙산벌 생존 법칙",
                "  - 1학기 및 2학기 각 15주간의 대학 생활을 헤쳐나갑니다.",
                "▪ 4대 핵심 스탯 관리 시스템",
                "  - 학점, 멘탈, 인간관계, 소지금 밸런스를 상시 유지하세요.",
                "▪ 친구 찬스 기능",
                "  - 조건이 모자란 선택지를 강제로 뚫어내는 히든 카드입니다.",
                "▪ 확률 분기 주의보",
                "  - AI 코드 표절 검사나 어깨동무는 50% 확률의 성/패가 갈립니다.",
                "▪ 조작 콘트롤",
                "  - 대화 넘기기 : 마우스 클릭 / Space / Enter",
                "  - 게임 즉시 종료 : ESC"
            ]
            
            ty = 185
            for h_line in help_lines:
                color = C_WHITE if h_line.startswith("▪") else C_GRAY
                font_obj = fonts["body"] if h_line.startswith("▪") else fonts["sm"]
                screen.blit(font_obj.render(h_line, True, color), (380, ty))
                ty += 28
            
            hc_col = C_CHOICE_HOV if btn_help_close.collidepoint(mouse_pos) else C_CHOICE_IDLE
            draw_rect_alpha(screen, hc_col, btn_help_close, radius=8)
            pygame.draw.rect(screen, C_WHITE, btn_help_close, 1, border_radius=8)
            close_surf = fonts["sm"].render("확인 (돌아가기)", True, C_WHITE)
            screen.blit(close_surf, (btn_help_close.x + (btn_help_close.w - close_surf.get_width()) // 2, 532))

        pygame.display.flip()


if __name__ == "__main__":
    main()