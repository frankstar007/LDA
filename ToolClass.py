import codecs
import configparser
import numpy as np

from collections import OrderedDict

#获取当前路径
path = os.getcwd()
#导入配置文件
conf = configparser.ConfigParser()
conf.read("setting.conf") 
#文件路径
trainfile = os.path.join(path,os.path.normpath(conf.get("filepath", "trainfile")))
wordidmapfile = os.path.join(path,os.path.normpath(conf.get("filepath","wordidmapfile")))
thetafile = os.path.join(path,os.path.normpath(conf.get("filepath","thetafile")))
phifile = os.path.join(path,os.path.normpath(conf.get("filepath","phifile")))
paramfile = os.path.join(path,os.path.normpath(conf.get("filepath","paramfile")))
topNfile = os.path.join(path,os.path.normpath(conf.get("filepath","topNfile")))
tassginfile = os.path.join(path,os.path.normpath(conf.get("filepath","tassginfile")))
#模型初始参数
K = int(conf.get("model_args","K"))
alpha = float(conf.get("model_args","alpha"))
beta = float(conf.get("model_args","beta"))
iter_times = int(conf.get("model_args","iter_times"))
top_words_num = int(conf.get("model_args","top_words_num"))


class Document(object):
	"""docstring for Document"""
	def __init__(self):
		super(Document, self).__init__()
		self.words = []
		self.length = 0


class DataPreProcessing(object):
	"""docstring for DataPreProcessing"""
	def __init__(self):
		super(DataPreProcessing, self).__init__()
		self.doc_count = 0
		self.words_count = 0
		self.docs = []
		self.word2id = OrderedDict()

	def cachewordidmap(self,wordidmapfile):
		with open(wordidmapfile,'w',encoding='utf-8') as f:
			for word,id in self.word2id.items():
				f.write(word + '\t' + str(id) + '\n')

class LDAModel(object):
	"""docstring for LDAModel"""
	def __init__(self, dpre):
		super(LDAModel, self).__init__()
		self.dpre = dpre 						#获取预处理参数
		self.K = K								#聚类个数
		self.beta = beta						#超参数β
		self.alpha = alpha						#超参数α
		self.iter_times = iter_times			#迭代次数
		self.top_words_num = top_words_num		#每个类特征词个数

		self.wordidmapfile = wordidmapfile		#词对应ID文件
		self.trainfile = trainfile				#分好词的文件
        self.thetafile = thetafile				#文章-主题分布文件
        self.phifile = phifile                  #词-主题分布文件
        self.topNfile = topNfile                #每个主题词topN词文件
        self.tassginfile = tassginfile 			#最后分派结果文件
        self.paramfile = paramfile				#模型训练选择的参数文件
        
		
        
        
        
        
        
        

        self.p = np.zeros(self.K)				#p,概率向量存储采样的临时变量
        self.nw = np.zeros((self.dpre.words_count,self.K),dtype='int')   #nw,词word在主题topic上的分布
        self.nwsum = np.zeros(self.K,dtype='int')	#nwsum,每个topic上的分布
        self.nd = np.zeros((self.dpre.docs_count,self.K),dtype='int')    #每个doc中各个topic的词的总数
        self.ndsum = np.zeros(dpre.docs_count,dtype='int')	#每个doc中词的总数
        self.Z = np.array([ [0 for y in xrange(dpre.docs[x].length)] for x in xrange(dpre.docs_count)])

        #随机分配类型
        for x in xrange(len(self.Z)):
        	self.ndsum[x] = self.dpre.docs[x].length


		
		
		