# main.py
# 한성대학교 신입생 생존기 — 비주얼 노벨 엔진 (Pygame)
#
# 실행 전 설치:
#   pip install pygame
#
# 권장 폴더 구조:
#   HANSUNGFRESHMANSURVIVAL/
#   ├─ main.py
#   ├─ player.py
#   ├─ story.py
#   └─ assets/
#      ├─ backgrounds/   ← 배경 이미지 (PNG/JPG)
#      ├─ characters/    ← 캐릭터 이미지 (PNG, 투명 배경 권장)
#      └─ audio/         ← BGM/SE (OGG/WAV)
#
# 이미지가 없을 때도 자동으로 색 블록으로 대체해 돌아갑니다.

import pygame
import sys
import os
import textwrap
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
C_BG_FALLBACK  = (30,  34,  50)   # 배경 없을 때
C_DIALOG_BG    = (15,  18,  35, 220)  # 대화창 (알파)
C_WHITE        = (255, 255, 255)
C_YELLOW       = (255, 220,  80)
C_GRAY         = (160, 160, 175)
C_DARK         = ( 20,  20,  35)
C_CHOICE_IDLE  = ( 30,  38,  70, 200)
C_CHOICE_HOV   = ( 60,  90, 160, 230)
C_CHOICE_DIS   = ( 30,  30,  45, 140)
C_STAT_BAR_BG  = ( 40,  40,  60)
C_ACCENT       = ( 80, 160, 255)

# 한국어 폰트 경로 탐색 순서
KOR_FONT_CANDIDATES = [
    # Windows
    "C:/Windows/Fonts/malgun.ttf",
    "C:/Windows/Fonts/gulim.ttc",
    # macOS
    "/Library/Fonts/AppleGothic.ttf",
    "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
    # Linux
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf",
]

# ──────────────────────────────────────────────
# 유틸
# ──────────────────────────────────────────────

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
    """이미지를 로드하고 실패 시 None 반환."""
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
    """알파 포함 색으로 둥근 사각형 그리기."""
    temp = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
    if radius > 0:
        pygame.draw.rect(temp, color, (0, 0, rect[2], rect[3]), border_radius=radius)
    else:
        temp.fill(color)
    surface.blit(temp, (rect[0], rect[1]))

def wrap_text(text, font, max_width):
    """긴 텍스트를 픽셀 너비에 맞게 줄 분리."""
    words = list(text)           # 한국어는 글자 단위로
    lines = []
    current = ""
    for ch in words:
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

# ──────────────────────────────────────────────
# 스탯 HUD
# ──────────────────────────────────────────────

def draw_hud(surface, player, fonts):
    """화면 우상단에 스탯 바 표시."""
    stat_order = ["학점", "멘탈", "인간관계", "소지금"]
    colors = {
        "학점":   ( 80, 180, 255),
        "멘탈":   (120, 220, 100),
        "인간관계": (255, 160,  80),
        "소지금": (255, 220,  60),
    }
    x, y = SCREEN_W - 210, 16
    bar_w, bar_h = 160, 12
    gap = 28
    sm = fonts["sm"]

    for name in stat_order:
        val = player.get(name)
        label = sm.render(f"{name}", True, C_GRAY)
        surface.blit(label, (x, y))
        # 배경 바
        pygame.draw.rect(surface, C_STAT_BAR_BG, (x, y+14, bar_w, bar_h), border_radius=4)
        # 채운 바
        fill_w = int(bar_w * val / 100)
        if fill_w > 0:
            pygame.draw.rect(surface, colors[name], (x, y+14, fill_w, bar_h), border_radius=4)
        # 숫자
        num = sm.render(str(val), True, C_WHITE)
        surface.blit(num, (x + bar_w + 6, y + 12))
        y += gap

    # 플래그
    if player.has_flag("동아리_가입"):
        flag_txt = sm.render("♪ 동아리", True, (180, 130, 255))
        surface.blit(flag_txt, (x, y + 4))
        y += gap
    fc = player.flags.get("친구_찬스", 0)
    if fc > 0:
        flag_txt = sm.render(f"👥 친구찬스×{fc}", True, (100, 220, 180))
        surface.blit(flag_txt, (x, y + 4))

# ──────────────────────────────────────────────
# 대화창
# ──────────────────────────────────────────────

