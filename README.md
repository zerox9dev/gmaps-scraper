# 🗺️ GMaps Scraper

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| **Простий скрипт для видобування даних про бізнеси з Google Maps: назви, адреси, телефони, рейтинги та відгуки.** | **Простой скрипт для извлечения данных о бизнесах из Google Maps: названия, адреса, телефоны, рейтинги и отзывы.** | **Simple script for extracting business data from Google Maps: names, addresses, phones, ratings and reviews.** |

## 📋 Вимоги / Требования / Requirements

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| • Python 3.8+<br>• Google Chrome | • Python 3.8+<br>• Google Chrome | • Python 3.8+<br>• Google Chrome |

## ⭐ Можливості / Возможности / Features

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| • Видобуває дані про компанії (назва, адреса, телефон, сайт)<br>• Збирає рейтинги та кількість відгуків<br>• Визначає час роботи<br>• Зберігає дані у CSV файл | • Извлекает данные о компаниях (название, адрес, телефон, сайт)<br>• Собирает рейтинги и количество отзывов<br>• Определяет время работы<br>• Сохраняет данные в CSV файл | • Extracts company data (name, address, phone, website)<br>• Collects ratings and review counts<br>• Determines working hours<br>• Saves data to CSV file |

## 🚀 Встановлення / Установка / Installation

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| **1. Клонуйте проект:**<br>`git clone <your-repo-url>`<br>`cd gmaps-scraper`<br><br>**2. Встановіть залежності:**<br>`pip install -r requirements.txt`<br>`playwright install` | **1. Клонируйте проект:**<br>`git clone <your-repo-url>`<br>`cd gmaps-scraper`<br><br>**2. Установите зависимости:**<br>`pip install -r requirements.txt`<br>`playwright install` | **1. Clone the project:**<br>`git clone <your-repo-url>`<br>`cd gmaps-scraper`<br><br>**2. Install dependencies:**<br>`pip install -r requirements.txt`<br>`playwright install` |

## 💻 Використання / Использование / Usage

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| **Запуск з пошуком та кількістю результатів:**<br>```bash<br>python main.py -s "Ресторани в Києві" -t 10<br>```<br><br>**Запуск у фоновому режимі (без вікна браузера):**<br>```bash<br>python main.py -s "Ресторани в Києві" -t 10 --headless<br>``` | **Запуск с поиском и количеством результатов:**<br>```bash<br>python main.py -s "Рестораны в Киеве" -t 10<br>```<br><br>**Запуск в фоновом режиме (без окна браузера):**<br>```bash<br>python main.py -s "Рестораны в Киеве" -t 10 --headless<br>``` | **Run with search query and result count:**<br>```bash<br>python main.py -s "Restaurants in Kyiv" -t 10<br>```<br><br>**Run in headless mode (without browser window):**<br>```bash<br>python main.py -s "Restaurants in Kyiv" -t 10 --headless<br>``` |

## ⚙️ Параметри / Параметры / Parameters

| Параметр | 🇺🇦 Опис | 🇷🇺 Описание | 🇺🇸 Description |
|---|---|---|---|
| `-s` | пошуковий запит | поисковый запрос | search query |
| `-t` | кількість результатів (за замовчуванням: 1) | количество результатов (по умолчанию: 1) | number of results (default: 1) |
| `-o` | ім'я вихідного файлу (за замовчуванням: result.csv) | имя выходного файла (по умолчанию: result.csv) | output file name (default: result.csv) |
| `--append` | додати до існуючого файлу | добавить к существующему файлу | append to existing file |
| `--headless` | запуск у фоновому режимі (без вікна браузера) | запуск в фоновом режиме (без окна браузера) | run in headless mode (without browser window) |

## 📝 Примітки / Примечания / Notes

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| • За замовчуванням скрипт відкриває видиме вікно браузера<br>• Використовуйте `--headless` для роботи у фоновому режимі (швидше)<br>• Не запускайте занадто часто, щоб Google не заблокував | • По умолчанию скрипт открывает видимое окно браузера<br>• Используйте `--headless` для работы в фоновом режиме (быстрее)<br>• Не запускайте слишком часто, чтобы Google не заблокировал | • By default, the script opens a visible browser window<br>• Use `--headless` for background operation (faster)<br>• Don't run too frequently to avoid Google blocking |

## 📄 Ліцензія / Лицензия / License

| 🇺🇦 Українська | 🇷🇺 Русский | 🇺🇸 English |
|---|---|---|
| MIT | MIT | MIT |