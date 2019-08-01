from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot = Flask(__name__)

line_bot_api = LineBotApi('/ujfMwthKlVo/73tkxmuOGi4fMeKwyv6A90my42c0CFfSJeiaHfc+Ls2ga9RbG1F4o/7FQerlYWc8YrWPopJjzY7gUKB777v9Y7qI93j75Z9pPm2fQHcxrTFZWr1PUOEwqHdtMOzzGZMjDbogwW/6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8be36aa787382fe5b87abd94affa7df7')


@line_bot.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    line_bot.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.line_bot(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    line_bot.run()