import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
import linebot.models

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))
    return "OK"

def send_sticker_message(reply_token):
    message = linebot.models.StickerSendMessage(
        package_id = "11537",
        sticker_id = "52002734"
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"
def send_button_message(reply_token):
    message = linebot.models.TemplateSendMessage(
        alt_text='Buttons template',
        template=linebot.models.ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/FwUCnbF.png',
            title='YOUTUBE',
            text='Please select',
            actions=[
                linebot.models.MessageTemplateAction(
                    label='musics',
                    text='music'
                ),
                linebot.models.MessageTemplateAction(
                    label='trending videos',
                    text='video'
                ),
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_carousel_message(reply_token):
    message = linebot.models.TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=linebot.models.ImageCarouselTemplate(
            columns=[
                linebot.models.ImageCarouselColumn(
                    image_url='https://i.imgur.com/2nVjVQM.jpg',
                    action=linebot.models.PostbackTemplateAction(
                        label='study music',
                        text='study',
                        data='action=buy&itemid=1'
                    )
                ),
                linebot.models.ImageCarouselColumn(
                    image_url='https://i.imgur.com/FChq6Yf.jpg',
                    action=linebot.models.PostbackTemplateAction(
                        label='funk music',
                        text='funk',
                        data='action=buy&itemid=2'
                    )
                ),
                linebot.models.ImageCarouselColumn(
                    image_url='https://i.imgur.com/pMvioiT.png',
                    action=linebot.models.PostbackTemplateAction(
                        label='guitar music',
                        text='guitar',
                        data='action=buy&itemid=3'
                    )
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)    
    
    return "OK"

def send_carousel_message2(reply_token):
    message = linebot.models.TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=linebot.models.ImageCarouselTemplate(
            columns=[
                linebot.models.ImageCarouselColumn(
                    image_url='https://i.imgur.com/om4dQrz.png',
                    action=linebot.models.PostbackTemplateAction(
                        label='news',
                        text='news',
                        data='action=buy&itemid=1'
                    )
                ),
                linebot.models.ImageCarouselColumn(
                    image_url='https://i.imgur.com/nhhzFC4.png',
                    action=linebot.models.PostbackTemplateAction(
                        label='movie',
                        text='movie',
                        data='action=buy&itemid=2'
                    )
                ),
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)    
    
    return "OK"

def send_video_message(reply_token):
    message = linebot.models.VideoSendMessage(
        original_content_url = 'https://i.imgur.com/qkEt1pV.mp4',
        preview_image_url = 'https://i.imgur.com/yZP9F4R.jpg'
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, message)

    return "OK"    
"""
def send_image_url(id, img_url):
    message = ImageSendMessage(
    original_content_url = img_url,
    preview_image_url = img_url
    )
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(id, message)

    return "OK"

def send_button_message(id, text, buttons):
    pass
"""