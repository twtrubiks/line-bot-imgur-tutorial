# line-bot-imgur-tutorial

透過 imgur api 製作簡單 line bot

## 教學

詳細 line bot 教學，請參考之前寫的  [line-bot-tutorial](https://github.com/twtrubiks/line-bot-tutorial)

## 特色

* 傳任意圖片給 line bot 機器人，機器人將自動幫你把圖片上傳到 imgur ( imgur 相簿可以事先定義好 )。
* 從大家上傳的圖片中任意回傳一張圖片給使用者。

## imgur  api 說明

請到下方獲取自己的 CLIENT_ID , CLIENT_SECRET

![alt tag](http://i.imgur.com/nQNQVD7.jpg)

 album_id 直接從相簿網址的最後看就可以看到了。

[config.py](https://github.com/twtrubiks/line-bot-imgur-tutorial/blob/master/config.py)  裡面為自己的 imgur 的 key

請記得將下方修改為自己的

```python
# imgur key
client_id = 'YOUR_IMGUR_CLIENT_ID'
client_secret = 'YOUR_IMGUR__CLIENT_SECRET'
album_id = 'YOUR_IMGUR_ALBUM_ID'
access_token = 'YOUR_IMGUR_ACCESS_TOKEN'
refresh_token = 'YOUR_IMGUR_ACCESS_TOKEN'

# line bot key
line_channel_access_token = 'YOUR_CHANNEL_ACCESS_TOKEN'
line_channel_secret = 'YOUR_CHANNEL_SECRET'
```

[auth.py](https://github.com/twtrubiks/line-bot-imgur-tutorial/blob/master/auth.py) 這支程式為取得 token ( access_token 以及 refresh_token )， 第一次執行時，需要請你輸入 pincode ，如下圖

![alt tag](http://imgur.com/xRW2WAF.jpg)

[upload_imgur_demo_1.py](https://github.com/twtrubiks/line-bot-imgur-tutorial/blob/master/upload_imgur_demo_1.py) 為測試  [imgurpython](https://github.com/Imgur/imgurpython) 上傳 api 簡單範例。

[upload_imgur_demo_2.py](https://github.com/twtrubiks/line-bot-imgur-tutorial/blob/master/upload_imgur_demo_2.py) 為取得token ( access_token 以及 refresh_token ) 之後， 透過下方 api 上傳圖片到自己指定的相簿。

( 透過 access_token 以及 refresh_token 可以不用再輸入 pincode )

```python
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
```

詳細範例可參考  [imgurpython](https://github.com/Imgur/imgurpython)，上傳範例為官方範例簡單修改。

### 執行畫面

請先加入好友

我的 QRCODE

![alt tag](http://imgur.com/P5GdOKX.jpg)

或是手機直接點選  [https://line.me/R/ti/p/%40gmy1077x](https://line.me/R/ti/p/%40gmy1077x)

***功能***

![alt tag](http://imgur.com/tcA7GZI.jpg)

![alt tag](http://imgur.com/cRdq9An.jpg)

![alt tag](http://imgur.com/4oOmbB6.jpg)

## 執行環境

* Python 3.6.2

## Reference

* [line messaging-api](https://devdocs.line.me/en/#messaging-api)
* [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
* [imgurpython](https://github.com/Imgur/imgurpython)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
