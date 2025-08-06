
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QIcon
import requests


def convert():
    crypto_id = crypto_box.currentText().lower()
    currency = currency_box.currentText().lower()
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

        if direction == "Крипта > Фіатт":
            result = round(amount * price, 2)
            result_lbl.setText(f"{amount} {crypto_id.upper()} = {result} {currency.upper()}")
        else:
            result = round(amount / price, 8)
            result_lbl.setText(f"{amount} {currency.upper()} = {result} {crypto_id.upper()}")
    except Exception:
        result_lbl.setText("Помилка або некоректне число")

#auth_token = 3c218e6662d4d3c84690f53a975ecac86a75d50b

def news():
    try:
        url = "/api/developer/v2/posts/?auth_token=3c218e6662d4d3c84690f53a975ecac86a75d50b&kind=news"
        responce = requests.get(url)
        data = responce.json()
        posts = data.get("results", [])
        text = ""
        for p in posts[:5]:
            title = p.get("title", "Без заголовка")
            text += f"{title}""\n"



    except:
        label.setText("Не вдалося знайти новини")


label = QLabel("Оновіти новини")
label.setWordWrap(True)

app = QApplication([])

window = QWidget()
window.resize(600, 400)

main_line = QVBoxLayout()

crypto_box = QComboBox()
crypto_box.addItem(QIcon("btc.png"), "bitcoin")
crypto_box.addItem(QIcon("sol.png"), "solana")
crypto_box.addItem(QIcon("eth.png"), "ethereum")

currency_box = QComboBox()
currency_box.addItem(QIcon("usd.png"), "usd")
currency_box.addItem(QIcon("eur.png"), "eur")
currency_box.addItem(QIcon("uah.png"), "uah")

direction_box = QComboBox()
direction_box.addItems(["Крипта > Фіат", "Фіат > Крипта"])

amount_input = QLineEdit()

convert_btn = QPushButton("Конвертувати")
convert_btn.clicked.connect(convert)

result_lbl = QLabel("Результат:")

main_line.addWidget(QLabel("Криптовалюта:"))
main_line.addWidget(crypto_box)
main_line.addWidget(QLabel("Валюта:"))
main_line.addWidget(currency_box)
main_line.addWidget(QLabel("Напрямок:"))
main_line.addWidget(direction_box)
main_line.addWidget(amount_input)
main_line.addWidget(convert_btn)
main_line.addWidget(label)
main_line.addWidget(result_lbl)


timer = QTimer()
timer.setInterval(10000)
timer.timeout.connect(convert)
timer.start()


window.setLayout(main_line)
window.show()
app.exec()
