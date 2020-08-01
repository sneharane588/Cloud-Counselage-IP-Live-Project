#!/usr/bin/env python
# coding: utf-8

# # <center>PROBLEM STATEMENT<br><br>TECHNOLOGY: DATA SCIENCE</center>

# Students from different cities from the state of Maharashtra had applied for the Cloud Counselage Internship Program. We have the dataset of consisting information of all the students. Using this data we want to get more insights and draw out more meaningful conclusions.

# ## 1. Interns need to preprocess the data for missing values, unknown values, encoding categorical values.

# In[1]:


# to read data and data manipulation

import pandas as pd
import sys

# In[2]:


df=pd.read_csv(sys.argv[1])



# In[3]:


# df.tail()


# In[4]:


total_stud, i = df.shape
# df.shape   # dimensions of DataFrame


# In[5]:


# df.columns


# In[6]:


# df.info()


# In[7]:


# df.describe()


# In[8]:


# df.isna().sum()


# In[9]:


# df.Label.value_counts()


# In[10]:


# df.Gender.value_counts()


# ## 1. Preprocess the data for missing values, unknown values, encoding categorical values.

# ### let's rename the columns so that they make sense

# In[11]:


# df.rename(columns={'DOB [DD/MM/YYYY]':'DOB', 
#                        'Email Address':'Email',
#                        'Major/Area of Study' : 'Area of Study',
#                        'Which-year are you studying in?' : 'Academic Year', 
#                        'CGPA/ percentage' : 'CGPA', 
#                        'Programming Language Known other than Java (one major)' : 'Programming Language except Java', 
#                        'Rate your written communication skills [1-10]' : 'Rating of written communication',
#                        'Rate your verbal communication skills [1-10]' : 'Rating of verbal communication',
#                        'How Did You Hear About This Internship?' : 'Reference'}, inplace=True)
# df.columns


# In[12]:


df.dropna(axis='columns', how='all',inplace=True) 
# df


# In[13]:


# dimensions of DataFrame

# df.shape


# In[14]:


# df['First Name'].value_counts()


# In[15]:


# df['Last Name'].value_counts()


# <h5>There are students having exactly same First Name or having exactly same Last Name</h5><br>
# So, to check that if there are any duplicate records,<h4><u>Combining the First Name and Last Name attribute to verify the redundancy or duplicate records.</u></h4>

# In[16]:


df['Full Name'] = df[['First Name', 'Last Name']].apply(lambda x: ' '.join(x), axis = 1)
# df['Full Name']


# In[17]:


# df['Full Name'].value_counts().head(20)


# Now its ensured that there are only unique records present for each student.<br>

# ## 3. Identify the best binary classifier to classify data into “eligible/1” and “not eligible/0”.

# In[18]:


# Label encoding
from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()

df_lencode = pd.DataFrame(df[['City', 'Age', 'College name', 'Degree', 
                              'Major/Area of Study', 'Which-year are you studying in?',
                              'CGPA/ percentage', 'Expected Graduation-year', 'Areas of interest',
                             'Current Employment Status', 'Have you worked core Java', 
                             'Programming Language Known other than Java (one major)', 
                             'Have you worked on MySQL or Oracle database',
                             'Have you studied OOP Concepts', 'Rate your written communication skills [1-10]',
                             'Rate your verbal communication skills [1-10]',
                             'How Did You Hear About This Internship?', 'Label']])

#  Splitting the attributes into independent and dependent attributes
label_encode = {'Label':{'ineligible': 0, 'eligible': 1}}
df_lencode.replace(label_encode, inplace=True)

X = df_lencode.iloc[:,:-1].values # attributes to determine dependent variable

# lb_make = LabelEncoder()   # label encoding
X[:,0] = lb_make.fit_transform(X[:,0])
for i in range(2,6):
    X[:,i] = lb_make.fit_transform(X[:,i])
for i in range(8,17):
   X[:,i] = lb_make.fit_transform(X[:,i])
X[:,16] = lb_make.fit_transform(X[:,16])
X = pd.DataFrame(X)
X


# Trying different ML algorithms for binary classification

# In[19]:


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix


# In[20]:


df["Label_encoded"] = lb_make.fit_transform(df["Label"])
df[["Label", "Label_encoded"]]

labels = df['Label_encoded']
features = X


# In[21]:


# Split our data
xtrain, xtest, ytrain, ytest = train_test_split(features,
                                                          labels,
                                                          test_size=0.3,
                                                          random_state=42)




# ### _Decision Tree Classifier_

# In[35]:


# from sklearn import tree 
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(xtrain, ytrain)
# preds = clf.predict(xtest)


# In[36]:


# print(f1_score(ytest, preds))


# F1 score achieved by Decision Tree Classifier kernel is 1.0

# ### _Random Forest Classifier_

# In[37]:


from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
RF.fit(xtrain, ytrain)
preds = RF.predict(xtest)


# In[38]:


print(f1_score(ytest, preds))


# F1 score achieved by Random Forest Classifier is 1.0

# ### <br><hr>_Here we can see that Random Forest classifier and  Decision Tree are giving the highest f1 score as 1.0 !_

# In[ ]:




