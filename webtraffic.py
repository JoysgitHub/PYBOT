import requests
import time
import random
from urllib3.exceptions import InsecureRequestWarning
import sys
from datetime import  datetime
from  fake_useragent import UserAgent


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

urlList = [ "https://cw2-student.infinityfreeapp.com/index.php",
        "https://cw2-student.infinityfreeapp.com/admin/index.php"]

proxyList = [
'http://34.126.125.90:8080',
'http://8.219.97.248:80',
'http://206.81.31.215:80',
'http://5.252.23.206:3128',
'http://34.126.125.90:8080',
'http://95.217.178.175',
'http://114.129.2.82:8081',
'http://154.38.171.242:80',
'http://65.21.159.49:80',
'http://185.217.143.96:80',
'http://130.58.218.30:80',
'http://133.18.234.13:80',
'http://183.234.215.11:8443',
'http://116.203.49.36:80'
]

def getProxy():
        loop = True
        while loop:
        
            ip = random.choice(proxyList)

            proxy = {'https': ip,
                    'http': ip}

            try:
                res = requests.get("https://ipinfo.io/json", proxies=proxy, timeout=6)
                if res.status_code == 200:
                    return ip
                    loop = False
                else:
                    continue
            except:
                continue 






def webBot():
    ua = UserAgent(browsers=["chrome", "edge", "firefox", "safari"])
    total = 0
    success = 0
    fail = 0
    while True:


        try:     
            user_agent = {'User-Agent': str(ua.random)}
            url = random.choice(urlList)
            ranTime = random.randint(1000, 5400)
            now = datetime.now()
            ip = getProxy()
            proxies = {'https': ip,
                    'http': ip}

            try:
                response  = requests.get(url, headers = user_agent, proxies=proxies, verify=False)



                if response.status_code == 200:
                    print("DATETIME: ",now)
                    print("IP: ",ip)
                    print("URL: ", url)
                    print("RESPONSE: 200  \n \ \n  ---- ", user_agent)
                    success += 1
                else:
                    print("DATETIME: ",now)
                    print("URL: ", url)
                    print("RESPONSE: FAIL, ", response.status_code)
                    fail += 1

                total += 1
                print("TTNR: ", ((ranTime / 60) / 60), " HRS" )
                print("-"* 60)
            except:
                fail += 1
                continue

            time.sleep(ranTime)

        except KeyboardInterrupt:
            print(f"SUCCESS: {success}\nFAIL: {fail}\nTOTAL: {total}")
            sys.exit()





webBot()
