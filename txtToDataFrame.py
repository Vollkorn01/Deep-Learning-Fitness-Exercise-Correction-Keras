import pandas as pd
import numpy as np

from pathlib import Path

dataDir = './plankExercisingKeypointsPredicted/'
firstRun = True
pathList = Path(dataDir).glob('*')
loops = 0
for path in pathList:
    loops += 1
    imgName = str(path).replace('plankExercisingKeypointsPredicted/', '').replace('.note.txt', '')
    print(imgName)
    df = pd.read_csv(path, sep=';')
    df = df.rename(columns={'ID\t': 'ID', '\tx\t': 'x', '\ty\t': 'y', '\tscore': 'score'})
    df = df.drop(columns=['score'])
    df = df.set_index('ID')
    df = df.reindex(np.arange(0,18,1))
    df= df.values.flatten()
    df[df > 330] = 'NaN'
    df = [df]
    df = pd.DataFrame(df)
    df['imgName'] = imgName
    if firstRun:
        completeDf = df
    else:
        completeDf = completeDf.append(df)
    firstRun = False
    if loops > 100:
        break
print(completeDf)