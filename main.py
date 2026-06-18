# main.py
# 한성대학교 신입생 생존기 — 비주얼 노벨 엔진 (Pygame + 타이밍 미니게임 탑재)

import pygame
import sys
import os
import textwrap
import random
from player import Player
from story import SCENE_MAP, ENDINGS_S2

# ──────────────────────────────────────────────
# 설정
# ──────────────────────────────────────────────
SCREEN_W, SCREEN_H = 1280, 720
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")
BG_DIR    = os.path.join(ASSET_DIR, "backgrounds")
CHAR_DIR  = os.path.join(ASSET_DIR, "characters")
AUDIO_DIR = os.path.join(ASSET_DIR, "audio")

# 팔레트
C_BG_FALLBACK  = (30,  34,  50)
C_DIALOG_BG    = (15, 18, 35, 220)
C_WHITE        = (255, 255, 255)
C_YELLOW       = (255, 220,  80)
C_GRAY         = (160, 160, 175)
C_DARK         = ( 20,  20,  35)
C_CHOICE_IDLE  = ( 30,  38,  70, 200)
C_CHOICE_HOV   = ( 60,  90, 160, 230)
C_CHOICE_DIS   = ( 30,  30,  45, 140)
C_STAT_BAR_BG  = ( 40,  40,  60)
C_ACCENT       = ( 80, 160, 255)

KOR_FONT_CANDIDATES = [
    "C:/Windows/Fonts/malgun.ttf", "C:/Windows/Fonts/gulim.ttc",
    "/Library/Fonts/AppleGothic.ttf", "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf", "/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf",
]

# ──────────────────────────────────────────────
# 유틸리티 함수 함수 (기존과 동일)
# ──────────────────────────────────────────────
def find_kor_font():
    for path in KOR_FONT_CANDIDATES:
        if os.path.exists(path): return path
    return None

def load_font(size, bold=False):
    path = find_kor_font()
    if path:
        try: return pygame.font.Font(path, size)
        except Exception: pass
    return pygame.font.SysFont("malgungothic,applegothic,nanumgothic,sans", size, bold=bold)

def load_image(folder, filename, size=None):
    if not filename: return None
    path = os.path.join(folder, filename)
    if not os.path.exists(path): return None
    try:
        img = pygame.image.load(path).convert_alpha()
        if size: img = pygame.transform.smoothscale(img, size)
        return img
    except Exception: return None

def draw_rect_alpha(surface, color, rect, radius=0):
    temp = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    if radius > 0: pygame.draw.rect(temp, color, (0, 0, rect[2], rect[3]), border_radius=radius)
    else: temp.fill(color)
    surface.blit(temp, (rect[0], rect[1]))

def wrap_text(text, font, max_width):
    words = list(text)
    lines = []
    current = ""
    for ch in words:
        test = current + ch
        if font.size(test)[0] <= max_width: current = test
        else:
            if current: lines.append(current)
            current = ch
    if current: lines.append(current)
    return lines

