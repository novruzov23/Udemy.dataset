#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
# In[2]:
import seaborn as sns

# In[3]:
df=pd.read_csv('7. Udemy Courses.csv')
df
# In[87]:

df.info()

# In[6]:

df['is_paid'].value_counts()

# In[8]:
df['subject'].value_counts()

# In[35]:

df.describe().T

# In[46]:

# tekrar eden her hangi bir setr var mi ona bakalim
df.duplicated()

# In[42]:

df.isnull().any()

# In[55]:

df.select_dtypes(include=['int64'])

# In[104]:

def data(data1):
    print('##### columns #####')
    print(data1.columns)
    print('####### shape #########')
    print(data1.shape)
    print('########## ndim #######')
    print(data1.ndim)
    
    
data(df)


# In[89]:

df.subject.unique()
# In[90]:

df.subject.nunique()

# In[60]:

df.loc[(df['subject']=='Web Development') & (df['is_paid']==True)]['is_paid'].count()

# In[61]:

df.loc[(df['subject']=='Web Development') & (df['is_paid']==False)]['is_paid'].count()

# In[106]:

df.loc[(df['subject']=='Web Development') & (df['is_paid']==True),['course_title','content_duration']].count()

# In[115]:

df.loc[(df['published_timestamp']=='2014-09-18T05:07:05Z') & (df['subject']=='Web Development')].count()
# In[124]:

# Ücretsiz olan tüm kursları göster
df[df['price']=='Free']['price'].count()

# In[127]:

# ücretli olan tüm kursları göster
df[df['price'] !='Free']['price'].count()

# In[134]:

df[df['is_paid']==True]['price'].count()

# In[154]:

# en cox satan kurslar
df.sort_values('num_subscribers', ascending=False)

# In[158]:

df.sort_values('num_subscribers')

# In[4]:

# fiyatın 100'ün altında olduğu tüm grafik kurslarını göster
df[(df['subject']=='Web Development') & (df['price'] < '200')]

# In[7]:

df[(df['subject']=='Web Development') &(df['content_duration'] < '5')]

# In[187]:

df[df.course_title.str.contains('Python')]

# In[195]:


# what are the Max Number of Subscribers for Each Level of courses
df.groupby('level').agg({'num_subscribers':'max'})

