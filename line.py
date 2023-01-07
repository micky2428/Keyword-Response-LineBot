#https://github.com/helgesander02/den_no_suke_LineBot/blob/main/hellofly.py

#https://github.com/SkyLiNing823/line-bot-python-on-render/blob/master/app.py

#https://github.com/colinjen88/line-bot-python-on-render/blob/master/render.yaml


import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('b+YZPLfqivSa3tY+uUr0nPP6tI4i3U6wChIrcjhIs6UlsdSF56k1S8E7EdDpvjRj8edR2U7bF9yDOjzcLqK7nG2ANizVg1XWHl+QxI8OLajHKteoE4Jprd3ZWRfDLgyIOll2KVNj6a0BbdckA0xtEwdB04t89/1O/w1cDnyilFU=', None))
handler = WebhookHandler(os.getenv('fb9bfa5297b2c04a610fde0caf3f74a5', None))

                                         
@app.route("/callback", methods=['POST'])
    # 取得網路請求的標頭 X-Line-Signature 內容，確認請求是從 LINE Server 送來的
def callback():
    signature = request.headers['X-Line-Signature']
    # 將請求內容取出
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_text = event.message.text   
    # App功能介紹
    if msg_text =='使用說明':
         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='歡迎使用小廢柴2.0🙌 在這裡您將可以拯救你的眼睛～0請輸入查核表的編號🤖您將收到對應的圖片'))


if __name__ == "__main__":
    app.run()
