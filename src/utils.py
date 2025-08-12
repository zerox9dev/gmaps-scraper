# --------------------------------------------------------------------------
# Утиліти для логування та роботи з веб-сторінками
# Utilities for logging and web page interactions
# --------------------------------------------------------------------------

import logging
import sys
from playwright.sync_api import Page


class ColoredFormatter(logging.Formatter):
    # --------------------------------------------------------------------------
    # Кольоровий форматер логів з іконками
    # Colored log formatter with icons
    # --------------------------------------------------------------------------
    """Colored log formatter with icons"""
    
    # --------------------------------------------------------------------------
    # Коди кольорів для різних рівнів логування
    # Color codes for different log levels
    # --------------------------------------------------------------------------
    COLORS = {
        'DEBUG': '\033[36m',    # Циан / Cyan
        'INFO': '\033[32m',     # Зелений / Green
        'WARNING': '\033[33m',  # Жовтий / Yellow
        'ERROR': '\033[31m',    # Червоний / Red
        'CRITICAL': '\033[35m', # Пурпуровий / Magenta
        'RESET': '\033[0m'      # Скидання / Reset
    }
    
    # --------------------------------------------------------------------------
    # Іконки для різних рівнів логування
    # Icons for different log levels
    # --------------------------------------------------------------------------
    ICONS = {
        'DEBUG': '🔍',
        'INFO': '✅',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🚨'
    }
    
    def format(self, record):
        # --------------------------------------------------------------------------
        # Отримання кольору та іконки для рівня логування
        # Get color and icon for the log level
        # --------------------------------------------------------------------------
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        icon = self.ICONS.get(record.levelname, '📝')
        reset = self.COLORS['RESET']
        
        # Форматування часу
        # Format time
        time_str = self.formatTime(record, '%H:%M:%S')
        
        # Створення форматованого повідомлення
        # Create formatted message
        message = f"{color}{icon} {time_str}{reset} {record.getMessage()}"
        
        return message


def setup_logging():
    # --------------------------------------------------------------------------
    # Налаштування кольорового логування з іконками
    # Setup colorful logging with icons
    # --------------------------------------------------------------------------
    """Setup colorful logging with icons"""
    
    # Створення власного логера
    # Create custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Видалення стандартних обробників
    # Remove default handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Створення обробника консолі з власним форматером
    # Create console handler with custom formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ColoredFormatter())
    
    logger.addHandler(console_handler)


def extract_text(page: Page, xpath: str) -> str:
    # --------------------------------------------------------------------------
    # Витягування тексту з елемента сторінки, обробка кількох збігів
    # Extract text from page element, handle multiple matches gracefully
    # --------------------------------------------------------------------------
    """Extract text from page element, handle multiple matches gracefully"""
    
    try:
        locator = page.locator(xpath)
        count = locator.count()
        
        if count > 0:
            # Якщо знайдено кілька елементів, взяти перший
            # If multiple elements found, take the first one
            if count > 1:
                return locator.first.inner_text()
            else:
                return locator.inner_text()
                
    except Exception as e:
        # Логувати попередження лише для неочікуваних помилок, не для відсутніх елементів
        # Only log warning for unexpected errors, not for missing elements
        if "timeout" not in str(e).lower() and "not found" not in str(e).lower():
            logging.debug(f"Could not extract text: {xpath[:50]}...")
    
    return ""
