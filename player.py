# player.py — 플레이어 스탯 관리

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
            "친구_찬스": 0,
        }

    def apply(self, **deltas):
        for key, delta in deltas.items():
            if key in self.stats:
                self.stats[key] = max(0, min(100, self.stats[key] + delta))

    def get(self, key):
        return self.stats.get(key, 0)

    def check(self, key, minimum):
        return self.get(key) >= minimum

    def has_flag(self, flag):
        val = self.flags.get(flag, False)
        if isinstance(val, int):
            return val > 0
        return bool(val)

    def add_friend_chance(self, n=1):
        self.flags["친구_찬스"] = self.flags.get("친구_찬스", 0) + n

    def use_friend_chance(self):
        if self.flags.get("친구_찬스", 0) > 0:
            self.flags["친구_찬스"] -= 1
            return True
        return False

    def grade(self):
        g = self.get("학점")
        if g >= 90:
            return "A+"
        if g >= 80:
            return "A"
        if g >= 70:
            return "B+"
        if g >= 60:
            return "B"
        if g >= 50:
            return "C+"
        return "C"

    def __repr__(self):
        return f"Player(stats={self.stats}, flags={self.flags})"
