# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import re

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」

# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能

# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない

agenda = []
date = []

@respond_to('アジェンダ表示')
def mention_func(message):
    message.reply(date[1] + "のミーティングアジェンダです")
    for i in range(len(agenda)):
        message.send(" +" + agenda[i] + "\n")

@respond_to(r'ミーティング設定：.*')
def menttion_func(message):
    global date
    date = message.body['text']
    date = re.split('ミーティング設定：',date)
    message.reply("ミーティングを"+date[1]+"に設定しました")

@respond_to(r'追加：.*')
def menttion_func(message):
    text = message.body['text']
    text = re.split('追加：',text)
    agenda.append(text[1])
    message.reply("議題「"+text[1]+"」を追加しました")
