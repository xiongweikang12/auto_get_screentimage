# #TODO 自动打卡青大学习
#

import time
import pyautogui
from pathlib import Path
import tkinter
from selenium import webdriver
import pyperclip
import logging as logg
import shutil
import random
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import datetime
import smtplib


file_screen=None

logg.basicConfig(level=logg.DEBUG,format='%(asctime)s -%(filename)s[line:%(lineno)d]-%(levelname)s -%(message)s')

def print_position():
    time.sleep(5)
    x, y = pyautogui.position()
    print(x, y)


def CmdToWechat():
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')
    pyautogui.keyUp('winleft')
    logg.debug('进入运行')

    pyautogui.typewrite('cmd',interval=0.1)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    logg.debug('进入cmd')

    pyautogui.typewrite(r'C:\Users\a1761\Desktop\WeChat.lnk',interval=0.05)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    logg.debug('进入微信')

    time.sleep(1)
    window_sys=pyautogui.getWindowsWithTitle('C:\\WINDOWS\\system32\\cmd.exe')[0]
    window_sys.close()
    logg.debug('关闭cmd窗口')

def OpearWechat_search():
    global WeChat
    CmdToWechat()

    time.sleep(3)
    WeChat=pyautogui.getWindowsWithTitle('微信')[0]
    WeChat.maximize()
    logg.debug('最大化窗口')

    time.sleep(2)
    pyautogui.moveTo(123,43)
    pyautogui.click()
    pyperclip.copy('江苏共青团')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    logg.debug('搜索公众号')

    time.sleep(2)
    pyautogui.moveTo(182,153)
    pyautogui.click()
    logg.debug('进入公众号')

    # time.sleep(5)
    # x, y = pyautogui.position()
    # print(x,y)


    #123,43
    #182,153


def Opear_main():
    OpearWechat_search()

    time.sleep(2)
    pyautogui.moveTo(1124,1045)
    pyautogui.click()
    logg.debug('进入大学习')

    pyautogui.moveTo(1138,873)
    pyautogui.click()
    logg.debug('进入季期')


    #1124 1045
    #1138 873
def screen_keep():
    global file_screen
    Opear_main()
    WeChat.minimize()
    logg.debug('微信页面最小化')

    window_screen=pyautogui.getActiveWindow()
    window_screen.maximize()
    logg.debug('加载页面最大化')

    time.sleep(2)
    pyautogui.scroll(-1000)
    pyautogui.moveTo(1579,907)
    pyautogui.click()
    logg.debug('滚轮到低，按钮')

    time.sleep(2)
    window_screen.close()
    WeChat.maximize()
    logg.debug('恢复最大')

    pyautogui.moveTo(1124,1045)
    pyautogui.click()
    pyautogui.moveTo(1167,905)
    pyautogui.click()
    logg.debug('点击成绩单')

    time.sleep(1)
    byscreen_window=pyautogui.getActiveWindow()
    byscreen_window.maximize()
    time.sleep(1)
    pyautogui.scroll(-100000)
    time.sleep(1)
    pyautogui.moveTo(101,964)
    pyautogui.click()
    logg.debug('下载表单')
    time.sleep(5)
    pyautogui.click(947,588,button='right')
    time.sleep(1)
    pyautogui.click(1005,631)
    file_name = '20220220熊伟康1'
    pyperclip.copy(file_name)


    def copy_cv():
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('v')
        pyautogui.keyUp('v')
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


    time.sleep(3)
    copy_cv()
    time.sleep(3)
    shutil.move(r'C:\Users\a1761\Downloads\%s.jpg'%(file_name),'D:\python\pythonProject4\自动化')
    file_screen=r'C:\Users\a1761\Downloads\%s.jpg'%(file_name)
    logg.debug('下载成绩单并保留，转移文件路径到当前文件')
    WeChat.close()
    byscreen_window.close()


#1579 907
#1167 905
#101 964
#947 588
#1005 631



