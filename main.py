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
        self.level = 1
        self.weapon_tier = "MK-I"

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
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M-%S')}] Tournament Champion: {winner_name}\n")

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
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE v6.0 🌟 ")
            print(" 🏆 Tournament Bracket & Championship Active")
            print("=" * 50)
            print("1. View Elite Roster")
            print("2. Enter Cyber Tournament (Ranked)")
            print("3. View Battle History")
            print("4. Exit Engine")
            print("=" * 50)
            choice = input("Select option (1-4): ")
            if choice == '1': self.show_roster()
            elif choice == '2': self.run_tournament()
            elif choice == '3': self.show_history()
            elif choice == '4': break

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- ELITE ROSTER & TIERS --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} [{char.country}] - Tier: {char.weapon_tier} (Lvl {char.level})")
        input("\nPress Enter to return...")

    def run_tournament(self):
        print("\nSelect Your Champion (1-4):")
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name} ({char.country})")
        try:
            choice = int(input("> "))
            player = self.roster[choice - 1]
        except:
            print("[!] Invalid selection.")
            return

        print("\n" + "=" * 50)
        print(f" 🏆 STARTING CYBER TOURNAMENT: {player.icon} {player.name} 🏆 ")
        print("=" * 50)
        time.sleep(1)

        # نصف النهائي (Semifinals)
        semi_opponents = [c for c in self.roster if c != player]
        semi_enemy = random.choice(semi_opponents)
        
        print(f"\n--- SEMIFINALS: {player.name} VS {semi_enemy.name} ---")
        input("Press Enter to fight Semifinals...")
        
        p_power = player.hp + player.shield + (player.level * 15)
        e_power = semi_enemy.hp + semi_enemy.shield + (semi_enemy.level * 15)
        
        if random.randint(1, 100) + (p_power - e_power) > 45:
            print(f"🔥 {player.name} wins the Semifinals with a stunning {player.skill}!")
        else:
            print(f"💀 DEFEAT in Semifinals! {semi_enemy.name} knocked you out of the tournament.")
            input("\nPress Enter to return...")
            return

        time.sleep(1)

        # النهائي الكبير (Grand Finale)
        remaining_pool = [c for c in semi_opponents if c != semi_enemy]
        final_enemy = random.choice(remaining_pool)
        
        print(f"\n" + "=" * 40)
        print(f" 🌟 GRAND FINALE: {player.name} VS {final_enemy.name} 🌟 ")
        print("=" * 40)
        input("Press Enter for the Ultimate Final Battle...")

        p_power_final = player.hp + player.shield + (player.level * 20)
        f_power_final = final_enemy.hp + final_enemy.shield + (final_enemy.level * 20)

        if random.randint(1, 100) + (p_power_final - f_power_final) > 40:
            print(f"\n👑 LEGENDARY VICTORY! {player.name} is crowned the Grand Champion of Ghayat!")
            player.level += 1
            player.weapon_tier = "MK-III (OMEGA APEX)"
            self.log_battle(f"{player.name} (Tournament Champion)")
        else:
            print(f"\n💔 HEARTBREAK IN THE FINALE! {final_enemy.name} clutched the victory at the last second.")
            self.log_battle(f"{final_enemy.name} (Defeated {player.name} in Finals)")

        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
