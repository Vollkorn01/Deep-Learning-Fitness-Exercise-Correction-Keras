# DeepLearningExerciseCorrection
Machine Learning Course at University of Zürich

Project Plan:

1. Convert predicted keypoints from old algorithm (as txt files) to a Pandas DataFrame:
Rows (8'000): Picture names (e.g. 3_12-22-09.655)
Columns (36): Keypoints in x and y as follows: 0x, 0y, 1x, 1y, ... , 17x, 17y

The folder with the txt files is named "plankExercisingKeypointsPredicted" and can be found in the drive folder: https://drive.google.com/open?id=1xIo56-Xmz_hPuXuhUnr-cUYANyrD-pMi

2. Convert labeled keypoints to a Pandas DataFrame:
Rows (8'000): Picture names (e.g. 3_12-22-09.655)
Columns (6): Keypoints in x and y as follows: 0, 1, 2, 3, 4, 5, 6

The files can be found in the drive folder: https://drive.google.com/open?id=1xIo56-Xmz_hPuXuhUnr-cUYANyrD-pMi

3. Calculate and add labels "correct", "tooHigh", "tooLow" to the labeled DataFrame as an additional column, by calculating the angle of the back.
The angle of the back can be calculated by using keypoints 2 (shoulders), 3 (hips), 4 (knees). If the angle is lower than 5 degrees, label is tooHigh,
if the angle is over 5 degrees, label is tooLow, else label is correct.

4. Add the created label column to the Pandas DataFrame from 1. Now each predicted picture has the correct ground-truth to it.

5. Create an Artificial Neural Network in Keras to train on this DataFrame.
