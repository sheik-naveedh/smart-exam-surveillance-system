# Smart Exam Surveillance System

A YOLOv8-based mobile phone detection system that can detect mobile phones in real-time video streams for exam surveillance.

## Features

- Real-time mobile phone detection using webcam
- YOLOv8 model for accurate object detection
- Custom trained model on mobile phone dataset
- High accuracy detection in various lighting conditions
- Easy-to-use interface with real-time visualization

## Files

- `detect_mobile.py` - Main detection script for real-time mobile phone detection
- `train_model.py` - Script to train the YOLO model on the mobile phone dataset
- `best.pt` - Trained model weights
- `yolov8n.pt` - Base YOLOv8 nano model
- `mobile_dataset/` - Dataset directory containing training, validation, and test images
- `data.yaml` - Dataset configuration file

## Requirements

- Python 3.8+
- OpenCV
- Ultralytics YOLO
- PyTorch
- NumPy
- Pillow

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sheik-naveedh/smart-exam-surveillance-system.git
   cd smart-exam-surveillance-system
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv myvenv
   # On Windows
   myvenv\Scripts\activate
   # On macOS/Linux
   source myvenv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install ultralytics opencv-python torch torchvision numpy pillow
   ```

## Usage

### Real-time Detection

Run the detection script to start real-time mobile phone detection:

```bash
python detect_mobile.py
```

The application will:
- Open your default camera
- Display live video feed with detection boxes around mobile phones
- Show confidence scores for detected objects
- Press 'q' to quit the application

### Training Your Own Model

To train the model on your own dataset:

```bash
python train_model.py
```

This will train a new model using the dataset specified in `mobile_dataset/data.yaml`.

## Dataset

The mobile phone dataset can be downloaded from Roboflow:

- **Download Link**: [Mobile Phone Detection Dataset](https://universe.roboflow.com/m17865515473-163-com/mobilephone-wusj2/dataset/7)
- **Format**: YOLO format with annotations
- **Classes**: Mobile-phone (1 class)
- **License**: CC BY 4.0
- **Workspace**: m17865515473-163-com
- **Project**: mobilephone-wusj2
- **Version**: 7

### Dataset Structure

The dataset includes:
- **Training images and labels**: For model training
- **Validation images and labels**: For model validation during training
- **Test images and labels**: For final model evaluation
- **Configuration file** (`data.yaml`): Contains dataset paths and class information

### Dataset Setup

1. Visit the [Roboflow dataset link](https://universe.roboflow.com/m17865515473-163-com/mobilephone-wusj2/dataset/7)
2. Download the dataset in YOLO format
3. Extract the files to the `mobile_dataset/` directory
4. Ensure the `data.yaml` file is properly configured with the correct paths:
   ```yaml
   train: ../train/images
   val: ../valid/images
   test: ../test/images
   
   nc: 1
   names: ['Mobile-phone']
   ```

## Model Performance

The model has been trained on a custom dataset of mobile phone images and achieves:
- High accuracy for mobile phone detection in various scenarios
- Good performance in different lighting conditions
- Robust detection across different phone models and orientations
- Real-time inference capabilities suitable for surveillance applications

## Project Structure

```
smart-exam-surveillance-system/
├── detect_mobile.py          # Main detection script
├── train_model.py           # Training script
├── README.md               # Project documentation
├── .gitignore             # Git ignore file
├── best.pt                # Trained model weights
├── yolov8n.pt            # Base YOLO model
├── mobile_dataset/       # Dataset directory
│   ├── data.yaml        # Dataset configuration
│   ├── train/           # Training data
│   ├── valid/           # Validation data
│   └── test/            # Test data
└── myvenv/              # Virtual environment (excluded from git)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the dataset license (CC BY 4.0) for dataset usage terms.

## Acknowledgments

- YOLOv8 by Ultralytics for the base detection model
- Roboflow for providing the mobile phone detection dataset
- OpenCV for computer vision utilities

## Contact

For questions or support, please open an issue on the GitHub repository.
