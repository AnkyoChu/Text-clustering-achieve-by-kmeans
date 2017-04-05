import nltk
from nltk.stem.lancaster import LancasterStemmer


file=open('dblp_KDD_2016_idf.txt','r',encoding='UTF-8')
list=file.readlines()
file.close()

tt='estimation'

#print(len(list))
#print(list[0])
#print(list[1])
#print(list[2])


list2=[]
for ww in list:
    LancasterStem=LancasterStemmer()
    list2.append(LancasterStem.stem(ww))

#print(list2)

if list2[0].find(tt)==-1 and list2[1].find(tt)==-1:
    print('wu')
else:
    print('you')

print(list2[0])