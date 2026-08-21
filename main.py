import time
import random

class EliteCharacter:
    def __init__(self, name, country, class_type, ascii_render, gaze, skill, weapon, icon):
        self.name = name
        self.country = country
        self.class_type = class_type
        self.ascii_render = ascii_render
        self.gaze = gaze
        self.skill = skill
        self.weapon = weapon
        self.icon = icon

class GhayatBattleEngine:
    def __init__(self):
        self.roster = [
            EliteCharacter(
                name="TAURI 'CYBER SHOGUN'", 
                country="Japan (اليابان)", 
                class_type="Cyber Samurai Vanguard", 
                ascii_render=["    /\\    ", "   /==\\   ", " [⚡(👁️_👁️)⚡]"], 
                gaze="Sharp Samurai Gaze", 
                skill="Cherry Blossom Void Dash", 
                weapon="Quantum Katana", 
                icon="⚡"
            ),
            EliteCharacter(
                name="LYRA 'NEON VALKYRIE'", 
                country="Europe (أوروبا)", 
                class_type="Quantum Spec Ops", 
                ascii_render=["   .---.   ", "  | (⊙_⊙) | ", "   \\ — /  "], 
                gaze="Quantum Scan Gaze", 
                skill="Plasma Phase Shift", 
                weapon="Plasma SMG X1", 
                icon="💎"
            ),
            EliteCharacter(
                name="ZAYN 'ATLAS NOMAD'", 
                country="Morocco (المغرب)", 
                class_type="Desert Scout", 
                ascii_render=["    _____  ", "  | (✧_✧) | ", " [:::COMP:::]"], 
                gaze="Desert Falcon Gaze", 
                skill="Atlas Sandstorm Hologram", 
                weapon="Atlas Tactical Bow", 
                icon="🌙"
            ),
            EliteCharacter(
                name="TARIK 'DESERT PHARAOH'", 
                country="Egypt (مصر)", 
                class_type="Solar Sniper Elite", 
                ascii_render=["   /\\___/\\  ", "  ( ⊙.⊙ ) ", " ==[####]->"], 
                gaze="Eye of Horus Gaze", 
                skill="Eye of Horus Thermal Lock", 
                weapon="Solar Railgun", 
                icon="☀️"
            )
        ]

    def menu(self):
        while True:
            print("\n" * 2)
            print("=" * 50)
            print(" 🌟 GHAYAT: CYBER BATTLE ROYALE ENGINE 🌟 ")
            print("=" * 50)
            print("1. View Elite Roster (Characters & Arsenal)")
            print("2. Run Holographic Battle Simulation")
            print("3. Exit Engine")
            print("=" * 50)
            choice = input("Select option (1-3): ")
            
            if choice == '1':
                self.show_roster()
            elif choice == '2':
                self.simulate_battle()
            elif choice == '3':
                print("\nExiting engine. See you in the battlefield, Operator! 🚀")
                break
            else:
                print("\n[!] Invalid choice, please select 1, 2, or 3.")

    def show_roster(self):
        print("\n" + "=" * 50)
        print(" --- GHAYAT ELITE ROSTER & ARSENAL --- ")
        print("=" * 50)
        for char in self.roster:
            print(f"\n{char.icon} {char.name} | Region: {char.country}")
            print(f"    Class: {char.class_type}")
            print(f"    Weapon: {char.weapon} | Skill: {char.skill}")
            print(f"    Neural Gaze: {char.gaze}")
            print("    ASCII Avatar:")
            for line in char.ascii_render:
                print(f"    {line}")
            print("-" * 40)
        input("\nPress Enter to return to main menu...")

    def simulate_battle(self):
        print("\n" + "=" * 50)
        print(" ⚔️ INITIALIZING HOLOGRAPHIC BATTLE ARENA ⚔️ ")
        print("=" * 50)
        time.sleep(1)
        p1, p2 = random.sample(self.roster, 2)
        print(f"\n[!] Matchup Found:")
        print(f"    {p1.icon} {p1.name} ({p1.country})")
        print(f"    VS")
        print(f"    {p2.icon} {p2.name} ({p2.country})")
        print("-" * 50)
        
        time.sleep(1.5)
        print(f"🔥 {p1.name} strikes with {p1.weapon}!")
        time.sleep(1.2)
        print(f"🛡️ {p2.name} counters by activating skill: [{p2.skill}]!")
        time.sleep(1.5)
        
        winner = random.choice([p1, p2])
        print("=" * 50)
        print(f"🏆 BATTLE WINNER: {winner.icon} {winner.name} from {winner.country}!")
        print("=" * 50)
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    engine = GhayatBattleEngine()
    engine.menu()
