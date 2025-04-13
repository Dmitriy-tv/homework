import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def currency_conversion(currency: dict[str, object], sum_transaction: float) -> Any:
    """Конвертирует валюту через API и возвращает его в виде float"""

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={sum_transaction}"
    try:
        response = requests.get(url, headers={"apikey": API_KEY})
        response.raise_for_status()
        print(response)
    except requests.exceptions.RequestException:
        return 0.00

    response_data = json.loads(response.text)
    print(response_data)
    return round(response_data["result"], 2)
