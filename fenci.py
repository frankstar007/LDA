#coding:utf-8
import jieba
import jieba.posseg as pseg
import configparser
import os
import sys


from os.path import join

count = 1
def splitSentence(src,dst):
    fin = open(src,'r')
    fout = open(dst,'a')
    global count
    fout.write(str(count) + " ")
    stopwords = [line.rstrip().decode("utf-8") for line in open('stopkey.txt')]
    #print(stopwords)
    for line in fin:
        contents = line.strip()
        wordlist = list(jieba.cut(contents))
        outstr = ''
        for word in wordlist:
            if word not in stopwords:
                outstr += word
                outstr += ' '
        fout.write(outstr.strip())
    fout.write('\n')
    fin.close()
    fout.close()
    count += 1

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
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
            # print(OnefullFileName)
            splitSentence(OnefullFileName,data)
