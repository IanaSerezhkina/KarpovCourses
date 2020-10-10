#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import apriori 


# In[2]:


purchases = pd.read_csv('https://stepik.org/media/attachments/lesson/409319/test1_completed.csv')
purchases.head()


# In[3]:


purchases = purchases.rename(columns={'Товар': 'goods', 'Количество': 'quantity'})


# In[4]:


df = pd.pivot_table(purchases, values='quantity', index='id', columns='goods').fillna(0)


# In[6]:


def encode_units(x):
    if x <= 0:
        return 0
    if x >= 0.1:
        return 1


# In[7]:


df_new = df.applymap(encode_units)
df_new.head()


# In[54]:


transactions = len(df_new.index)


# In[109]:


frequent_itemsets = apriori(df_new, min_support=0.05, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets = frequent_itemsets[frequent_itemsets['length']==2]
frequent_itemsets.head()


# In[110]:


frequent_itemsets['Встречаемость'] = frequent_itemsets['support'] * transactions
frequent_itemsets = frequent_itemsets.drop(columns=['length', 'support'])


# In[111]:


frequent_itemsets = frequent_itemsets.sort_values('Встречаемость', ascending=False)


# In[112]:


frequent_itemsets = pd.DataFrame(frequent_itemsets).reset_index(drop=True)


# In[115]:


frequent_itemsets_top = frequent_itemsets.head(5)
frequent_itemsets_top


# In[ ]:




