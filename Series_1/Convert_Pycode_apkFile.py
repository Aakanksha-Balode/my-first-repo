from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main_App(MDApp):
    def build(self):
        return MDLabel(text= "welcome to my page", halign= "center")

if __name__== '__main__': # for window system open google collab -> new book-> !pip install buildozer-> pip install cython-> sudo apt get install -y -> sudo apt-get install libffi-dev -> buildozer init , add your file in collab -> buildozer -v android debug
    Main_App().run()
    
