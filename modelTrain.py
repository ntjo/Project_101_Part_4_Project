import ultralytics

model: ultralytics.engine.model.Model = ultralytics.models.yolo.model.YOLO('yolov8n-seg.pt', ch=4)

res = model.train(
    data='mock.yaml', # change this to the .yaml file directory
    epochs=100, # these parameters can be adjusted
    batch=16,
    imgsz=736)