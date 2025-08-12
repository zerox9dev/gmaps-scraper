# --------------------------------------------------------------------------
# Головний модуль для парсингу даних з Google Maps
# Main module for parsing data from Google Maps
# --------------------------------------------------------------------------

import argparse

from src.scraper import scrape_places
from src.csv_handler import save_places_to_csv

def main():
    # --------------------------------------------------------------------------
    # Створення парсеру аргументів командного рядка
    # Creating command line argument parser
    # --------------------------------------------------------------------------
    parser = argparse.ArgumentParser()
    
    # Пошуковий запит для Google Maps
    # Search query for Google Maps
    parser.add_argument("-s", "--search", type=str, help="Search query for Google Maps")
    
    # Загальна кількість результатів для парсингу
    # Total number of results to scrape  
    parser.add_argument("-t", "--total", type=int, help="Total number of results to scrape")
    
    # Шлях до вихідного CSV файлу
    # Output CSV file path
    parser.add_argument("-o", "--output", type=str, default="result.csv", help="Output CSV file path")
    
    # Додати результати до файлу замість перезапису
    # Append results to the output file instead of overwriting
    parser.add_argument("--append", action="store_true", help="Append results to the output file instead of overwriting")
    
    # Запуск браузера у фоновому режимі
    # Run browser in headless mode (background)
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode (background)")
    
    # --------------------------------------------------------------------------
    # Обробка аргументів та встановлення значень за замовчуванням
    # Processing arguments and setting default values
    # --------------------------------------------------------------------------
    args = parser.parse_args()
    search_for = args.search or "turkish stores in toronto Canada"
    total = args.total or 1
    output_path = args.output
    append = args.append
    headless = args.headless
    
    # --------------------------------------------------------------------------
    # Виконання парсингу та збереження результатів
    # Executing scraping and saving results
    # --------------------------------------------------------------------------
    places = scrape_places(search_for, total, headless=headless)
    save_places_to_csv(places, output_path, append=append)

if __name__ == "__main__":
    main()