DIALOG_H = 200
DIALOG_Y = SCREEN_H - DIALOG_H - 10
DIALOG_X = 30
DIALOG_W = SCREEN_W - 250

def draw_dialog(surface, speaker, text, fonts, anim_chars):
    """하단 대화창 그리기. anim_chars: 현재 표시할 글자 수 (타이핑 효과)."""
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

    # 타이핑 애니메이션 적용
    visible = text[:anim_chars]
    lines = wrap_text(visible, fonts["body"], inner_w)
    for line in lines[:4]:
        txt_surf = fonts["body"].render(line, True, C_WHITE)
        surface.blit(txt_surf, (DIALOG_X + pad, text_y))
        text_y += fonts["body"].get_linesize() + 4

    # '계속' 힌트
    if anim_chars >= len(text):
        hint = fonts["sm"].render("▶ 클릭 또는 Space", True, C_GRAY)
        surface.blit(hint, (DIALOG_X + DIALOG_W - hint.get_width() - pad,
                             DIALOG_Y + DIALOG_H - 28))

# ──────────────────────────────────────────────
# 선택지 버튼
# ──────────────────────────────────────────────

CHOICE_X = 60
CHOICE_W = SCREEN_W - 120
CHOICE_H = 56
CHOICE_GAP = 10

def draw_choices(surface, choices, player, fonts, mouse_pos):
    """선택지 목록을 화면 중앙에 그린다. 반환: 호버 중인 인덱스."""
    total = len(choices)
    start_y = SCREEN_H // 2 - (total * (CHOICE_H + CHOICE_GAP)) // 2

    # 어두운 오버레이
    draw_rect_alpha(surface, (0, 0, 0, 160), (0, 0, SCREEN_W, SCREEN_H))

    hovered = -1
    for i, ch in enumerate(choices):
        ry = start_y + i * (CHOICE_H + CHOICE_GAP)
        rect = pygame.Rect(CHOICE_X, ry, CHOICE_W, CHOICE_H)

        cond = ch.get("condition")
        enabled = (cond is None) or cond(player)

        if not enabled:
            col = C_CHOICE_DIS
            text_col = C_GRAY
        elif rect.collidepoint(mouse_pos):
            col = C_CHOICE_HOV
            text_col = C_WHITE
            hovered = i
        else:
            col = C_CHOICE_IDLE
            text_col = C_WHITE

        draw_rect_alpha(surface, col, (rect.x, rect.y, rect.w, rect.h), radius=10)
        pygame.draw.rect(surface, C_ACCENT if enabled else C_GRAY,
                         rect, 2, border_radius=10)

        label = fonts["body"].render(ch["text"], True, text_col)
        lx = rect.x + (rect.w - label.get_width()) // 2
        ly = rect.y + (rect.h - label.get_height()) // 2
        surface.blit(label, (lx, ly))

        if not enabled:
            lock = fonts["sm"].render("(조건 미충족)", True, (160, 80, 80))
            surface.blit(lock, (rect.x + rect.w - lock.get_width() - 12, ly))

    return hovered

# ──────────────────────────────────────────────
# 엔딩 화면
# ──────────────────────────────────────────────

