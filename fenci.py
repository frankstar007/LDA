#coding:utf-8
import jieba
import jieba.posseg as pseg
import configparser
import os

from os.path import join

def splitSentence(src,dst):
    fin = open(src,'r',encoding='utf-8')
    fout = open(dst,'a',encoding='utf-8')

    fout.write(src)
    for line in fin:
        contents = line.strip()
        wordlist = list(jieba.cut(contents))
        outstr = ''
        for word in wordlist:
            outstr += word
            outstr += ' '
        fout.write(outstr.strip())
    fout.write('\n')
    fin.close()
    fout.close()

if __name__ == '__main__':
    #获取当前路径
    path = os.getcwd()
    #导入配置文件
    conf = configparser.ConfigParser()
    conf.read('setting.conf')

    datafile = conf.get('datadir','rawdatadir')
    data     = conf.get('filepath','trainfile')

    for root,dirs,files in os.walk(datafile):
        for Onefile in files:
            OnefullFileName = join(root,Onefile)
            splitSentence(OnefullFileName,data)
