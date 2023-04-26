import requests
link = "https://www.sohodogrescue.com/adopt-a-dog"
result = requests.get(link)

import bs4
soup = bs4.BeautifulSoup(result.text,"lxml")
nm = 'blog-post-homepage-title-color blog-post-homepage-title-font _3gVhF'
sp = soup.find_all("div",class_=nm)
lst1=[]
for i in sp:
    lst1.append(i.text)
#print(lst1)
#print((sp))




#<span class="Aiy-u has-custom-focus" tabindex="0">1,692 views</span>

soup = bs4.BeautifulSoup(result.text,"lxml")
nm = "Aiy-u has-custom-focus"
sp = soup.find_all("span",class_=nm)
#first_item = sp[0]
#print(first_item.text)
lst2=[]
for i in sp:
    lst2.append(i.text)
#print(lst2)

soup = bs4.BeautifulSoup(result.text,"lxml")
nm = "_81XUh"
sp = soup.find_all("div",class_=nm)
#first_item = sp[0]
#print(first_item.text)
lst3=[]
for i in sp:
    lst3.append(i.text)
#print(lst3)



dt = dict(zip(lst1,lst3))
#print(dt)

import pandas as pd

dict1 = dt
df = pd.DataFrame()
#df = pd.DataFrame(data=dict1, index=[0])
#d={'a':lst1,'b':lst2,'c':lst3}
#df = pd.DataFrame(d,columns=['1','2','3'])
#df = (df.T)
df['a']=lst1
df['b']=lst2
df['c']=lst3
print (df)

df.to_excel('dict1.xlsx')
