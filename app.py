from flask import Flask,request,render_template
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
app = Flask(__name__,template_folder='templates')


url ="http://ltpapi.xfyun.cn/v2/sa"

x_appid = "8e6ea343"
api_key = "5fd1fbcddb08dbf56852f638fdbd67d9"


def work(TEXT):
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    return result.decode('utf-8')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def upload():

    words = request.form.get('input_text')
    json_data = json.loads(work(words))
    sentiment = json_data['data']['sentiment']
    sentiment = str(sentiment)
    if sentiment=='1':
        return  '正面的'
    elif sentiment=='-1':
        return '负面的'
    elif sentiment=='0':
        return '中立的'
    else:
        return '出bug了'


