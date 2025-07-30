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


app = QApplication([])

window = QWidget()
window.setWindowTitle("Конвертер криптовалют")
window.resize(600, 400)

main_layout = QVBoxLayout()


crypto_box = QComboBox()
crypto_box.addItems(["bitcoin", "ethereum", "solana", "dogecoin", "cardano"])


currency_box = QComboBox()
currency_box.addItems(["usd", "eur", "uah", "gbp"])

price_lbl = QLabel("Оберіть криптовалюту та валюту")
price_btn = QPushButton("Оновити ціну")
price_btn.clicked.connect(get_price)

main_layout.addWidget(QLabel("Криптовалюта:"))
main_layout.addWidget(crypto_box)
main_layout.addWidget(QLabel("Фіатна валюта:"))
main_layout.addWidget(currency_box)
main_layout.addWidget(price_btn)
main_layout.addWidget(price_lbl)

window.setLayout(main_layout)
window.show()
app.exec()
