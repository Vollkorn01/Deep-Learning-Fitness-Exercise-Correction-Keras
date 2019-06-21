import pandas as pd


df_labeled = pd.read_csv('./plankExercisingKeypointsCorrect/plank_correct_keypoints.csv', sep=',')
df_labeled = df_labeled.drop(['region_count', 'region_id'], axis=1)
cc = df_labeled.groupby('filename').cumcount() + 1
df_labeled = df_labeled.set_index(['filename', cc]).unstack().sort_index(1, level=1)
df_labeled.columns = ['_'.join(map(str,i)) for i in df_labeled.columns]
df_labeled.reset_index()
print(df_labeled)
df_labeled.to_pickle('annotatedDataFrame')