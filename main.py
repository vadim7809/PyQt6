from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
import requests

app = QApplication([])
window = QWidget()
window.resize(600, 500)

main_line = QVBoxLayout(window)

btn_news = QPushButton("Новини")
btn_converter = QPushButton("Конвертер")
nav_layout = QHBoxLayout()
nav_layout.addWidget(btn_news)
nav_layout.addWidget(btn_converter)
main_line.addLayout(nav_layout)

news_widget = QWidget()
news_line = QVBoxLayout(news_widget)

news_label = QLabel("Тут з’являться новини")
news_label.setWordWrap(True)
news_btn = QPushButton("Оновити новини")

def load_news():
    try:
        url = "https://cryptopanic.com/api/v1/posts/?auth_token=3c218e6662d4d3c84690f53a975ecac86a75d50b&kind=news"
        response = requests.get(url)
        data = response.json()
        posts = data.get("results", [])
        text = ""
        for p in posts[:5]:
            title = p.get("title", "Без заголовка")
            text += f"• {title}\n\n"
        news_label.setText(text)
    except:
        news_label.setText("Не вдалося знайти новини")

news_btn.clicked.connect(load_news)
news_line.addWidget(news_btn)
news_line.addWidget(news_label)

converter_widget = QWidget()
conv_line = QVBoxLayout(converter_widget)

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
result_lbl = QLabel("Результат:")

def convert():
    crypto_id = crypto_box.currentText().lower()
    currency = currency_box.currentText().lower()
    direction = direction_box.currentText()
    amount_text = amount_input.text()

    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": crypto_id, "vs_currencies": currency}
        response = requests.get(url, params=params)
        data = response.json()
        price = data[crypto_id][currency]
        amount = float(amount_text)

        if direction == "Крипта > Фіат":
            result = round(amount * price, 2)
            result_lbl.setText(f"{amount} {crypto_id.upper()} = {result} {currency.upper()}")
        else:
            result = round(amount / price, 8)
            result_lbl.setText(f"{amount} {currency.upper()} = {result} {crypto_id.upper()}")
    except Exception as e:
        result_lbl.setText("Помилка або некоректне число")
        print(str(e))

convert_btn.clicked.connect(convert)

conv_line.addWidget(QLabel("Криптовалюта:"))
conv_line.addWidget(crypto_box)
conv_line.addWidget(QLabel("Валюта:"))
conv_line.addWidget(currency_box)
conv_line.addWidget(QLabel("Напрямок:"))
conv_line.addWidget(direction_box)
conv_line.addWidget(amount_input)
conv_line.addWidget(convert_btn)
conv_line.addWidget(result_lbl)

timer = QTimer()
timer.setInterval(10000)
timer.timeout.connect(convert)
timer.start()

main_line.addWidget(news_widget)
main_line.addWidget(converter_widget)

news_widget.show()
converter_widget.hide()

btn_news.clicked.connect(lambda: (news_widget.show(), converter_widget.hide()))
btn_converter.clicked.connect(lambda: (converter_widget.show(), news_widget.hide()))


app.setStyleSheet("""
    QWidget {
        background-color: #1e1e2f;
        color: #f0f0f0;
        font-family: Arial;
        font-size: 14px;
    }

    QPushButton {
        background-color: #2ecc71;
        color: white;
        border-radius: 8px;
        padding: 6px 12px;
    }

    QPushButton:hover {
        background-color: #27ae60;
    }

    QPushButton:pressed {
        background-color: #1e8449;
    }

    QLineEdit {
        background-color: #2c3e50;
        color: white;
        border: 1px solid #27ae60;
        border-radius: 6px;
        padding: 4px;
    }

    QComboBox {
        background-color: #2c3e50;
        color: white;
        border-radius: 6px;
        padding: 4px;
    }

    QLabel {
        font-size: 14px;
        padding: 2px;
    }
""")


window.show()
app.exec()
