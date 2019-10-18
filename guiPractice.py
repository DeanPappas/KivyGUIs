#https://kivy.org/#home to install kivy
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		
		self.inside = GridLayout()
		self.inside.cols = 2
		
		self.firstname = TextInput(multiline=False)
		self.inside.add_widget(Label(text = "First Name: "))
		self.inside.add_widget(self.firstname)
		
		self.lastname = TextInput(multiline=False)
		self.inside.add_widget(Label(text = "Last Name: "))
		self.inside.add_widget(self.lastname)
		
		self.email = TextInput(multiline=False)
		self.inside.add_widget(Label(text = "Email: "))
		self.inside.add_widget(self.email)
		
		
		self.submit = Button(text ="Submit", font_size = 30)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)
		self.add_widget(self.inside)
		
	def pressed(self, instance):
		name = self.firstname.text
		last = self.lastname.textemail = self.email.text
		
		print("Name: %s %s Email: %s" % (name,last,email))

class MyApp(App):
	def build(self):
		return MyGrid()
	
		
if __name__ == "__main__":
	MyApp().run()