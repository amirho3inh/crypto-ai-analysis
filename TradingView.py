import requests
import json
import os
from dotenv import load_dotenv

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
            return {
                "count": len(news_result),
                "news": news_result
            }
        except Exception as e:
            return {"error": str(e)}

    def get_ideas(self):
        try:
            response = requests.get(self.ideas_url)
            response.raise_for_status()
            ideas_result = response.json()['data']['ideas']['data']
            return {
                "count": len(ideas_result),
                "ideas": ideas_result
            }
        except Exception as e:
            return {"error": str(e)}


class TradingViewAPI:
    def __init__(self, symbol):
        self.crypto = CryptoAPI(symbol)

    def get_all_data(self):
        """
        دریافت ترکیبی از اخبار و ایده‌ها
        :return: JSON شامل اخبار و ایده‌ها
        """
        news = self.crypto.get_news()
        ideas = self.crypto.get_ideas()

        return json.dumps({
            "news": news,
            "ideas": ideas
        }, indent=2)
