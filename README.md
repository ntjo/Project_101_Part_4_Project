# Project_101_Part_4_Project

## Project Overview

This project involves the development of a segmentation model to improve the detection of leaf segments on tomato plants using computer vision and advanced AI detection systems.

## Scope

The goal is to improve the segmentation model results on tomato plant leaves. Lighting plays a crucial role in agricultural robotics, as it directly impacts the quality and accuracy of image data for monitoring plant health and growth. Inconsistent lighting conditions can reduce image clarity, often hindering the effectiveness of detection systems.

This project proposes a solution for improving plant monitoring using computer vision and advanced AI detection systems. These systems often have clarity issues due to external factors, mainly ambient lighting. The experiment involved capturing RGBN images under various artificial lighting conditions such as halogen, LED floodlights, and NIR LED lights, then training a YOLOv8 model to detect leaf segments on tomato plants. Results showed that while improvements to detection are made in the presence of weak ambient lighting with the NIR and Flood LEDs, artificial lighting is often overpowered by ambient sunlight, reducing its effectiveness. In the context of weak ambient sunlight, the combined RGBN data yielded a 10.6% improvement over the baseline; however, no improvement is seen in strong ambient sunlight.

## Files Included

- `modelTrain.py` - Training code for the YOLOv8 model.
- `imageNameChanger.py` - Changes the names of the images taken from the RGBN camera.
- `imageNIRColorMap.py` - Applies NIR colormap to images.
- `imageMerger.py` - Merges NIR and RGB images into one.
- `labelling_different_time.py` - Applies labels to different datasets taken at different times.
- `labelling_NIR.py` - Applies labels from RGB to NIR images.
  
  For more information, please read the project compendium.

## Sample Data

Sample data can be found on [Google Drive](https://drive.google.com/drive/folders/1Z8isAoTu_j5Sb9TDEHEHbmBx9IByRf7s?usp=drive_link). It contains images from the data collection period.

## Roboflow

Labelled segmentation images of leaves and deployed segmentation model can be found on this [link](https://universe.roboflow.com/project101-jmq8d/project-101-disease-detection).

## Colab

All code was run through [Google Colab](https://colab.research.google.com/drive/1NYIlyVP1GfGYG6f_wBcZJrECttxJydl6?usp=sharing) using their T4 GPU.

## Getting Started

To get the project started, follow the steps below.

## Prerequisites

- **[python](https://www.python.org/downloads/)** - Version 3.X.X or higher
- **[pip](https://pypi.org/project/pip/)**
- **[opencv](https://opencv.org/)**
- **[numpy](https://numpy.org/)**
- **[roboflow](https://roboflow.com/)**
- **[ultralytics](https://www.ultralytics.com/)**

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/project-team-3.git
   cd project-team-3
   ```
