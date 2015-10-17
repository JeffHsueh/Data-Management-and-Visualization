# Course: Data Management and Visualization
# Week2
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np

df = pd.read_csv("gapminder.csv", low_memory = False, index_col = 0)
df2 = pd.read_csv("country_population.csv", low_memory = False, index_col = 0)

df["incomeperperson"] = df["incomeperperson"].convert_objects(convert_numeric=True)
df["femaleemployrate"] = df["femaleemployrate"].convert_objects(convert_numeric=True)
df["polityscore"] = df["polityscore"].convert_objects(convert_numeric=True)
df['employrate'] = df['employrate'].convert_objects(convert_numeric=True)

df2['Population (2014)'] = df2['Population (2014)'].convert_objects(convert_numeric=True)
df2['Fertility Rate'] = df2['Fertility Rate'].convert_objects(convert_numeric=True)

#Concatenate df and df2
df3 =  pd.concat([df, df2], axis=1, join_axes=[df.index])

# Calulating mean for incomeperperson excluding missing data
mean_ipp = (df3["incomeperperson"].mean(skipna=True)) 

country_abovemean = df3.loc[df3["incomeperperson"] >= mean_ipp] # countries having greater income/person than the average
country_belowmean = df3.loc[df3["incomeperperson"] < mean_ipp]  # countries having less income/person than the average



#Country Distribution
print ("Counts for country_abovemean:",
       len(country_abovemean),"counts")  
print ("Percentage for country_abovemean:", len(country_abovemean)/ len(df))# percentage


print ("Counts for country_belowmean:",
       len(country_belowmean), "counts") 
print ("Percentage for country_belowmean:" ,len(country_belowmean)/ len(df))# percentage


#Polityscore Distribution
po_data1 = {'Counts':country_abovemean['polityscore'].value_counts(sort=True, dropna = False, normalize = False),
         'Percentage': country_abovemean['polityscore'].value_counts(sort=True, dropna = False, normalize = True)} # data from country_abovemean
po_data2 = {'Counts':country_belowmean['polityscore'].value_counts(sort=True, dropna = False, normalize = False),
         'Percentage': country_belowmean['polityscore'].value_counts(sort=True, dropna = False, normalize = True)} # data from country_belowmean

c1 = pd.DataFrame(data = po_data1)
c2 = pd.DataFrame(data = po_data2)
sum1 = country_abovemean['polityscore'].value_counts(sort=True, dropna = False, normalize = True).sum()
sum2 = country_belowmean['polityscore'].value_counts(sort=True, dropna = False, normalize = True).sum()


print ('Polityscore distribution for country_abovemean:')
print (c1)
print ('Polityscore distribution for country_belowmean:')
print (c2)


###Femaleemployrate Distribution
print ('country_abovemean with femaleemployrate >=50%: ',
       len(country_abovemean['femaleemployrate'].loc[country_abovemean['femaleemployrate']>=50])/len(country_abovemean)*100, '%')
print ('country_belowmean with femaleemployrate >=50%: ',
       len(country_belowmean['femaleemployrate'].loc[country_belowmean['femaleemployrate']>=50])/len(country_belowmean)*100,'%')



sub1 = country_abovemean.copy()
sub2 = country_belowmean.copy()


print (df3)
## Split into 3 groups.

sub1['femalegroup3'] = pd.cut(sub1['femaleemployrate'], 3)
c3 = sub1['femalegroup3'].value_counts(sort= False)
print ("Female Employ Rate Distribution: (country_abovemean)")
print (c3)


sub2['femalegroup3'] = pd.cut(sub2['femaleemployrate'], 3)
c4 = sub2['femalegroup3'].value_counts(sort= False)
print ("Female Employ Rate Distribution: (country_belowmean)")
print (c4)
