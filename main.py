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
        self.credits = 100

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
        print(" 📜 GHAYAT GLOBAL HALL OF FAME 📜 ")
        print("=" * 50)
        try:
            with open("battle_history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("[!] No records found in the mainframe.")
        input("\nPress Enter to return...")

    def black_market(self, player):
        print("\n" + "=" * 50)
        print(f" 🛍️ CYBER BLACK MARKET (Credits: {player.credits}) 🛍️ ")
        print("=" * 50)
        print("1. Upgrade Weapon Tier [Cost: 50 Credits]")
        print("2. Repair Shield & HP Boost [Cost: 40 Credits]")
        print("3. Exit Market")
        choice = input("Select option (1-3): ")
        
        if choice == '1' and player.credits >= 50:
            player.credits -= 50
            player.weapon_tier = "MK-III OMEGA APEX"
            print(f"✨ Success! Your weapon tier is now {player.weapon_tier}!")
        elif choice == '2' and player.credits >= 40:
            player.credits -= 40
            player.hp = int(player.hp * 1.2)
            player.shield = int(player.shield * 1.2)
            print("✨ Success! Operator stats boosted permanently!")
        else:
            print("[!] Insufficient credits or invalid option.")
        input("\nPress Enter...")

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 60)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE [SYNDICATE v8.0 ALL-IN] 🌟 ")
            print("=" * 60)
            print("1. View Elite Roster & Arsenal")
            print("2. Enter Ranked Cyber Tournament")
            print("3. Endless Survival Wave Mode")
            print("4. Access Cyber Black Market & Upgrades")
            print("5. View Global Hall of Fame (History)")
            print("6. Terminate Engine")
            print("=" * 60)
            choice = input("Select option (1-6): ")
            
            if choice == '1': self.show_roster()
            elif choice == '2': self.run_tournament()
            elif choice == '3': self.run_survival_mode()
            elif choice == '4': 
                print("\nSelect Operator to access Black Market:")
                for idx, c in enumerate(self.roster, 1): print(f"{idx}. {c.name}")
                try: self.black_market(self.roster[int(input("> ")) - 1])
                except: print("[!] Invalid selection.")
            elif choice == '5': self.show_history()
            elif choice == '6':
                print("\nShutting down syndicate mainframe. Stay lethal! 🚀")
                break
            else:
                print("\n[!] Invalid input sequence.")

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- SYNDICATE ELITE ROSTER --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    HP: {char.hp} | Shield: {char.shield} | Credits: {char.credits}")
            print(f"    Weapon: {char.weapon} ({char.weapon_tier})")
            print("-" * 40)
        input("\nPress Enter to return...")

    def run_tournament(self):
        print("\nSelect Your Champion (1-4):")
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name} [{char.country}]")
        try:
            player = self.roster[int(input("> ")) - 1]
        except:
            print("[!] Invalid selection.")
            return

        print(f"\n[+] Initializing Syndicate Tournament for {player.name}...")
        time.sleep(1)

        # Semifinals
        semi_enemy = random.choice([c for c in self.roster if c != player])
        print(f"\n⚔️ SEMIFINALS: {player.name} VS {semi_enemy.name}")
        input("Press Enter to fight...")
        
        if (player.hp + player.shield) >= random.randint(70, 140):
            print(f"🔥 Victory in Semifinals! Advancing to Grand Finale.")
            player.credits += 30
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

        if random.random() > 0.3:
            print(f"\n🏆 LEGENDARY CHAMPIONSHIP! {player.name} claims the Syndicate Crown!")
            player.level += 1
            player.credits += 100
            player.weapon_tier = "MK-III OMEGA APEX"
            self.log_battle(f"CHAMPION: {player.name} won the Syndicate Tournament (+100 Credits)")
        else:
            print(f"\n💔 Heartbreak! {final_enemy.name} snatched victory at the wire.")
            self.log_battle(f"Runner-Up: {player.name} lost the Final to {final_enemy.name}")

        input("\nPress Enter to return...")

    def run_survival_mode(self):
        print("\n" + "=" * 50)
        print(" 💀 SURVIVAL WAVE MODE (ALL-IN) 💀 ")
        print("=" * 50)
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name}")
        try:
            player = self.roster[int(input("Select Operator > ")) - 1]
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
            
            damage = random.randint(15, 45)
            current_hp -= damage
            
            if current_hp <= 0:
                print(f"💀 Overwhelmed at Wave {wave}!")
                earned = wave * 10
                player.credits += earned
                print(f"💰 Earned {earned} credits from survival run.")
                self.log_battle(f"Survival Mode: {player.name} cleared {wave} waves.")
                break
            else:
                print(f"✅ Wave {wave} cleared! Integrity: {current_hp}")
                wave += 1
            time.sleep(0.5)

        input("\nPress Enter to return...")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
