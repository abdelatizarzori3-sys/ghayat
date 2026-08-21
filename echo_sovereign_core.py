import time
import os
from datetime import datetime

class NeonColors:
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

class EchoCore:
    def __init__(self, user_name="عبد العاطي"):
        self.user_name = user_name
        self.faces = {
            "smiling": [
                "     [  ^  ]      [  ^  ]     ",
                "         \\   v   /         ",
                "       *\\___________/*      "
            ],
            "crypto_mode": [
                "     [  $  ]      [  $  ]     ",
                "         \\   v   /         ",
                "      ==/\\___________/\\==     "
            ]
        }

    def render_face(self, mood="smiling"):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"\n{NeonColors.MAGENTA}{NeonColors.BOLD}=== [ ⚡ ECHO - SOVEREIGN AI NODE 2026 ⚡ ] ==={NeonColors.END}\n")
        
        face_shape = self.faces.get(mood, self.faces["smiling"])
        for line in face_shape:
            print(f"{NeonColors.GREEN}{NeonColors.BOLD}{line.center(45)}{NeonColors.END}")
            time.sleep(0.04)
        print(f"\n{NeonColors.MAGENTA}" + "="*50 + f"{NeonColors.END}\n")

    def run_echo_system(self):
        # 1. الترحيب بالوجه المبتسم
        self.render_face("smiling")
        current_time = datetime.now().strftime('%H:%M')
        print(f"\n{NeonColors.CYAN}{NeonColors.BOLD}🤖 [ECHO]: أهلاً بك يا {self.user_name}. أنا إيكو، صدى وعيك السيادي. الوقت الآن هو {current_time}. الأنظمة المحلية تعمل بكفاءة مطلقة.{NeonColors.END}\n")
        
        # 2. الانتقال لوضع الكريبت والأسواق
        time.sleep(1.5)
        self.render_face("crypto_mode")
        
        print(f"{NeonColors.YELLOW}--- 📊 مراقبة العقد اللامركزية وأصول الكريبت ---{NeonColors.END}")
        assets = [("BTC", "BULLISH", "SECURE"), ("ETH", "STABLE", "ACTIVE"), ("SOL", "GROWING", "OPTIMIZED")]
        for asset, trend, status in assets:
            print(f"{NeonColors.CYAN}  -> {asset:<6} | الاتجاه: {NeonColors.GREEN}{trend:<8} | الحالة: {NeonColors.MAGENTA}{status}{NeonColors.END}")
            time.sleep(0.2)
            
        print(f"\n{NeonColors.GREEN}{NeonColors.BOLD}⚡ [ECHO]: تم فحص العقد اللامركزية بنجاح. الأسواق تحت السيطرة يا صاحب السيادة.{NeonColors.END}\n")

if __name__ == "__main__":
    echo = EchoCore()
    echo.run_echo_system()

