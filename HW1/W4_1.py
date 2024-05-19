from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.track(source="video/argoverse.mp4", show=True, save=True, classes=[2])
