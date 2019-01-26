
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy import nan as NA


# In[ ]:

df=pd.read_csv('iris.csv')
arr1 = np.array(df)
arr2=arr1.T
arr1[: ,4] #index


# In[ ]:

arr=np.arange(16).reshape((2,2,4))
arr  


# # Numpy for data processing

# In[ ]:

points = np.arange(-5,5,0.01) #1000 points
xs,ys = np.meshgrid(points,points)#meshgrid: accept two one dimentional array and produce two two-dimentional matrix
ys


# In[ ]:

import matplotlib.pyplot as plt
z=np.sqrt(xs**2 + ys**2)
z


# In[ ]:

plt.imshow(z,cmap=plt.cm.gray)
plt.colorbar()
plt.show()


# In[ ]:

plt.title ("image111")


# # np.where

# In[ ]:

arr1= np.array([1,2,3,4,5])
arr2= np.array([6,7,8,9,10])
cond= np.array([True,False,True,True,False])
result= np.where(cond,arr1,arr2)
result


# In[ ]:

arr=np.random.random(3)
np.where(arr>0.5,1,0)
np.save('123',arr)


# In[ ]:

np.load('123.npy')


# # matrix multiplication

# In[ ]:

x= np.arange(15).reshape(3,5)
y= np.random.random((5,5))
z= x.dot(y)
z.shape
print(z)
x
y


# # random number generator

# In[5]:

a = np.random.normal(size=(4,4))
a


# 随机漫步

# In[6]:

import random as rand
time = []
step = 1000
position = 0
count = 0
time.append(count)
walk = [position]
for i in range(step):
        if rand.randint(0,1):
            step=1
        else:
            step=-1
        count = count+1
        position=position+step
        walk.append(position)
        time.append(count)


# In[ ]:




# In[7]:

df = pd.DataFrame({'time': time, 'walk': walk})
df


# In[10]:


import matplotlib.pyplot as plt


# In[11]:

df.plot.scatter(x='time',y='walk',)
plt.show()#随机漫步折线图


# In[ ]:

n=1000
a=1000
draws = np.random.randint(0,2,size=n)
steps = np.where(draws>0,1,-1)
walk =steps.cumsum()
walk.min()
walk.max()


# # Pandas

# In[51]:

object= Series([4,7,5,-3])
object
object.index
object.values
object.index=['a','b','c','d']
object


# In[5]:

object= Series([4,7,5,-3],index=['a','b','c','d'])
object
object.index
object['a']
object[object>0]
object*2
np.exp(object)


# In[ ]:

object.index.name= 'cute'
object.name = 'baby'
object


# In[18]:

data={'state':['ohio','ohio','ohio','nevada','nevada'],
         'year':['2000','2001','2002','2003','2004'],
     'pop':['1,1','2.2','2.3','2.4','3.5']}
df1=pd.DataFrame(data,columns=['year','pop','state','debt'])

df1['debt']=16.5
df1['debt']=np.arange(5)
df1.index[1]


# In[14]:

ocject= Series([4.5,3.4,21,1],index=['a','b','c','d'])
ocject.reindex(['a','b','c','d','e','f'],fill_value=0)


# # Index

# In[48]:

data = DataFrame(np.arange(16).reshape((4,4)),index=['ohio','Colorado','Ylah','Newyork'],
                 columns = ['one','two','three','four',])
# data.drop(['one','two'],axis=1) #丢弃轴上指定的项
# data.drop(['ohio','Colorado'])


# In[36]:

# data[['two','one']]
data[data['three']>5]


# In[41]:

data<5#布尔型dataframe进行索引
data[data<5]=0
data


# In[44]:

data.ix['Colorado',['two','three']]
data.ix[['Colorado','Ylah'],[3,0,1]]
data.ix[2]


# In[29]:

frame = DataFrame(np.random.randn(12).reshape((4,3)),index=['ohio','Colorado','Ylah','Newyork'],
                 columns =list('zde'))


# In[12]:

f = lambda x : x.max()-x.min()
frame.apply(f)
frame.apply(f,axis=1)


# # Order

# In[37]:

frame = DataFrame(np.random.randn(12).reshape((4,3)),index=['ohio','Colorado','Ylah','Newyork'],
                 columns =list('zde'))
frame2= frame[['z','d']]
frame2
frame2.sort_index()
frame.sort_index(axis=1)
frame


# In[38]:

frame.sort_values(by='d')
frame.sort_values(by=['d','e'])#多个列排序


# 排名

# In[50]:

obj2=Series([1,2,3,22,5,6,7])
obj2.rank()


# In[48]:

obj2.rank(method='first')


# # Unique

# In[5]:

obj3=Series(range(10),index=list('aaabbdeeee'))
obj3


# In[6]:

#检验是否唯一
obj3.index.is_unique


# In[7]:

print(obj3.index.value_counts())


# In[20]:

for i in enumerate (obj3.index.value_counts()):
    if i[1] >3:
        print(i)


# In[ ]:




# # Statistics

# In[64]:

df=DataFrame([[1.4,np.nan],[7.1,-1.6],[np.nan,np.nan],[0.3,-0.6],],columns=['one','two'],index=list('abcd'))
df


# In[67]:

df.sum()
df.sum(axis=1)
df.mean(axis=1,skipna=True)


# # Missing Values

# In[83]:

data= DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,3]])
df1= data.dropna(how='all')
df=DataFrame(np.random.rand(7,3))
df.loc[0:4,1]=NA; df.loc[:2,2]=NA
df


# In[79]:

df
df.fillna(df.mean())


# # 层次化索引

# In[9]:

df= Series(np.random.randn(10),
           index=[['a','a','a','b','b','b','c','c','d','d'],
                                      [1,2,3,1,2,3,1,2,2,3]])


# In[23]:

df
df['b']#外层索引
df[:, 1]#内层索引


# In[12]:

df.unstack()


# In[36]:

df9= DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]]
              ,columns=[['ohio','NY','colorado'],['Green','Red','Green']])
df9.index.names=['key1','key2']
df9.columns.names=['State','color']
df9


# In[43]:

df9.sort_index(level=1)
df9.swaplevel(0,1).sort_index(0)


# # Index
# 

# In[47]:

df10= DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],
                'd': [0,1,2,0,1,2,3]})
df10


# In[53]:

df11=df10.set_index(['c','d'])


# In[55]:

df11.reset_index()


# # Pandas Read File

# In[9]:

df=pd.read_csv('iris.csv',index_col=['Id'])
df


# In[19]:

df1=DataFrame({'key':['a','b','b'],'data1':range(3)})
df2=DataFrame({'key':['a','b','c'],'data2':range(3)})
# df1.merge(df2,on='key')
pd.merge(df1,df2,how='outer')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



