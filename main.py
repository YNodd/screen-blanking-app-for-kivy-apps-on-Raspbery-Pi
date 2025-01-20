
"""
Quick and dirty solution for screen blanking on a Raspberry Pi, as my Kivy app blocked the normal screensaver.
When leaving the screen, it has to be open and the timer set to zero (by clicking on the window) to ensure it blanks the
screen after the desired time.
"""


#import os  # needed for logging
#os.environ['KIVY_LOG_MODE'] = 'MIXED'  # is needed to let the logging module work normally

from kivy.config import Config
# everything here must be above all the other imports:
Config.set("graphics", "position", "custom")   # position must be set to "custom" (here that way or manually in the kivy configuration file), otherwise it doesn't work
Config.set("graphics", "left", 0)  # coordinate system
Config.set("graphics", "top", 0)
Config.set("graphics", "height", 430)
Config.set("graphics", "width", 795)

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from subprocess import run, CalledProcessError
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

#import logging

#logfile = "screensaverlogs.txt"
#logging.basicConfig(filename=logfile, level=logging.DEBUG, format= '[%(asctime)s] %(levelname)s - %(message)s')
#window_title = "Screensaver with logs"
window_title = "Screensaver-App"


class ScreenSaverApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.inactivity_timer = 0
        self.max_inactivity = 20  # seconds
        self.screen_turned_off = False

    def build(self):
        Window.bind(on_motion=self.on_motion)
        self.title = window_title
        screens_layout = FloatLayout()

        Clock.schedule_interval(self.check_inactivity, 1)  # seconds

        self.textlbl = Label(text = "This window should\n be open + in front ...", font_size = 70, color = "lightblue", bold = True, size_hint = (.4, .23), pos_hint={'center_x': .50, 'center_y': .50}, )
        screens_layout.add_widget(self.textlbl)

        self.durationlbl = Label(text = f"Duration: {int(self.max_inactivity)}sek", color = "lightblue", bold = True, pos_hint={'center_x': .50, 'center_y': .20})  # Duration: {int(self.max_inactivity/60)}min"
        screens_layout.add_widget(self.durationlbl)

        self.infolbl = Label(text = "This is a provisional screensaver program WITH XSET", color = "lightblue", bold = True, pos_hint={'center_x': .50, 'center_y': .75})
        screens_layout.add_widget(self.infolbl)

        self.timerlbl = Label(text = f"{str(self.inactivity_timer)}", color = "lightblue", pos_hint={'center_x': .90, 'center_y': .20})
        screens_layout.add_widget(self.timerlbl)

        return screens_layout

    def on_motion(self, instance, etype, me):
        if self.screen_turned_off == True:
            self.turn_on_screen()
        self.inactivity_timer = 0

    def check_inactivity(self, dt):
        self.inactivity_timer += 1
        self.timerlbl.text = f"{str(self.inactivity_timer)}/{self.max_inactivity} s"
        if self.screen_turned_off == False:
            if self.inactivity_timer >= self.max_inactivity:
                self.turn_off_screen()

    def turn_off_screen(self):
        #print("turn screen off")
        run("xset dpms force off", shell = True)
        self.screen_turned_off = True

    def turn_on_screen(self):
        #print("turn screen on")
        run("xset dpms force on", shell = True)
        self.screen_turned_off = False
        #logging.info("screen turned on")


if __name__ == '__main__':
    ScreenSaverApp().run()
