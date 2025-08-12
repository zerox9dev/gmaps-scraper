# 🗺️ GMaps Scraper

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| **Простий скрипт для видобування даних про бізнеси з Google Maps: назви, адреси, телефони, рейтинги та відгуки.** | **Simple script for extracting business data from Google Maps: names, addresses, phones, ratings and reviews.** |

## 📋 Вимоги / Requirements

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| • Python 3.8+<br>• Google Chrome | • Python 3.8+<br>• Google Chrome |

## ⭐ Можливості / Features

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| • Видобуває дані про компанії (назва, адреса, телефон, сайт)<br>• Збирає рейтинги та кількість відгуків<br>• Визначає час роботи<br>• Зберігає дані у CSV файл | • Extracts company data (name, address, phone, website)<br>• Collects ratings and review counts<br>• Determines working hours<br>• Saves data to CSV file |

## 🚀 Встановлення / Installation

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| **1. Клонуйте проект:**<br>`git clone <your-repo-url>`<br>`cd gmaps-scraper`<br><br>**2. Встановіть залежності:**<br>`pip install -r requirements.txt`<br>`playwright install` | **1. Clone the project:**<br>`git clone <your-repo-url>`<br>`cd gmaps-scraper`<br><br>**2. Install dependencies:**<br>`pip install -r requirements.txt`<br>`playwright install` |

## 💻 Використання / Usage

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| **Запуск з пошуком та кількістю результатів:**<br>```bash<br>python main.py -s "Ресторани в Києві" -t 10<br>```<br><br>**Запуск у фоновому режимі (без вікна браузера):**<br>```bash<br>python main.py -s "Ресторани в Києві" -t 10 --headless<br>``` | **Run with search query and result count:**<br>```bash<br>python main.py -s "Restaurants in Kyiv" -t 10<br>```<br><br>**Run in headless mode (without browser window):**<br>```bash<br>python main.py -s "Restaurants in Kyiv" -t 10 --headless<br>``` |

## ⚙️ Параметри / Parameters

| Параметр | 🇺🇦 Опис | 🇺🇸 Description |
|---|---|---|
| `-s` | пошуковий запит | search query |
| `-t` | кількість результатів (за замовчуванням: 1) | number of results (default: 1) |
| `-o` | ім'я вихідного файлу (за замовчуванням: result.csv) | output file name (default: result.csv) |
| `--append` | додати до існуючого файлу | append to existing file |
| `--headless` | запуск у фоновому режимі (без вікна браузера) | run in headless mode (without browser window) |

## 📝 Примітки / Notes

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| • За замовчуванням скрипт відкриває видиме вікно браузера<br>• Використовуйте `--headless` для роботи у фоновому режимі (швидше)<br>• Не запускайте занадто часто, щоб Google не заблокував | • By default, the script opens a visible browser window<br>• Use `--headless` for background operation (faster)<br>• Don't run too frequently to avoid Google blocking |

## 📄 Ліцензія / License

| 🇺🇦 Українська | 🇺🇸 English |
|---|---|
| MIT | MIT |