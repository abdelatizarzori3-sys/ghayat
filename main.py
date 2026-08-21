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
        self.gems = 10  # الجواهر النادرة الجديدة

class GhayatBattleEngine:
    def __init__(self):
        self.dev_email = "abdelatizarzori3@gmail.com"
        self.roster = [
            EliteCharacter("TAURI 'CYBER SHOGUN'", "Japan", "Cyber Samurai Vanguard", ["    /\\    ", "   /==\\   ", " [⚡(👁️_👁️)⚡]"], 120, 50, "Cherry Blossom Void Dash", "Quantum Katana", "⚡"),
            EliteCharacter("LYRA 'NEON VALKYRIE'", "Europe", "Quantum Spec Ops", ["   .---.   ", "  | (⊙_⊙) | ", "   \\ — /  "], 100, 80, "Plasma Phase Shift", "Plasma SMG X1", "💎"),
            EliteCharacter("ZAYN 'ATLAS NOMAD'", "Morocco", "Desert Scout", ["    _____  ", "  | (✧_✧) | ", " [:::COMP:::]"], 110, 60, "Atlas Sandstorm Hologram", "Atlas Tactical Bow", "🌙"),
            EliteCharacter("TARIK 'DESERT PHARAOH'", "Egypt", "Solar Sniper Elite", ["   /\\___/\\  ", "  ( ⊙.⊙ ) ", " ==[####]->"], 90, 100, "Eye of Horus Thermal Lock", "Solar Railgun", "☀️")
        ]

    def log_battle(self, record):
        try:
            with open("battle_history.txt", "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {record}\n")
        except Exception as e:
            print(f"[!] Warning: Could not write to log file: {e}")

    def show_history(self):
        print("\n" + "=" * 50)
        print(" 📜 GHAYAT GLOBAL HALL OF FAME 📜 ")
        print("=" * 50)
        try:
            with open("battle_history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("[!] No records found in the mainframe yet.")
        input("\nPress Enter to return...")

    def safe_input(self, prompt, max_val):
        while True:
            try:
                val = int(input(prompt))
                if 1 <= val <= max_val:
                    return val
                print(f"[!] Please enter a number between 1 and {max_val}.")
            except ValueError:
                print("[!] Invalid input. Please enter a valid number.")

    def paypal_gem_store(self, player):
        print("\n" + "=" * 55)
        print(" 💎 PAYPAL CYBER GEM STORE (Developer Gateway) 💎 ")
        print(f" Linked Merchant: {self.dev_email}")
        print(f" Current Operator Gems: {player.gems} 💎")
        print("=" * 55)
        print("1. Starter Pack: +50 Gems [Cost: $0.99 via PayPal]")
        print("2. Elite Syndicate Pack: +200 Gems [Cost: $2.99 via PayPal]")
        print("3. Omega God Pack: +500 Gems [Cost: $4.99 via PayPal]")
        print("4. Exit Store")
        
        choice = self.safe_input("Select option (1-4) > ", 4)
        
        if choice in [1, 2, 3]:
            gem_amounts = {1: 50, 2: 200, 3: 500}
            added_gems = gem_amounts[choice]
            print(f"\n[🔄] Connecting to PayPal secure gateway for {self.dev_email}...")
            time.sleep(1.5)
            print(f"[✅] Payment Successful! Added {added_gems} Gems to {player.name}!")
            player.gems += added_gems
            self.log_battle(f"PayPal Purchase: {player.name} bought {added_gems} gems via {self.dev_email}")
        input("\nPress Enter to return...")

    def black_market(self, player):
        print("\n" + "=" * 50)
        print(f" 🛍️ CYBER BLACK MARKET (Credits: {player.credits} | Gems: {player.gems}💎) 🛍️ ")
        print("=" * 50)
        print("1. Upgrade Weapon Tier [Cost: 50 Credits]")
        print("2. Buy Ultimate Armor with Gems [Cost: 15 Gems 💎]")
        print("3. Exit Market")
        
        choice = self.safe_input("Select option (1-3) > ", 3)
        
        if choice == 1:
            if player.credits >= 50:
                player.credits -= 50
                player.weapon_tier = "MK-III OMEGA APEX"
                print(f"✨ Success! Your weapon tier is now {player.weapon_tier}!")
            else:
                print("[!] Insufficient credits!")
        elif choice == 2:
            if player.gems >= 15:
                player.gems -= 15
                player.hp += 50
                player.shield += 50
                print(f"✨ Success! Ultimate Armor equipped! Stats boosted permanently!")
            else:
                print("[!] Insufficient gems! Visit the PayPal Gem Store to top-up.")
        input("\nPress Enter...")

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 60)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE [PAYPAL v8.2] 🌟 ")
            print(f" Developer: Abdelati Zarzori ({self.dev_email})")
            print("=" * 60)
            print("1. View Elite Roster & Arsenal")
            print("2. Enter Ranked Cyber Tournament")
            print("3. Endless Survival Wave Mode")
            print("4. Access Cyber Black Market & Upgrades")
            print("5. PayPal Gem Store (Top-up Gems)")
            print("6. View Global Hall of Fame (History)")
            print("7. Terminate Engine")
            print("=" * 60)
            
            choice = self.safe_input("Select option (1-7) > ", 7)
            
            if choice == 1: self.show_roster()
            elif choice == 2: self.run_tournament()
            elif choice == 3: self.run_survival_mode()
            elif choice == 4: 
                print("\nSelect Operator to access Black Market:")
                for idx, c in enumerate(self.roster, 1): print(f"{idx}. {c.name}")
                idx_choice = self.safe_input("Select Operator > ", len(self.roster))
                self.black_market(self.roster[idx_choice - 1])
            elif choice == 5:
                print("\nSelect Operator to top-up via PayPal:")
                for idx, c in enumerate(self.roster, 1): print(f"{idx}. {c.name}")
                idx_choice = self.safe_input("Select Operator > ", len(self.roster))
                self.paypal_gem_store(self.roster[idx_choice - 1])
            elif choice == 6: self.show_history()
            elif choice == 7:
                print("\nShutting down mainframe securely. Stay lethal, Abdelati! 🚀")
                break

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- SYNDICATE ELITE ROSTER --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    HP: {char.hp} | Shield: {char.shield} | Credits: {char.credits} | Gems: {char.gems}💎")
            print(f"    Weapon: {char.weapon} ({char.weapon_tier})")
            print("-" * 40)
        input("\nPress Enter to return...")

    def run_tournament(self):
        print("\nSelect Your Champion (1-4):")
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name} [{char.country}]")
        
        player = self.roster[self.safe_input("Select Champion > ", len(self.roster)) - 1]

        print(f"\n[+] Initializing Syndicate Tournament for {player.name}...")
        time.sleep(1)

        semi_enemy = random.choice([c for c in self.roster if c != player])
        print(f"\n⚔️ SEMIFINALS: {player.name} VS {semi_enemy.name}")
        input("Press Enter to fight...")
        
        if (player.hp + player.shield) >= random.randint(70, 140):
            print(f"🔥 Victory in Semifinals! Advancing to Grand Finale.")
            player.credits += 30
            player.gems += 5
        else:
            print(f"💀 Eliminated in Semifinals by {semi_enemy.name}.")
            self.log_battle(f"Tournament Loss: {player.name} knocked out by {semi_enemy.name}")
            input("\nPress Enter...")
            return

        time.sleep(1)
        final_enemy = random.choice([c for c in self.roster if c != player and c != semi_enemy])
        print(f"\n👑 GRAND FINALE: {player.name} VS {final_enemy.name}")
        input("Press Enter for the Ultimate Showdown...")

        if random.random() > 0.3:
            print(f"\n🏆 LEGENDARY CHAMPIONSHIP! {player.name} claims the Syndicate Crown!")
            player.level += 1
            player.credits += 100
            player.gems += 20
            player.weapon_tier = "MK-III OMEGA APEX"
            self.log_battle(f"CHAMPION: {player.name} won the Syndicate Tournament (+20 Gems)")
        else:
            print(f"\n💔 Heartbreak! {final_enemy.name} snatched victory at the wire.")
            self.log_battle(f"Runner-Up: {player.name} lost the Final to {final_enemy.name}")

        input("\nPress Enter to return...")

    def run_survival_mode(self):
        print("\n" + "=" * 50)
        print(" 💀 SURVIVAL WAVE MODE (PAYPAL v8.2) 💀 ")
        print("=" * 50)
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name}")
            
        player = self.roster[self.safe_input("Select Operator > ", len(self.roster)) - 1]

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
                earned_credits = wave * 10
                earned_gems = max(1, wave // 2)
                player.credits += earned_credits
                player.gems += earned_gems
                print(f"💰 Earned {earned_credits} credits & {earned_gems} Gems💎 from survival run.")
                self.log_battle(f"Survival Mode: {player.name} cleared {wave} waves.")
                break
            else:
                print(f"✅ Wave {wave} cleared! Integrity: {current_hp}")
                wave += 1
            time.sleep(0.4)

        input("\nPress Enter to return...")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
