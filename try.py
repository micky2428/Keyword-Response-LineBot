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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        message)

if __name__ == "__main__":
    app.run()
