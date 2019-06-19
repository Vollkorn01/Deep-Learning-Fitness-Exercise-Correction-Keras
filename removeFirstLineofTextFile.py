# the first line of the txt files of the predicted keypoints needs to be removed
from pathlib import Path

dataDir = './plankExercisingKeypointsPredicted/'

pathList = Path(dataDir).glob('*')
for path in pathList:
    print(path)
    with open(path, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(path, 'w') as fout:
        fout.writelines(data[1:])
