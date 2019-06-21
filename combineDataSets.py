import pandas as pd
import numpy as np

df_labeled = pd.read_pickle('labeledDataFrame')
df_predicted = pd.read_pickle('predictedDataFrame')
df_predicted = df_predicted.rename(columns={'imgName': 'filename'})
#print(df_labeled)
#print(df_predicted)
df = pd.merge(df_predicted, df_labeled, on='filename')
df = df.drop(columns = ['angle', 'x_1', 'x_1', 'y_1', 'x_2', 'y_2', 'x_3', 'y_3', 'x_4', 'y_4', 'x_5', 'y_5', 'x_6', 'y_6', 'index'])

# delte rows with too many missing values
for index, row in df.iterrows():
    #print('row 0: ' + str(row[0]) + ' ' + str(type(row[0])))
    if np.isnan(row[0]) & np.isnan(row[3]) &  np.isnan(row[5]) &  np.isnan(row[20]) &  np.isnan(row[30]) &  np.isnan(row[31]) &  np.isnan(row[35]) &  np.isnan(row[16]):
        print('isnan')
        df.drop(index, inplace=True)
print(df)
df.to_pickle('fullDataFrame')