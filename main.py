from PyQt6.QtWidgets import *
import requests

app = QApplication([])

window = QWidget()
window.resize(600, 400)

main_line = QVBoxLayout()

price_lbl = QLabel("Натисни на кнопку для отримання цін")
price_btn = QPushButton("Оновити ціни")

main_line.addWidget(price_lbl)
main_line.addWidget(price_btn)


url = requests.get("https://pro-api.coingecko.com/api/v3/simple/price")
params = [
    {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }
]

ethereum = requests.get("https://pro-api.coingecko.com/api/v3/simple/token_price/ethereum")

window.show()
app.exec()