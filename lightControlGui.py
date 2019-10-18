#https://kivy.org/#home to install kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')


screen_manager = ScreenManager()
Builder.load_string("""
<ScreenOne>:
    BoxLayout:
        Button:
            text: "Go to Screen 2"
            on_press:
                # You can define the duration of the change
                # and the direction of the slide
                root.manager.transition.direction = 'left'
                root.manager.transition.duration = 1
                root.manager.current = 'screen_two'
""")




class ScreenOne(Screen):
	pass


class ScreenTwo(Screen):	
	pass



class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		# ----------------------------------- Create elements -----------------------------------
		super(MyGrid, self).__init__(**kwargs)
		# Main Container
		self.cols = 1
		# Sub containers
		self.topRow = GridLayout()
		self.topRow.cols = 3
		self.bottomRow = GridLayout()
		self.bottomRow.cols = 3
		
		# Brightness + button
		self.addBrightButton = Button(text ="+", font_size = 50)
		self.addBrightButton.background_color = (.5, .5, .5, 1)
		self.addBrightButton.bind(on_press=self.addBrightPressed)
		# Brightness - button
		self.subBrightButton = Button(text ="-", font_size = 50)
		self.subBrightButton.background_color = (.5, .5, .5, 1)
		self.subBrightButton.bind(on_press=self.subBrightPressed)
		# Blue button
		self.blueButton = Button(text ="", font_size = 30)
		self.blueButton.background_color = (0, 0, 1, 1)
		self.blueButton.bind(on_press=self.blueButtonPressed)
		# Red button
		self.redButton = Button(text ="", font_size = 30)
		self.redButton.background_color = (1, 0, 0, 1)
		self.redButton.bind(on_press=self.redButtonPressed)
		# Green button
		self.greenButton = Button(text ="", font_size = 30)
		self.greenButton.background_color = (0, 1, 0, 1)
		self.greenButton.bind(on_press=self.greenButtonPressed)
		# Yellow button
		self.yellowButton = Button(text ="", font_size = 30)
		self.yellowButton.background_color = (1, 1, 0, 1)
		self.yellowButton.bind(on_press=self.yellowButtonPressed)
		
		
		# ----------------------------------- Add elements -----------------------------------
		self.add_widget(self.topRow) # Add top row container
		self.add_widget(self.bottomRow) # Add bottom row container
		self.topRow.add_widget(self.blueButton) # Add blueButton
		self.topRow.add_widget(self.redButton) # Add redButton
		self.topRow.add_widget(self.addBrightButton) # Add brightness + button
		self.bottomRow.add_widget(self.greenButton) # Add greenButton
		self.bottomRow.add_widget(self.yellowButton) # Add yellowButton
		self.bottomRow.add_widget(self.subBrightButton) # Add brightness - button
		
		
		
	# ----------------------------------- Button Press Actions -----------------------------------
	def addBrightPressed(self, instance):
		pass
	def subBrightPressed(self, instance):
		pass
	def blueButtonPressed(self, instance):
		pass
	def redButtonPressed(self, instance):
		pass
	def greenButtonPressed(self, instance):
		pass
	def yellowButtonPressed(self, instance):
		pass
		
# ----------------------------------- Running the app -----------------------------------

screentwo = ScreenTwo()
#mygrid = MyGrid()
ScreenTwo.add_widget(MyGrid())
print("TESTESTSETSTESTESTSET")
screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))



class MyApp(App):
	def build(self):
		return screen_manager
	
		
if __name__ == "__main__":
	MyApp().run()