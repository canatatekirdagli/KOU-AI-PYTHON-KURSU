#!/usr/bin/env python
# coding: utf-8

# In[6]:


def TemizVeri(ilk_str, ikinci_str, ucuncu_str):
    temizVeri = ""
    for i in range(len(ilk_str)):
        if not ilk_str[i].isdigit():
            temizVeri += ilk_str[i]
    temizVeri += "-"

    for i in range(len(ikinci_str)):
        if not ikinci_str[i].isdigit():
            temizVeri += ikinci_str[i]
    temizVeri += "-"

    for i in range(len(ucuncu_str)):
        if not ucuncu_str[i].isdigit():
            temizVeri += ucuncu_str[i]

    return temizVeri

yeniveri=TemizVeri("Ah5me4t", "M9eHm4eT", "Ha3K5a1n")
a=yeniveri.title()
print(a)


# In[ ]:





# In[ ]:




