import csv
import openpyxl
import pandas as pd
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('b+YZPLfqivSa3tY+uUr0nPP6tI4i3U6wChIrcjhIs6UlsdSF56k1S8E7EdDpvjRj8edR2U7bF9yDOjzcLqK7nG2ANizVg1XWHl+QxI8OLajHKteoE4Jprd3ZWRfDLgyIOll2KVNj6a0BbdckA0xtEwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fb9bfa5297b2c04a610fde0caf3f74a5')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

alllst = pd.read_excel("final.xlsx")
products = []
websites = []
for row in alllst.iterrows():
        products.append(row[1]["商品型號"])
        websites.append(row[1]["照片"])
dic = {}
for num in range(len(websites)):
        dic[num+1] = [products[num],websites[num]]
 
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext =='info':
        message = TextSendMessage(text='''歡迎使用小廢柴2.0🙌 
請輸入查核表的編號🤖
您將收到對應的圖片''')
        line_bot_api.reply_message(
            event.reply_token, message)       
    elif mtext =='0':
        message = TextSendMessage(text='''未附圖片''')
        line_bot_api.reply_message(
            event.reply_token, message) 
   
    elif int(mtext) in dic:        
        message = TextSendMessage(text = "'''"+dic[mtext][0]+"'''")
        line_bot_api.reply_message(
            event.reply_token, message) 
        if dic[mtext][1] != "None":
            image_message = ImageSendMessage(
            original_content_url= "'" + dic[mtext][1] +"'",
            preview_image_url= "'" +dic[mtext][1]+"'"
            )
            line_bot_api.reply_message(event.reply_token, image_message)
        else:
            wordmessage = TextSendMessage(text = "'''"+dic[mtext][1]+"'''")
            line_bot_api.reply_message(
                event.reply_token, wordmessage)

    
            

if __name__ == "__main__":
    app.run()
