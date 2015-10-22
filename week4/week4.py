# Course: Data Management and Visualization
# Week4
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt

df = pd.read_csv("gapminder.csv", low_memory = False, index_col = 0)
maleemployrate = pd.read_csv("maleemployrate_sub.csv", low_memory = False, index_col = 0)

df["incomeperperson"] = df["incomeperperson"].convert_objects(convert_numeric=True)
df["femaleemployrate"] = df["femaleemployrate"].convert_objects(convert_numeric=True)
df["polityscore"] = df["polityscore"].convert_objects(convert_numeric=True)
df['employrate'] = df['employrate'].convert_objects(convert_numeric=True)

maleemployrate['2007'] = maleemployrate['2007'].convert_objects(convert_numeric=True)


#Concatenate df , df2
df3 =  pd.concat([df, maleemployrate], axis=1, join_axes=[df.index])

df3.rename(columns= {'2007':'maleemployrate'}, inplace=True) #rename column

#Scatterplot for the Association Between female employ rate and income per person
scat1 = seaborn.regplot(x="incomeperperson", y="femaleemployrate", fit_reg=True, data=df)
plt.xlabel('incomeperperson')
plt.ylabel('femaleemployrate')
plt.title('Scatterplot for the Association Between female employ rate and income per person')
plt.show()

#Scatterplot for the Association Between polity score and female employ rate
scat2 = seaborn.regplot(x="polityscore", y="femaleemployrate", fit_reg=True, data=df)
plt.xlabel('polityscore')
plt.ylabel('femaleemployrate')
plt.title('Scatterplot for the Association Between polity score and female employ rate')
plt.show()

#Scatterplot for the Association Between polity score and income per person
scat3 = seaborn.regplot(x="polityscore", y="incomeperperson", fit_reg=True, data=df)
plt.xlabel('polityscore')
plt.ylabel('incomeperperson')
plt.title('Scatterplot for the Association Between polity score and income per person')
plt.show()


# quartile split (use qcut function & ask for 4 groups - gives you quartile split)
print ('Income per person - 4 categories - quartiles')
df['INCOMEGRP4']=pd.qcut(df.incomeperperson, 4, labels=["1=25th%tile","2=50%tile","3=75%tile","4=100%tile"])
c10 = df['INCOMEGRP4'].value_counts(sort=False, dropna=True)
print(c10)

df3['INCOMEGRP4']=pd.qcut(df3.incomeperperson, 4, labels=["1=25th%tile","2=50%tile","3=75%tile","4=100%tile"])
c11 = df3['INCOMEGRP4'].value_counts(sort=False, dropna=True)
print(c11)


# bivariate bar graph
seaborn.factorplot(x='INCOMEGRP4', y='femaleemployrate', data=df3, kind="bar", ci=None)
plt.xlabel('income group')
plt.ylabel('femaleemployrate')
plt.show()


ax2 = seaborn.factorplot(x='INCOMEGRP4', y='maleemployrate', data=df3, kind="bar", ci=None)
plt.xlabel('income group')
plt.ylabel('maleemployrate')
plt.show()

# Calulating mean for incomeperperson
mean_ipp = (df3["incomeperperson"].mean(skipna=True)) 

country_abovemean = df3.loc[df3["incomeperperson"] >= mean_ipp] # countries having higher income/person than the average
country_belowmean = df3.loc[df3["incomeperperson"] < mean_ipp]  # countries having less income/person than the average

sub1 = country_abovemean.copy()
sub2 = country_belowmean.copy()




# Polity Score bar graph 
sub1["polityscore"] = sub1["polityscore"].astype('category')
sub2["polityscore"] = sub2["polityscore"].astype('category')

seaborn.countplot(x="polityscore", data=sub1)
plt.xlabel('Polity Score')
plt.title('a country\'s democratic and free nature(country_abovemean)')
plt.show()
seaborn.countplot(x="polityscore", data=sub2)
plt.xlabel('Polity Score')
plt.title('a country\'s democratic and free nature(country_belowmean)')
plt.show()
