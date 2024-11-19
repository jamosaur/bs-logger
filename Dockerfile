FROM python:3.12

ADD . .

RUN pip install requests
RUN pip install python-dotenv
RUN pip install easyocr
RUN pip install discord.py
RUN pip install pillow

CMD ["python", "/bot.py"]
