#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Lütfen 5 tane sayı giriniz.")
sayac=0
while sayac<5:
    sayi=int(input("Sayıyı Girin : "))
    sayac=sayac+1
    if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               print("Asal Sayı Değildir.")
               break
       else:
           print("Asal Sayıdır.")
    else:
       print("Asal Sayı Değildir.")