#TODO 自动浏览网页并，提交表单截图，获取截图
def other_screen():
    option=webdriver.ChromeOptions()
    option.add_argument('all')
    dirver=webdriver.Chrome(chrome_options=option)
    dirver.get('http://gwc7ecvtnzonykr1.mikecrm.com/5N9ii54')
    time.sleep(3)
    logg.debug('进入网站')

    def login_sys():
        student_name='熊伟康'
        student_id='20220220'
        class_ip='012243547'
        dirver.find_element_by_xpath('//*[@id="207052557"]/div[2]/div/div/input').send_keys(student_name)
        time.sleep(1)
        dirver.find_element_by_xpath('//*[@id="207052558"]/div[2]/div/div/input').send_keys(student_id)
        time.sleep(1)
        dirver.find_element_by_xpath('//*[@id="207052562"]/div[2]/div/div/input').send_keys(class_ip)
        time.sleep(1)
        dirver.find_element_by_xpath('//*[@id="207052559"]/div[2]/div/div/ul/li/div/div').click()
        logg.debug('填写信息')

        def copy_image():
            pyperclip.copy(r'D:\python\pythonProject4\自动化\20220220熊伟康1.jpg')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('ctrl')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            logg.debug('上传截图')

        def full_size_screenshot():
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
            time.sleep(1)
            pyautogui.hotkey('ctrl','shift','p')
            time.sleep(1)
            pyperclip.copy('Capture full size screenshot')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('ctrl')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            logg.debug('下载截图1')

        def comfirm_up():
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
            dirver.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div/a').click()
            time.sleep(1)
            pyautogui.keyDown('f12')
            pyautogui.keyUp('f12')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'shift', 'p')
            time.sleep(1)
            pyperclip.copy('Capture full size screenshot')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('ctrl')
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
            logg.debug('确认文件，并截图2')

        def search_image(file_name):
            time.sleep(10)
            rote=Path(r'C:\Users\a1761\Downloads')
            print(list(rote.glob('*.png'))[0])
            screen_image_2=list(rote.glob('*.png'))[0]
            print(screen_image_2)
            dir_name=os.path.dirname(screen_image_2)
            time.sleep(1)
            new_image_2=os.path.join(dir_name,file_name)
            os.rename(screen_image_2,new_image_2)
            time.sleep(1)
            shutil.move(new_image_2,Path.cwd())
            logg.debug('将截图重命名并转移路径（到当前文件夹下）')



        copy_image()
        copy_image()
        time.sleep(1)
        full_size_screenshot()
        time.sleep(1)
        search_image('20220220熊伟康2.png')
        time.sleep(3)
        comfirm_up()
        search_image('20220220熊伟康3.png')
        time.sleep(3)





    login_sys()




#TODO 发送邮件
def send_email(): #'file_name' and 'annex_path'
    '#创建报表和发送邮件'
    try:
        # file_name_new = str(datetime.datetime.now().date()) + file_name  # 根据当前日期拼接附件名称
        # annex_path_new = annex_path + '/' + file_name_new  # 拼接报表存储完整路径
        # create_report(host, port, user, passwd, db, sql, annex_path_new)  # 创建报表

        # 传入邮件发送者、接受者、抄送者邮箱以及主题
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ','.join(receiver)
        message['Cc'] = ";".join(Cc_receiver)
        message['Subject'] = Header(str(datetime.datetime.now().date()) + title, 'utf-8')

        # 添加邮件内容
        text_content = MIMEText(content)
        message.attach(text_content)

        # 添加附件
        # annex = MIMEApplication(open(annex_path_new, 'rb').read())  # 打开附件
        # annex.add_header('Content-Disposition', 'attachment', filename=file_name_new)
        # message.attach(annex)
        def image_to_eamil(file_name):
            image_path = str(Path.cwd()/Path(file_name))
            image = MIMEImage(open(image_path , 'rb').read())
            image.add_header('Content-Disposition', 'attachment', filename=file_name)
            message.attach(image)
        image_to_eamil('20220220熊伟康2.png')
        image_to_eamil('20220220熊伟康3.png')
        logg.debug('两个附件')

        # 登入邮箱发送报表
        server = smtplib.SMTP(smtp_ip)  # 端口默认是25,所以不用指定
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        print('success!', datetime.datetime.now())

    except smtplib.SMTPException as e:
         print('error:', e, datetime.datetime.now())  # 打印错误




sender='1761322862@qq.com'
password='oawciodevrgzdeej'
smtp_ip='smtp.qq.com'#oiqjlvkaxqkudhib
receiver=['1761322862@qq.com']
Cc_receiver=['1761322862@qq.com']
title='青年大学习'
content='hello ,这是你的截图,hhh'
ts=datetime.datetime

if __name__=='__main__':
    screen_keep()
    other_screen()
    send_email()
    print('alright')
    time.sleep(1)
    # 完成后删除相关截图文件
    for k in list(Path.cwd().glob('*20220220熊伟康*')):
        os.remove(str(k))
    print('del comfirm')











