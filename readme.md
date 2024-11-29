<div align="center">
    
# Crypto Analysis :rocket:

[![python version][python-version]](#)
[![download size][download-size]](#)
[![version size][version-size]](#)

[python-version]: https://img.shields.io/badge/python-3.12%2B-brightgreen.svg
[download-size]: https://img.shields.io/badge/download-16kb-brightgreen.svg
[version-size]: https://img.shields.io/badge/version-1.3-blue.svg
</div>


just **BINANCE** crypto

## Requirements

features requires the following to run:

  * [Python][Python] 3.12+

[Python]: https://python.com/

## Install

insall packages:
```cmd
pip3 install requests
pip3 install openai
pip3 install streamlit
pip3 install python-dotenv
pip install huggingface_hub --upgrade
```
create `.env` file (copy `.env.example` file) and add OpenAi API key in `.env` file

## Run

in dir open Terminal and run command:
```cmd
streamlit run checker.py
```

## Changing AIs
Open AI Code `GPT`:
```code
from openai_client import OpenAIClient

prompt = "Hello"

openai_client = OpenAIClient()
response = openai_client.get_response(prompt)
```

Huggingface AI Code `Qwen2.5-72B`: :star_struck:`FREE`:free:
```code
from Huggingface import HuggingfaceAIClient

promptTranslate = "Hello"

huggingface_client = HuggingfaceAIClient()
translateResponse = huggingface_client.get_response(promptTranslate)
```


## Resources

- [Python documentation](https://docs.python.org/3/)
- [Open AI API documentation](https://platform.openai.com/docs/api-reference/introduction)
- [huggingface](https://huggingface.co/chat/)
- [Qwen2.5](https://qwenlm.github.io/blog/qwen2.5/)

## License

MIT © [AmirHossein Hashemi](https://github.com/amirho3inh)
