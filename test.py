from ultralytics import YOLO

if __name__ ==  '__main__':
# Load a model
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
# Train the model
    results = model.train(data="coco128.yaml", epochs=100, imgsz=640)