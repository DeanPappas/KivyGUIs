import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#power = True
ans = ""


class Calculator():
	
	inputs = "Numbers Only"
	
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		
		
	def add(self):
		return (self.num1+self.num2)
		
	def sub(self):
		print(num1-num2)
		
	def mult(self):
		print(num1*num2)
		
	def div(self):
		print(num1/num2)
		
	def exp(self):
		print(num1**num2)
	
	def rem(self):
		print(num1%num2)
		
'''
while power:
	
	num1 = int(input("Type first number: "))
	num2 = int(input("Type second number: "))

	userCalc = Calculator(num1,num2)
	
	
	print(("%d, %d") % (num1,num2))
	button = input("""(+) (-) (*)
(/) (^) (%)
Choose an operation...
""")
	if button == "+":
		userCalc.add()
	if button == "-":
		userCalc.sub()
	if button == "*":
		userCalc.mult()
	if button == "/":
		userCalc.div()
	if button == "^":
		userCalc.exp()
	if button == "%":
		userCalc.rem()
	
	choice = input("Turn  off calculator? (y/n)")
	if choice == "y":
		power = False
	if choice == "n":
		power == True
		print("Turning off...")
'''	
		
class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1
		
		self.nums = GridLayout()
		self.nums.cols = 2
		
		self.topOps = GridLayout()
		self.topOps.cols = 3
		
		self.bottomOps = GridLayout()
		self.bottomOps.cols = 3
		
		self.firstnum = TextInput(multiline=False)
		self.nums.add_widget(Label(text = "First Number: "))
		self.nums.add_widget(self.firstnum)
		
		self.secondnum = TextInput(multiline=False)
		self.nums.add_widget(Label(text = "Second Number: "))
		self.nums.add_widget(self.secondnum)
		
		'''
		self.submit = Button(text ="Add", font_size = 30)
		self.submit.bind(on_press=self.pressed)
		'''
		
		self.add = Button(text ="+", font_size = 30)
		self.add.bind(on_press=self.pressed)
		self.topOps.add_widget(self.add)
		
		self.subtract = Button(text ="-", font_size = 30)
		self.subtract.bind(on_press=self.pressed)
		self.topOps.add_widget(self.subtract)
		
		self.multiply = Button(text ="*", font_size = 30)
		self.multiply.bind(on_press=self.pressed)
		self.topOps.add_widget(self.multiply)
		
		self.divide = Button(text ="/", font_size = 30)
		self.divide.bind(on_press=self.pressed)
		self.bottomOps.add_widget(self.divide)
		
		self.exponent = Button(text ="^", font_size = 30)
		self.exponent.bind(on_press=self.pressed)
		self.bottomOps.add_widget(self.exponent)
		
		self.remainder = Button(text ="%", font_size = 30)
		self.remainder.bind(on_press=self.pressed)
		self.bottomOps.add_widget(self.remainder)
		
		self.add_widget(self.nums)
		self.add_widget(Label(text = "Your answer is..."))
		self.answer = TextInput(multiline=False)
		self.add_widget(self.answer)
		self.add_widget(self.topOps)
		self.add_widget(self.bottomOps)
		#self.add_widget(self.submit)
		
	def pressed(self, instance):
		num1 = self.firstnum.text
		num2 = self.secondnum.text
		print(type(num1))
		userCalc = Calculator(num1,num2)
		ans = userCalc.add()
		print(ans)
		self.answer.text = ans
		
		

class MyApp(App):
	def build(self):
		return MyGrid()
	
		
if __name__ == "__main__":
	MyApp().run()