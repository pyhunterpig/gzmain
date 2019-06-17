﻿# -*- coding:utf-8 -*-
# 13585582354
# 147258369zaq


import os
import sys
import time
from collections import deque

import aircv as ac
import uiautomation as automation

os.environ['DISPLAY'] = ':0'
import pyautogui
# from pywinauto import application

from database.redis_mangager import RedisDB

# 初始化当前模板环境

REDIS_GZ = RedisDB()

dirs = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# dirs = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
# file = os.getcwd()
file = sys.path[0]
IMGSRC = file + '\screenshot.jpg'


# print(IMGSRC)


class YCTGZ():
    def __init__(self):
        self.restart_login = False
        self.change_account = False

    def yzdl(self):
        '''用于验证登录匹配是否有办理进度跟踪字样，如果有返回1说明登录成功'''
        time.sleep(5)
        result = automation.ButtonControl(Depth=3, Name='继续')
        if automation.WaitForExist(result, 5):
            automation.SendKeys('{Enter}')
            time.sleep(5)
        automation.SendKeys('{F6}')
        automation.SendKeys('http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do?x=12')
        automation.SendKeys('{Enter}')
        time.sleep(5)
        result = automation.CustomControl(Depth=9, Name='办理进度跟踪')
        if automation.WaitForExist(result, 5):
            return 1
        else:
            automation.SendKeys('{F6}')
            automation.SendKeys('{Enter}')
            result = automation.CustomControl(Depth=9, Name='办理进度跟踪')
            if automation.WaitForExist(result, 5):
                return 1
            else:
                self.restart_login = True

    def gain_session(self, name):
        '''获取点击暂存以后得到的session'''
        print(name, 'name')
        if '退回修改' in name:
            time.sleep(5)
            for i in range(1, 3):
                automation.SendKeys('{Down}')
            time.sleep(5)
            pyautogui.screenshot(IMGSRC)
            time.sleep(5)
            imgobj = r'\thyj.jpg'
            imsrc = ac.imread(IMGSRC)
            imobj = ac.imread(file + imgobj)
            match_result = ac.find_template(imsrc, imobj,
                                            0.7)
            if match_result:
                REDIS_GZ.hset('specify_account_session', {'session': 'true'})
                result = REDIS_GZ.hget('specify_account_yctAppNo_page')
                if result['total'] == result['getpage']:
                    return 2
                automation.SendKeys('{Ctrl}k{Ctrl}k')
                time.sleep(2)
                automation.SendKeys(
                    'http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do{Enter}')
                pyautogui.screenshot(IMGSRC)
                imsrc = ac.imread(IMGSRC)
                imobj = ac.imread(file + r'\bljdgz.jpg')
                match_result = ac.find_template(imsrc, imobj,
                                                0.8)
                if match_result:
                    return 1
                else:
                    print('96行')
                    self.restart_login = True
                    return 1
            else:
                self.restart_login = True
                return 1
        elif '填报成功' in name:
            print(name, 'name')
            time.sleep(5)
            pyautogui.screenshot(IMGSRC)
            time.sleep(5)
            imgobj = r'\tbcg.jpg'
            imsrc = ac.imread(IMGSRC)
            imobj = ac.imread(file + imgobj)
            match_result = ac.find_template(imsrc, imobj,
                                            0.8)
            if match_result:
                REDIS_GZ.hset('specify_account_session', {'session': 'true'})
                result = REDIS_GZ.hget('specify_account_yctAppNo_page')
                if result['total'] == result['getpage']:
                    return 2
                automation.SendKeys('{Ctrl}k{Ctrl}k')
                time.sleep(2)
                automation.SendKeys(
                    'http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do{Enter}')
                time.sleep(8)
                print(123)
                pyautogui.screenshot(IMGSRC)
                print(125)
                imsrc = ac.imread(IMGSRC)
                print(127)
                imgobj = r'\bljdgz.jpg'
                imobj = ac.imread(file + imgobj)
                print(130)
                match_result = ac.find_template(imsrc, imobj,
                                                0.8)
                print(match_result, 133)
                if match_result:
                    print('128')
                    return 1
                else:
                    print('131行')
                    self.restart_login = True
                    return 1
            else:
                self.restart_login = True
                print('136行')
                return 1

    def lddb(self):
        # 判断页数是否是相同不相同则继续点击下一页
        time.sleep(5)
        pyautogui.screenshot(IMGSRC)
        imsrc = ac.imread(IMGSRC)
        imobj = ac.imread(file + r'\bljdgz.jpg')
        match_result = ac.find_template(imsrc, imobj,
                                        0.8)
        print(match_result, '143行')
        if match_result:
            name = REDIS_GZ.hget('specify_account_yctAppNo_page')
            print(name)
            # result = automation.EditControl(Depth=14, foundIndex=10)
            # redis 里面去数据
            # name = re.compile('\d+').findall(result.Name)
            for i in range(1, 3):
                time.sleep(2)
                automation.SendKeys('{Down}')
            res = REDIS_GZ.hget('specify_account_session')
            print(res['session'])
            for i in range(1, 6):
                for x in range(1, 8):
                        automation.SendKeys('{Down}')
                        if'false'==res['session']:
                            pyautogui.screenshot(IMGSRC)
                            imgobj = file + r'\th.jpg'
                            imsrc = ac.imread(IMGSRC)
                            imobj = ac.imread(imgobj)
                            match_result = ac.find_template(imsrc, imobj,
                                                            0.8)
                            if match_result:
                                automation.HyperlinkControl(Depth=17, Name='退回修改', foundIndex=i).Click()
                                time.sleep(5)
                                if self.gain_session(name='退回修改') == 2:
                                    print('165行')
                                    return 1
                                elif self.restart_login == True:
                                    print('168行')
                                    return 1
                                else:
                                    print('171行')
                                    self.lddb()
                            imgobj = file + r'\txcg.jpg'
                            imobj = ac.imread(imgobj)
                            match_result = ac.find_template(imsrc, imobj,
                                                            0.8)
                            if match_result:
                                res=automation.HyperlinkControl(Depth=17, Name='填报成功（查看详情）').Click()
                                print(res)
                                time.sleep(5)
                                if self.gain_session(name='填报成功') == 2:
                                    print('192')
                                    return 1
                                elif self.restart_login == True:
                                    print('190行')
                                    return 1
                                else:
                                    print(193)
                                    time.sleep(5)
                                    self.lddb()
                        else:
                            print(196)
                            continue
            if name['getpage'] == name['total']:
            # if name['getpage'] == '3':
                print('205')
                return 1
            else:
                print(208)
                return
        else:
            self.restart_login = True
            print('204行')
            return 1

    def djxyy(self):
        '''根据当前是否有下一页,如果有则点击如果没有下一页就返回1'''
        print('djxyy', 209)
        pyautogui.screenshot(IMGSRC)
        imgobj = file + r'\djxyy.jpg'
        imsrc = ac.imread(IMGSRC)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj,
                                        0.8)
        if match_result:
            automation.ButtonControl(Depth=14, foundIndex=4).Click()
        time.sleep(8)

    def pjurl(self):
        '''控制鼠标到url栏，删除，重写，按enter键'''
        print('237行')
        specify_account_yctAppNo = REDIS_GZ.hget('specify_account_yctAppNo')
        print(specify_account_yctAppNo)
        if specify_account_yctAppNo:
            for yctAppNo in specify_account_yctAppNo:
                if '退回修改' in specify_account_yctAppNo[yctAppNo]:
                    automation.SendKeys('{Ctrl}k{Ctrl}k')
                    automation.SendKeys(
                        '%s{Enter}' % (
                            'http://yct.sh.gov.cn/bizhallnz_yctnew/apply/appendix/print?yctAppNo={}'.format(yctAppNo)))
                    time.sleep(10)
                    if self.pcontent():
                        print(249)
                        return 1
                    break
                elif '填报成功' in specify_account_yctAppNo[yctAppNo]:
                    print('253')
                    automation.SendKeys('{Ctrl}k{Ctrl}k')
                    automation.SendKeys(
                        '%s{Enter}' % (
                            'http://yct.sh.gov.cn/bizhallnz_yctnew/apply/appendix/print?yctAppNo={}'.format(yctAppNo)))
                    time.sleep(10)
                    results = REDIS_GZ.hget('specify_account_tbcg_' + yctAppNo)
                    for result in results:
                        if len(result) > 15:
                            id_, app_no = result.split('&')
                            automation.SendKeys('{Ctrl}k{Ctrl}k')
                            # http://yct.sh.gov.cn/bizhallnz_yctnew/apply/appendix/content_special?id=041175&p=1&app_no=2900000320190604A008&yctAppNO=faee7e7331ea42f58400c72a1e441209
                            automation.SendKeys(
                                '%s{Enter}' % (
                                    'http://yct.sh.gov.cn/bizhallnz_yctnew/apply/appendix/content_special?id=-{}&p=1&app_no={}&papers={}&yctAppNo={}'.format(
                                        id_, app_no, result,
                                        yctAppNo)))
                            time.sleep(10)
                        else:
                            automation.SendKeys('{Ctrl}k{Ctrl}k')
                            automation.SendKeys(
                                '%s{Enter}' % (
                                    'http://yct.sh.gov.cn/bizhallnz_yctnew/apply/appendix/content?id=-{}&appendixStatus=&isPrint=1&p=1&papers={}yctAppNo={}'.format(
                                        result,result, yctAppNo)
                                )
                            )
                            time.sleep(10)
                        if self.pcontent():
                            return 1
                    break

        else:
            return 1

    def pcontent(self):
        '''celery调度broker做任务从代理中获取文本内容'''
        time.sleep(10)
        print('286行')
        pyautogui.screenshot(IMGSRC)
        imgobj = file + '\ysjg_thxg.jpg'
        imsrc = ac.imread(IMGSRC)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj,
                                        0.8)
        if match_result:
            return
        imgobj = file + '\zjdy.jpg'
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj,
                                        0.8)
        if match_result:
            return
        else:
            self.restart_login = True
            return 1

    def yztc_dl(self):
        '''判断当前是否跳转重新登录的提示'''
        result = automation.HyperlinkControl(Depth=11, Name='账号密码登录')
        if automation.WaitForExist(result, 5):
            result.Click()
            return 1
        else:
            raise ('yztc_dl异常')

    def portal_yct(self):
        '''第一次跳转到登录页'''
        result = automation.EditControl(Depth=11, Name='开办企业申请信息填写人需进行实名认证，系统将跳转至“一网通办”总门户进行用户注册和认证')
        if automation.WaitForExist(result, 5):
            automation.HyperlinkControl(Depth=10, Name='确定').Click()
            # pyautogui.screenshot(IMGSRC)
            # imgobj = file + '\zyts.jpg'
            # imsrc = ac.imread(IMGSRC)
            # imobj = ac.imread(imgobj)
            # match_result = ac.find_template(imsrc, imobj,
            #                                 0.8)
            # if match_result:
            #     x, y = match_result['result']
            #     pyautogui.click(x, y)
            # if automation.WaitForExist(result, 5):
            #     result.Click()
            return 1
        else:
            raise ('portal_yct异常')


