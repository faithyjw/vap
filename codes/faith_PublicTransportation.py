#libraries
import pandas as pd

#loading dataset
df = pd.read_excel('Public Transportation.xlsx', 'T126')

df.drop(df.head(6).index, inplace = True) #removing rows
df = df.drop(df.columns[[0, 3, 4, 6, 7, 9, 10, 12, #dropping unnecessary columns
                         13, 15, 16, 17, 18, 20, 21, 
                         23, 24, 26, 27, 29, 30]],axis = 1)
df.columns = ['Mode of Transport', 'Total', 'No Qualification', 'Primary', 
              'Lower Secondary', 'Secondary', 'Post-Secondary (Non-Tertiary)', 
              'Polytechnic Diploma', 'Professional Qualification and Other Diploma', 
              'University'] #column headers
df.drop(df.tail(3).index, inplace = True) #last few rows

#print(df)
df.to_excel('faith_PublicTransportation.xlsx', index=False, sheet_name= 'T126') 