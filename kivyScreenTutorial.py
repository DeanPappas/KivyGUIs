from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')

kv_text = """\
#:import WipeTransition kivy.uix.screenmanager.WipeTransition
<MainScreen>:
    #transition: WipeTransition()
    id: sm
    FirstScreen:
    SecondScreen:
	ThirdScreen:

<FirstScreen>:
    name: "first_screen"
    GridLayout:
        id: sterowanie_serv
        rows: 3
        padding: 0
        spacing: 0
		BoxLayout:
			size_hint_y: None
			height: 100
            spacing: 0
            Button:
                text:'RGBY'
                on_press: 
					app.root.current = 'first_screen'
            Button:
                text:'TOVP'
                on_press: 
					app.root.transition.direction = 'left'
					app.root.current = 'second_screen'
            Button:
                text:'BWG'
                on_press: 
					app.root.transition.direction = 'left'
					app.root.current = 'third_screen'
        BoxLayout:
            spacing: 0
            Button:
				background_color: (0, 0, 2, 2)
                text:''
                on_press: print(app.root)
            Button:
				background_color: (2, 0, 0, 2)
                text:''
                on_press: print('Button X')
            Button:
                text:'+'
                on_press: print('placeholder')
		BoxLayout:
			spacing: 0
            Button:
				background_color: (0, 2, 0, 2)
                text:''
                on_press: print(app.root)
            Button:
				background_color: (2, 2, 0, 1)
                text:''
                on_press: print('Button X')
            Button:
                text:'-'
                on_press: print('tasklj')

<SecondScreen>:
    name: "second_screen"
    GridLayout:
        id: sterowanie_serv
        rows: 3
        padding: 0
        spacing: 0
		BoxLayout:
			size_hint_y: None
			height: 100
            spacing: 0
            Button:
                text:'RGBY'
                on_press: 
					app.root.transition.direction = 'right'
					app.root.current = 'first_screen'
            Button:
                text:'TOVP'
                on_press: app.root.current = 'second_screen'
            Button:
                text:'BWG'
                on_press: 
					app.root.transition.direction = 'left'
					app.root.current = 'third_screen'
        BoxLayout:
            spacing: 0
            Button:
				background_color: (.5, 1, .8, 1)
                text:''
                on_press: print(app.root)
            Button:
				background_color: (4, .5, .2, 1)
                text:''
                on_press: print('Button X')
            Button:
                text:'+'
                on_press: print('placeholder')
		BoxLayout:
			spacing: 0
            Button:
				background_color: (1, 0, 1, 1)
                text:''
                on_press: print(app.root)
            Button:
				background_color: (3, 2, 2, 1)
                text:''
                on_press: print('Button X')
            Button:
                text:'-'
                on_press: print('tasklj')
				
<ThirdScreen>:
    name: "third_screen"
    GridLayout:
        id: sterowanie_serv
        rows: 3
        padding: 0
        spacing: 0
		BoxLayout:
			size_hint_y: None
			height: 100
            spacing: 0
            Button:
                text:'RGBY'
                on_press: 
					app.root.transition.direction = 'right'
					app.root.current = 'first_screen'
            Button:
                text:'TOVP'
                on_press: 
					app.root.transition.direction = 'right'
					app.root.current = 'second_screen'
            Button:
                text:'BWG'
                on_press: app.root.current = 'third_screen'
        BoxLayout:
            spacing: 0
            Button:
				background_color: (2, 2, 2, 1)
                text:''
                on_press: print('tajekj')
            Button:
				background_color: (1, 1, 1, 1)
                text:''
                on_press: print('Button X')
            Button:
                text:'+'
                on_press: print('placeholder')
		BoxLayout:
			spacing: 0
            Button:
				background_color: (0, 0, 0, .5)
                text:''
                on_press: print(app.root)
            Button:
				background_color: (5, 5, 5, 1)
                text:''
                on_press: print('Button X')
            Button:
                text:'-'
                on_press: print('tasklj')
"""

class MainScreen(ScreenManager):
    def __init__(self):
        super(MainScreen, self).__init__()

class FirstScreen(Screen):
    #some methods
    pass

class SecondScreen(Screen):
    #some methods
    pass
	
class ThirdScreen(Screen):
    #some methods
    pass

class MyKivyApp(App):
    def build(self):
        return MainScreen()

def main():
    Builder.load_string(kv_text)
    app = MyKivyApp()
    app.run()

if __name__ == '__main__':
    main()