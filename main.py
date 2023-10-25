from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import requests
from kivy.core.window import Window

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "Конвертер"

API_URL = 'https://api3.binance.com/api/v3/avgPrice'

def get_price(coin: str) -> float:
   data = {'symbol': f'{coin}USDT'}
   response = requests.get(API_URL, data)
   return float(response.json()['price'])


class CalculatorApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертер')
        self.miles = Label(text='Мили')
        self.metres = Label(text='bitok')
        self.santimetres = Label(text='Сантиметры')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        btc = get_price('BTC')
        if data.isnumeric():
            self.miles.text = 'Мили: ' + str(float(data) * 0.62)
            self.metres.text = '1 Bitcoin = ' + str(float(btc)) + ' USD'
            self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.santimetres)
        return box


if __name__ == "__main__":
    CalculatorApp().run()