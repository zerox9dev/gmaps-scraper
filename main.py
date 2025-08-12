import argparse

from src.scraper import scrape_places
from src.csv_handler import save_places_to_csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str, help="Search query for Google Maps")
    parser.add_argument("-t", "--total", type=int, help="Total number of results to scrape")
    parser.add_argument("-o", "--output", type=str, default="result.csv", help="Output CSV file path")
    parser.add_argument("--append", action="store_true", help="Append results to the output file instead of overwriting")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode (background)")
    args = parser.parse_args()
    search_for = args.search or "turkish stores in toronto Canada"
    total = args.total or 1
    output_path = args.output
    append = args.append
    headless = args.headless
    places = scrape_places(search_for, total, headless=headless)
    save_places_to_csv(places, output_path, append=append)

if __name__ == "__main__":
    main()
