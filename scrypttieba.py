#coding=utf-8
import urllib
import re
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,pageNo):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
	#create dir
    curPath = os.getcwd()
    pageDicPath = curPath + "\\" + bytes(pageNo)
    isDirExist = os.path.exists(pageDicPath)
    if not isDirExist:
        print 'create page dic'
        os.mkdir(pageDicPath)
    #save pics in a page
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, pageDicPath + '//%s.jpg' % x)
        x+=1
        #print imgurl

def getAllImg(url):
    #imgIndex = 0
    for pageNo in range(1, 10):
        newUrl = url + "?pn=" + str(pageNo)
        #print "newUrl = " + newUrl
        html = getHtml(newUrl)
        getImg(html, pageNo)
		

html = getAllImg("http://tieba.baidu.com/p/2460150866")

#print getImg(html)