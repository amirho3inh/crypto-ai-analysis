from openai_client import OpenAIClient
from TradingView import TradingViewAPI
import streamlit as st

st.title("Cryptocurrency Analysis")
symbol = st.text_input("Enter a symbol BTC,ETH,ADA").upper().strip()
TranslateLanguage = st.selectbox(
    "Translate to ?",
    ("English", "swedish", "Arabic"),
)
btn = st.button("Check")

if symbol != "" and btn:
    trading_view_api = TradingViewAPI(symbol)
    news_data = trading_view_api.crypto.get_news()
    ideas_data = trading_view_api.crypto.get_ideas()

    news_count = news_data.get('count')
    ideas_count = ideas_data.get('count')

    promptNews = f"""
    این خبر ها و ایده ها را تحلیل کن و در نهایت به من بگو که خبرها و ایده ها مثبت هستند یا منفی
    خروجی به صورت جدول باشه و خبر ها و ایده ها جدا باشد و فقط 5 تا ی مهم رو برای هرکدوم نمایش بده
    به لینک و ساعت انتشار و منبع آن اشاره کن
    اگر ایده ها لینک چارت (chart_url) یا لینک عکس (image.big) دارن به جدول اضافه کن
    درنهایت به من توصیه کن که بخرم یا نخرم یا نگه دارم و تحلیل ایده ها هم بگو
     همه چیز به فارسی بگو بعد به آخرش ترجمه اش رو به {TranslateLanguage} هم بگو
    خبرها :
    {news_data}
    ایده ها :
    {ideas_data}
    عنوان متن ترجمه شده فقط این باشه "Translate To {TranslateLanguage}" نوشته اضافه نداشته باشه
    """

    openai_client = OpenAIClient()
    response = openai_client.get_response(promptNews)

    st.header("Number of input data", divider="gray")
    st.html(f"<div>news count: <b>{news_count}</b></div><div>ideas count: <b>{ideas_count}</b></div>")
    st.header("Response", divider="gray")
    st.markdown(response)