def draw_ending(surface, player, fonts):
    surface.fill(C_DARK)

    title = fonts["title"].render("── 1학기 종료 ──", True, C_YELLOW)
    surface.blit(title, (SCREEN_W // 2 - title.get_width() // 2, 80))

    grade = player.grade()
    grade_col = {
        "A+": (255, 215, 0), "A": (200, 255, 100),
        "B+": (100, 200, 255), "B": (120, 200, 220),
        "C+": (200, 160, 80), "C": (180, 100, 80),
    }.get(grade, C_WHITE)

    g_surf = fonts["title"].render(f"최종 학점: {grade}", True, grade_col)
    surface.blit(g_surf, (SCREEN_W // 2 - g_surf.get_width() // 2, 160))

    stat_names = ["학점", "멘탈", "인간관계", "소지금"]
    colors = [(80,180,255),(120,220,100),(255,160,80),(255,220,60)]
    y = 260
    bar_w = 400
    for name, col in zip(stat_names, colors):
        val = player.get(name)
        lbl = fonts["md"].render(f"{name}  {val}/100", True, C_WHITE)
        surface.blit(lbl, (SCREEN_W // 2 - bar_w // 2, y))
        pygame.draw.rect(surface, C_STAT_BAR_BG,
                         (SCREEN_W // 2 - bar_w // 2, y + 30, bar_w, 18), border_radius=6)
        fw = int(bar_w * val / 100)
        if fw > 0:
            pygame.draw.rect(surface, col,
                             (SCREEN_W // 2 - bar_w // 2, y + 30, fw, 18), border_radius=6)
        y += 70

    # 감상평
    msgs = []
    if player.get("학점") >= 80:
        msgs.append("학업을 성실하게 해낸 한 학기였다!")
    elif player.get("학점") < 50:
        msgs.append("학점이 많이 아쉽다… 다음 학기에는 더 노력하자.")
    if player.get("멘탈") < 30:
        msgs.append("멘탈이 많이 닳았다. 스스로를 돌봐야 해.")
    if player.get("인간관계") >= 70:
        msgs.append("사람들과 좋은 관계를 쌓은 한 학기!")
    if not msgs:
        msgs.append("평범하지만 나쁘지 않은 첫 학기였다.")

    for i, m in enumerate(msgs):
        ms = fonts["sm"].render(m, True, C_GRAY)
        surface.blit(ms, (SCREEN_W // 2 - ms.get_width() // 2, y + i * 28))

    hint = fonts["sm"].render("[ 클릭 또는 Space 로 종료 ]", True, C_GRAY)
    surface.blit(hint, (SCREEN_W // 2 - hint.get_width() // 2, SCREEN_H - 60))

# ──────────────────────────────────────────────
# 주차 레이블
# ──────────────────────────────────────────────

def draw_week_label(surface, week_str, fonts):
    if not week_str:
        return
    lbl = fonts["md"].render(week_str, True, C_YELLOW)
    draw_rect_alpha(surface, (0, 0, 0, 160), (10, 10, lbl.get_width() + 20, lbl.get_height() + 10), radius=6)
    surface.blit(lbl, (20, 14))

# ──────────────────────────────────────────────
# 메인 게임 루프
# ──────────────────────────────────────────────

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("한성대학교 신입생 생존기")
    clock = pygame.time.Clock()

    # 폰트
    fonts = {
        "title": load_font(48, bold=True),
        "md":    load_font(26, bold=True),
        "body":  load_font(22),
        "sm":    load_font(17),
    }

    # 이미지 캐시
    bg_cache   = {}
    char_cache = {}

    def get_bg(name):
        if name not in bg_cache:
            bg_cache[name] = load_image(BG_DIR, name, (SCREEN_W, SCREEN_H))
        return bg_cache[name]

    def get_char(name):
        if name not in char_cache:
            char_cache[name] = load_image(CHAR_DIR, name, (360, 540))
        return char_cache[name]

    # 플레이어 & 씬 초기화
    player   = Player()
    scene_id = "title"
    state    = "dialog"   # "dialog" | "choices" | "ending"

    scene      = SCENE_MAP[scene_id]
    line_idx   = 0
    anim_chars = 0
    anim_speed = 2       # 프레임당 글자 수
    anim_done  = False

    def load_scene(sid):
        nonlocal scene, line_idx, anim_chars, anim_done, state
        scene = SCENE_MAP[sid]

        # effects_on_enter 처리
        if "effects_on_enter" in scene:
            player.apply(**scene["effects_on_enter"])
        if "flags_on_enter" in scene:
            for k, v in scene["flags_on_enter"].items():
                if k == "친구_찬스":
                    player.flags["친구_찬스"] = player.flags.get("친구_찬스", 0) + v
                else:
                    player.flags[k] = v

        # 조건부 스탯 변경 (w13_b 벼락치기)
        if "effects_on_enter_cond" in scene:
            c = scene["effects_on_enter_cond"]
            if c["condition"](player):
                player.apply(**c["true_effects"])
            else:
                player.apply(**c["false_effects"])

        line_idx   = 0
        anim_chars = 0
        anim_done  = False

        if not scene["lines"] and not scene.get("choices"):
            # 빈 씬 → 특별이벤트 분기 처리
            advance_scene()
            return

        if scene["id"] == "ending":
            state = "ending"
        # ── 2학기 엔딩 분기 처리 ──────────────────────────────
        elif scene.get("_ending_branch"):
            for ending in ENDINGS_S2:
                if ending["condition"](player):
                    load_scene(ending["id"])
                    return
            load_scene("s2_end_okay")
            return
        elif scene["id"] in ("s2_end_star", "s2_end_inssa", "s2_end_money", "s2_end_okay"):
            state = "dialog"  # 대사 출력 후 ending 상태로 전환은 advance_scene에서 처리
        elif scene.get("choices"):
            # 대사가 없으면 바로 선택지
            if not scene["lines"]:
                state = "choices"
            else:
                state = "dialog"
        else:
            state = "dialog"

    def advance_scene():
        """현재 씬이 끝난 뒤 다음으로 이동."""
        nonlocal scene_id

        # _special 분기 (조건부 특별 씬)
        special = scene.get("_special")
        cond    = scene.get("_condition")
        if special and cond and cond(player):
            scene_id = special
        else:
            nxt = scene.get("next")
            if nxt is None:
                # 2학기 엔딩 씬이면 ending 상태로 전환
                s2_ending_ids = {"s2_end_star", "s2_end_inssa", "s2_end_money", "s2_end_okay"}
                if scene["id"] in s2_ending_ids:
                    nonlocal state
                    state = "ending"
                    return
                scene_id = "ending"
            else:
                scene_id = nxt

        load_scene(scene_id)

    def apply_choice(ch):
        """선택지 효과 적용."""
        player.apply(**ch.get("effects", {}))
        for k, v in ch.get("flags", {}).items():
            player.flags[k] = v
        load_scene(ch["next"])

    # ── 내부 헬퍼 ───────────────────────────────

    def next_line_or_advance():
        nonlocal line_idx, anim_chars, anim_done, state
        if scene["lines"] and line_idx < len(scene["lines"]) - 1:
            line_idx  += 1
            anim_chars = 0
            anim_done  = False
        else:
            # 대사 끝 → 선택지 or 다음 씬
            if scene.get("choices"):
                state = "choices"
            else:
                advance_scene()

    # ── 게임 루프 ───────────────────────────────
    hovered_choice = -1
    load_scene(scene_id)

    while True:
        dt = clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        # ── 이벤트 ──────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if state == "ending":
                        pygame.quit()
                        sys.exit()
                    elif state == "dialog":
                        if not anim_done:
                            # 스킵: 전체 텍스트 바로 표시
                            anim_chars = 9999
                            anim_done  = True
                        else:
                            # 다음 대사
                            next_line_or_advance()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "ending":
                    pygame.quit()
                    sys.exit()
                elif state == "dialog":
                    if not anim_done:
                        anim_chars = 9999
                        anim_done  = True
                    else:
                        next_line_or_advance()
                elif state == "choices":
                    if hovered_choice >= 0:
                        ch = scene["choices"][hovered_choice]
                        cond = ch.get("condition")
                        if cond is None or cond(player):
                            apply_choice(ch)

        # ── 타이핑 애니메이션 ──────────────────
        if state == "dialog" and scene["lines"] and not anim_done:
            _, text = scene["lines"][line_idx]
            anim_chars += anim_speed
            if anim_chars >= len(text):
                anim_chars = len(text)
                anim_done  = True

        # ── 그리기 ──────────────────────────────
        # 배경
        bg = get_bg(scene.get("bg", ""))
        if bg:
            screen.blit(bg, (0, 0))
        else:
            screen.fill(C_BG_FALLBACK)

        # 캐릭터
        char_name = scene.get("character")
        if char_name:
            char_img = get_char(char_name)
            if char_img:
                cx = SCREEN_W // 2 - char_img.get_width() // 2
                cy = SCREEN_H - char_img.get_height() - DIALOG_H - 20
                screen.blit(char_img, (cx, cy))

        # HUD
        draw_hud(screen, player, fonts)

        # 주차 레이블
        draw_week_label(screen, scene.get("week", ""), fonts)

        if state == "dialog":
            if scene["lines"]:
                speaker, text = scene["lines"][line_idx]
                draw_dialog(screen, speaker, text, fonts, anim_chars)

        elif state == "choices":
            # 선택지 전 마지막 대사 표시 (있으면)
            if scene["lines"]:
                speaker, text = scene["lines"][-1]
                draw_dialog(screen, speaker, text, fonts, len(text))
            hovered_choice = draw_choices(screen, scene["choices"], player, fonts, mouse_pos)

        elif state == "ending":
            draw_ending(screen, player, fonts)

        pygame.display.flip()


if __name__ == "__main__":
    main()