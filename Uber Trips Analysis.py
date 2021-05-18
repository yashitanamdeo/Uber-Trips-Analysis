#!/usr/bin/env python
# coding: utf-8

# # Uber Trips Analysis using Python

# ### Importing the necessary Python libraries and dataset

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:/Users/Arvind/Desktop/Uber_Trips_Analysis/Dataset/uber-raw-data-sep14.csv")
data["Date/Time"] = data["Date/Time"].map(pd.to_datetime) 
data.head()


# ##### let’s prepare the data to analyze the Uber trips according to days and hours:

# In[5]:


data["Day"] = data["Date/Time"].apply(lambda x: x.day)
data["Weekday"] = data["Date/Time"].apply(lambda x: x.weekday())
data["Hour"] = data["Date/Time"].apply(lambda x: x.hour)
print(data.head())


# ##### As this dataset contains Uber trips for the September month so let’s have a look at each day to see on which day the Uber trips were highest:

# In[6]:


sns.set(rc={'figure.figsize':(12, 10)})
sns.distplot(data["Day"])


# ##### By looking at the daily trips we can say that the Uber trips are rising on the working days and decreases on the weekends. Now let’s analyze the Uber trips according to the hours:

# In[7]:


sns.distplot(data["Hour"])


# ##### According to the hourly data, the Uber trips decreases after midnight and then start increasing after 5 am and the trips keep rising till 6 pm such that 6 pm is the busiest hour for Uber then the trips start decreasing. Now let’s analyze the Uber trips according to the weekdays:

# In[8]:


sns.distplot(data["Weekday"])


# ##### In the above figure 0 indicates Sunday, on Sundays the Uber trips and more than Saturdays so we can say people also use Uber for outings rather than for just going to work. On Saturdays, the Uber trips are the lowest and on Mondays, they are the highest. Now let’s have a look at the correlation of hours and weekdays on the Uber trips:

# In[9]:


# Correlation of Weekday and Hour
df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
df = df.unstack()
sns.heatmap(df, annot=False)


# ##### As we are having the data about longitude and latitude so we can also plot the density of Uber trips according to the regions of the New Your city:

# In[10]:


data.plot(kind='scatter', x='Lon', y='Lat', alpha=0.4, s=data['Day'], label='Uber Trips',
figsize=(12, 8), cmap=plt.get_cmap('jet'))
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()


# # Summary 

# So this is how we can analyze the Uber trips for New York City. Some of the conclusions that I got from this analysis are:
# 
# 1. Monday is the most profitable day for Uber.
# 2. On Saturdays less number of people use Uber.
# 3. 6 pm is the busiest day for Uber.
# 4. On average a rise in Uber trips start around 5 am.
# 5. Most of the Uber trips originate near the Manhattan region in New York.
