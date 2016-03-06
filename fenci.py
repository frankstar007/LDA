#coding:utf-8
import jieba
import jieba.posseg as pseg
import configparser
import os

#获取当前路径
path = os.getcwd()
#导入配置文件
conf = configparser.ConfigParser()
conf.read('setting.conf')

datafile = conf.get('datadir','rawdatadir')
data     = conf.get('filepath','trainfile')


for root,dirs,files in os.walk(datafile):
    for Onefile in files:
        # print(Onefile)
        OnefullFileName = join(root,Onefile)
        fwrite = open(data,'a')
        fread = open(OnefullFileName,'rb')
        words = jieba.cut(fread)
        fwrite.write(words + '\n')
        fwrite.close()
        fread.close()
    # fread = open(file,'rb').read()
    # words = jieba.cut(fread)
    # fwrite.write(words+'\n')
