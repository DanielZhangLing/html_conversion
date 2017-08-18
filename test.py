# # -*- coding: utf-8 -*-
import subprocess
import os
# import os
import urllib
import urllib2
#
from docx2html import convert
# from pdf2html import convert
#
# url = 'Formation.pdf'
# html = convert(url)
# html = convert('Formation.pdf')
# print html
#
# fp = urllib2.urlopen(url)
# html = fp.read()
# print html.decode("utf8")

# command = 'pdf2htmlEX Formation.pdf my_project/a.html'
# os.remove('my_project/a.html')
# p = subprocess.call(command, shell=True)
# # html = p.stdout.readlines()
# print ''.join(html)
# print urllib.urlopen("Formati`on.html").read()
# s = 'abcde'
# print s[:-3]
# a=[(1,2),(2,3),(3,4)]
# for x,y in a:
#     print x+y
# def parent(num):
#
#     def first_child():
#         return "Printing from the first_child() function."
#
#     def second_child():
#         return "Printing from the second_child() function."
#
#     try:
#         assert num == 10
#         return first_child
#     except AssertionError:
#         return second_child
#
# foo = parent(10)
# bar = parent(11)
#
# print(foo)
# print(bar)
#
# print(foo())
# print(bar())
# import threading
# import time
# def test():
#     print "run multi"
#     time.sleep(30)
#     print "end multi"
# t =threading.currentThread()
#
# t2 = threading.Thread(target=test, args=())
# t2.setName("sub1")
# t2.setDaemon(False)
# t2.start()
#
# print t.getName()
#
new_file = open('Formation.pdf')
def html_conversion(file_extension, path):

    if file_extension.lower() == '.docx':
        bodyHtml = convert(path)
        print bodyHtml

    elif file_extension.lower() == '.pdf':
        url = path[:-3] + 'html'
        command = "pdf2htmlEX " + " " + path
        subprocess.call(command, shell=True)
        bodyHtml = urllib.urlopen(url).read()
        os.remove(url)
        print bodyHtml

# testing pdf
file_extension = '.pdf'
path = 'Formation.pdf'
# testing docx
# file_extension = '.docx'
# path = 'Business Loan Agreement - SKM Media Group Inc. and JPMorgan Chase Bank NA.docx'
html_conversion(file_extension, path)