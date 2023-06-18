from pyfiglet import Figlet
import argparse
from concurrent.futures import ThreadPoolExecutor
from poc import DocumentEdit_SQL,DocumentEdit_deal,download_ftp,smartupload_rce,downloadhtp,downloadservlet,fileupload_controller,OfficeServer_upload,download_old


if __name__== "__main__":
    f=Figlet(font='doom')
    print('\033[31m====================================================\033[0m')
    print('\033[34m{}\033[0m'.format(f.renderText('xk-exp')))
    print('\033[31m====================================================\033[0m'+'\n')


thread_pool = ThreadPoolExecutor(max_workers=10)

def poc_task(url):
    DocumentEdit_SQL.poc(url)
    DocumentEdit_deal.poc(url)
    download_ftp.poc(url)
    smartupload_rce.poc(url)
    downloadhtp.poc(url)
    downloadservlet.poc(url)
    fileupload_controller.poc(url)
    download_old.poc(url)
    OfficeServer_upload.poc(url)

def process_url(url):
    if url[:4] != "http":
        url = "http://" + url
    poc_task(url)

def process_file(file_path):
    with open(file_path, "r") as f:
        for line in f.readlines():
            url = line.strip()
            if url:
                thread_pool.submit(process_url, url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-u', '--url', default='', dest='poc_url')
    parser.add_argument('-f', '--file', default='', dest='poc_file')
    args = parser.parse_args()

    if args.poc_url:
        process_url(args.poc_url)
    elif args.poc_file:
        process_file(args.poc_file)
thread_pool.shutdown()






    