class Iter_Task(YCTGZ):
    def __init__(self):
        YCTGZ.__init__(self)

    def breadth_first(self, STATE):
        '''获取一个账号然后分别轮询login，trace_list和detail事件'''
        self.STATE = STATE
        # app = application.Application()
        # app.connect(path=dirs, timeout=20)
        while not self.change_account:
            while self.restart_login:
                for process_bar in ['request_login']:
                    eval('self.{}()'.format(process_bar))
                    if not self.restart_login:
                        return False
                    else:
                        pass
            self.run_step()
            if not self.restart_login:
                self.change_account = True
        return True

    def run_step(self):
        for process_bar in ['login', 'trace_list', 'detail', 'changeaccount']:
            try:
                eval('self.{}()'.format(process_bar))
            except Exception as e:
                print(e, '355')
            if self.restart_login:
                automation.SendKeys('{Ctrl}k{Ctrl}k')
                automation.SendKeys(
                    '%s{Enter}' % (
                        'http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do?x=11'))
                # 如果是这样点击一般mitmproxy就不需要在去拦截了
                return
        REDIS_GZ.hset('specify_account_yctAppNo_page', {'getpage': '-1', 'total': '-2'})
        return 'success'

    def Intelligent_verification(self, zip_key):
        '''定义了一个双向队列，用于步骤的依次轮询，每次会去取出一个键，
        如果返回的值为1则跳出否则从字典里面拿到对应键的值'''
        global q_q
        q_q = zip_key.pop('q_q')
        circle = zip_key.pop('circle')
        while q_q:
            token_plugin_cls = q_q.popleft()
            try:
                if eval('self.{}()'.format(token_plugin_cls)) == 1:
                    break
                else:
                    q_q += circle[token_plugin_cls]
            except Exception as e:
                raise e
        return True

    def request_login(self):
        '''请求url页面'''
        q_q = deque()
        circle = {}
        circle['order'] = ['portal_yct']
        circle['protal_yct'] = ['yztc_dl']
        q_q += circle['order']
        zip_key = {'q_q': q_q, 'circle': circle}
        return self.Intelligent_verification(zip_key)

    def login(self):
        # 轮询login的步骤
        q_q = deque()
        circle = {}
        circle['order'] = ['yzdl']
        q_q += circle['order']
        zip_key = {'q_q': q_q, 'circle': circle}
        return self.Intelligent_verification(zip_key)

    def trace_list(self):
        # 轮询trace_list的步骤f
        q_q = deque()
        circle = {}
        circle['order'] = ['lddb']
        circle['lddb'] = ['djxyy']
        circle['djxyy'] = ['lddb']
        q_q += circle['order']
        zip_key = {'q_q': q_q, 'circle': circle}
        return self.Intelligent_verification(zip_key)

    def detail(self):
        # 轮询所有detail的步骤  03079c59a5714ca9a9ff2349efb66877
        specify_account_yctAppNo = REDIS_GZ.hget('specify_account_yctAppNo')
        # 判断specify_account_yctAppNo如果<0说明yctAppNo全部都拼接成功 ，则返回1，否则将一直轮询
        if specify_account_yctAppNo:
            q_q = deque()
            circle = {}
            circle['order'] = ['pjurl']
            circle['pjurl'] = ['pjurl']
            q_q += circle['order']
            zip_key = {'q_q': q_q, 'circle': circle}
            return self.Intelligent_verification(zip_key)

    def changeaccount(self):
        time.sleep(2)
        try:
            automation.SendKeys('{Ctrl}k{Ctrl}k')
            time.sleep(2)
            automation.SendKeys(
                'http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do{Enter}')
        except Exception as e:
            print(e, 434)
        else:
            time.sleep(5)
            pyautogui.screenshot(IMGSRC)
            imgobj = file + r'\tc.jpg'
            imsrc = ac.imread(IMGSRC)
            imobj = ac.imread(imgobj)
            match_result = ac.find_template(imsrc, imobj,
                                            0.8)
            if match_result:
                print('准备自动退出')
                res = input('准备自动退出')
                if res == 'y':
                    automation.HyperlinkControl(Depth=12, Name='退出').Click()
                    time.sleep(5)
                    REDIS_GZ.hset('specify_account_session', {'session': 'false'})
                    automation.HyperlinkControl(Depth=11, Name='账号密码登录').Click()
            else:
                self.restart_login = True


# https://zwdtuser.sh.gov.cn/uc/login/login.jsp?self=self&type=1&jump=&redirect_uri=http://yct.sh.gov.cn/portal_yct/webportal/handle_progress.do
Iter_Task().breadth_first('手动')

# 500服务器内部错误
