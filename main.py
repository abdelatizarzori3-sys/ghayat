import time
import random

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
            EliteCharacter(
                name="TAURI 'CYBER SHOGUN'", 
                country="Japan", 
                class_type="Cyber Samurai Vanguard", 
                ascii_render=["    /\\    ", "   /==\\   ", " [⚡(👁️_👁️)⚡]"], 
                hp=120, shield=50, 
                skill="Cherry Blossom Void Dash", 
                weapon="Quantum Katana", 
                icon="⚡"
            ),
            EliteCharacter(
                name="LYRA 'NEON VALKYRIE'", 
                country="Europe", 
                class_type="Quantum Spec Ops", 
                ascii_render=["   .---.   ", "  | (⊙_⊙) | ", "   \\ — /  "], 
                hp=100, shield=80, 
                skill="Plasma Phase Shift", 
                weapon="Plasma SMG X1", 
                icon="💎"
            ),
            EliteCharacter(
                name="ZAYN 'ATLAS NOMAD'", 
                country="Morocco", 
                class_type="Desert Scout", 
                ascii_render=["    _____  ", "  | (✧_✧) | ", " [:::COMP:::]"], 
                hp=110, shield=60, 
                skill="Atlas Sandstorm Hologram", 
                weapon="Atlas Tactical Bow", 
                icon="🌙"
            ),
            EliteCharacter(
                name="TARIK 'DESERT PHARAOH'", 
                country="Egypt", 
                class_type="Solar Sniper Elite", 
                ascii_render=["   /\\___/\\  ", "  ( ⊙.⊙ ) ", " ==[####]->"], 
                hp=90, shield=100, 
                skill="Eye of Horus Thermal Lock", 
                weapon="Solar Railgun", 
                icon="☀️"
            )
        ]

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 50)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE v3.0 🌟 ")
            print("=" * 50)
            print("1. View Elite Roster & Stats")
            print("2. Play Interactive Match (With Cyber Events)")
            print("3. Exit Engine")
            print("=" * 50)
            choice = input("Select option (1-3): ")
            
            if choice == '1':
                self.show_roster()
            elif choice == '2':
                self.play_match()
            elif choice == '3':
                print("\nExiting engine. See you in the battlefield, Operator! 🚀")
                break
            else:
                print("\n[!] Invalid choice, please select 1, 2, or 3.")

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- GHAYAT ELITE ROSTER & STATS --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    HP: {char.hp} | Shield: {char.shield}")
            print(f"    Weapon: {char.weapon} | Skill: {char.skill}")
            print("    ASCII Avatar:")
            for line in char.ascii_render:
                print(f"    {line}")
            print("-" * 40)
        input("\nPress Enter to return to main menu...")

    def play_match(self):
        print("\n" + "=" * 50)
        print(" 🎯 CHOOSE YOUR ELITE HERO 🎯 ")
        print("=" * 50)
        for idx, char in enumerate(self.roster, 1):
            print(f"{idx}. {char.icon} {char.name} ({char.country}) - HP: {char.hp} / Shield: {char.shield}")
        
        try:
            choice = int(input("\nSelect your hero number (1-4): "))
            if choice < 1 or choice > 4:
                print("[!] Invalid selection. Returning to menu.")
                return
            player = self.roster[choice - 1]
        except ValueError:
            print("[!] Please enter a valid number.")
            return

        opponents = [c for c in self.roster if c != player]
        enemy = random.choice(opponents)

        print("\n" + "=" * 50)
        print(f" ⚔️ ARENA ENGAGEMENT: {player.icon} {player.name} VS {enemy.icon} {enemy.name} ⚔️ ")
        print("=" * 50)
        time.sleep(1)

        p_hp, p_sh = player.hp, player.shield
        e_hp, e_sh = enemy.hp, enemy.shield

        while p_hp > 0 and e_hp > 0:
            print(f"\n--- Status ---")
            print(f"Your [{player.name}]: HP={p_hp} | Shield={p_sh}")
            print(f"Enemy [{enemy.name}]: HP={e_hp} | Shield={e_sh}")
            print("-" * 20)
            
            input("Press Enter to execute attack round...")
            
            # حدث عشوائي محتمل بنسبة 30% أثناء الجولة
            event_chance = random.random()
            if event_chance < 0.25:
                print("\n⚡ [ALERT: EMP STORM DETECTED ACROSS THE ARENA!] ⚡")
                emp_damage = 15
                e_sh = max(0, e_sh - emp_damage)
                print(f"   The storm disrupts {enemy.name}, draining {emp_damage} shield points!\n")
            elif event_chance < 0.45:
                print("\n📦 [TACTICAL AIRDROP DEPLOYED!] 📦")
                heal_boost = 20
                p_hp = min(player.max_hp, p_hp + heal_boost)
                print(f"   You secured medical supplies, restoring {heal_boost} HP!\n")

            # دور اللاعب
            dmg_to_enemy = random.randint(25, 45)
            print(f"🔥 You strike {enemy.name} with {player.weapon} for {dmg_to_enemy} damage!")
            if e_sh > 0:
                if e_sh >= dmg_to_enemy:
                    e_sh -= dmg_to_enemy
                else:
                    dmg_to_enemy -= e_sh
                    e_sh = 0
                    e_hp -= dmg_to_enemy
            else:
                e_hp -= dmg_to_enemy
            
            if e_hp <= 0:
                break

            time.sleep(1)

            # دور الخصم
            dmg_to_player = random.randint(20, 40)
            print(f"⚡ {enemy.name} retaliates using {enemy.skill} for {dmg_to_player} damage!")
            if p_sh > 0:
                if p_sh >= dmg_to_player:
                    p_sh -= dmg_to_player
                else:
                    dmg_to_player -= p_sh
                    p_sh = 0
                    p_hp -= dmg_to_player
            else:
                p_hp -= dmg_to_player
            
            time.sleep(1)

        print("\n" + "=" * 50)
        if p_hp > 0:
            print(f"🏆 VICTORY! {player.name} has dominated the arena!")
        else:
            print(f"💀 DEFEAT! {enemy.name} crushed you this time.")
        print("=" * 50)
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    engine = GhayatBattleEngine()
    engine.menu()
