import logging
import sys
from playwright.sync_api import Page


class ColoredFormatter(logging.Formatter):
    """Colored log formatter with icons"""
    
    # Color codes
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
        'RESET': '\033[0m'      # Reset
    }
    
    # Icons
    ICONS = {
        'DEBUG': '🔍',
        'INFO': '✅',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🚨'
    }
    
    def format(self, record):
        # Get color and icon for the log level
        color = self.COLORS.get(record.levelname, self.COLORS['RESET'])
        icon = self.ICONS.get(record.levelname, '📝')
        reset = self.COLORS['RESET']
        
        # Format time
        time_str = self.formatTime(record, '%H:%M:%S')
        
        # Create formatted message
        message = f"{color}{icon} {time_str}{reset} {record.getMessage()}"
        
        return message


def setup_logging():
    """Setup colorful logging with icons"""
    # Create custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Remove default handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Create console handler with custom formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(ColoredFormatter())
    
    logger.addHandler(console_handler)


def extract_text(page: Page, xpath: str) -> str:
    """Extract text from page element, handle multiple matches gracefully"""
    try:
        locator = page.locator(xpath)
        count = locator.count()
        
        if count > 0:
            # If multiple elements found, take the first one
            if count > 1:
                return locator.first.inner_text()
            else:
                return locator.inner_text()
                
    except Exception as e:
        # Only log warning for unexpected errors, not for missing elements
        if "timeout" not in str(e).lower() and "not found" not in str(e).lower():
            logging.debug(f"Could not extract text: {xpath[:50]}...")
    
    return ""
