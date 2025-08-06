from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
import requests


def convert():
    crypto_id = crypto_box.currentText()
    currency = currency_box.currentText()
    direction = direction_box.currentText()
    amount_text = amount_input.text()

    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto_id,
                  "vs_currencies": currency}

        response = requests.get(url, params=params)
        data = response.json()
        price = data[crypto_id][currency]

        amount = float(amount_text)

        if direction == "Крипта > Валюта":
            result = round(amount * price, 2)
            result_lbl.setText(f"{amount} {crypto_id} = {result} {currency.upper()}")
        else:
            result = round(amount / price, 8)
            result_lbl.setText(f"{amount} {currency.upper()} = {result} {crypto_id}")
    except:
        result_lbl.setText("Помилка або некоректне число")
        print(result_lbl)



timer = QTimer()
timer.setInterval(10000)
timer.timeout.connect(convert)
timer.start()

app = QApplication([])

window = QWidget()
window.resize(600, 400)

layout = QVBoxLayout()

crypto_box = QComboBox()
crypto_box.addItem(QIcon("btc.png"), "BTC")
crypto_box.addItem(QIcon("sol.png"), "SOL")
crypto_box.addItem(QIcon("eth.png"), "ETH")


currency_box = QComboBox()
currency_box.addItem(QIcon("usd.png"), "USD")
currency_box.addItem(QIcon("eur.png"), "EUR")
currency_box.addItem(QIcon("uah.png"), "UAH")

direction_box = QComboBox()
direction_box.addItems(["Крипта > Валюта", "Валюта > Крипта"])

amount_input = QLineEdit()


convert_btn = QPushButton("Конвертувати")
convert_btn.clicked.connect(convert)

result_lbl = QLabel("Результат:")

layout.addWidget(QLabel("Криптовалюта:"))
layout.addWidget(crypto_box)
layout.addWidget(QLabel("Валюта:"))
layout.addWidget(currency_box)
layout.addWidget(QLabel("Напрямок:"))
layout.addWidget(direction_box)
layout.addWidget(amount_input)
layout.addWidget(convert_btn)
layout.addWidget(result_lbl)

window.setLayout(layout)
window.show()
app.exec()
