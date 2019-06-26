# DeepLearningExerciseCorrection

## Overview
This repository is created during the Neural Networks and Deep Learning course at the University of Zürich.
The goal is to detect wrong posture from the plank fitness exercise using outputs from human keypoint detection.
The use case of this project is an AI fitness coach that can detect wrong posture during a workout by just using a smartphone.

The following picture shows the keypoint detection during a plank. In this case, it would be easy to detect whether the hips are too high by calculating the angle between the shoulder, hips and feet.

![title](images/19-17-24.187.humans.jpeg)

However, often the detection is erroneous: 

![title](images/14-37-42.747.humans.jpeg)

In this case, we would need to use another approach to detect an angle. This is time-consuming and prone to errors, since there are many possibilities of badly detected keypoints. Fortunately, thanks to our collected dataset and the power of neural networks these problems belong to the past!

We trained an artificial neural network to detect whether the position of the back was too low, correct or too high from the keypoints, even if not all keypoints were detected.


## Training

In order to collect the ground-truth, we labeled 8'000 pictures of people doing plank. The images were labeled by freelancers on the outsourcing platform upwork.
VGG image annotator was used to label relevant keypoints:

![title](images/plankAnnotation.gif)


As a next step, we calculated the angle of the back from these keypoints. If the angle is between 178 and 190 degrees the position was correct (label 1), else too low (label 0) or too high (label 2). These thresholds were set by consulting a professional fitness coach.
We then added the correct labels to the original data, where keypoints were often missing or erroneous, which was the dataset we trained on.

## Architecture

After testing many combinations, the following architecture yielded the best results:
Inputs: 36 features (18 keypoints with their x and y values)

### 4 fully connected layers:
1. layer: 36 neurons, activation relu
2. layer: 18 neurons, activation relu
3. layer: 9 neurons, activation relu
4. layer: 3 output neurons, activation Softmax (Softmax makes sure, that the outputs get transformed to probabilities)

### Loss function: Categorical crossentropy (since we're delaing with multi label outputs)
### Optimizer: adam

## Get Started

To run the training of the artificial neural network, run the ANN.ipynb with jupyter notebook. All necessary requirements are in the requirements.txt which can be installed by running `pip install -r requirements.txt`.

## Results

The network yielded a top accuracy of 90 %.

However, the real accuracy is probably much higher, since many pictures are edge cases (e.g. where the angle was only 0.1 degree too high for a correct prediction).

The following accuracy and loss plots show that the ANN learned very well:

![title](images/accuracyGraph.png)
![title](images/lossGraph.png)


## Project Plan:

**1. Convert predicted keypoints from old algorithm (as txt files) to a Pandas DataFrame:**
- Rows (8'000): Picture names (e.g. 3_12-22-09.655)
- Columns (36): Keypoints in x and y as follows: 0x, 0y, 1x, 1y, ... , 17x, 17y


**2. Convert labeled keypoints to a Pandas DataFrame:**
- Rows (8'000): Picture names (e.g. 3_12-22-09.655)
- Columns (6): Keypoints in x and y as follows: 0, 1, 2, 3, 4, 5, 6


**3. Calculate and add labels "correct", "tooHigh", "tooLow" to the labeled DataFrame as an additional column, by calculating the angle of the back.**
The angle of the back can be calculated by using keypoints 2 (shoulders), 3 (hips), 4 (knees). If the angle is lower than 178 degrees, label is too low (0),
if the angle is over 190 degrees, label is tooHigh (2), else label is correct (1).

**4. Add the created label column to the Pandas DataFrame from 1. Now each predicted picture has the correct ground-truth to it.**

**5. Create an Artificial Neural Network in Keras to train on this DataFrame.**
