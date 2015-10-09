# Course: Data Management and Visualization
# Week2
#Editor: Kuo-Lin Hsueh
import pandas as pd
import numpy as np

df = pd.read_csv("gapminder.csv", low_memory = False)
df["incomeperperson"] = df["incomeperperson"].convert_objects(convert_numeric=True)
df["femaleemployrate"] = df["femaleemployrate"].convert_objects(convert_numeric=True)
df["polityscore"] = df["polityscore"].convert_objects(convert_numeric=True)

# Calulating mean for incomeperperson excluding missing data
mean_ipp = (df["incomeperperson"].mean(skipna=True)) 

country_abovemean = df.loc[df["incomeperperson"] >= mean_ipp] # countries having greater income/person than the average
country_belowmean = df.loc[df["incomeperperson"] < mean_ipp]  # countries having less income/person than the average



#Country Distribution
print ("Counts for country_abovemean:",
       len(country_abovemean['country']),"counts")  
print ("Percentage for country_abovemean:", len(country_abovemean)/ len(df))# percentage


print ("Counts for country_belowmean:",
       len(country_belowmean['country']), "counts") 
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
print ('Sum:', sum1)
print ('Polityscore distribution for country_belowmean:')
print (c2)
print ('Sum:', sum2)


#Femaleemployrate Distribution
print ('country_abovemean with femaleemployrate >=50%: ',
       len(country_abovemean[['country','femaleemployrate']].loc[country_abovemean['femaleemployrate']>=50])/len(country_abovemean)*100, '%')
print ('country_belowmean with femaleemployrate >=50%: ',
       len(country_belowmean[['country','femaleemployrate']].loc[country_belowmean['femaleemployrate']>=50])/len(country_belowmean)*100,'%')
