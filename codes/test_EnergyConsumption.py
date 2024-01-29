#libraries
import pandas as pd

#loading dataset
df = pd.read_excel('Energy Consumption.xlsx', 'T3.11')

#base df
df.drop(df.index[range(0,22)], axis = 0, inplace = True) #remove unnecessary space
df.columns = df.iloc[0] #set first row as headers
df = df[2:] #remove rows
df = df.drop(columns =['Crude Oil', 'Others']) #drop columns
df.drop(df.tail(9).index, inplace = True) #last few rows
df.to_excel('test_EnergyConsumption.xlsx', index=False, sheet_name= '2011') #export out to Microsoft Excel

#df.tail() #shows the bottom rows
#df.head() #shows the top rows
print(df) #print dataframe