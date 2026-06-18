def make_classroom():
    img = gradient((W, H), (240, 235, 225), (200, 195, 185))
    draw = ImageDraw.Draw(img)
    draw.rectangle([80, 80, 1200, 380], fill=(40, 45, 55))
    draw.rectangle([0, 400, W, H], fill=(120, 100, 80))
    for x in range(150, 1100, 100):
        draw.rectangle([x, 420, x + 70, 520], fill=(90, 70, 55))
    return add_text(img, "강의실", "교양 · 전공 · 팀플")


def make_library():
    img = gradient((W, H), (220, 210, 195), (160, 150, 140))
    draw = ImageDraw.Draw(img)
    for row in range(4):
        for col in range(10):
            x = 60 + col * 115
            y = 100 + row * 110
            c = (120 + col * 8, 80 + row * 15, 60)
            draw.rectangle([x, y, x + 90, y + 95], fill=c)
    return add_text(img, "도서관", "중간고사 · 기말고사 · 스터디")


def make_cafe():
    img = gradient((W, H), (180, 140, 100), (120, 90, 70))
    draw = ImageDraw.Draw(img)
    draw.rectangle([300, 250, 980, 550], fill=(220, 200, 180))
    draw.ellipse([560, 300, 720, 420], fill=(100, 60, 40))
    return add_text(img, "카페", "과제 · 스터디 · 아르바이트")


def make_restaurant():
    img = gradient((W, H), (40, 30, 35), (80, 50, 45))
    draw = ImageDraw.Draw(img)
    for x in range(200, 1000, 150):
        draw.ellipse([x, 380, x + 80, 450], fill=(255, 200, 80))
    draw.rectangle([0, 450, W, H], fill=(60, 45, 40))
    return add_text(img, "삼선교 · 포차", "술자리 · 종강 · 뒤풀이")


def make_festival():
    img = gradient((W, H), (30, 20, 60), (80, 40, 100))
    draw = ImageDraw.Draw(img)
    draw.rectangle([400, 200, 880, 420], fill=(40, 40, 50))
    for i, c in enumerate([(255, 80, 120), (80, 200, 255), (255, 220, 80), (120, 255, 120)]):
        draw.ellipse([480 + i * 80, 120, 540 + i * 80, 180], fill=c)
    draw.rectangle([0, 420, W, H], fill=(50, 40, 30))
    return add_text(img, "한성대학교 대동제", "축제 · 공연 · 푸드트럭")


def make_sangsang():
    img = gradient((W, H), (100, 130, 170), (60, 80, 110))
    draw = ImageDraw.Draw(img)
    draw.polygon([(640, 120), (980, 480), (300, 480)], fill=(170, 50, 50))
    draw.rectangle([500, 480, 780, 620], fill=(190, 190, 200))
    draw.line([(640, 620), (640, H)], fill=(100, 100, 110), width=8)
    return add_text(img, "상상관 언덕", "한성대입구역 · 마을버스 · 죽음의 경사")


def make_lab():
    img = gradient((W, H), (25, 35, 50), (15, 20, 35))
    draw = ImageDraw.Draw(img)
    for x in range(100, 1100, 200):
        draw.rectangle([x, 200, x + 160, 500], fill=(30, 40, 55), outline=(60, 80, 100))
        draw.rectangle([x + 20, 220, x + 140, 360], fill=(50, 120, 180))
    return add_text(img, "전공 실습실", "파이썬 · AI · 팀 프로젝트")


def make_pcbang():
    img = gradient((W, H), (20, 15, 40), (40, 20, 60))
    draw = ImageDraw.Draw(img)
    for row in range(2):
        for col in range(5):
            x = 140 + col * 210
            y = 200 + row * 180
            draw.rectangle([x, y, x + 170, y + 140], fill=(30, 30, 45), outline=(80, 60, 120))
            draw.rectangle([x + 15, y + 15, x + 155, y + 100], fill=(40, 80, 120))
    return add_text(img, "PC방", "밤샘 · 게임 · (또) 밤샘")


def try_download_campus():
    urls = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Hansung_University_main_building.jpg/1280px-Hansung_University_main_building.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Hansung_University.jpg/1280px-Hansung_University.jpg",
    ]
    for url in urls:
        try:
            r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200:
                img = Image.open(io.BytesIO(r.content)).convert("RGB")
                img = img.resize((W, H), Image.Resampling.LANCZOS)
                img = img.filter(ImageFilter.GaussianBlur(1))
                return add_text(img, "한성대학교", "정문 · 캠퍼스")
        except Exception:
            continue
    return None


def make_character(name, body, face, accent):
    img = Image.new("RGBA", (360, 540), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([110, 40, 250, 180], fill=face)
    draw.arc([130, 90, 170, 130], 0, 180, fill=(40, 40, 50), width=3)
    draw.arc([190, 90, 230, 130], 0, 180, fill=(40, 40, 50), width=3)
    if "happy" in name:
        draw.arc([145, 115, 215, 155], 20, 160, fill=(180, 80, 80), width=3)
    elif "sad" in name:
        draw.line([(150, 140), (170, 130)], fill=(80, 80, 90), width=2)
        draw.line([(190, 130), (210, 140)], fill=(80, 80, 90), width=2)
        draw.arc([150, 145, 210, 175], 200, 340, fill=(120, 80, 80), width=3)
    else:
        draw.line([(155, 135), (175, 138)], fill=(60, 60, 70), width=2)
        draw.line([(185, 138), (205, 135)], fill=(60, 60, 70), width=2)
    draw.rounded_rectangle([80, 190, 280, 480], radius=30, fill=body)
    draw.rounded_rectangle([30, 220, 90, 400], radius=20, fill=body)
    draw.rounded_rectangle([270, 220, 330, 400], radius=20, fill=body)
    draw.rounded_rectangle([110, 480, 160, 530], radius=10, fill=accent)
    draw.rounded_rectangle([200, 480, 250, 530], radius=10, fill=accent)
    return img


def main():
    os.makedirs(BG_DIR, exist_ok=True)
    os.makedirs(CHAR_DIR, exist_ok=True)

    backgrounds = {
        "title.png": make_title,
        "campus.png": make_campus,
        "room.png": make_room,
        "hall.png": make_hall,
        "clubbooth.png": make_clubbooth,
        "classroom.png": make_classroom,
        "library.png": make_library,
        "cafe.png": make_cafe,
        "restaurant.png": make_restaurant,
        "festival.png": make_festival,
        "sangsang.png": make_sangsang,
        "lab.png": make_lab,
        "pcbang.png": make_pcbang,
    }

    real = try_download_campus()
    if real:
        real.save(os.path.join(BG_DIR, "campus_photo.png"))
        backgrounds["campus.png"] = lambda: real

    for fname, fn in backgrounds.items():
        fn().save(os.path.join(BG_DIR, fname), quality=92)
        print(f"  bg: {fname}")

    chars = {
        "player_normal.png": ((90, 130, 200), (255, 220, 190), (60, 80, 120)),
        "player_happy.png": ((100, 160, 110), (255, 220, 190), (50, 90, 70)),
        "player_sad.png": ((80, 90, 110), (240, 210, 190), (50, 55, 70)),
    }
    for fname, colors in chars.items():
        make_character(fname, *colors).save(os.path.join(CHAR_DIR, fname))
        print(f"  char: {fname}")

    print("에셋 생성 완료!")


if __name__ == "__main__":
    main()