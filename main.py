import time
import random
from datetime import datetime

class EliteCharacter:
    def __init__(self, name, country, class_type, ascii_render, hp, shield, skill, weapon, icon, is_gem_exclusive=False):
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
        self.weapon_tier = "MYTHIC-OMEGA" if is_gem_exclusive else "MK-I"
        self.credits = 200
        self.gems = 50 if is_gem_exclusive else 10
        self.is_gem_exclusive = is_gem_exclusive

class GhayatBattleEngine:
    def __init__(self):
        self.dev_email = "abdelatizarzori3@gmail.com"
        self.roster = [
            # الشخصيات الأساسية
            EliteCharacter("TAURI 'CYBER SHOGUN'", "Japan", "Cyber Samurai Vanguard", ["    /\\    ", "   /==\\   ", " [⚡(👁️_👁️)⚡]"], 120, 50, "Cherry Blossom Void Dash", "Quantum Katana", "⚡"),
            EliteCharacter("LYRA 'NEON VALKYRIE'", "Europe", "Quantum Spec Ops", ["   .---.   ", "  | (⊙_⊙) | ", "   \\ — /  "], 100, 80, "Plasma Phase Shift", "Plasma SMG X1", "💎"),
            EliteCharacter("ZAYN 'ATLAS NOMAD'", "Morocco", "Desert Scout", ["    _____  ", "  | (✧_✧) | ", " [:::COMP:::]"], 110, 60, "Atlas Sandstorm Hologram", "Atlas Tactical Bow", "🌙"),
            EliteCharacter("TARIK 'DESERT PHARAOH'", "Egypt", "Solar Sniper Elite", ["   /\\___/\\  ", "  ( ⊙.⊙ ) ", " ==[####]->"], 90, 100, "Eye of Horus Thermal Lock", "Solar Railgun", "☀️"),
            
            # شخصيات الجواهر الأسطورية الجديدة (مخصصة لعبد العاطي وامتيازاته)
            EliteCharacter("AZAZEL 'CYBER PHANTOM'", "Morocco/Global", "Mythic Shadow Assassin", ["   .-'""'-.  ", "  ( ಠ_ರೃ ) ", "  /==<O>==\\ "], 160, 100, "Atlas Quantum Eclipse", "Mythic Solar Scythe", "🔥", is_gem_exclusive=True),
            EliteCharacter("NYX 'QUANTUM EMPEROR'", "Egypt/Global", "God-Tier Overlord", ["    _.-._    ", "   ( ¤̴uj¤̴ )  ", "  ==[Ω]===="], 180, 120, "Eye of Ra Singularity", "Singularity Cannon", "👑", is_gem_exclusive=True)
        ]

    def log_battle(self, record):
        try:
            with open("battle_history.txt", "a") as f:
                f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {record}\n")
        except Exception as e:
            print(f"[!] Warning: {e}")

    def show_history(self):
        print("\n" + "=" * 50)
        print(" 📜 GHAYAT MYTHIC HALL OF FAME 📜 ")
        print("=" * 50)
        try:
            with open("battle_history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("[!] No combat records found yet.")
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
        print(" 💎 PAYPAL MYTHIC GEM STORE (Abdelati Gateway) 💎 ")
        print(f" Merchant: {self.dev_email}")
        print(f" Operator Gems: {player.gems} 💎")
        print("=" * 55)
        print("1. Starter Pack: +50 Gems [Cost: $0.99]")
        print("2. Elite Mythic Pack: +200 Gems [Cost: $2.99]")
        print("3. Unlock Mythic Overlord Character [Cost: 35 Gems 💎]")
        print("4. Exit Store")
        
        choice = self.safe_input("Select option (1-4) > ", 4)
        
        if choice in [1, 2]:
            amt = 50 if choice == 1 else 200
            print(f"\n[🔄] Processing secure PayPal payment for {self.dev_email}...")
            time.sleep(1)
            player.gems += amt
            print(f"[✅] Success! Added {amt} Gems to {player.name}!")
        elif choice == 3:
            if player.gems >= 35:
                player.gems -= 35
                player.hp += 80
                player.shield += 80
                player.weapon_tier = "GOD-TIER MYTHIC APEX"
                print(f"\n[👑] SUCCESS! {player.name} unlocked God-Tier Mythic Powers!")
            else:
                print("[!] Not enough Gems! Top-up via PayPal first.")
        input("\nPress Enter...")

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 65)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE [MYTHIC OMEGA v9.0] 🌟 ")
            print(f" Creator & Lead Producer: Abdelati Zarzori ({self.dev_email})")
            print("=" * 65)
            print("1. View Elite & Mythic Roster (Gem Heroes)")
            print("2. Enter Ranked Mythic Tournament")
            print("3. Endless Survival Wave Mode (Mythic)")
            print("4. PayPal Mythic Gem Store & Unlocks")
            print("5. View Global Hall of Fame")
            print("6. Terminate Engine")
            print("=" * 65)
            
            choice = self.safe_input("Select option (1-6) > ", 6)
            
            if choice == 1: self.show_roster()
            elif choice == 2: self.run_tournament()
            elif choice == 3: self.run_survival_mode()
            elif choice == 4:
                print("\nSelect Operator to access Mythic Store:")
                for idx, c in enumerate(self.roster, 1): print(f"{idx}. {c.icon} {c.name}")
                idx_c = self.safe_input("Select > ", len(self.roster))
                self.paypal_gem_store(self.roster[idx_c - 1])
            elif choice == 5: self.show_history()
            elif choice == 6:
                print(f"\nShutting down safely. Stay legendary, Abdelati! 🚀🔥")
                break

    def show_roster(self):
        print("\n" + "=" * 55)
        print(" --- SYNDICATE & MYTHIC GEM ROSTER --- ")
        print("=" * 55)
        for char in self.roster:
            tag = " [MYTHIC GEM HERO]" if char.is_gem_exclusive else " [STANDARD]"
            print(f"\n{char.icon} {char.name}{tag} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    HP: {char.hp} | Shield: {char.shield} | Gems: {char.gems}💎")
            print(f"    Ultimate Weapon: {char.weapon} ({char.weapon_tier})")
            print(f"    Signature Skill: {char.skill}")
            print("-" * 45)
        input("\nPress Enter to return...")

    def run_tournament(self):
        print("\nSelect Your Champion (1-6):")
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name} ({char.weapon_tier})")
        
        player = self.roster[self.safe_input("Select Champion > ", len(self.roster)) - 1]

        print(f"\n[+] Initializing Mythic Tournament Bracket for {player.name}...")
        time.sleep(1)

        semi_enemy = random.choice([c for c in self.roster if c != player])
        print(f"\n⚔️ SEMIFINALS: {player.name} VS {semi_enemy.name}")
        input("Press Enter to fight Semifinals...")
        
        power_bonus = 50 if player.is_gem_exclusive else 0
        if (player.hp + player.shield + power_bonus) >= random.randint(60, 130):
            print(f"🔥 Absolute Domination! {player.name} crushes the Semifinals with {player.skill}!")
            player.gems += 15
        else:
            print(f"💀 Shock defeat by {semi_enemy.name}.")
            self.log_battle(f"Tournament Loss: {player.name} eliminated by {semi_enemy.name}")
            input("\nPress Enter...")
            return

        time.sleep(1)
        final_enemy = random.choice([c for c in self.roster if c != player and c != semi_enemy])
        print(f"\n👑 MYTHIC GRAND FINALE: {player.name} VS {final_enemy.name}")
        input("Press Enter for the Ultimate God-Tier Showdown...")

        if random.random() > 0.2 or player.is_gem_exclusive:
            print(f"\n🏆 LEGENDARY GOD-TIER CHAMPION! {player.name} reigns supreme over the entire grid!")
            player.level += 5
            player.gems += 50
            player.weapon_tier = "GOD-TIER MYTHIC APEX"
            self.log_battle(f"MYTHIC CHAMPION: {player.name} won the v9.0 Championship (+50 Gems)")
        else:
            print(f"\n💔 Heartbreak in the final seconds! {final_enemy.name} stole the crown.")
            self.log_battle(f"Runner-Up: {player.name} lost the Mythic Final")

        input("\nPress Enter to return...")

    def run_survival_mode(self):
        print("\n" + "=" * 55)
        print(" 💀 MYTHIC ENDLESS SURVIVAL WAVE MODE 💀 ")
        print("=" * 55)
        for idx, char in enumerate(self.roster, 1): 
            print(f"{idx}. {char.icon} {char.name}")
            
        player = self.roster[self.safe_input("Select Operator > ", len(self.roster)) - 1]

        wave = 1
        current_hp = player.hp + player.shield + (50 if player.is_gem_exclusive else 0)
        print(f"\n[!] Deploying Mythic Operator {player.name} into the Infinite Grid...")
        
        while current_hp > 0:
            print(f"\n--- WAVE {wave} ---")
            enemy = random.choice(self.roster)
            print(f"Incoming Hostile: {enemy.name}")
            
            damage = random.randint(10, 35) if player.is_gem_exclusive else random.randint(20, 50)
            current_hp -= damage
            
            if current_hp <= 0:
                print(f"💀 Overwhelmed at Wave {wave}!")
                earned_gems = wave * 3
                player.gems += earned_gems
                print(f"💎 Earned {earned_gems} Mythic Gems from survival run.")
                self.log_battle(f"Mythic Survival: {player.name} cleared {wave} waves.")
                break
            else:
                print(f"✅ Wave {wave} cleared! Remaining Integrity: {current_hp}")
                wave += 1
            time.sleep(0.3)

        input("\nPress Enter to return...")

if __name__ == "__main__":
    GhayatBattleEngine().menu()
