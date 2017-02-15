# SlackEmojiBot

## What`s this?
Slackで絵文字を追加するのって、リサイズしたり面倒くさいじゃないですか、イメージを投げると適当なBotを作れば便利かと思ってEmojiを追加するBotをPythonでつくりました

## How to Use
さてまずはいつも通りapitokenを取りに行きます

#### slackbot_settings.py
```
API_TOKEN = "hogefugapiyo-token"

default_reply = "I'm very sleepy"

PLUGINS = [
    'plugins',
]
```
のAPI_TOKENのところに自分のチームのBot用のTokenを発行して記述します。


さて次に、誰か、または絵文字専用のSlack用のアカウントのパスワードを以下のように直に打ちます。
#### plugins/upload.py
```
from bs4 import BeautifulSoup
import requests
from PIL import Image
import shutil

TEAM_NAME = "nittcprocon"

login_url = 'https://' + TEAM_NAME + '.slack.com/'

param = {
    'signin': '1',
    'email': 's1xxxx@tokyo.kosen-ac.jp',
    'password': 'hogefugapiyo',
}

.
.
.
```
見てわかるように、
* TEAM_NAMEのところに自分のチームの名前
* paramの **email** にメールアドレス
* paramの **password** にパスワード

を入力します。

さてここまで来たら、気合いでDockerを使えるようにします。使えるようになったら

```
$ docker build . -t emojibot
```

```
$ docker start emojibot
```

emojibotは任意の文字列で結構です。

## 最後に
LT用に一晩で気合いで作ったので、いろいろと雑です。気が向いたら使いやすいように改修します。あくまで気が向いたらです。
暇な人適当に機能追加してPR投げてくれるとうれしいなぁ...
