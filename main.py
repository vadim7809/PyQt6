from PyQt6.QtWidgets import *
import requests


def get_price():
    crypto_id = crypto_box.currentText()
    currency = currency_box.currentText()

    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": crypto_id,
            "vs_currencies": currency
        }
        response = requests.get(url, params=params)
        data = response.json()

        price = data[crypto_id][currency]
        price_lbl.setText(f"{crypto_id.capitalize()} = {price} {currency.upper()}")
    except Exception as e:
        price_lbl.setText(f"Помилка: {e}")

    amount_text = h.text()
    if amount_text:
        try:
            amount = float(amount_text)
            total = amount * price, 2
            price_lbl.setText(f"{crypto_id.capitalize()} = {price} {currency.upper()}")
        except ValueError:
            price_lbl.setText("Невірне число")
app = QApplication([])

window = QWidget()
window.setWindowTitle("Конвертер криптовалют")
window.resize(600, 400)

main_line = QVBoxLayout()

crypto_lbl = QLabel("Криптовалюта")
crypto_box = QComboBox()
crypto_box.addItems(["bitcoin", "ethereum", "solana", "dogecoin", "cardano"])


currenc_lbl = QLabel("Фіатна валюта")
currency_box = QComboBox()

currency_box.addItems(["usd", "eur", "uah", "gbp"])


h = QLabel("Введіть суму криптовалюти яка у вас є")
h1 = QLineEdit()
#h2 = QLabel("Наприклад 0.5 ")

price_lbl = QLabel("Оберіть криптовалюту та валюту")
price_btn = QPushButton("Оновити ціну")
price_btn.clicked.connect(get_price)

main_line.addWidget(h)
main_line.addWidget(h1)
main_line.addWidget(crypto_lbl)
main_line.addWidget(crypto_box)
main_line.addWidget(currenc_lbl)
main_line.addWidget(currency_box)
main_line.addWidget(price_btn)
main_line.addWidget(price_lbl)


window.setLayout(main_line)
window.show()
app.exec()
