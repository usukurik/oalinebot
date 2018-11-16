import errno

import os

import sys

import tempfile



from flask import Flask, request, abort



from linebot import (

    LineBotApi, WebhookHandler

)

from linebot.exceptions import (

    InvalidSignatureError

)

from linebot.models import *

import requests, json



from linebot.models import (

    MessageEvent, TextMessage, TextSendMessage,

    SourceUser, SourceGroup, SourceRoom,

    TemplateSendMessage, ConfirmTemplate, MessageAction,

    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,

    PostbackAction, DatetimePickerAction,

    CarouselTemplate, CarouselColumn, PostbackEvent,

    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,

    ImageMessage, VideoMessage, AudioMessage, FileMessage,

    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,

    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,

    TextComponent, SpacerComponent, IconComponent, ButtonComponent,

    SeparatorComponent,

)



app = Flask(__name__)



# Channel Access Token

line_bot_api = LineBotApi('S23UsHtGQz0prriXJjTaVYFv5XOpYBEFB55pP24OW+V/oMzKk2JKsTU1ejYtsEjsxAeOURfqx6DxLvED2puqb7V/hkgttEtgS8B9dG3f8plq6FOY2SHZBRCOzMECaRoxTIWKbcO7tC7uPj1/d8QQSAdB04t89/1O/w1cDnyilFU=')

# Channel Secret

handler = WebhookHandler('5a8da5e914b5698358a01e4ce9973d03')

#===========[ NOTE SAVER ]=======================

notes = {}



# Post Request

@app.route("/callback", methods=['POST'])

def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    try:

        handler.handle(body, signature)

    except InvalidSignatureError:

        abort(400)

    return 'OK'



@handler.add(JoinEvent)

def handle_join(event):

    line_bot_api.reply_message(

        event.reply_token,

        TextSendMessage(text='Type /help for command :D')) 

    

@handler.add(MessageEvent, message=TextMessage)

def handle_text_message(event):

    text = event.message.text

    

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):

    text = event.message.text #simplify for receove message

    sender = event.source.user_id #get user_id

    gid = event.source.sender_id #get group_id

    

#=====[ LEAVE GROUP OR ROOM ]==========[ Ucup ]======================

    if text == '/me':

        if isinstance(event.source, SourceUser):

            profile = line_bot_api.get_profile(event.source.user_id)

            line_bot_api.reply_message(

                event.reply_token, [

                    TextSendMessage(text='Display name: ' + profile.display_name),

                    TextSendMessage(text='Status message: ' + profile.status_message)

                ]

            )

        else:

            line_bot_api.reply_message(

                event.reply_token,

                TextSendMessage(text="Bot can't use profile in group chat"))



    if text == '#ucupbye':

        if isinstance(event.source, SourceGroup):

            line_bot_api.reply_message(

                event.reply_token, TextSendMessage(text='Ucup pergi bye-bye'))

            line_bot_api.leave_group(event.source.group_id)

        elif isinstance(event.source, SourceRoom):

            line_bot_api.reply_message(

                event.reply_token, TextSendMessage(text='Ucup pergi bye-bye'))

            line_bot_api.leave_room(event.source.room_id)

        else:

            line_bot_api.reply_message(

                event.reply_token,

                TextSendMessage(text="Bot can't leave from 1:1 chat"))

#=====[ TES MESSAGE ]=============[ Ucup ]======================

    if text == "redtube on":

    	angka = random.randint(1, 20)

    	r = requests.get('https://api.eater.pw/redtube/{}'.format(angka))

    	data=r.text

    	data=json.loads(data)

    	for anu in data["result"]:

        	line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))

    elif text == "xvideos on":

    	angka = random.randint(1, 20)

    	r = requests.get('https://api.eater.pw/xvideos/{}'.format(angka))

    	data=r.text

    	data=json.loads(data)

    	for anu in data["result"]:

    		line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))

