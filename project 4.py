import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df= pd.read_csv("netflix_titles.csv")
#print(df)
# Data handling 
df.isnull().sum()
df1= df.dropna(subset=["type","release_year","rating","country","duration"])
print(df1)
#df.info()
#numbers of tv vs  movies on netflix
#df.head(2)
#type1= df1.type.value_counts()
#type1.index
#print(type1)
#Now i want to  plot it 
#plt.title("Number of Movies vs show on netflix")
#plt.axes(facecolor= "gray")#FOR BACK GROUND COLOUR
#plt.bar(type1.index,type1, color=['r', 'black'],tick_label=type1.index)
#plt.xlabel("type")
#plt.ylabel("count")# Question 1 is complete
#plt.show()
# Question 2 : what is the percentage  of each rating
df.head(2)
rating= df1['rating'].value_counts()
rating.index
print(rating)
# calculate percentage
#plt.title("percentage of each rating")
#plt.pie(rating,labels=rating.index,autopct="%1.0f%%")
#plt.show()
#Question 3 is How many number  of realses changed over the year?
#df1.head(2)
#ry=  df1["release_year"].value_counts()
#ry.index
#print(ry)
#print(ry.index)
#plt.title("yearly realeasing trends")
#plt.axes(fc="red")
#plt.plot(ry.index,ry,color="black",lw=4,marker="o", mfc="white")
#plt.show()
#Question 4 what is the distribution  of movies duration
df1.head(2)

#movie = df1[df1.type == "movie"]
#movie.head(2)
#movie.index

#m_d = movie["duration"].str.replace("min", "").astype(int)
#print(m_d)

#plt.pie(movie.index,m_d,  colors=["red", "blue", "green"])
#plt.title("Movie Duration Distribution")
#plt.show()
#top 5 country withthe 5 numbers of shows 
df1.head(2)
cc= df.country.value_counts()
ccc=cc.head(5)
print(cc)

cc.index
plt.barh(ccc.index,ccc,color="red")
plt.title("top 5 country of frequency")
plt.show()