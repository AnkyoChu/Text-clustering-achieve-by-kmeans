#encoding=utf-8
import jieba
import jieba.analyse

# 导入自定义词典
jieba.load_userdict("dict.txt")

# 精确模式
text="i am the winner,and the winner is me"
seg_list = jieba.cut(text, cut_all=False)
print(u"分词结果:")
print("/".join(seg_list))

# 获取关键词
tags = jieba.analyse.extract_tags(text, topK=3)
print(u"关键词:")
print(" ".join(tags))