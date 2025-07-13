from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # You can also use yolov8s.pt
model.train(data="mobile_dataset/data.yaml", epochs=50, imgsz=640)
