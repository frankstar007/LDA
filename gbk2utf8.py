#coding:utf-8
import configparser
import codecs
import os

from os.path import join 

def readFile(filepath,encoding='gbk'):
	with codecs.open(filepath,encoding) as f:
		return f.read()

def writeFile(filepath,u,encoding='utf-8'):
	with codecs.open(filepath,'w',encoding) as f:
		fwrite(u)

def gbk2utf8(src,dst):
	content = readFile(src,encoding='gbk')
	writeFile(dst,content,encoding='utf-8')

if __name__ == '__main__':
	conf = configparser.ConfigParser()
	conf.read('setting.conf')

	rawdatadir = conf.get('datadir','rawdatadir')
	for root,dirs,files in os.walk(rawdatadir):
		for Onefile in files:
			OnefullFileName = join(root,Onefile)
			gbk2utf8(OnefullFileName,OnefullFileName)
      
        	