#=====[ TES MESSAGE ]=============[ Ucup ]======================

    elif text == 'confirm':

        confirm_template = ConfirmTemplate(text='Bot nya bagus?', actions=[

            MessageTemplateAction(label='Yes', text='Yes!'),

            MessageTemplateAction(label='No', text='No!'),

        ])

        template_message = TemplateSendMessage(

            alt_text='Confirm alt text', template=confirm_template)

        line_bot_api.reply_message(event.reply_token, template_message)

    elif "/idline: " in event.message.text:

        skss = event.message.text.replace('/idline: ', '')

        sasa = "http://line.me/R/ti/p/~" + skss

        text_message = TextSendMessage(text=sasa)

        line_bot_api.reply_message(event.reply_token, text_message)

        return 0

    elif "/apakah " in event.message.text:

        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')

        jwb = random.choice(quo)

        text_message = TextSendMessage(text=jwb)

        line_bot_api.reply_message(event.reply_token, text_message)

        return 0

    elif (text == 'Bot') or (text == 'bot'):

        message = TextSendMessage(text='Siapa bot? ke bot an lu')

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Tes') or (text == 'tes') or (text == 'Test') or (text == 'test'):

        message = TextSendMessage(text='suk beybeh')

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Ucup') or (text == 'Cup') or (text == 'cup') or (text == 'yusuf'):

        message = TextSendMessage(text='Apa manggil-manggil cogan')

        line_bot_api.reply_message(event.reply_token, message)

    elif text == '.':

        message = TextSendMessage(text='Titik titik amat so high lu')

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Bah') or (text == 'bah'):

        message = TextSendMessage(text='Beh')

        line_bot_api.reply_message(event.reply_token, message)

#=====[ TEMPLATE MESSAGE ]=============[ Ucup ]======================

    elif text == '/tools':

        buttons_template = TemplateSendMessage(

            alt_text='Tools message',

            template=ButtonsTemplate(

                title='[ TOOLS MESSAGE ]',

                text= 'Tap the Button',

                actions=[

                    MessageTemplateAction(

                        label='App Cloner',

                        text='/app clone'

                    ),

                    MessageTemplateAction(

                        label='Cek idline',

                        text='/idline: yuta221217'

                    ),

                    MessageTemplateAction(

                        label='Your profile',

                        text='/me'

                    )

                ]

            )

        )

        

        line_bot_api.reply_message(event.reply_token, buttons_template)

    elif (text == '/help') or (text == 'help') or (text == 'Help'):

        buttons_template = TemplateSendMessage(

            alt_text='Help message',

            template=ButtonsTemplate(

                title='[ HELP MESSAGE ]',

                text= 'Tap the Button',

                actions=[

                    MessageTemplateAction(

                        label='My Creator',

                        text='/creator'

                    ),

                    MessageTemplateAction(

                        label='List bot',

                        text='/bots ucup'

                    ),

                    MessageTemplateAction(

                        label='Tools',

                        text='/tools'

                    ),

                    MessageTemplateAction(

                        label='Bot bye',

                        text='#Ucupbye'

                    )

                ]

            )

        )

        

        line_bot_api.reply_message(event.reply_token, buttons_template)

