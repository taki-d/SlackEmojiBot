from slackbot.bot import respond_to, listen_to
import slackbot_settings
from plugins.upload import upload_emoji



@respond_to('who')
def cheer(message):
    message.reply("I'm Emoji Bot")


@listen_to('(.*)')
def anyonemessage(message, something):
    if 'file' in message.body:
        slack_token = slackbot_settings.API_TOKEN

        url = message.body['file']['url_private_download']
        filename = url.split("/")[-1]
        name = filename.split(".")[0]
        error = upload_emoji(url, name)

        if error != "":
            message.send("error: " + error + "  :no_good: \n"
                                             "Please tell @kinoshita to fix this problem  :bow: ")

        else:
            message.send("Added Emoji  :" + name + ": \n"
                                                   "name : " + name)

    else:
        message.reply('Please send picture')