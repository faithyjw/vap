#libraries
import pandas as pd

#loading datasets
df2011 = pd.read_excel('test_EnergyConsumption.xlsx')
df2012 = pd.read_excel('test_EnergyConsumption.xlsx')
df2013 = pd.read_excel('test_EnergyConsumption.xlsx')
df2014 = pd.read_excel('test_EnergyConsumption.xlsx')
df2015 = pd.read_excel('test_EnergyConsumption.xlsx')
df2016 = pd.read_excel('test_EnergyConsumption.xlsx')
df2017 = pd.read_excel('test_EnergyConsumption.xlsx')
df2018 = pd.read_excel('test_EnergyConsumption.xlsx')
df2019 = pd.read_excel('test_EnergyConsumption.xlsx')
df2020 = pd.read_excel('test_EnergyConsumption.xlsx')
df2021 = pd.read_excel('test_EnergyConsumption.xlsx')

#table2011
df2011.drop(df2011.tail(100).index, inplace = True)
df2011 = df2011[1:]
# print(df2011)

#table2012
df2012.drop(df2012.head(8).index, inplace = True)
df2012.columns = df2012.iloc[0]
df2012.drop(df2012.index[range(0,3)], axis=0, inplace=True)
df2012.drop(df2012.tail(90).index, inplace = True)
# print(df2012)

#table2013
df2013.drop(df2013.head(18).index, inplace = True)
df2013.columns = df2013.iloc[0]
df2013.drop(df2013.index[range(0,3)], axis=0, inplace=True)
df2013.drop(df2013.tail(80).index, inplace = True)
# print(df2013)

#table2014
df2014.drop(df2014.head(28).index, inplace = True)
df2014.columns = df2014.iloc[0]
df2014.drop(df2014.index[range(0,3)], axis=0, inplace=True)
df2014.drop(df2014.tail(70).index, inplace = True)
# print(df2014)

#table2015
df2015.drop(df2015.head(38).index, inplace = True)
df2015.columns = df2015.iloc[0]
df2015.drop(df2015.index[range(0,3)], axis=0, inplace=True)
df2015.drop(df2015.tail(60).index, inplace = True)
# print(df2015)

#table2016
df2016.drop(df2016.head(48).index, inplace = True)
df2016.columns = df2016.iloc[0]
df2016.drop(df2016.index[range(0,3)], axis=0, inplace=True)
df2016.drop(df2016.tail(50).index, inplace = True)
# print(df2016)

#table2017
df2017.drop(df2017.head(58).index, inplace = True)
df2017.columns = df2017.iloc[0]
df2017.drop(df2017.index[range(0,3)], axis=0, inplace=True)
df2017.drop(df2017.tail(40).index, inplace = True)
# print(df2017)

#table2018
df2018.drop(df2018.head(68).index, inplace = True)
df2018.columns = df2018.iloc[0]
df2018.drop(df2018.index[range(0,3)], axis=0, inplace=True)
df2018.drop(df2018.tail(30).index, inplace = True)
# print(df2018)

#table2019
df2019.drop(df2019.head(78).index, inplace = True)
df2019.columns = df2019.iloc[0]
df2019.drop(df2019.index[range(0,3)], axis=0, inplace=True)
df2019.drop(df2019.tail(20).index, inplace = True)
# print(df2019)

#table2020
df2020.drop(df2020.head(88).index, inplace = True)
df2020.columns = df2020.iloc[0]
df2020.drop(df2020.index[range(0,3)], axis=0, inplace=True)
df2020.drop(df2020.tail(10).index, inplace = True)
# print(df2020)

#table2021
df2021.drop(df2021.head(98).index, inplace = True)
df2021.columns = df2021.iloc[0]
df2021.drop(df2021.index[range(0,3)], axis=0, inplace=True)
# print(df2021)

with pd.ExcelWriter('faith_EnergyConsumption.xlsx') as writer:  
    df2011.to_excel(writer, sheet_name='2011', index=False)
    df2012.to_excel(writer, sheet_name='2012', index=False)
    df2013.to_excel(writer, sheet_name='2013', index=False)
    df2014.to_excel(writer, sheet_name='2014', index=False)
    df2015.to_excel(writer, sheet_name='2015', index=False)
    df2016.to_excel(writer, sheet_name='2016', index=False)
    df2017.to_excel(writer, sheet_name='2017', index=False)
    df2018.to_excel(writer, sheet_name='2018', index=False)
    df2019.to_excel(writer, sheet_name='2019', index=False)
    df2020.to_excel(writer, sheet_name='2020', index=False)
    df2021.to_excel(writer, sheet_name='2021', index=False)