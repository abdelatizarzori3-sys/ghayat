import time
import random
from datetime import datetime

class EliteCharacter:
    def __init__(self, name, country, class_type, ascii_render, hp, shield, skill, weapon, icon):
        self.name = name
        self.country = country
        self.class_type = class_type
        self.ascii_render = ascii_render
        self.hp = hp
        self.shield = shield
        self.max_hp = hp
        self.max_shield = shield
        self.skill = skill
        self.weapon = weapon
        self.icon = icon

class GhayatBattleEngine:
    def __init__(self):
        self.roster = [
            EliteCharacter("TAURI 'CYBER SHOGUN'", "Japan", "Cyber Samurai Vanguard", ["    /\\    ", "   /==\\   ", " [⚡(👁️_👁️)⚡]"], 120, 50, "Cherry Blossom Void Dash", "Quantum Katana", "⚡"),
            EliteCharacter("LYRA 'NEON VALKYRIE'", "Europe", "Quantum Spec Ops", ["   .---.   ", "  | (⊙_⊙) | ", "   \\ — /  "], 100, 80, "Plasma Phase Shift", "Plasma SMG X1", "💎"),
            EliteCharacter("ZAYN 'ATLAS NOMAD'", "Morocco", "Desert Scout", ["    _____  ", "  | (✧_✧) | ", " [:::COMP:::]"], 110, 60, "Atlas Sandstorm Hologram", "Atlas Tactical Bow", "🌙"),
            EliteCharacter("TARIK 'DESERT PHARAOH'", "Egypt", "Solar Sniper Elite", ["   /\\___/\\  ", "  ( ⊙.⊙ ) ", " ==[####]->"], 90, 100, "Eye of Horus Thermal Lock", "Solar Railgun", "☀️")
        ]

    def log_battle(self, winner_name):
        with open("battle_history.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Winner: {winner_name}\n")

    def show_history(self):
        print("\n--- BATTLE HISTORY ---")
        try:
            with open("battle_history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No battle history found yet.")
        input("\nPress Enter to return...")

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE v4.0 🌟 ")
            print(" 💾 History Tracking Enabled")
            print("=" * 50)
            print("1. View Elite Roster")
            print("2. Play Match")
            print("3. View Battle History")
            print("4. Exit Engine")
            print("=" * 50)
            choice = input("Select option (1-4): ")
            if choice == '1': self.show_roster()
            elif choice == '2': self.play_match()
            elif choice == '3': self.show_history()
            elif choice == '4': break

    def show_roster(self):
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | HP: {char.hp} | Shield: {char.shield}")
        input("\nPress Enter...")

    def play_match(self):
        print("\nSelect Hero (1-4):")
        for idx, char in enumerate(self.roster, 1): print(f"{idx}. {char.name}")
        try:
            choice = int(input("> "))
            player = self.roster[choice - 1]
            enemy = random.choice([c for c in self.roster if c != player])
            print(f"\nBattle: {player.name} VS {enemy.name}")
            
            # محاكاة بسيطة للقتال
            winner = player if random.random() > 0.4 else enemy
            print(f"🏆 Winner: {winner.name}!")
            self.log_battle(winner.name)
            input("\nPress Enter...")
        except: print("Invalid!")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
