#f=open('dblp_KDD_2016.txt','rb')
#print(f.read())
#f.close()

import math
import nltk
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer

#载入文档
file=open('dblp_KDD_2016.txt','rb')
#整个文档的变量
data=file.read()
file.close()
data=data.decode('utf-8')
#print(data)

#所处理的文档总数
num_of_sum_text=218

#单一文档变量
text="Graphons and Machine Learning: Modeling and Estimation of Sparse Massive Networks There are numerous examples of sparse massive networks, in particular the Internet, WWW and online social networks. How do we model and learn these networks? In contrast to conventional learning problems, where we have many independent samples, it is often the case for these networks that we can get only one independent sample. How do we use a single snapshot today to learn a model for the network, and therefore be able to predict a similar, but larger network in the future? In the case of relatively small or moderately sized networks, it's appropriate to model the network parametrically, and attempt to learn these parameters. For massive networks, a non-parametric representation is more appropriate. In this talk, we first review the theory of graphons, developed over the last decade to describe limits of dense graphs, and the more the recent theory describing sparse graphs of unbounded average degree, including power-law graphs. We then show how to use these graphons as non-parametric models for sparse networks. Finally, we show how to get consistent estimators of these non-parametric models, and moreover how to do this in a way that protects the privacy of individuals on the network. "

#########################分词#######################################################
data_aft_apt=nltk.word_tokenize(data)
text_aft_apt=nltk.word_tokenize(text)
#print(data_aft_apt)
#data4w=data_aft_apt
#text4w=text_aft_apt

#词干化
#LancasterStem=LancasterStemmer()
#data4w=LancasterStem.stem(data_aft_apt)
#print(data4w)
data4w=[]
for ww in data_aft_apt:
    LancasterStem=LancasterStemmer()
    data4w.append(LancasterStem.stem(ww))

#print(data4w)
text4w=[]
for tt in text_aft_apt:
    LancasterStem=LancasterStemmer()
    text4w.append(LancasterStem.stem(tt))

#########################去停用词####################################################
filtered_words = [w for w in data4w if w not in stopwords.words('english')]
#print(filtered_words)

filtered_words_text=[c for c in text4w if c not in stopwords.words('english')]

#去多余的字符和标点
filtered_chars=[word for word in filtered_words if word not in [',','.',':','(',')','?']]
#print(filtered_chars)

filtered_chars_text=[t for t in filtered_words_text if t not in [',','.',':','(',')','?']]
#print(filtered_chars_text)
#######################提取特征#########################################################################
#######################计算TF-IDF#######################################################################

#文档总词数
total_words_len=len(filtered_chars)
#print(total_words_len)

#各个文档词数
total_text_len=len(filtered_chars_text)

#记录有哪些单词和词频(总词库中的)
words_dic=[]
num_dic=[]

n=0
j_word_dic_len=0
while n<total_words_len:
    if filtered_chars[n] not in words_dic:
        words_dic.append(filtered_chars[j_word_dic_len])
        num_dic.append(1)
        j_word_dic_len=j_word_dic_len+1
        n=n+1
    else:
        k=0
        while k<j_word_dic_len:
            if words_dic[k]==filtered_chars[n]:
                num_dic[k]=num_dic[k]+1
                k=j_word_dic_len
            else:
                k=k+1
        n=n+1
#print(words_dic)
#print(num_dic)
#print(len(words_dic))
#print(len(num_dic))

#打印词典
'''
kkk=0
while kkk<len(words_dic):
    print("%s:%d",words_dic[kkk],num_dic[kkk])
    kkk=kkk+1
'''

#所处理文档中的词数与词频
'''
words_dic_text=[]
num_dic_text=[]
n=0
j_word_dic_text_len=0
while n<total_text_len:
    if filtered_chars_text[n] not in words_dic_text:
        words_dic_text.append(filtered_chars_text[j_word_dic_text_len])
        num_dic_text.append(1)
        j_word_dic_text_len=j_word_dic_text_len+1
        n=n+1
    else:
        k=0
        while k<j_word_dic_text_len:
            if words_dic_text[k]==filtered_chars_text[n]:
                num_dic_text[k]=num_dic_text[k]+1
                k=j_word_dic_text_len
            else:
                k=k+1
        n=n+1
'''

#所处理文档输出
'''
kkk=0
while kkk<len(words_dic_text):
    if num_dic_text[kkk]>2:
        print("%s:%d",words_dic_text[kkk],num_dic_text[kkk])
    kkk=kkk+1
'''

#计算词典中的单词的TF值
num_dic_tf=[]

#num_dic_tf=num_dic

prpr=0
while prpr<len(num_dic):
    num_dic_tf.append(0)
    prpr=prpr+1


pr=0

while pr<len(words_dic):
    num_dic_tf[pr]=num_dic[pr]
    pr=pr+1



for iii in range(len(num_dic)):
    num_dic_tf[iii]=num_dic[iii]/len(num_dic)

#print(num_dic_tf)
#print(len(num_dic_tf))

#计算词典中的单词的IDF值
num_dic_idf=[]

for kkkk in range(len(num_dic)):
    num_dic_idf.append(0)

#print(num_dic_idf)
#print(len(num_dic_idf))

file=open('dblp_KDD_2016_idf.txt','r',encoding='UTF-8')
list=file.readlines()
file.close()

list_aft_stem=[]

for tttt in list:
    LancasterStem = LancasterStemmer()
    list_aft_stem.append(LancasterStem.stem(tttt))

counter4list_aft=0
counter4words_dic=0

while counter4words_dic<len(words_dic):
    while counter4list_aft<len(list_aft_stem):
        if list_aft_stem[counter4list_aft].find(words_dic[counter4words_dic])==-1 and list_aft_stem[counter4list_aft+1].find(words_dic[counter4words_dic])==-1 :
            counter4list_aft = counter4list_aft + 3
        else:
            num_dic_idf[counter4words_dic]=num_dic_idf[counter4words_dic]+1
            counter4list_aft=counter4list_aft+3
    counter4words_dic=counter4words_dic+1
    counter4list_aft=0

#print(num_dic_idf)
#print(len(num_dic_idf))
#print(len(num_dic_tf))
#print(len(words_dic))
#print(words_dic[0])

flag_idf=0
while flag_idf<len(num_dic_idf):
    num_dic_idf[flag_idf]=math.log((num_of_sum_text/(num_dic_idf[flag_idf]+1)))
    flag_idf=flag_idf+1

#print(num_dic_idf)

#文档的TF_IDF值
num_dic_tf_idf=[]
for xxxx in range(len(num_dic)):
    num_dic_tf_idf.append(0)

tf_idf=0

while tf_idf<len(num_dic):
    num_dic_tf_idf[tf_idf]=num_dic_tf[tf_idf]*num_dic_idf[tf_idf]
    tf_idf=tf_idf+1

#print(num_dic_tf_idf)
#print(len(num_dic_tf_idf))
#print(len(num_dic))
#print(len(words_dic))


#处理无用的特征
pp=0
while pp<len(words_dic):
    if num_dic_tf_idf[pp]==0.0:
        words_dic.pop(pp)
        num_dic_tf_idf.pop(pp)
        num_dic.pop(pp)
        num_dic_tf.pop(pp)
        num_dic_idf.pop(pp)
    pp=pp+1


#打印词典以及它的tf-idf值
'''
kkk=0
while kkk<len(words_dic):
    print(words_dic[kkk],num_dic_tf_idf[kkk])
    kkk=kkk+1
'''
#print(len(words_dic),len(num_dic),len(num_dic_tf_idf))

#################################################聚类###############################################################
