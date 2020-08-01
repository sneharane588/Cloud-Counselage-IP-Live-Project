#!/usr/bin/env python
# coding: utf-8

# # <center>PROBLEM STATEMENT<br><br>TECHNOLOGY: DATA SCIENCE</center>

# Students from different cities from the state of Maharashtra had applied for the Cloud Counselage Internship Program. We have the dataset of consisting information of all the students. Using this data we want to get more insights and draw out more meaningful conclusions.

# ## 1. Interns need to preprocess the data for missing values, unknown values, encoding categorical values.

# In[1]:


# to read data and data manipulation

import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import sys

# In[2]:


df =pd.read_csv(sys.argv[1])
# df.head(10)


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

# ## 2. Create a data visualization model to build graphs from the dataset answering the following questions:

# ## a. The number of students applied to different technologies.

# In[19]:


# get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
with PdfPages('Visualization-output.pdf') as pdf:
    # <i>Bar Plot Representation</i>

    # In[20]:


    df1 = df['Areas of interest'].value_counts()
    # print(df1)

    colors = [plt.cm.Spectral(i/float(len(df1.keys()))) for i in range(len(df1.keys()))]

    ax = df1.plot(kind='bar', figsize=(18, 8), color=colors)


    ax.set_title('\nDistribution of students applied to different technologies\n\n', fontsize=20)
    ax.set_xlabel('\nAreas of Interest', fontsize=18)
    ax.set_ylabel('Number of students applied', fontsize=18)

    # create a list to collect the plt.patches data
    totals = []

    # find the values and append to list
    for i in ax.patches:
        totals.append(i.get_height())

    # set individual bar lables using above list
    total = sum(totals)

    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+.5,             str(round((i.get_height()/total)*100, 2))+'%', fontsize=15,
                    color='dimgrey')
        
    #save the graph into pdf.
    from matplotlib.backends.backend_pdf import PdfPages

    pdf = PdfPages('1.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # <i>Pie Chart Representation through Percentages</i>

    # In[21]:


    fig = plt.figure(figsize = (22, 10))
    ax = fig.add_subplot()

    # ----------------------------------------------------------------------------------------------------
    # plot the data using matplotlib
    ax.pie(df1, # pass the values from our dictionary
           labels = df1.keys(), # pass the labels from our dictonary
           autopct = '%1.1f%%', # specify the format to be plotted
           textprops = {'fontsize': 20, 'color' : "white"} # change the font size and the color of the numbers inside the pie
          )

    # set the title
    ax.set_title("\nPie chart", fontsize=22)

    # set the legend and title to the legend
    ax.legend(loc = "upper left", bbox_to_anchor = (1, 0, 0.5, 1), fontsize = 20, title = "Technologies");
    pdf = PdfPages('2.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## b. The number of students applied for Data Science who knew ‘’Python” and who didn’t.

    # In[22]:


    df['Areas of interest'].value_counts()


    # In[23]:


    df_area = pd.DataFrame(df[['Full Name', 'Areas of interest']])

    df_area = df_area[df_area['Areas of interest'].str.contains('Data Science',case=False)]
    ds_stud, col = df_area.shape
    # df_area


    # In[24]:


    df_area['prog'] = df[['Programming Language Known other than Java (one major)']] == 'Python'
    df_area['prog'].replace({True: "Knows Python", False: "Don't know Python"}, inplace=True)

    df_python = df_area['prog'].value_counts()


    # Horizontal Bar

    # In[25]:


    # print(df_python)
    fig = plt.figure(figsize = (12, 8))
    ax = fig.add_subplot()

    ax = df_python.plot(kind='barh', color=['lightgreen','lightblue']) 

    # iterate over every x and y and annotate the value on the top of the barchart

    for rect in ax.patches:
        width = rect.get_width()
        plt.text(rect.get_x()-30+rect.get_width(), rect.get_y()+0.5*rect.get_height(),
        '%d' % int(width),
        ha='center', va='center')

    ax.set_title("Number of students applied for Data Science\nwho knew Python and who didn’t.\n", fontsize = 18);
    ax.set_xlabel('\nNumber of Students', fontsize = 14)
    # change the size of the x and y ticks
    ax.tick_params(axis = 'x', labelrotation = 90, labelsize = 12)
    ax.tick_params(axis = 'y', labelsize = 16)

    pdf = PdfPages('3.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[26]:


    df_area['other than Java'] = df[['Programming Language Known other than Java (one major)']]
    df_area = df_area[df_area['other than Java'].str.contains('Python',case=False)]

    ds_py, col = df_area.shape

    # df_area


    # <i>Grouped Bar Plot Representation</i>

    # In[27]:


    # Grouped Bar Plot using MatPlotLib

    # print('\n\n') 
    # print('Total Number of Students                               : ', total_stud)
    # print('Number of Data Science students                        : ', ds_stud)
    # print('Number of students other students                      : ', total_stud - ds_stud)
    # print('Number of Data Science students who knows Python       : ', ds_py)
    # print('Number of Data Science students who don\'t know Python  : ', ds_stud - ds_py,'\n\n')

    pos = list(range(1)) 
    width = 0.2
        
    # Plotting the bars
    fig, ax = plt.subplots(figsize=(12,10))

    # Create a bar with Total Number of Students,
    # in position pos,
    plt.bar(pos, 
            #using total stud data,
            total_stud, 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#EE3224', 
            # with label the first value in first_name
            label='Total') 

    # Create a bar with Data Science students,
    # in position pos + some width buffer,
    plt.bar([p + width for p in pos], 
            #Data Science students,
            ds_stud,
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#F78F1E', 
            # with label the second value in first_name
            label='Data Science students') 

    # Create a bar with Data Science students who knows Python,
    # in position pos + some width buffer,
    plt.bar([p + width*2 for p in pos], 
            #Data Science students who knows Python,
            ds_py, 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#FFC222', 
            # with label the third value in first_name
            label='Data Science students who knows Python') 

    plt.bar([p + width*3 for p in pos], 
            #using Data Science students who don\'t know Python,
            ds_stud - ds_py, 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#FFEF85', 
            # with label the third value in first_name
            label='Data Science students who don\'t know Python') 


    # Set the y axis label
    ax.set_ylabel('Number of Students', fontsize=16)

    # Set the chart's title
    ax.set_title('The number of students applied for Data Science\nwho knew "Python” and who didn’t.\n', fontsize=22)

    # Set the position of the x ticks
    ax.set_xticks([p + width for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels(['The number of students applied for Data Science\nwho knew "Python” and who didn’t.'], fontsize=16)

    # Setting the x-axis and y-axis limits
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0,total_stud+1500] )

    # Adding the legend and showing the plot
    plt.legend(['Total Students' , 'Data Science Students' , 'Data Science students who knows Python','Data Science students who don\'t know Python'], loc='upper right')
    # plt.grid()

    # create a list to collect the plt.patches data
    totals = []

    # find the values and append to list
    for i in ax.patches:
        totals.append(i.get_height())

    # set individual bar lables using above list
    total = sum(totals)-1202

    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()+.06, i.get_height(),
                str(round((i.get_height()/total)*100, 2))+'%\n', fontsize=15,
                    color='dimgrey')

    pdf = PdfPages('4.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## c. The different ways students learned about this program.

    # In[28]:


    df_ref = df['How Did You Hear About This Internship?'].value_counts()
    # print(df_ref)

    ax = df_ref.plot(kind='bar', figsize=(16, 12), color=colors, rot=0)


    ax.set_title('Sources of Information about internship\n\n', fontsize=20)
    ax.set_xlabel('Sources',fontsize=18)
    ax.set_ylabel('Number of students applied',fontsize=18)

    # create a list to collect the plt.patches data
    totals = []

    # find the values and append to list
    for i in ax.patches:
        totals.append(i.get_height())

    # set individual bar lables using above list
    total = sum(totals)

    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.03, i.get_height()+.5,             str(round((i.get_height()/total)*100, 2))+'%\n', fontsize=15,
                    color='dimgrey')

    pdf = PdfPages('5.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # Donut Chart

    # In[29]:


    # colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','lightgreen', 'gold', 'lightblue', 'lightcoral','magenta']
    # explode = (0, 0, 0, 0, 1, 0, 1, 0, 1)  # explode a slice if required
    from palettable.colorbrewer.qualitative import Pastel1_9

    plt.figure(figsize=(22,10))

    plt.pie(df_ref,  labels=df_ref.keys(),colors=Pastel1_9.hex_colors, autopct='%1.1f%%',
            shadow=True,
            wedgeprops = { 'linewidth' : 0.8, 'edgecolor' : 'white' })

    plt.rcParams['text.color'] = 'brown'

    #draw a circle at the center of pie to make it look like a donut
    centre_circle = plt.Circle((0,0),0.65, fc='white',linewidth=0.5)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Sources of Information about internship',fontsize=20)

    pdf = PdfPages('6.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[30]:


    import seaborn as sns

    sns.catplot(x='How Did You Hear About This Internship?',kind="count", palette="ch:.25", data=df,height=6, aspect=2)

    # f, ax = plt.subplots(figsize=(14, 8))
    # sns.countplot(y="How Did You Hear About This Internship?", data=df, color="orange");

    pdf = PdfPages('7.pdf')    
    pdf.savefig()

    plt.close()
    #pdf.close()


    # ## d. Students who are in the fourth year and have a CGPA greater than 8.0.

    # In[31]:


    # df['Which-year are you studying in?'].value_counts()


    # In[32]:


    year=pd.DataFrame(df[['First Name','Last Name']])

    year['Which-year are you studying in?']=df[['Which-year are you studying in?']]=='Fourth-year'
    # year[~year[['Which-year are you studying in?']].isin([False])]
    # print(year['Which-year are you studying in?'].value_counts())

    vFalse, vTrue = year['Which-year are you studying in?'].value_counts()

    # year['Which-year are you studying in?']=year[year['Which-year are you studying in?']]
    # print(year)

    import numpy as np
    year.replace(False, np.nan,inplace=True)
    year.replace(1.0, 'Fourth-year',inplace=True)
    # print(year)
    year = year.dropna(axis=0)
    year


    # Pie Chart

    # In[33]:


    labels = 'Students who are in 4th year', 'Others'
    explode = (0.1, 0)  # only "explode" the 1st slice

    fig = plt.figure(figsize = (22, 10))
    ax = fig.add_subplot()

    # print('\nOut of 10,000 Students,\n\nNumber of 4th year students : ', vTrue)
    # print('Others : ', vFalse)

    # plot the data using matplotlib
    ax.pie([vFalse, vTrue], # pass the values from our dictionary
           labels = labels, # pass the labels from our dictonary
           autopct = '%1.1f%%', # specify the format to be plotted
           colors=['lightgreen','green'],
           startangle=100,
           explode=explode,
           shadow=True,
           textprops = {'fontsize': 20, 'color' : "white"} # change the font size and the color of the numbers inside the pie
          )

    # set the title
    ax.set_title("\nDistribution of Students with respect to Academic year", fontsize=22)

    # set the legend and title to the legend
    ax.legend(loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1), fontsize = 20, title = "Description");

    pdf = PdfPages('8.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[34]:


    year['CGPA']=df['CGPA/ percentage']
    x=len(year[year.CGPA>8.0])
    x1=len(year[year.CGPA<=8.0]) 

    # print('\nOut of 2,477 4th year Students,\n\n Having CGPA greater than 8.0 : ',x )
    # print('others : ', x1)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = '4th year Students having CGPA greater than 8.0', 'Other 4th year Students'
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig = plt.figure(figsize = (22, 10))
    ax = fig.add_subplot()

    # plot the data using matplotlib
    ax.pie([x,x1], # pass the values from our dictionary
           labels = labels, # pass the labels from our dictonary
           autopct = '%1.1f%%', # specify the format to be plotted
           colors=['lightcoral','brown'],
           startangle=180,
           explode=explode,
           shadow=True,
           textprops = {'fontsize': 20, 'color' : "white"} # change the font size and the color of the numbers inside the pie
          )

    # set the title
    ax.set_title("\nDistribution of Students with respect to CGPA", fontsize=22)

    # set the legend and title to the legend
    ax.legend(loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1), fontsize = 20, title = "Description");

    pdf = PdfPages('9.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[35]:


    year['CGPA']=df['CGPA/ percentage']>8.0

    year.replace(False, np.nan,inplace=True)
    year.dropna(inplace=True)

    year['CGPA']=df['CGPA/ percentage']

    # year


    # In[36]:


    # Nested Donut chart
    # to display Hierarchical data
    # print('\n\n') 
    # print('Total Number of Students                                        : ', total_stud)
    # print('Number of 4th year students :                                   : ', vTrue)
    # print('Number of students other than fourth year :                     : ', vFalse)
    # print('Number of 4th year Students with greater than 8.0 CGPA          : ', x)
    # print('Number of 4th year Students with less than or equal to 8.0 CGPA : ', x1,'\n\n')

    group_names=['4th year studentes', 'other than 4th year Students']
    group_size=[vTrue, vFalse]
    subgroup_names=['Greater than\n8.0 CGPA', 'Others','']
    d1 = 7523

    subgroup_size=[x, x1,d1]
       
    # Create colors
    a, b=[plt.cm.Blues, plt.cm.Greens]
    plt.rcParams['text.color'] = 'red'
     
    # First Ring (outside)
    fig=plt.subplots(figsize = (22, 10))

    plt.pie(group_size, radius=1.3, labels=group_names, autopct = '%1.2f%%', colors=[a(0.6), b(0.6)],shadow=True,
             textprops={"fontsize":13},
            wedgeprops = { 'linewidth' : 0.8, 'edgecolor' : 'white' } )

        
    # Second Ring (Inside)
    plt.pie(subgroup_size, radius=1.3-0.6, labels=subgroup_names, labeldistance=0.7,autopct = '%1.2f%%',
            colors=[a(0.5), a(0.4), b(0.3)], shadow=True,  textprops={"fontsize":13},
            wedgeprops = { 'linewidth' : 0.8, 'edgecolor' : 'white' },
            rotatelabels=True)

    circle1=plt.Circle((0,0),.35,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(circle1)
    # fig.gca().add_artist(circle2)


    plt.title('Disribution of Students w.r.t. Academic year and CGPA\n\n',color='brown',fontsize=20)
    # plt.legend(loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1), fontsize = 20, title = "Description");

    # show it
    pdf = PdfPages('10.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[37]:


    # Grouped Bar Plot using MatPlotLib

    # print('\n\n') 
    # print('Total Number of Students                               : ', total_stud)
    # print('Number of 4th year students                            : ', vTrue)
    # print('Number of students other than fourth year :            : ', vFalse)
    # print('Number of 4th year Students with greater than 8.0 CGPA : ', x)
    # print('Number of Students with less than or equal to 8.0 CGPA : ', x1,'\n\n')

    pos = list(range(1)) 
    width = 0.25 
        
    # Plotting the bars
    fig, ax = plt.subplots(figsize=(10,9))

    # Create a bar with pre_score data,
    # in position pos,
    plt.bar(pos, 
            #using total stud data,
            total_stud, 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#EE3224', 
            # with label the first value in first_name
            label='Total') 

    # Create a bar with mid_score data,
    # in position pos + some width buffer,
    plt.bar([p + width for p in pos], 
            #using 4th data,
            vTrue,
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#F78F1E', 
            # with label the second value in first_name
            label='Total 4th') 

    # Create a bar with post_score data,
    # in position pos + some width buffer,
    plt.bar([p + width*2 for p in pos], 
            #using gt cgpa data,
            x, 
            # of width
            width, 
            # with alpha 0.5
            alpha=0.5, 
            # with color
            color='#FFC222', 
            # with label the third value in first_name
            label='cgpa gt 8.0') 

    # plt.bar([p + width*3 for p in pos], 
    #         #using other cgpa data,
    #         x1, 
    #         # of width
    #         width, 
    #         # with alpha 0.5
    #         alpha=0.5, 
    #         # with color
    #         color='#FFEF85', 
    #         # with label the third value in first_name
    #         label='other cgpa') 


    # Set the y axis label
    ax.set_ylabel('Number of Students', fontsize=16)

    # Set the chart's title
    ax.set_title('Students who are in the fourth year and have a CGPA greater than 8.0\n', fontsize=22)

    # Set the position of the x ticks
    ax.set_xticks([p + width for p in pos])

    # Set the labels for the x ticks
    ax.set_xticklabels(['Students who are in the fourth year and have a CGPA greater than 8.0'], fontsize=16)

    # Setting the x-axis and y-axis limits
    plt.xlim(min(pos)-width, max(pos)+width*3)
    plt.ylim([0,total_stud+1500] )

    # Adding the legend and showing the plot
    plt.legend(['Total Students' , '4th year Students' , '4th year Students with CGPA greater than 8.0'], loc='upper right')

    # create a list to collect the plt.patches data
    totals = []

    # find the values and append to list
    for i in ax.patches:
        totals.append(i.get_height())

    # set individual bar lables using above list
    total = sum(totals) - 4174

    # set individual bar lables using above list
    for i in ax.patches:
        # get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()+.06, i.get_height(),
                str(round((i.get_height()/total)*100, 2))+'%\n', fontsize=15,
                    color='dimgrey')
    # plt.grid()
    pdf = PdfPages('11.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## e. Students who applied for Digital Marketing with verbal and written communication score greater than 8.

    # In[38]:


    df_digi = pd.DataFrame(df[['Full Name', 'Areas of interest',
                               'Rate your verbal communication skills [1-10]',
                              'Rate your written communication skills [1-10]']])

    df_digi = df_digi[df_digi['Areas of interest'].str.contains('Digital Marketing',case=False)]
    digi_stud, col = df_digi.shape
    # df_digi[['Full Name', 'Areas of interest']]


    # In[39]:


    # print("Total Digital Marketing Students : ", digi_stud)

    df_digi['verbal'] =  df_digi[['Rate your verbal communication skills [1-10]']] > 8
    vfalse, vtrue = df_digi['verbal'].value_counts()

    # print("\nDigital Marketing Students with :\n\n1) Verbal communication rate greater than 8 : \n",
    #      df_digi['verbal'].value_counts(),"\n")

    df_digi['written'] =  df_digi[['Rate your written communication skills [1-10]']] > 8
    wfalse, wtrue = df_digi['written'].value_counts()

    # print("2) Written communication rate greater than 8 : \n",
    #     df_digi['written'].value_counts(),"\n")


    # In[40]:


    # removing DM students records with <=8 verbal comm. rate

    df_digi = df_digi[df_digi['Rate your verbal communication skills [1-10]'] > 8]   # returns 251 rows

    # removing DM students records with <=8 written comm. rate

    df_digi = df_digi[df_digi['Rate your written communication skills [1-10]'] > 8]  # returns 92 rows

    # print('\nNumber of Students who applied for \nDigital Marketing with both verbal and written communication score greater than 8 : ')

    both_true,t = df_digi.shape
    df_digi.drop(df_digi.columns[[4, 5]], axis = 1, inplace = True)

    # df_digi


    # Stacked Bar Chart

    # In[41]:


    from matplotlib import rc

    rc('font', weight='bold')
     
    # Values of each group
    bars1 = [digi_stud]
    bars2 = [vtrue]
    bars3 = [wtrue]
    bars4 = [both_true]

    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()
    # Heights of bars1 + bars2 + bars3
    barss = np.add(bars, bars3).tolist()

    # The position of the bars on the x-axis
    r = [0]
     
    # Names of group and bar width
    names = ['Digital Marketing']
    barWidth = 1

    plt.subplots(figsize=(8,10))
        
    # Create lighgreen bars
    plt.bar(r, bars1, color='#b5ffb9', edgecolor='white', width=barWidth, label = "Digital Marketing\nStudents\n")

    # Create orange bars (2nd), on top of the firs ones
    plt.bar(r, bars2, bottom=bars1, color='#f9bc86', edgecolor='white', width=barWidth, label = "with verbal\ncomm. score > 8\n")

    # Create lightblue bars (2nd), on top of the firs ones
    plt.bar(r, bars3, bottom=bars, color='#a3acff', edgecolor='white', width=barWidth, label = "with written\ncomm. score > 8\n")

    # Create coral bars (top)
    plt.bar(r, bars4, bottom=barss, color='coral', edgecolor='white', width=barWidth, label = "with both\n scores > 8")

    plt.rcParams['text.color'] = 'dimgrey'

    # Custom X axis
    plt.xticks(r, names, fontsize=16)
    plt.ylabel("Number of students", fontsize=16)
    plt.title('\nStudents who applied for Digital Marketing\n', fontsize=20) 

    plt.xlim(barWidth, barWidth-2)
    # plt.ylim([0,total_stud+1500] )
    plt.legend(loc='upper center', bbox_to_anchor=(1,1), ncol=1, fontsize=16)

    pdf = PdfPages('12.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[42]:


    # df_digi[['Rate your verbal communication skills [1-10]', 'Rate your written communication skills [1-10]']].corr()


    # Heat map to display correlation

    # In[43]:


    sns.heatmap(df_digi[['Rate your verbal communication skills [1-10]', 'Rate your written communication skills [1-10]']].corr())
    plt.title('Covariance Plot\nverbal vs written communication\n')

    pdf = PdfPages('13.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[44]:


    # scatterplot

    plt.figure(figsize = (20,8))

    plt.scatter(df_digi['Rate your verbal communication skills [1-10]'],df_digi['Rate your written communication skills [1-10]'])
    plt.title('Verbal ratings vs Written ratings')
    plt.xlabel('Verbal ratings')
    plt.ylabel('Written ratings')
    # pdf = PdfPages('14.pdf')    
    pdf.savefig()
    #plt.show()
    plt.close()
    #pdf.close()


    # Venn diagram

    # In[45]:


    from matplotlib_venn import venn2

    # First way to call the 2 group Venn diagram:
    out = venn2(subsets = (vtrue, wtrue, both_true),
          set_labels = ('with verbal\ncomm. score > 8', 
                        'with written\ncomm. score > 8'),
               set_colors=('b', 'orange'), alpha=0.5, normalize_to=7
    #             subset_label_formatter=True
               )

    for text in out.subset_labels:
        text.set_fontsize(16)
        
    plt.title("Students who applied\nfor Digital Markeing\n", fontsize = 20)    

    pdf = PdfPages('15.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## f. Year-wise and area of study wise classification of students.

    # In[46]:


    # Major/Area of Study', 'Course Type', 'Which-year are you studying in?

    ddff=pd.DataFrame(df[['Major/Area of Study', 'Which-year are you studying in?']])

    # print(df['Which-year are you studying in?'].value_counts())
    ii, i, iv, iii = df['Which-year are you studying in?'].value_counts()

    # print("\n", df['Major/Area of Study'].value_counts())
    comp, elect, electro = df['Major/Area of Study'].value_counts()

    ddff.describe()


    # Treemap

    # In[47]:


    import squarify    # pip install squarify (algorithm for treemap)
     
    # If you have 2 lists
    squarify.plot(sizes=[i, ii, iii, iv], norm_x=100, norm_y=100, label=["First-year", "Second-year", "Third-year", "Fourth-year"], alpha=.66, pad = False)
    plt.axis('off')
    plt.title('treemap for Academic year')

    pdf = PdfPages('16.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[48]:


    import squarify    # pip install squarify (algorithm for treemap)
     
    # If you have 2 lists
    squarify.plot(sizes=[comp, elect, electro], label=["Computer Engineering", "Electrica\nEngineering", "Electronics\nan\nTelecommunication"], alpha=.6 )
    plt.axis('off')
    plt.title('Treemap for Area of Study')

    pdf = PdfPages('17.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## g. City and college wise classification of students.

    # In[49]:


    df_city_clg = pd.DataFrame(df[['College name', 'City']])
    # df_city_clg.describe()
    # df_city_clg.plot(kind='pie', figsize=(18,6))
    # plt.show()


    # In[50]:


    city = pd.get_dummies(df_city_clg['City'])
    #city


    # In[51]:


    #df_city_clg['City'].value_counts()


    # Bar chart

    # In[52]:


    f, ax = plt.subplots(figsize=(14, 8))
    ax = (df_city_clg['City'].value_counts()/len(df)*100).plot(kind="bar",color='lightgrey', rot=0)
    for p in ax.patches:
        ax.annotate('{:.2f}%'.format(p.get_height()), (p.get_x()+0.1, p.get_height()-1))
    ax.set_title('\nCity wise classification of Students\n', fontsize=18)
    ax.set_xlabel('\nCity Names', fontsize=16)
    ax.set_ylabel('Number of Students', fontsize=16)

    pdf = PdfPages('18.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[53]:


    # df['College name'].value_counts()


    # In[54]:


    # df_city_clg.groupby('City', axis=0).sum()


    # In[55]:


    df_city_clg['Full Name'] = df['Full Name']
    # df_city_clg


    # In[56]:


    # horizontal Bar chart

    f, ax = plt.subplots(figsize=(30, 34))
    ax = (df_city_clg['College name'].value_counts()/len(df)*100).plot(kind="barh",color=colors, rot=0)

    for rect in ax.patches:
        width = rect.get_width()
        plt.text(rect.get_x()+0.4+rect.get_width(), rect.get_y()+0.5*rect.get_height(),
        '{:.2f}%'.format(width), fontsize=24,
        ha='center', va='center')

    # ax.set_title("Number of students applied for Data Science who knew Python and who didn’t.\n", fontsize = 18);
    # ax.set_xlabel('\nNumber of Students', fontsize = 14)
    # change the size of the x and y ticks
    ax.tick_params(axis = 'x', labelrotation = 90, labelsize = 26)
    ax.tick_params(axis = 'y', labelsize = 26)

    ax.set_title('\nCollege wise classification of Students\n', fontsize=38)
    ax.set_xlabel('\nPercentages of Number of Students', fontsize=30)
    ax.set_ylabel('College Names', fontsize=30)

    pdf = PdfPages('19.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## h. Plot the relationship between the CGPA and the target variable.

    # In[57]:


    from sklearn.preprocessing import LabelEncoder

    lb_make = LabelEncoder()
    df["Label_encoded"] = lb_make.fit_transform(df["Label"])
    # df[["Label", "Label_encoded"]]


    # In[58]:


    df[['Label_encoded', 'CGPA/ percentage']].corr()


    # In[59]:


    # scatterplot
    plt.scatter(df["Label"], df["CGPA/ percentage"])
    plt.title('Scatterplot CGPA vs Target variable')

    pdf = PdfPages('20.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[60]:


    # df.boxplot(by='Label_encoded', 
    #                        column=['CGPA/ percentage'], 
    #                        grid=False)

    # make boxplot with Seaborn
    sns.boxplot(y='CGPA/ percentage', x='Label', 
                     data=df, 
                     width=0.5,
                     palette="colorblind")
    plt.title('Boxplot CGPA vs Target variable')


    pdf = PdfPages('21.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # In[61]:


    # make boxplot with Seaborn
    sns.boxplot(y='CGPA/ percentage', x='Label', 
                     data=df, 
                     width=0.5,
                     palette="colorblind")

     
    # add stripplot to boxplot with Seaborn
    sns.stripplot(y='CGPA/ percentage', x='Label', 
                       data=df, 
                       jitter=False, 
                       marker='o', 
                       alpha=0.5,
                       color='lightblue')

    plt.title('boxplot with Stipplot\nCGPA vs Target variable')

    pdf = PdfPages('22.pdf')    
    pdf.savefig()
    plt.close()
    #pdf.close()


    # In[62]:


    # violinplot
    sns.violinplot(x ='Label', y ='CGPA/ percentage', data = df) 
    plt.title('Violinplot CGPA vs Target variable')

    pdf = PdfPages('23.pdf')    
    pdf.savefig()
    plt.close()
    #pdf.close()


    # ## i. Plot the relationship between the Area of Interest and the target variable.

    # In[63]:


    # get the area wise count of eligible and non-eligile students

    aoi = pd.get_dummies(df['Areas of interest'])

    # for c in aoi.columns:
    #     print("---- %s ---" % c)
    #     print(aoi[c].value_counts())


    # Grouped Bar chart

    # In[64]:


    # count the number of eligible and ineligible students area of interest wise.

    df_rel= df.groupby(['Areas of interest','Label'])['Areas of interest'].size()[lambda x: x < 1000]
    # df_rel

    #now plot the bar graph.
    fig,ax = plt.subplots(figsize = (15,7))
    df_rel = df_rel.to_frame()
    df_rel.unstack().plot.bar(ax =ax)
    plt.xlabel("Eligible and Ineligible students with Areas of Interest", fontsize = 16)
    plt.ylabel("Number of Applicants", fontsize = 16)
    plt.title("\nRelationship between\nthe Area of Interest and and Eligiblity\n", fontsize = 16)

    pdf = PdfPages('24.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()


    # ## j. Plot the relationship between the year of study, major, and the target variable.

    # In[65]:


    #prepare data.
    df_r = df[['Which-year are you studying in?','Major/Area of Study','Label','State']]
    df_r = df_r.rename(columns={'Which-year are you studying in?':'Year of Study','Major/Area of Study':'Major','State':'Count'})
    #now count the number of students.
    df_r = df_r.groupby(["Year of Study","Major","Label"],as_index=False)['Count'].count()
    #set the index year of study.
    df_r = df_r.set_index(['Year of Study','Major','Label'],drop=True).unstack('Major','Label')

    #now plot the bar graph.
    ax=df_r.plot(kind='bar',figsize=(18,10),width=0.8,color=['#ff0000','#0000ff','#00ff00'],fontsize=16)
    ax.set_title('\nYear and Major wise Eligibilty of Students\n',fontsize=20)
    ax.set_xlabel('Year and Eligiblity')
    ax.set_ylabel('Number of Applicants')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=14)
    ax.get_yaxis().set_visible(False)
    for p in ax.patches:
        ax.annotate(np.round(p.get_height(),decimals=2), 
                    (p.get_x()+p.get_width()/2., p.get_height()), 
                    ha='center', 
                    va='center', 
                    xytext=(0, 10), 
                    textcoords='offset points',
                    fontsize = 14, fontweight='bold'
                    
                   )
        
    pdf = PdfPages('25.pdf')    
    pdf.savefig()
    # plt.show()
    plt.close()
    #pdf.close()
    print("Visualization-output.pdf Created successfully !")

    
