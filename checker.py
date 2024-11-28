from openai_client import OpenAIClient
from TradingView import TradingViewAPI
import streamlit as st

st.title("تحلیل ارز دیجیتال")
symbol = st.text_input("Enter a symbol BTC,ETH,ADA").upper().strip()
btn = st.button("Check")

if symbol != "" and btn:
    trading_view_api = TradingViewAPI(symbol)
    news_data = trading_view_api.crypto.get_news()
    ideas_data = trading_view_api.crypto.get_ideas()

    news_count = trading_view_api.crypto.get_news().get("count")
    ideas_count = trading_view_api.crypto.get_ideas().get("count")

    promptNews = f"""
    این خبر ها و ایده ها را تحلیل کن و در نهایت به من بگو که خبرها و ایده ها مثبت هستند یا منفی
    خروجی به صورت جدول باشه و خبر ها و ایده ها جدا باشد
    به لینک و ساعت انتشار و منبع آن اشاره کن
    درنهایت به من توصیه کن که بخرم یا نخرم یا نگه دارم و تحلیل ایده ها هم بگو
    همه چیز به فارسی بگو
    خبرها :
    {news_data}
    ایده ها :
    {ideas_data}
    """

    openai_client = OpenAIClient()
    response = openai_client.get_response(promptNews)
    st.divider()
    st.html(f"<div>news count: <b>{news_count}</b></div><div>ideas count: <b>{ideas_count}</b></div>")
    st.divider()
    st.markdown(response)

