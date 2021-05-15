#!/usr/bin/env python
# coding: utf-8

# In[9]:


lx=open('odev.txt')
liste=list()
liste2=['(',')','?','-','=','+']
for la in lx:
    ly=la.rstrip()
    liste.append(ly)
for any in liste:
    temizVeri = ""
    for i in range(len(any)):
        if any[i].isdigit():
            continue
        elif any[i] in liste2:
            continue
        else:
            temizVeri += any[i]
    temizVeri += ""
    print(temizVeri)
    
    

    


# In[ ]:





# In[ ]:





# In[ ]:




