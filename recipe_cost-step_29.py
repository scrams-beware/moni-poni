# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: RecipeCost
APP_CONFIG = {
    "currency": "RUB",
    "decimal_places": 2,
    "default_servings": 1,
    "price_format": "{:.2f}",
    "report_separator": "=",
}


def init_app():
    """Инициализация приложения с проверкой обязательных настроек."""
    required_keys = {"currency", "decimal_places"}
    missing = required_keys - APP_CONFIG.keys()
    if missing:
        raise ValueError(f"Отсутствуют обязательные настройки: {missing}")


def get_config(key, default=None):
    """Получение значения из конфигурации с дефолтом."""
    return APP_CONFIG.get(key, default)
