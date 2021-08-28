# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:33:29 2021

@author: chnt2
"""

import pandas as pd    
     
data = pd.read_csv("main.csv")    
    
 
dic=data.to_dict()
ls=list(dic.keys())
print(ls,len(ls))
pr=list(dic.values())


#print(pr[0])
l=[]

for z in range(11196):
    o=[]
    for a in pr:
        
        o.append(a[z])
    l.append(o)
#print(l[0])   here we can see all the list individually 

il=[]

#kai=[]
for a in l:
    #if a[8] not in kai:
     #   kai.append(a[8])
     if a[8] in ['USA (CA)', 'USA (CO)', 'USA (CT)', 'USA (DC)', 
                'USA (FL)', 'USA (IL)', 'USA (IN)', 'USA (MA)',
                'USA (MI)', 'USA (MN)', 'USA (MO)', 'USA (NJ)',
                'USA (NV)', 'USA (NY)', 'USA (OH)', 'USA (OR)', 
                'USA (PA)', 'USA (RI)', 'USA (TN)', 'USA (TX)',
                'USA (VA)', 'USA (WA)']:
        t=a[5]
        if t[0]=="$":
            #f "Case" in t:
             #   t="$0.0"
            #else:
            #print(a)
            
            t=t.replace(",","")
            tm=[float(t[1:])]
        else:
            t=t.replace(",","")
            tm=[int(t[:-1])]
        pp=a[:5]+tm+a[6:]
        il.append(pp)
                
#print(fil[0])
#print(len(il))
#kai.sort()
#print(il)
print("records where country contains the word USA: ",len(il))
#print(len(il[0]),(len(ls)))
#print(ls)
#print(il[0])

import csv  


fields = ls 
     
filename = "filteredCountry.csv"

with open(filename, 'w',newline='',encoding="utf8") as csvfile: 
     
    csvwriter = csv.writer(csvfile) 
        
    csvwriter.writerow(fields) 
        
    csvwriter.writerows(il)
#-----------------------------task one complete upto here ...
#print(list(data))
#print(type(data))

daa= pd.read_csv("filteredCountry.csv")   
  
dic=daa.to_dict()
kl={}

#print(list(dic.keys()))

pr=list(dic.values())
#print(la[0])

l=[]

for z in range(3030):
    o=[]
    for a in pr:
        o.append(a[z])
    l.append(o)  
print(l[0],"ASDFasfd")

for a in l:
    
    if a[0] in kl:
        #print(a[0],"thisis",kl)
        kl[a[0]].append(float(a[5]))
    else:
        kl[a[0]]=[float(a[5])]
    
        
fin=[]


ik=list(kl.keys())
ik.sort()
opl,ipl=[],[]
for a in ik:
    if len(kl[a])>1:
        opl=[]
        km=kl[a]
        km.sort()
        opl.append(a)
        opl=opl+km[:2]
        ipl.append(opl)

print("For each group of SKU are:",len(ipl))

fields = ["SKU","FIRST_MINIMUM_PRICE","SECOND_MINIMUM_PRICE"]
    
filename = "lowestPrice.csv"

with open(filename, 'w',newline='',encoding="utf8") as csvfile: 
    
    csvwriter = csv.writer(csvfile) 
         
    csvwriter.writerow(fields) 
         
    csvwriter.writerows(ipl)        
    
    
#print(kl) ----------the final dic
#print(len(kl))
#l=list(dic["SKU"])
#print(len(l))






