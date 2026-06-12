# player.py
# 플레이어 스탯 관리

class Player:
    def __init__(self):
        self.stats = {
            "학점": 50,
            "멘탈": 60,
            "인간관계": 30,
            "소지금": 60,
        }
        self.flags = {
            "동아리_가입": False,
            "친구_찬스": 0,   # 친구 찬스 횟수
        }

    # ── 스탯 조작 ──────────────────────────────────────────
    def apply(self, **deltas):
        """딕셔너리 형태로 스탯 변화를 일괄 적용."""
        for key, delta in deltas.items():
            if key in self.stats:
                self.stats[key] = max(0, min(100, self.stats[key] + delta))

    def get(self, key):
        return self.stats.get(key, 0)

    # ── 조건 체크 헬퍼 ─────────────────────────────────────
    def check(self, key, minimum):
        return self.get(key) >= minimum

    def has_flag(self, flag):
        return bool(self.flags.get(flag, False))

    def use_friend_chance(self):
        if self.flags["친구_찬스"] > 0:
            self.flags["친구_찬스"] -= 1
            return True
        return False

    # ── 학점 등급 ──────────────────────────────────────────
    def grade(self):
        g = self.get("학점")
        if g >= 90: return "A+"
        if g >= 80: return "A"
        if g >= 70: return "B+"
        if g >= 60: return "B"
        if g >= 50: return "C+"
        return "C"

    # ── 디버그 출력 ────────────────────────────────────────
    def __repr__(self):
        return f"Player(stats={self.stats}, flags={self.flags})"
