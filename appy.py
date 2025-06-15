from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# 🔑 あなたのLINEチャネル情報をここに貼る！
CHANNEL_ACCESS_TOKEN = 'jCo+7hn+QLJzuPTXr/9nM6MG5nxpTo171djApJGmlGa/gxSCc7GIDMtbC24EZ2GPPx01aF40sH2XBaHr6TFz0zK2ow7ml5xdekynycnffERcSjLtPr81eL6ik2A1P3gFyGMVCX8SbMw9ygPg+0zl7QdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = 'bce373e918202e93c46d5934cc6ad79e'

# Flaskアプリの初期化
app = Flask(__name__)
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# Webhookのエンドポイント
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"エラー: {e}")
        return 'Error', 400

    return 'OK'

# メッセージを受け取ったときの動作
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text

    if 'リマインド' in user_message:
        reply_text = 'リマインドをセットしました！（※時間指定はまだ未対応です）'
    else:
        reply_text = f'あなたのメッセージ：{user_message}'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
