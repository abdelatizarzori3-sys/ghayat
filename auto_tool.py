
import random
import time
import json
import os

class UltimateCyberGame:
    def __init__(self):
        self.save_file = "save_game.json"
        self.player = {
            "name": "CyberKnight",
            "hp": 100,
            "credits": 500,
            "inventory": []
        }
        self.load_game()

    def save_game(self):
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(self.player, f, ensure_ascii=False, indent=4)
        print(" [💾] نظام الحفظ التلقائي: تم حفظ حالة اللاعب والتقدم بنجاح!")

    def load_game(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, "r", encoding="utf-8") as f:
                self.player = json.load(f)
            print(" [📂] نظام التحميل: تم استعادة بيانات اللاعب من الحفظ السابق.")
        else:
            print(" [✨] بدء رحلة جديدة كلياً للمرة الأولى.")

    def render_hud(self, level):
        print("==================================================")
        print(f" 🎮 | اللعبة: Ultimate Cyber Odyssey | المستوى: {level}")
        print(f" 👤 | اللاعب: {self.player['name']} | ❤️ الطاقة: {self.player['hp']} | 💰 الأرصدة: {self.player['credits']}")
        print(f" 🎒 | المخزون: {self.player['inventory'] if self.player['inventory'] else 'فارغ'}")
        print("==================================================")

    def play(self):
        print("\n" + "="*50)
        print(" [🚀] جاري إقلاع اللعبة الشاملة بكل التفاصيل...")
        print("="*50 + "\n")
        
        for level in range(1, 4):
            self.render_hud(level)
            
            # مستويات صعوبة متصاعدة
            target_range = 10 + (level * 5)
            secret_code = random.randint(1, target_range)
            print(f" [🔐] تحدي المستوى {level}: اختر التردد الصحيح بين (1 و {target_range})")
            
            # محاكاة حل التحدي أو الاختراق
            guess = secret_code if level % 2 != 0 else random.randint(1, target_range)
            print(f" [⚡] محاولة النظام لاختراق التردد: {guess}")
            
            if guess == secret_code:
                print(" [🎉] نجاح باهر! تم اجتياز التحدي وكسر الشفرة.")
                self.player['credits'] += 150
                loot = f"Cyber_Relic_Lvl{level}"
                self.player['inventory'].append(loot)
                print(f" [🎁] مكافأة فريدة: حصلت على عنصر جديد [{loot}]!")
            else:
                print(" [⚠️] فشل الاختراق! حدث ضرر لأنظمة الطاقة.")
                self.player['hp'] -= 20
                
            # حفظ تلقائي بعد كل مستوى
            self.save_game()
            time.sleep(1)
            print("\n" + "-"*50 + "\n")
            
        print("==================================================")
        print(" [🏆] انتهت مغامرة النظام الشاملة بنجاح تامة!")
        print(f" [📊] الحصيلة النهائية - الرصيد: {self.player['credits']} | الطاقة: {self.player['hp']}")
        print("==================================================")

if __name__ == '__main__':
    game = UltimateCyberGame()
    game.play()
