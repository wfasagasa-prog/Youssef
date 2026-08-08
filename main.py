from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.label import Label

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

        self.num1 = TextInput(hint_text="الرقم الأول", input_filter="float")
        self.add_widget(self.num1)

        self.num2 = TextInput(hint_text="الرقم الثاني", input_filter="float")
        self.add_widget(self.num2)

        self.operation = Spinner(
            text="+",
            values=["+", "-", "*", "/"]
        )
        self.add_widget(self.operation)

        btn = Button(text="احسب")
        btn.bind(on_press=self.calculate)
        self.add_widget(btn)

        self.result = Label(text="النتيجة")
        self.add_widget(self.result)

    def calculate(self, instance):
        try:
            a = float(self.num1.text)
            b = float(self.num2.text)

            if self.operation.text == "+":
                self.result.text = str(a + b)
            elif self.operation.text == "-":
                self.result.text = str(a - b)
            elif self.operation.text == "*":
                self.result.text = str(a * b)
            elif self.operation.text == "/":
                self.result.text = str(a / b)
        except:
            self.result.text = "أدخل أرقامًا صحيحة"

class MyApp(App):
    def build(self):
        return Calculator()

MyApp().run()
