# GMaps Scraper
# GMaps Scraper

Простий скрипт для видобування даних про бізнеси з Google Maps: назви, адреси, телефони, рейтинги та відгуки.  
Simple script for extracting business data from Google Maps: names, addresses, phones, ratings and reviews.

## Вимоги  
## Requirements

- Python 3.8+  
- Python 3.8+
- Google Chrome  
- Google Chrome

## Можливості  
## Features

- Видобуває дані про компанії (назва, адреса, телефон, сайт)  
- Extracts company data (name, address, phone, website)
- Збирає рейтинги та кількість відгуків  
- Collects ratings and review counts
- Визначає час роботи  
- Determines working hours
- Зберігає дані у CSV файл  
- Saves data to CSV file

## Встановлення  
## Installation

1. Клонуйте проект:  
1. Clone the project:
   ```bash
   git clone <your-repo-url>
   cd gmaps-scraper
   ```

2. Встановіть залежності:  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## Використання  
## Usage

Запуск з пошуком та кількістю результатів:  
Run with search query and result count:

```bash
python main.py -s "Ресторани в Києві" -t 10
# python main.py -s "Restaurants in Kyiv" -t 10
```

Запуск у фоновому режимі (без вікна браузера):  
Run in headless mode (without browser window):

```bash
python main.py -s "Ресторани в Києві" -t 10 --headless
# python main.py -s "Restaurants in Kyiv" -t 10 --headless
```

**Параметри:**  
**Parameters:**

- `-s` - пошуковий запит  
- `-s` - search query
- `-t` - кількість результатів (за замовчуванням: 1)  
- `-t` - number of results (default: 1)
- `-o` - ім'я вихідного файлу (за замовчуванням: result.csv)  
- `-o` - output file name (default: result.csv)
- `--append` - додати до існуючого файлу  
- `--append` - append to existing file
- `--headless` - запуск у фоновому режимі (без вікна браузера)  
- `--headless` - run in headless mode (without browser window)

## Примітки  
## Notes

- За замовчуванням скрипт відкриває видиме вікно браузера  
- By default, the script opens a visible browser window
- Використовуйте `--headless` для роботи у фоновому режимі (швидше)  
- Use `--headless` for background operation (faster)
- Не запускайте занадто часто, щоб Google не заблокував  
- Don't run too frequently to avoid Google blocking

## Ліцензія  
## License

MIT  
MIT