def draw_hud(surface, player, fonts):
    stat_order = ["학점", "멘탈", "인간관계", "소지금"]
    colors = {"학점": (80, 180, 255), "멘탈": (120, 220, 100), "인간관계": (255, 160, 80), "소지금": (255, 220, 60)}
    x, y = SCREEN_W - 210, 16
    bar_w, bar_h = 160, 12
    gap = 28
    sm = fonts["sm"]

    for name in stat_order:
        val = player.get(name)
        label = sm.render(f"{name}", True, C_GRAY)
        surface.blit(label, (x, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (x, y+14, bar_w, bar_h), border_radius=4)
        fill_w = int(bar_w * val / 100)
        if fill_w > 0:
            pygame.draw.rect(surface, colors[name], (x, y+14, fill_w, bar_h), border_radius=4)
        num = sm.render(str(val), True, C_WHITE)
        surface.blit(num, (x + bar_w + 6, y + 12))
        y += gap

    if player.has_flag("동아리_가입"):
        flag_txt = sm.render("♪ 동아리", True, (180, 130, 255))
        surface.blit(flag_txt, (x, y + 4))
        y += gap
    fc = player.flags.get("친구_찬스", 0)
    if fc > 0:
        flag_txt = sm.render(f"👥 친구찬스×{fc}", True, (100, 220, 180))
        surface.blit(flag_txt, (x, y + 4))

DIALOG_H = 200
DIALOG_Y = SCREEN_H - DIALOG_H - 10
DIALOG_X = 30
DIALOG_W = SCREEN_W - 250

def draw_dialog(surface, speaker, text, fonts, anim_chars):
    draw_rect_alpha(surface, C_DIALOG_BG, (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H), radius=12)
    pygame.draw.rect(surface, C_ACCENT, (DIALOG_X, DIALOG_Y, DIALOG_W, DIALOG_H), 2, border_radius=12)
    pad = 20
    inner_w = DIALOG_W - pad * 2

    if speaker:
        name_surf = fonts["md"].render(f"【 {speaker} 】", True, C_YELLOW)
        surface.blit(name_surf, (DIALOG_X + pad, DIALOG_Y + 12))
        text_y = DIALOG_Y + 50
    else:
        text_y = DIALOG_Y + 20

    visible = text[:anim_chars]
    lines = wrap_text(visible, fonts["body"], inner_w)
    for line in lines[:4]:
        txt_surf = fonts["body"].render(line, True, C_WHITE)
        surface.blit(txt_surf, (DIALOG_X + pad, text_y))
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

    for i, ch in enumerate(choices):
        ry = start_y + i * (CHOICE_H + CHOICE_GAP)
        rect = pygame.Rect(CHOICE_X, ry, CHOICE_W, CHOICE_H)
        cond = ch.get("condition")
        enabled = (cond is None) or cond(player)

        if not enabled: col, text_col = C_CHOICE_DIS, C_GRAY
        elif rect.collidepoint(mouse_pos):
            col, text_col = C_CHOICE_HOV, C_WHITE
            hovered = i
        else: col, text_col = C_CHOICE_IDLE, C_WHITE

        draw_rect_alpha(surface, col, (rect.x, rect.y, rect.w, rect.h), radius=10)
        pygame.draw.rect(surface, C_ACCENT if enabled else C_GRAY, rect, 2, border_radius=10)

        label = fonts["body"].render(ch["text"], True, text_col)
        lx = rect.x + (rect.w - label.get_width()) // 2
        ly = rect.y + (rect.h - label.get_height()) // 2
        surface.blit(label, (lx, ly))

        if not enabled:
            lock = fonts["sm"].render("(조건 미충족)", True, (160, 80, 80))
            surface.blit(lock, (rect.x + rect.w - lock.get_width() - 12, ly))
    return hovered

def draw_ending(surface, player, fonts, current_scene_id):
    surface.fill(C_DARK)
    if current_scene_id == "s2_ending":
        title_str, hint_str = "── 2학기 및 1학년 종료 ──", "[ 클릭 또는 Space 로 게임 완전 종료 ]"
    else:
        title_str, hint_str = "── 1학기 종료 ──", "[ 클릭 또는 Space 로 2학기 시작 ]"

    title = fonts["title"].render(title_str, True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 80))

    grade = player.grade()
    grade_col = {"A+": (255, 215, 0), "A": (200, 255, 100), "B+": (100, 200, 255), "B": (120, 200, 220)}.get(grade, C_WHITE)
    g_surf = fonts["title"].render(f"현재 종합 학점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 160))

    stat_names = ["학점", "멘탈", "인간관계", "소지금"]
    colors = [(80,180,255),(120,220,100),(255,160,80),(255,220,60)]
    y = 260
    bar_w = 400
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        lbl = fonts["md"].render(f"{name}  {val}/100", True, C_WHITE)
        surface.blit(lbl, (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG, (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        fw = int(bar_w * val / 100)
        if fw > 0: pygame.draw.rect(surface, col, (SCREEN_W // 2 - bar_w // 2, y + 30, fw, 18), border_radius=6)
        y += 70

    hint = fonts["sm"].render(hint_str, True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))

def draw_week_label(surface, week_str, fonts):
    if not week_str: return
    lbl = fonts["md"].render(week_str, True, C_YELLOW)
    draw_rect_alpha(surface, (0, 0, 0, 160), (10, 10, lbl.get_width() + 20, lbl.get_height() + 10), radius=6)
    surface.blit(lbl, (20, 14))

# ──────────────────────────────────────────────
# 미니게임 전용 드로잉 헬퍼
# ──────────────────────────────────────────────
def draw_minigame_ui(surface, cursor_x, target_rect, bar_rect, fonts):
    """화면 중앙에 타이밍 미니게임 바와 텍스트 연출 그리기"""
    draw_rect_alpha(surface, (0, 0, 0, 200), (0, 0, SCREEN_W, SCREEN_H)) # 어두운 블러 오버레이
    
    title_text = fonts["title"].render("수강신청 광클 타이밍!!", True, C_YELLOW)
    desc_text = fonts["md"].render("스페이스바를 눌러 노란색 세이프 존에 커서를 맞추세요!", True, C_WHITE)
    
    surface.blit(title_text, (SCREEN_W // 2 - title_text.get_width() // 2, SCREEN_H // 2 - 160))
    surface.blit(desc_text, (SCREEN_W // 2 - desc_text.get_width() // 2, SCREEN_H // 2 - 90))
    
    # 베이스 바 & 타겟 구역
    pygame.draw.rect(surface, C_STAT_BAR_BG, bar_rect, border_radius=8)
    pygame.draw.rect(surface, C_YELLOW, target_rect, border_radius=4)
    
    # 왕복하는 커서 지시선
    pygame.draw.line(surface, (255, 50, 50), (cursor_x, bar_rect.y - 15), (cursor_x, bar_rect.bottom + 15), 6)
    pygame.draw.circle(surface, (255, 50, 50), (cursor_x, bar_rect.y - 15), 6)

# ──────────────────────────────────────────────
# 메인 게임 루프
# ──────────────────────────────────────────────
def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("한성대학교 신입생 생존기")
    clock = pygame.time.Clock()

    fonts = {"title": load_font(48, bold=True), "md": load_font(26, bold=True), "body": load_font(22), "sm": load_font(17)}
    bg_cache, char_cache = {}, {}
    def get_bg(name):
        if name not in bg_cache: bg_cache[name] = load_image(BG_DIR, name, (SCREEN_W, SCREEN_H))
        return bg_cache[name]
    def get_char(name):
        if name not in char_cache: char_cache[name] = load_image(CHAR_DIR, name, (360, 540))
        return char_cache[name]

    # 플레이어 초기화 (전략 1에 적합하도록 기본 스탯 설정 지원 가능)
    player = Player() 
    scene_id = "title"
    state = "dialog" 

    scene = SCENE_MAP[scene_id]
    line_idx, anim_chars, anim_speed, anim_done = 0, 0, 2, False

    # 미니게임 시스템 변수들
    mg_bar_rect = pygame.Rect(SCREEN_W // 2 - 300, SCREEN_H // 2, 600, 40)
    mg_target_rect = pygame.Rect(SCREEN_W // 2 - 40, SCREEN_H // 2, 80, 40) # 정중앙 80픽셀 안전구역
    mg_cursor_x = mg_bar_rect.left
    mg_speed = 6
    mg_active_data = None # 현재 선택한 선택지의 미니게임 설정 임시 저장소

    def load_scene(sid):
        nonlocal scene, line_idx, anim_chars, anim_done, state, scene_id
        scene_id = sid
        scene = SCENE_MAP[sid]

        if "effects_on_enter" in scene: player.apply(**scene["effects_on_enter"])
        if "flags_on_enter" in scene:
            for k, v in scene["flags_on_enter"].items():
                if k == "친구_찬스": player.flags["친구_찬스"] = player.flags.get("친구_찬스", 0) + v
                else: player.flags[k] = v

        if "effects_on_enter_cond" in scene:
            c = scene["effects_on_enter_cond"]
            if c["condition"](player): player.apply(**c["true_effects"])
            else: player.apply(**c["false_effects"])

        line_idx, anim_chars, anim_done = 0, 0, False

        if not scene["lines"] and not scene.get("choices"): advance_scene(); return
        if scene["id"] in ("ending", "s2_ending"): state = "ending"
        elif scene.get("_ending_branch"):
            for ending in ENDINGS_S2:
                if ending["condition"](player): load_scene(ending["id"]); return
            load_scene("s2_end_okay"); return
        elif scene.get("choices") and not scene["lines"]: state = "choices"
        else: state = "dialog"

    def advance_scene():
        nonlocal scene_id
        special, cond = scene.get("_special"), scene.get("_condition")
        if special and cond and cond(player): scene_id = special
        else:
            nxt = scene.get("next")
            if nxt is None:
                if scene["id"] in {"s2_end_star", "s2_end_inssa", "s2_end_money", "s2_end_okay"} or scene["id"] == "s2_w15_result":
                    nonlocal state; state = "ending"; scene_id = "s2_ending"; return
                scene_id = "ending"
            else: scene_id = nxt
        load_scene(scene_id)

    def apply_choice(ch):
        nonlocal state, mg_cursor_x, mg_speed, mg_active_data
        
        # [핵심] 선택지에 minigame 설정이 잡혀있다면 미니게임 상태로 즉시 전환
        if "minigame" in ch:
            state = "minigame"
            mg_active_data = ch
            mg_cursor_x = mg_bar_rect.left
            mg_speed = ch["minigame"]["speed"] # 선택지 기반 개별 난이도 적용
            return

        # 일반 선택지 처리
        if "random_branches" in ch: ch = random.choice(ch["random_branches"])
        player.apply(**ch.get("effects", {}))
        for k, v in ch.get("flags", {}).items(): player.flags[k] = v
        load_scene(ch["next"])

    def process_minigame_hit():
        """미니게임 스페이스바 클릭 판정 및 전략 1 스탯 누적 함수"""
        nonlocal state, mg_active_data
        cfg = mg_active_data["minigame"]
        
        # 1. 디폴트 기본 스탯 적용 (전략 1 무조건 지급부)
        player.apply(**cfg["base_effects"])
        
        # 2. 판정 검사 (붉은 커서선이 노란 세이프티 구역 상자 범위 내에 있는지 확인)
        is_success = mg_target_rect.collidepoint(mg_cursor_x, mg_target_rect.centerY)
        
        if is_success:
            print("★ 타이밍 대성공! 보너스 획득")
            player.apply(**cfg["success_bonus"])
        else:
            print("☠ 타이밍 실패! 추가 페널티 발생")
            player.apply(**cfg["fail_penalty"])
            
        # 3. 다음 이야기 시나리오 씬으로 정상 복귀 워프
        load_scene(mg_active_data["next"])
        state = "dialog"

    def next_line_or_advance():
        nonlocal line_idx, anim_chars, anim_done, state
        if scene["lines"] and line_idx < len(scene["lines"]) - 1:
            line_idx += 1; anim_chars = 0; anim_done = False
        else:
            if scene.get("choices"): state = "choices"
            else: advance_scene()

    hovered_choice = -1
    load_scene(scene_id)

    while True:
        dt = clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        # ── 데이터 업데이트 (미니게임 상태일 때 왕복 피지컬 바 이동) ──
        if state == "minigame":
            mg_cursor_x += mg_speed
            if mg_cursor_x >= mg_bar_rect.right or mg_cursor_x <= mg_bar_rect.left:
                mg_speed *= -1 # 벽 충돌 시 튕김 반전

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

                # 미니게임 상태에서 스페이스바 입력 시 타격 판정 트리거
                if state == "minigame" and event.key == pygame.K_SPACE:
                    process_minigame_hit()
                
                elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if state == "ending":
                        if scene_id == "ending": load_scene("s2_title")
                        else: pygame.quit(); sys.exit()
                    elif state == "dialog":
                        if not anim_done: anim_chars = 9999; anim_done = True
                        else: next_line_or_advance()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "ending":
                    if scene_id == "ending": load_scene("s2_title")
                    else: pygame.quit(); sys.exit()
                elif state == "dialog":
                    if not anim_done: anim_chars = 9999; anim_done = True
                    else: next_line_or_advance()
                elif state == "choices" and hovered_choice >= 0:
                    ch = scene["choices"][hovered_choice]
                    cond = ch.get("condition")
                    if cond is None or cond(player): apply_choice(ch)

        if state == "dialog" and scene["lines"] and not anim_done:
            _, text = scene["lines"][line_idx]
            anim_chars += anim_speed
            if anim_chars >= len(text): anim_chars = len(text); anim_done = True

        # ── 그리기 렌더링 파트 ──
        bg = get_bg(scene.get("bg", ""))
        if bg: screen.blit(bg, (0, 0))
        else: screen.fill(C_BG_FALLBACK)

        char_name = scene.get("character")
        if char_name and state != "minigame":
            char_img = get_char(char_name)
            if char_img:
                screen.blit(char_img, (SCREEN_W // 2 - char_img.get_width() // 2, SCREEN_H - char_img.get_height() - DIALOG_H - 20))

        draw_hud(screen, player, fonts)
        draw_week_label(screen, scene.get("week", ""), fonts)

        if state == "dialog" and scene["lines"]:
            speaker, text = scene["lines"][line_idx]
            draw_dialog(screen, speaker, text, fonts, anim_chars)
        elif state == "choices":
            if scene["lines"]: draw_dialog(screen, scene["lines"][-1][0], scene["lines"][-1][1], fonts, len(scene["lines"][-1][1]))
            hovered_choice = draw_choices(screen, scene["choices"], player, fonts, mouse_pos)
        elif state == "minigame":
            # 대화창 뒷배경 깔아주고 그 위에 미니게임 UI 오버레이
            if scene["lines"]: draw_dialog(screen, scene["lines"][-1][0], scene["lines"][-1][1], fonts, len(scene["lines"][-1][1]))
            draw_minigame_ui(screen, mg_cursor_x, mg_target_rect, mg_bar_rect, fonts)
        elif state == "ending":
            draw_ending(screen, player, fonts, scene_id)

        pygame.display.flip()

if __name__ == "__main__":
    main()