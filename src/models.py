# --------------------------------------------------------------------------
# Моделі даних для зберігання інформації про місця
# Data models for storing information about places
# --------------------------------------------------------------------------

from dataclasses import dataclass
from typing import Optional


@dataclass
class Place:
    # --------------------------------------------------------------------------
    # Основна інформація про місце
    # Basic place information
    # --------------------------------------------------------------------------
    
    # Назва місця/бізнесу
    # Name of the place/business
    name: str = ""
    
    # Адреса місця
    # Address of the place
    address: str = ""
    
    # Веб-сайт
    # Website
    website: str = ""
    
    # Номер телефону
    # Phone number
    phone_number: str = ""
    
    # --------------------------------------------------------------------------
    # Рейтинги та відгуки
    # Ratings and reviews
    # --------------------------------------------------------------------------
    
    # Кількість відгуків
    # Number of reviews
    reviews_count: Optional[int] = None
    
    # Середній рейтинг
    # Average rating
    reviews_average: Optional[float] = None
    
    # --------------------------------------------------------------------------
    # Додаткова інформація про послуги
    # Additional service information
    # --------------------------------------------------------------------------
    
    # Покупки в магазині (так/ні)
    # In-store shopping (yes/no)
    store_shopping: str = "No"
    
    # Самовивіз з магазину (так/ні)
    # In-store pickup (yes/no)
    in_store_pickup: str = "No"
    
    # Доставка з магазину (так/ні)
    # Store delivery (yes/no)
    store_delivery: str = "No"
    
    # Тип місця (ресторан, магазин, тощо)
    # Type of place (restaurant, store, etc.)
    place_type: str = ""
    
    # Час відкриття
    # Opening hours
    opens_at: str = ""
    
    # Опис/введення
    # Description/introduction
    introduction: str = ""
