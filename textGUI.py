import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config
from twilio.rest import Client

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '80')

accountSID = 'AC29ee37284a70927284dfd0e7bdcb3b89'
authToken = '6d3ea8e996a90a495bdceba652801899'
myNumber = '+18479158252'
twilioNumber = '+13344599879'


def textmyself(message):
	twilioCli = Client(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
	

class MyGrid(GridLayout):
	
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		
		self.inside = GridLayout()
		self.inside.cols = 2

		self.textBody = TextInput(multiline=False)
		self.inside.add_widget(Label(text = "Text: "))
		self.inside.add_widget(self.textBody)

		
		self.add_widget(self.inside)
		
		self.submit = Button(text ="Submit", font_size = 30)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)
			
	def pressed(self, instance):
		text = self.textBody.text
		textmyself(text)
		self.textBody.text = "Sent!"
		
		


class MyApp(App):
	def build(self):
		return MyGrid()
	
		
if __name__ == "__main__":
	MyApp().run()