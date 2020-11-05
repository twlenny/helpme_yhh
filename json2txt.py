#!/usr/bin/env python
# coding: utf-8

# In[198]:



import json
 
path = r"translation2019zh_valid.json"
file = open(path, 'r',encoding='utf-8')
file1 = open(r"test.txt", 'w')


# In[ ]:





# In[199]:


#for line in file.readlines():

for line in file.readlines():
    fileJson = json.loads(line)
    chinese = fileJson["chinese"]
    english = fileJson["english"]


# In[200]:


print(chinese)


# In[201]:


print(english)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




