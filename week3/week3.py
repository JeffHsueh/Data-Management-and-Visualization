# Course: Data Management and Visualization
# Week3
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np

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

# Calulating mean for incomeperperson excluding missing data
mean_ipp = (df3["incomeperperson"].mean(skipna=True)) 

country_abovemean = df3.loc[df3["incomeperperson"] >= mean_ipp] # countries having higher income/person than the average
country_belowmean = df3.loc[df3["incomeperperson"] < mean_ipp]  # countries having less income/person than the average

sub1 = country_abovemean.copy()
sub2 = country_belowmean.copy()

###Femaleemployrate & Maleemployrate Distribution
sub1_employ= pd.DataFrame(data = sub1, columns = ['femaleemployrate', 'maleemployrate', 'employrate'],index=sub1.index)
sub2_employ= pd.DataFrame(data = sub2, columns = ['femaleemployrate', 'maleemployrate', 'employrate'],index=sub2.index)

print ("average of female employ rate in country_abovemean:",sub1_employ['femaleemployrate'].mean())
print ("average of female employ rate in country_belowmean:",sub2_employ['femaleemployrate'].mean())

print ("average of male employ rate in country_abovemean:",sub1_employ['maleemployrate'].mean())
print ("average of male employ rate in country_belowmean:",sub2_employ['maleemployrate'].mean())

## Split into 3 groups.
filter_value=[0,30,50,70,90,100]
sub1_employ['femalegroup3'] = pd.cut(sub1_employ['femaleemployrate'], bins = filter_value)
sub1_employ['malegroup3'] = pd.cut(sub1_employ['maleemployrate'], bins = filter_value)
c3 = sub1_employ['femalegroup3'].value_counts(sort= False)
c3_2 = sub1_employ['femalegroup3'].value_counts(sort= False, normalize=True)
c3_3 = pd.concat([c3, c3_2], axis=1)
c3_3.columns=['counts', 'percentage']
c4 = sub1_employ['malegroup3'].value_counts(sort= False)
c4_2 = sub1_employ['malegroup3'].value_counts(sort= False, normalize=True)
c4_3 = pd.concat([c4, c4_2], axis=1)
c4_3.columns=['counts', 'percentage']
print ("Female Employ Rate Distribution: (country_abovemean)\n",c3_3)
print ("Male Employ Rate Distribution: (country_abovemean)\n",c4_3)

sub2_employ['femalegroup3'] = pd.cut(sub2_employ['femaleemployrate'], bins = filter_value)
sub2_employ['malegroup3'] = pd.cut(sub2_employ['maleemployrate'], bins = filter_value)
c5 = sub2_employ['femalegroup3'].value_counts(sort= False)
c5_2 = sub2_employ['femalegroup3'].value_counts(sort= False, normalize=True)
c5_3 = pd.concat([c5, c5_2], axis=1)
c5_3.columns=['counts', 'percentage']

c6 = sub2_employ['malegroup3'].value_counts(sort= False)
c6_2 = sub2_employ['malegroup3'].value_counts(sort= False, normalize=True)
c6_3 = pd.concat([c6, c6_2], axis=1)
c6_3.columns=['counts', 'percentage']
print ("Female Employ Rate Distribution: (country_belowmean)\n",c5_3)
print ("Male Employ Rate Distribution: (country_belowmean)\n",c6_3)
