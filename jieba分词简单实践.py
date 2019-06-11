# -*- coding:utf-8 -*-
import jieba
text = '我来到北京清华大学'
default_mode =jieba.cut(text)
full_mode = jieba.cut(text,cut_all=True)
search_mode = jieba.cut_for_search(text)
 
print "精确模式:","/".join(default_mode)
print "全模式:","/".join(full_mode)
print "搜索引擎模式:","/".join(search_mode)

