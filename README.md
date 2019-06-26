# DeepLearningExerciseCorrection

## Overview
This repository is created during the Neural Networks and Deep Learning course at the University of Zürich.
The goal is to detect wrong posture from the plank fitness exercise using outputs from human keypoint detection.

The following picture shows the keypoint detection during a plank. In this case, it would be easy to detect execution mistakes (such as the hips being too low).

![title](images/19-17-24.187.humans.jpeg)

However, often the detection is erroneous: 

![title](images/14-37-42.747.humans.jpeg)

We trained an artificial neural network to detect whether the position of the back was too low, correct or too high from the keypoints, even if not all keypoints were detected.


## Training

In order to collect the ground truth, we labeled 8'000 pictures of people doing plank. The images were labeled by freelancers on the outsourcing platform upwork.
VGG image annotator was used to label relevant keypoints from which the angle of the back was calculated. 

![title](images/plankAnnotation.gif)


If the angle was between 178 and 190 degrees the position was correct (label 1), else too low (label 0) or too high (label 2).


Project Plan:

**1. Convert predicted keypoints from old algorithm (as txt files) to a Pandas DataFrame:**
- Rows (8'000): Picture names (e.g. 3_12-22-09.655)
- Columns (36): Keypoints in x and y as follows: 0x, 0y, 1x, 1y, ... , 17x, 17y

The folder with the txt files is named "plankExercisingKeypointsPredicted" and can be found in the drive folder: https://drive.google.com/open?id=1xIo56-Xmz_hPuXuhUnr-cUYANyrD-pMi

**2. Convert labeled keypoints to a Pandas DataFrame:**
- Rows (8'000): Picture names (e.g. 3_12-22-09.655)
- Columns (6): Keypoints in x and y as follows: 0, 1, 2, 3, 4, 5, 6

The files can be found in the drive folder: https://drive.google.com/open?id=1xIo56-Xmz_hPuXuhUnr-cUYANyrD-pMi

**3. Calculate and add labels "correct", "tooHigh", "tooLow" to the labeled DataFrame as an additional column, by calculating the angle of the back.**
The angle of the back can be calculated by using keypoints 2 (shoulders), 3 (hips), 4 (knees). If the angle is lower than 5 degrees, label is tooHigh,
if the angle is over 5 degrees, label is tooLow, else label is correct.

**4. Add the created label column to the Pandas DataFrame from 1. Now each predicted picture has the correct ground-truth to it.**

**5. Create an Artificial Neural Network in Keras to train on this DataFrame.**
