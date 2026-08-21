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

    def log_battle(self, record):
        with open("battle_history.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {record}\n")

    def show_history(self):
        print("\n" + "=" * 50)
        print(" 📜 GHAYAT: HALL OF FAME & HISTORY 📜 ")
        print("=" * 50)
        try:
            with open("battle_history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("[!] No combat logs recorded in the mainframe yet.")
        input("\nPress Enter to return...")

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 55)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE [OMEGA v7.0] 🌟 ")
            print("=" * 55)
            print("1. View Elite Roster & Arsenal")
            print("2. Enter Cyber Tournament (Ranked Bracket)")
            print("3. Endless Survival Wave Mode (New!)")
            print("4. View Hall of Fame (Battle History)")
            print("5. Terminate Engine")
            print("=" * 55)
            choice = input("Select option (1-5): ")
            
            if choice == '1': self.show_roster()
            elif choice == '2': self.run_tournament()
            elif choice == '3': self.run_survival_mode()
            elif choice == '4': self.show_history()
            elif choice == '5':
                print("\nShutting down mainframe. Stay lethal, Operator! 🚀")
                break
            else:
                print("\n[!] Invalid command sequence.")

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- ELITE ROSTER & GLOBAL OPERATIVES --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    Base Stats -> HP: {char.hp} | Shield: {char.shield}")
            print(f"    Arsenal: {char.weapon} ({char.weapon_tier})")
            print(f"    Tactical Skill: {char.skill}")
            print("    ASCII Signature:")
            for line in char.ascii_render:
                print(f"    {line}")
            print("-" * 40)
        input("\nPress Enter to return...")

    def run_tournament(self):
        print("\nSelect Your Champion (1-4):")
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name} [{char.country}]")
        try:
            choice = int(input("> "))
            player = self.roster[choice - 1]
        except:
            print("[!] Invalid selection.")
            return

        print(f"\n[+] Initializing Tournament Bracket for {player.name}...")
        time.sleep(1)

        # Semifinals
        semi_enemy = random.choice([c for c in self.roster if c != player])
        print(f"\n⚔️ SEMIFINALS: {player.name} VS {semi_enemy.name}")
        input("Press Enter to simulate Semifinals...")
        
        if (player.hp + player.shield) >= random.randint(80, 150):
            print(f"🔥 Victory in Semifinals! {player.name} advances to the Grand Finale.")
        else:
            print(f"💀 Eliminated in Semifinals by {semi_enemy.name}.")
            self.log_battle(f"Tournament Loss: {player.name} knocked out by {semi_enemy.name}")
            input("\nPress Enter...")
            return

        time.sleep(1)
        # Grand Finale
        final_enemy = random.choice([c for c in self.roster if c != player and c != semi_enemy])
        print(f"\n👑 GRAND FINALE: {player.name} VS {final_enemy.name}")
        input("Press Enter for the Ultimate Showdown...")

        if random.random() > 0.35:
            print(f"\n🏆 LEGENDARY CHAMPIONSHIP! {player.name} claims ultimate glory in Ghayat!")
            player.level += 1
            player.weapon_tier = "MK-III OMEGA"
            self.log_battle(f"CHAMPION: {player.name} won the Omega Tournament!")
        else:
            print(f"\n💔 Heartbreak! {final_enemy.name} stole the championship at the wire.")
            self.log_battle(f"Runner-Up: {player.name} lost the Final to {final_enemy.name}")

        input("\nPress Enter to return...")

    def run_survival_mode(self):
        print("\n" + "=" * 50)
        print(" 💀 ENDLESS SURVIVAL WAVE MODE 💀 ")
        print("=" * 50)
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name}")
        try:
            choice = int(input("Select Operator for Survival > "))
            player = self.roster[choice - 1]
        except:
            print("[!] Invalid input.")
            return

        wave = 1
        current_hp = player.hp + player.shield
        print(f"\n[!] Deploying {player.name} into the Endless Grid...")
        
        while current_hp > 0:
            print(f"\n--- WAVE {wave} ---")
            enemy = random.choice(self.roster)
            print(f"Incoming Hostile: {enemy.name}")
            
            damage_taken = random.randint(20, 50)
            current_hp -= damage_taken
            
            if current_hp <= 0:
                print(f"💀 Overwhelmed at Wave {wave}!")
                self.log_battle(f"Survival Mode: {player.name} survived {wave} waves.")
                break
            else:
                print(f"✅ Wave {wave} cleared! Remaining Integrity: {current_hp}")
                wave += 1
            time.sleep(0.8)

        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
