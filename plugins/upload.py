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

def upload_emoji(url,emoji_name):

    # Login
    session = requests.Session()
    response = session.get(login_url)
    bs = BeautifulSoup(response.text, "html.parser")
    auth_token = bs.find(attrs={'name': 'crumb'}).get('value')
    param['crumb'] = auth_token
    session.post(login_url, data=param)

    print(url)

    # DownloadPicture
    files_name = url.split("/")[-1]
    pic_res = session.get(url, stream=True)
    if pic_res.status_code == 200:
        with open(files_name, "wb") as file:
            shutil.copyfileobj(pic_res.raw, file)

    # Resize Image
    image = Image.open(files_name, 'r').resize((125, 125))
    image.save('resize_image.png')
    image.close()

    post_image = open('resize_image.png', 'rb')

    files = {
        'img': post_image,
    }

    # Post Emoji
    res = session.get(login_url + "customize/emoji")
    bs = BeautifulSoup(res.text, "html.parser")
    crumb = bs.find(attrs={'name': 'crumb'}).get('value')

    request_param = {
        'add': 1,
        'name': emoji_name,
        'crumb': crumb,
        'mode': 'data'
    }

    r = session.post(login_url + "customize/emoji", data=request_param, files=files, allow_redirects=False)
    r.raise_for_status()

    if b'alert_error' in r.content:
        soup = BeautifulSoup(r.text, "html.parser")
        error_message = soup.find("p", attrs={"class": "alert_error"})
        print("Error with uploading" + error_message.text)
        return error_message.text

    print("成功")

    return ""