#=====[ CAROUSEL MESSAGE ]==========[ Ucup ]======================

    elif text == '/bots cup':

        message = TemplateSendMessage(

            alt_text='List Bot',

            template=CarouselTemplate(

                columns=[

                    CarouselColumn(

                        title='Bots v1',

                        text='ucup public bot v1',

                        actions=[

                            URITemplateAction(

                                label='>ucup bot<',

                                uri='https://line.me/ti/p/~yuta221217'

                            )

                        ]

                    ),

                    CarouselColumn(

                        title='Bots v2',

                        text='ucup public bot v2',

                        actions=[

                            URITemplateAction(

                                label='>ucup bot<',

                                uri='https://line.me/ti/p/~yuta221217'

                            )

                        ]

                    ),

                    CarouselColumn(

                        title='Bots official',

                        text='ucup public bot official',

                        actions=[

                            URITemplateAction(

                                label='>ucup bot<',

                                uri='https://line.me/ti/p/yuta221217'

                            )

                        ]

                    ),

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == '/creator') or (text == 'About'):

        message = TemplateSendMessage(

            alt_text='My creator',

            template=CarouselTemplate(

                columns=[

                    CarouselColumn(

                        title='Creator-PC',

                        text='This is my creator',

                        actions=[

                            URITemplateAction(

                                label='>ucup<',

                                uri='https://line.me/ti/p/~yuta221217'

                            )

                        ]

                    ),

                    CarouselColumn(

                        title='Creator-OA',

                        text='This is my creator',

                        actions=[

                            URITemplateAction(

                                label='>ucup<',

                                uri='https://line.me/ti/p/~yuta221217'

                            )

                        ]

                    ),

                    CarouselColumn(

                        title='OA-FAMS',

                        text='This is my Fams',

                        actions=[

                            URITemplateAction(

                                label='>ucup<',

                                uri='https://line.me/ti/p/~yuta221217'

                            )

                        ]

                    ),

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text == "/app clone":

        buttons_template = TemplateSendMessage(

            alt_text='App clone',

            template=ButtonsTemplate(

                title='Aplikasi clone',

                text='Klik salah satu menu dibawah ini.',

                thumbnail_image_url='https://imgur.com/Hbv4GWl.jpg',

                actions=[

                    URITemplateAction(

                        label='Parallel Space',

                        uri='https://play.google.com/store/apps/details?id=com.lbe.parallel.intl'

                    ),

                    URITemplateAction(

                        label='APP Cloner',

                        uri='https://play.google.com/store/apps/details?id=com.applisto.appcloner'

                    ),

                    URITemplateAction(

                        label='2Accounts',

                        uri='https://play.google.com/store/apps/details?id=com.excelliance.multiaccount'

                    ),

                    URITemplateAction(

                        label='Multi clone',

                        uri='https://play.google.com/store/apps/details?id=com.jumobile.multiapp'

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, buttons_template)

        return 0

#=====[ FLEX MESSAGE ]==========[ Ucup ]======================

    elif text == 'cup test':

        message = ImagemapSendMessage(

            base_url='https://i.imgur.com/g8P1V9Q.jpg',

            alt_text='manyimak corom',

            base_size=BaseSize(height=1040, width=1040),

            actions=[

                URIImagemapAction(

                    link_uri='https://line.me/ti/p/~yuta221217',

                    area=ImagemapArea(

                        x=0, y=0, width=1040, height=1040

                    )

                ),

                MessageImagemapAction(

                    text='ucup ganteng',

                    area=ImagemapArea(

                        x=520, y=0, width=520, height=1040

                    )

                )

            ]

        )

        line_bot_api.reply_message(event.reply_token, message)

#=====[ Sticker MESSAGE ]==========[ Ucup ]======================

    elif (text == 'makasih') or (text == 'Makasih'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/153453/IOS/sticker.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'nyimak') or (text == 'Nyimak'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/13162615/IOS/sticker.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'good night') or (text == 'Good night') or (text == 'selamat malam') or (text == 'Selamat malam'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683546/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'hai') or (text == 'Hai') or (text == 'halo') or (text == 'Halo'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002738/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'sabar') or (text == 'Sabar'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'wkwk') or (text == 'Wkwk'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/27695296/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'hehe') or (text == 'Hehe'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002763/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'siap') or (text == 'Siap'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626520/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif text == '?':

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'please') or (text == 'Please') or (text == 'tolong') or (text == 'Tolong'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626499/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'ok') or (text == 'oke') or (text == 'Ok') or (text == 'Oke'):

        message = TemplateSendMessage(

            alt_text='Ucup public bot',

            template=ImageCarouselTemplate(

                columns=[

                    ImageCarouselColumn(

                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626500/IOS/sticker_animation@2x.png',

                        action=URIAction(uri='http://line.me/ti/p/~yuta221217')

                    )

                ]

            )

        )

        line_bot_api.reply_message(event.reply_token, message)

#=======================================================================================================================

import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
