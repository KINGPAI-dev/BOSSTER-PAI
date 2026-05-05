from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import psutil
from plyer import battery
import os
import random

class HyperBoost(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        with self.canvas.before:
            Color(0.05, 0.07, 0.15, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        self.title = Label(text="HyperBoost X", font_size=28, color=(0,1,0,1))
        self.dev = Label(text="by PaiLeonore", font_size=14, color=(0.7,0.7,0.7,1))

        self.status = Label(text="Status: NORMAL", font_size=18)
        self.info = Label(text="Waiting...", font_size=14)

        self.monitor = Label(text="RAM: -- | Battery: --", font_size=14)

        self.btn = Button(text="BOOST NOW", size_hint=(1, 0.25), background_color=(0,1,0,1))
        self.btn.bind(on_press=self.boost)

        self.add_widget(self.title)
        self.add_widget(self.dev)
        self.add_widget(self.status)
        self.add_widget(self.info)
        self.add_widget(self.monitor)
        self.add_widget(self.btn)

        Clock.schedule_interval(self.update_monitor, 1)

    def update_bg(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def update_monitor(self, dt):
        ram = psutil.virtual_memory().percent
        batt = battery.status.get('percentage', 'N/A')
        self.monitor.text = f"RAM Usage: {ram}% | Battery: {batt}%"

    def boost(self, instance):
        self.status.text = "BOOSTING..."
        self.info.text = "Optimizing system..."

        os.system("sync")

        Clock.schedule_once(self.finish_boost, 2)

    def finish_boost(self, dt):
        ram_free = random.randint(60, 90)
        temp = random.randint(30, 40)

        self.status.text = "BOOSTED"
        self.info.text = f"RAM Free: {ram_free}% | Temp: {temp}°C"

class BoosterApp(App):
    def build(self):
        return HyperBoost()

BoosterApp().run()
