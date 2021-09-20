import requests
import os, sys
import json
green_color = "\033[1;32m"
red_color = "\033[1;31m"
detect_color = "\033[1;34m"
banner_color = "\033[1;33;40m"
end_banner_color = "\33[00m"

r = requests.session()



print ("""

---------------------------------------
                 
(O)\  /(O)          
 `. \/ .'   (O)_  (O)_  (O)_  
   \  /    .' __).' __).' __) 
   /  \   (  _) (  _) (  _)   
 .' /\ `.  )/    )/    )/     
(_.'  `._)(     (     (       

++ The developer : Falah - 0xfff080 ++ 3v 

snapchat : flaah999

https://www.google.com/maps/place

( google maps ) -> 27.470736 , 41.660869

---------------------------------------


    """)

ss = input ('latitude -> ')
ss1 = input ('longitude -> ')

url = "https://api.tellonym.me/suggestions/people?latitude="+ss+"&longitude="+ss1+"&adExpId=94&limit=31"

payload = ""
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "X-Parse-Installation-Id": "25cfde8f-7204-434e-a7fb-dde295ee4f70",
    "User-Agent": "Tellonym/394 CFNetwork/1128.0.1 Darwin/19.6.0",
    "Connection": "close",
    "X-Parse-Application-Id": "RTE8CXsUiVWfG1XlXOyJAxfonvt",
    "Host": "api.tellonym.me",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "__cfduid=d33a508cb83e93afa6ed43597936c019b1602694651",
    "Upgrade-Insecure-Requests": "1",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NzY1OTc2MzksImlhdCI6MTYzMDc5MjM5NX0.a13pTAy30OIdR6XyathRow1heGe1VaRyDJh3u2jOKjc",
    "tellonym-client": "ios:2.51.4:394:13:iPhone10,6",
    "X-Parse-OS-Version": "12.9 (saud)"
}

response = r.get(url, data=payload, headers=headers).text
info = json.loads(response)


for i in range(94):

  if 'peopleSuggestions' in response:
            try:
                print(red_color+"---------------------------------------")
                print(green_color +" --> Name : "+str(info["peopleSuggestions"][i]["displayName"]))
                print(green_color +" --> username : "+str(info["peopleSuggestions"][i]["username"]))
                print(green_color +" --> aboutMe : "+str(info["peopleSuggestions"][i]["aboutMe"]))
            except:
                print ("---E----N----D")
                exit()
