#coding:utf-8
#!usr/bin/python

class QuestionItem(object):
    '''
    问题页面类
    '''
    def __init__(self, title, url, starCount):
        '''
        @title:问题名称
        @url:url 地址
        @starCount:用户关注数量
        '''
        self.title = title
        self.url = url
        self.starCount = starCount

class UserInfo(object):
    '''
    用户基础信息
    '''
    def __init__(self, alias, sex, age, location, headImg):
        self.alias = alias
        self.sex  = sex
        self.age = age
        self.location = location
        self.headImg = headImg        
        