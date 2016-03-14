#coding:utf-8
import logging
import logging.config
import configparser
import numpy as np
import random
import codecs
import os
import ToolClass

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
conf.read('setting.conf',encoding='utf-8')
#以列表的形式返回所有的section
#sections = conf.sections()
#options  = conf.options('filepath')
#items  = conf.items('filepath')
# 配置文件路径
trainfile      = os.path.join(path,os.path.normpath(conf.get('filepath','trainfile')))
wordidmapfile = os.path.join(path,os.path.normpath(conf.get('filepath','wordidmapfile')))
thetafile      = os.path.join(path,os.path.normpath(conf.get('filepath','thetafile')))
phifile        = os.path.join(path,os.path.normpath(conf.get('filepath','phifile')))
paramfile      = os.path.join(path,os.path.normpath(conf.get('filepath','paramfile')))
topNfile       = os.path.join(path,os.path.normpath(conf.get('filepath','topNfile')))
tassginfile    = os.path.join(path,os.path.normpath(conf.get('filepath','tassginfile')))

#模型初始参数
K = int(conf.get('model_args','K'))
alpha = float(conf.get('model_args','alpha'))
beta = float(conf.get('model_args','beta'))
iter_times = int(conf.get('model_args','iter_times'))
top_words_num = int(conf.get('model_args','top_words_num'))


#数据预处理
def preprocessing():
    Consolelogger.debug('载入数据......')
    loggerInfo.debug('载入数据......')
    with codecs.open(trainfile,'r',encoding='utf-8') as f:
        docs = f.readlines()

    Consolelogger.debug('载入完成，准备生成字典对象和统计文本数据...')
    dpre = ToolClass.DataPreProcessing()
    items_idx = 0
    for line in docs:
        if line != '':
        	tmp = line.strip().split()
        	#print(len(tmp))
        	#生成一个文档对象
        	doc = ToolClass.Document()
        	for item in tmp:
        		if item in dpre.word2id:
        			doc.words.append(dpre.word2id[item])
        		else:
        			dpre.word2id[item] = items_idx
        			doc.words.append(items_idx)
        			items_idx += 1
        		# print(doc.words)
        	doc.length = len(tmp)
        	dpre.docs.append(doc)
        else:
        	pass
    dpre.docs_count = len(dpre.docs)
    dpre.words_count = len(dpre.word2id)
    # print(dpre.word2id)
    Consolelogger.info('共有%s个文档' % dpre.docs_count)
    Consolelogger.info('共有%s个词' % dpre.words_count)
    dpre.cachewordidmap()
    Consolelogger.info('词与序号对应关系已保存到%s' % wordidmapfile)
    loggerInfo.info('词与序号对应关系已保存到%s' % wordidmapfile)

    return dpre

def run():
 	dpre = preprocessing()
 	lda = ToolClass.LDAModel(dpre)
 	print(lda.Z)
 	
if __name__ == '__main__':
	run()


