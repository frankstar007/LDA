#coding:utf-8
import logging
import logging.config
import configparser
import numpy as np
import random
import codecs
import os

from collections import OrderedDict

#获取当前路径
path = os.getcwd()
#print(path)#G:\lda\LDA
#导入日志配置文件
logging.config.fileConfig('logging.conf')
#创建日志对象
loggerInfo = logging.getLogger('TimeInfoLogger')
Consolelogger = logging.getLogger('Consolelogger')
#导入配置文件
conf = configparser.ConfigParser()
conf.read('setting.conf')
#以列表的形式返回所有的section
#sections = conf.sections()
#options  = conf.options('filepath')
#items  = conf.items('filepath')
