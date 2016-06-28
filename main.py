#coding:utf-8

#!usr/bin/python

import requests
import string,re,os
from Model import QuestionItem,UserInfo
from bs4 import BeautifulSoup #用于解析html数据

baseUrl = 'https://www.zhihu.com/'

cookies_str = r'd_c0="AIBALYZ9HwqPTlb5KXgSwSWui1fs5EPmxdc=|1466691972"; q_c1=469d851b543e4c7f88135ed935a43f57|1466691972000|1466691972000; _za=3cbe8cd9-b848-4563-998b-85dbb45f76e3; _zap=1197c360-ee4f-4c09-a092-9d3334be2d76; _xsrf=88d16f60ca0b8b773565fd40a279c6be; l_cap_id="YTAwNWI3N2E2OWIyNGE3ZTkwMDdlNmU5YzhkMjZkN2Q=|1467037056|b7ed44a76d63eb8bcb1ce19ac2590a8905e6cf7e"; cap_id="NmI4YWQ0MTU4ODk2NGMwOGE4ZmE3MDcyNGJmOGE2ODQ=|1467037056|9f0e64a9b8b6c3a4bcb6da102e506ffdf8693148"; __utmt=1; __utma=51854390.1906158685.1466691972.1466692162.1467037059.3; __utmb=51854390.2.10.1467037059; __utmc=51854390; __utmz=51854390.1467037059.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20160623=1; login="YTliYzMxYWMzZWVlNGZjYTlkZjYwNGNiMmFkMzk2MDY=|1467037537|8f4b2f54261330a5a356e70dbcf45a97dae785df"; a_t="2.0ABCCylOLJggXAAAAYcSYVwAQgspTiyYIAIBALYZ9HwoXAAAAYQJVTWHEmFcAtV5-3BUdKRSsuzxuXwN9P5Xwkp_sVd2BNo_4mMWMSXWpJUAkz698QA=="; z_c0=Mi4wQUJDQ3lsT0xKZ2dBZ0VBdGhuMGZDaGNBQUFCaEFsVk5ZY1NZVndDMVhuN2NGUjBwRkt5N1BHNWZBMzBfbGZDU253|1467037537|2a065a5c9e665d8306f1019752f25d5ad9cbbc42; n_c=1'


def GetResp(url):
    '''
    get the response object
    '''
    #requests.cookies.create_cookie
    ls = string.split(cookies_str,';')
    cookies_dict = {}
    for item in ls:
        temp = string.split(item,'=',1)
        cookies_dict[temp[0]] = temp[1]
    print cookies_dict

    options = {
        'Host':'www.zhihu.com',
        'Referer':'https://www.zhihu.com/',
        'Upgrade-Insecure-Requests':1,
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    req = requests.get(url,None,cookies=cookies_dict,headers=options)
    return req

def DownloadImgs(imgUrl,imgName,imgFloder):
    resp = requests.get(imgUrl,stream=True)
    with open(imgFloder + imgName, 'w+') as f:  
        for chunk in resp.iter_content(chunk_size=1024):  
            if chunk: # filter out keep-alive new chunks  
                f.write(chunk)
                f.flush()  
        f.close()

def AnalyseItem(html):
    '''
    分析单项数据并返回
    '''
    soup = BeautifulSoup(html,'html.parser')
    title_imgs = soup.find_all(class_='side-topic-avatar') #获取首页中图片项
    for img in title_imgs:
        DownloadImgs(img.attrs['src'],img.attrs['alt']+'.png','downloads/')
    return soup.find_all(class_='question_link') #问题的链接

def GetSimpleQuestionUserStar(questionUrl):
    '''
    获取当前关注此问题的用户
    '''
    resp = GetResp(baseUrl + questionUrl) #问题的主页面


def test():
    '''
    回归测试
    '''
    resp = GetResp(baseUrl)
    hrefs = AnalyseItem(resp.content)
    return hrefs

if __name__ == '__main__':
    resp = GetResp(baseUrl)
    hrefs = AnalyseItem(resp.content)
