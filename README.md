# Smart Exam Surveillance System

A YOLOv8-based mobile phone detection system that can detect mobile phones in real-time video streams for exam surveillance.

## Features

- Real-time mobile phone detection using webcam
- YOLOv8 model for accurate object detection
- Custom trained model on mobile phone dataset

## Files

- `detect_mobile.py` - Main detection script for real-time mobile phone detection
- `train_model.py` - Script to train the YOLO model on the mobile phone dataset
- `best.pt` - Trained model weights
- `yolov8n.pt` - Base YOLOv8 nano model
- `mobile_dataset/` - Dataset directory containing training, validation, and test images

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLO
- PyTorch

## Installation

1. Clone this repository
2. Install required packages:
   ```bash
   pip install ultralytics opencv-python
   ```

## Usage

### Real-time Detection

Run the detection script to start real-time mobile phone detection:

```bash
python detect_mobile.py
```

Press 'q' to quit the application.

### Training

To train the model on your own dataset:

```bash
python train_model.py
```

## Dataset

The mobile phone dataset can be downloaded from Roboflow:
- **Download Link**: [Mobile Phone Detection Dataset on Roboflow](https://universe.roboflow.com/mobile-phone-detection)
- **Format**: YOLO format with annotations
- **Classes**: Mobile phone

Once downloaded, the dataset should be placed in the `mobile_dataset/` directory and includes:
- Training images and labels
- Validation images and labels
- Test images and labels
- Configuration file (`data.yaml`)

### Dataset Setup

1. Visit the Roboflow link above
2. Download the dataset in YOLO format
3. Extract the files to the `mobile_dataset/` directory
4. Ensure the `data.yaml` file is properly configured with the correct paths

## Model Performance

The model has been trained on a custom dataset of mobile phone images and achieves good accuracy for mobile phone detection in various scenarios.
