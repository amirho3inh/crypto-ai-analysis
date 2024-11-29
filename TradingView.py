import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

class CryptoAPI:
    def __init__(self, symbol):
        self.symbol = symbol
        self.news_url = os.getenv("NEWS_URL").format(symbol=symbol)
        self.ideas_url = os.getenv("IDEAS_URL").format(symbol=symbol)

    def get_news(self):
        try:
            response = requests.get(self.news_url)
            response.raise_for_status()
            news_result = response.json().get('items', [])
            filtered_data = [
                {
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "provider": item.get("provider"),
                    "sourceLogoId": item.get("sourceLogoId"),
                    "published": item.get("published"),
                    "source": item.get("source"),
                    "urgency": item.get("urgency"),
                    "link": item.get("link") if item.get("link") is not None else "No link available"
                }
                for item in news_result]
            return {
                "count": len(filtered_data),
                "news": filtered_data
            }
        except Exception as e:
            return {"error": str(e)}

    def get_ideas(self):
        try:
            response = requests.get(self.ideas_url)
            response.raise_for_status()
            ideas_result = response.json().get('data', {}).get('ideas', {}).get('data', []).get('items', [])
            filtered_data = [
                {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "description": item.get("description"),
                    "created_at": item.get("created_at"),
                    "date_timestamp": item.get("date_timestamp"),
                    "user.id": item.get("user", {}).get("id") if isinstance(item.get("user"), dict) else None,
                    "user.username": item.get("user", {}).get("username") if isinstance(item.get("user"), dict) else None,
                    "image.big": item.get("image", {}).get("big") if isinstance(item.get("image"), dict) else "No image big available",
                    "image.middle": item.get("image", {}).get("middle") if isinstance(item.get("image"), dict) else "No image middle available",
                    "image.middle_webp": item.get("image", {}).get("middle_webp") if isinstance(item.get("image"), dict) else "No image middle webp available",
                    "image.bg_color": item.get("image", {}).get("bg_color") if isinstance(item.get("image"), dict) else "No image bg color available",
                    "chart_url": item.get("chart_url") if item.get("chart_url") is not None else "No chart available"
                }
                for item in ideas_result
            ]
            return {
                "count": len(filtered_data),
                "ideas": filtered_data
            }
        except Exception as e:
            return {"error": str(e)}


class TradingViewAPI:
    def __init__(self, symbol):
        self.crypto = CryptoAPI(symbol)

    def get_all_data(self):
        news = self.crypto.get_news()
        ideas = self.crypto.get_ideas()

        return json.dumps({
            "news": news,
            "ideas": ideas
        }, indent=2)
