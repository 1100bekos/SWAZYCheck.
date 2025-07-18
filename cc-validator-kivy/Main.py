from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime

class CCLayout(BoxLayout):
    def kontrol_et(self):
        kart = self.ids.kart.text.strip()
        cvc = self.ids.cvc.text.strip()
        ay = self.ids.ay.text.strip()
        yil = self.ids.yil.text.strip()
        self.ids.sonuc.text = self.validate_card(kart, cvc, ay, yil)

    def validate_card(self, num, cvc, m, y):
        # (Buraya Luhn + CVC + tarih kontrolleri kodu gelecek)
        return "✅ Geçerli"  # Basitleştirilmiş çıktı
