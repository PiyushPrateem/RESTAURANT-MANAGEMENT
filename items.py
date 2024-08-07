#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def items1():
    fp=open("items.txt","r")
    contents=fp.readlines()
    for i in contents:
        i=i.rstrip().split(',')
        print(i[0],'---->',i[1],'---->',i[2])
    fp.close()
items1(0)

