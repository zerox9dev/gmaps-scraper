import logging
import platform
import time
from typing import List
from playwright.sync_api import sync_playwright, Page

from .models import Place
from .utils import setup_logging, extract_text


def handle_cookie_consent(page: Page):
    """Handle Google cookie consent dialog"""
    try:
        # Wait for consent dialog to appear (if it exists)
        consent_button = None
        
        # Try to find "Accept all" button first
        try:
            consent_button = page.wait_for_selector('button[jsname="b3VHJd"]', timeout=3000)
            if consent_button:
                logging.info("Accepting Google cookie consent...")
                consent_button.click()
                page.wait_for_timeout(1000)
                return
        except:
            pass
        
        # Try alternative selectors for consent buttons
        selectors = [
            '//button[contains(text(), "Accept all")]',
            '//button[contains(text(), "Принять все")]', 
            '//button[contains(text(), "Прийняти всі")]',
            '//button[contains(text(), "Принимаю")]',
            'button[aria-label*="Accept"]',
            'button[aria-label*="Принять"]'
        ]
        
        for selector in selectors:
            try:
                consent_button = page.wait_for_selector(selector, timeout=2000)
                if consent_button:
                    logging.info("Accepting cookies with alternative selector...")
                    consent_button.click()
                    page.wait_for_timeout(1000)
                    return
            except:
                continue
                
        logging.info("No cookie consent dialog found or already handled")
        
    except Exception as e:
        logging.warning(f"Cookie consent handling failed: {e}")
        # Continue anyway as this is not critical


def extract_place(page: Page) -> Place:
    # XPaths
    name_xpath = '//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]'
    address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
    website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
    phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
    reviews_count_xpath = '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span//span//span[@aria-label]'
    reviews_average_xpath = '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span[@aria-hidden]'
    info1 = '//div[@class="LTs0Rc"][1]'
    info2 = '//div[@class="LTs0Rc"][2]'
    info3 = '//div[@class="LTs0Rc"][3]'
    opens_at_xpath = '//button[contains(@data-item-id, "oh")]//div[contains(@class, "fontBodyMedium")]'
    opens_at_xpath2 = '//div[@class="MkV9"]//span[@class="ZDu9vd"]//span[2]'
    place_type_xpath = '//div[@class="LBgpqf"]//button[@class="DkEaL "]'
    intro_xpath = '//div[@class="WeS02d fontBodyMedium"]//div[@class="PYvSYb "]'

    place = Place()
    place.name = extract_text(page, name_xpath)
    place.address = extract_text(page, address_xpath)
    place.website = extract_text(page, website_xpath)
    place.phone_number = extract_text(page, phone_number_xpath)
    place.place_type = extract_text(page, place_type_xpath)
    place.introduction = extract_text(page, intro_xpath) or "None Found"

    # Reviews Count
    reviews_count_raw = extract_text(page, reviews_count_xpath)
    if reviews_count_raw:
        try:
            temp = reviews_count_raw.replace('\xa0', '').replace('(','').replace(')','').replace(',','')
            place.reviews_count = int(temp)
        except Exception as e:
            logging.warning(f"Failed to parse reviews count: {e}")
    # Reviews Average
    reviews_avg_raw = extract_text(page, reviews_average_xpath)
    if reviews_avg_raw:
        try:
            temp = reviews_avg_raw.replace(' ','').replace(',','.')
            place.reviews_average = float(temp)
        except Exception as e:
            logging.warning(f"Failed to parse reviews average: {e}")
    # Store Info
    for idx, info_xpath in enumerate([info1, info2, info3]):
        info_raw = extract_text(page, info_xpath)
        if info_raw:
            temp = info_raw.split('·')
            if len(temp) > 1:
                check = temp[1].replace("\n", "").lower()
                if 'shop' in check:
                    place.store_shopping = "Yes"
                if 'pickup' in check:
                    place.in_store_pickup = "Yes"
                if 'delivery' in check:
                    place.store_delivery = "Yes"
    # Opens At
    opens_at_raw = extract_text(page, opens_at_xpath)
    if opens_at_raw:
        opens = opens_at_raw.split('⋅')
        if len(opens) > 1:
            place.opens_at = opens[1].replace("\u202f","")
        else:
            place.opens_at = opens_at_raw.replace("\u202f","")
    else:
        opens_at2_raw = extract_text(page, opens_at_xpath2)
        if opens_at2_raw:
            opens = opens_at2_raw.split('⋅')
            if len(opens) > 1:
                place.opens_at = opens[1].replace("\u202f","")
            else:
                place.opens_at = opens_at2_raw.replace("\u202f","")
    return place


def scrape_places(search_for: str, total: int, headless: bool = False) -> List[Place]:
    setup_logging()
    
    mode = "headless" if headless else "visible"
    logging.info(f"🚀 Starting Google Maps scraper in {mode} mode")
    logging.info(f"🎯 Target: {total} places for '{search_for}'")
    
    places: List[Place] = []
    with sync_playwright() as p:
        if platform.system() == "Windows":
            browser_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            browser = p.chromium.launch(executable_path=browser_path, headless=headless)
        else:
            browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        try:
            page.goto("https://www.google.com/maps/@32.9817464,70.1930781,3.67z?", timeout=60000)
            page.wait_for_timeout(1000)
            
            # Handle cookie consent dialog if it appears
            handle_cookie_consent(page)
            
            logging.info(f"🔍 Searching for: '{search_for}'")
            page.locator('//input[@id="searchboxinput"]').fill(search_for)
            page.keyboard.press("Enter")
            page.wait_for_selector('//a[contains(@href, "https://www.google.com/maps/place")]')
            page.hover('//a[contains(@href, "https://www.google.com/maps/place")]')
            
            logging.info(f"📍 Loading places... Target: {total}")
            previously_counted = 0
            while True:
                page.mouse.wheel(0, 10000)
                page.wait_for_selector('//a[contains(@href, "https://www.google.com/maps/place")]')
                found = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').count()
                
                # Progress indicator
                progress = min(found, total)
                percentage = (progress / total) * 100
                bar_length = 20
                filled_length = int(bar_length * progress // total)
                bar = '█' * filled_length + '░' * (bar_length - filled_length)
                logging.info(f"📊 Loading [{bar}] {progress}/{total} ({percentage:.0f}%)")
                
                if found >= total:
                    break
                if found == previously_counted:
                    logging.info("🏁 All available places loaded")
                    break
                previously_counted = found
                
            listings = page.locator('//a[contains(@href, "https://www.google.com/maps/place")]').all()[:total]
            listings = [listing.locator("xpath=..") for listing in listings]
            logging.info(f"🎯 Found {len(listings)} places to extract")
            
            for idx, listing in enumerate(listings):
                try:
                    progress = idx + 1
                    percentage = (progress / len(listings)) * 100
                    logging.info(f"📋 Extracting place {progress}/{len(listings)} ({percentage:.0f}%)")
                    
                    listing.click()
                    page.wait_for_selector('//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]', timeout=10000)
                    time.sleep(1.5)  # Give time for details to load
                    place = extract_place(page)
                    if place.name:
                        places.append(place)
                        logging.info(f"✅ {place.name}")
                    else:
                        logging.warning(f"❌ Place {progress}: No name found, skipping")
                except Exception as e:
                    logging.error(f"❌ Failed to extract place {progress}: {str(e)[:100]}...")
        finally:
            browser.close()
            
    logging.info(f"🎉 Scraping completed! Extracted {len(places)}/{total} places")
    return places
