import csv
import re
import pandas as pd
import os
import shutil

from pathlib import Path


# Deleting all picture files and accompanying text files with human body keypoints, where user is not exercising

dataDir = './dataset/vay-alpha-release/storage/'
workoutNumber = 0

pathList = Path(dataDir).glob('*/*/plank*.txt')
for path in pathList:
    workoutNumber += 1
    # because path is object not string
    pathStr = str(path)
    print(pathStr)
    with open(pathStr, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        noTabs = (line.replace("    ", "").replace("	", "") for line in stripped)
        lines = (line.split(";") for line in noTabs if re.match("(.*)STATE_EXER(.*)", line) or re.match("(.*)STATE_DONE(.*)", line))
        # save text file with all pictures having STATE_EXERCISING or STATE_DONE to same location
        csvPath = pathStr + 'filesToCopy'
        with open(csvPath, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)

    # read in saved csv again
    data = pd.read_csv(csvPath, sep=',', header=None, index_col=False,
                       names=["imgName", "millis", "type", "state"])

    # copy all pictures and keypoints, where user is exercising, to folders
    for index, row in data.iterrows():
        try:
            # copy files to one folder, so all pictures are in one place
            toCopyPath = str(path)[:-4] + '/pictures/' + row['imgName'] + '.jpeg'
            shutil.copy(toCopyPath, './plankExercisingPictures')

            # rename image to decrease the chance of files having the same name
            oldName = './plankExercisingPictures/' + row['imgName'] + '.jpeg'
            newName = './plankExercisingPictures/' + str(workoutNumber) + '_' + row['imgName'] + '.jpeg'
            os.rename(oldName, newName)
        except:
            print('error copying or naming ' + toCopyPath)
        try:
            # copy files to one folder, so all keypoints are in one place
            toCopyPath = str(path)[:-4] + '/training_points/' + row["imgName"] + '.note.txt'
            shutil.copy(toCopyPath, './plankExercisingKeypoints')

            # rename text files to decrease the chance of files having the same name
            oldName = './plankExercisingKeypoints/' + row['imgName'] + '.note.txt'
            newName = './plankExercisingKeypoints/' + str(workoutNumber) + '_' + row['imgName'] + '.note.txt'
            os.rename(oldName, newName)
        except:
            print('error copying or naming ' + toCopyPath)
print('done')