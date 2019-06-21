import math
import pandas as pd
import numpy as np


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang

df_labeled = pd.read_pickle('annotatedDataFrame')
df_labeled["angle"] = np.nan
df_labeled["label"] = np.nan
print(df_labeled)

for index, row in df_labeled.iterrows():
    angle = getAngle((row['x_3'], row['y_3']), (row['x_4'], row['y_4']), (row['x_6'], row['y_6']))

    # if image is flipped, angle needs to be flipped as well
    if row['x_6'] < 100:
        angle = 360-angle
    # add angle value to angle column
    df_labeled.loc[index, 'angle'] = angle

    # add labels 0 (too_low), 1 (correct) and 2 (too_high) to label column
    if angle < 178:
        df_labeled.loc[index, 'label'] = 0
    elif angle > 192:
        df_labeled.loc[index, 'label'] = 2
    else:
        df_labeled.loc[index, 'label'] = 1
print(df_labeled)
df_labeled.to_pickle('labeledDataFrame')