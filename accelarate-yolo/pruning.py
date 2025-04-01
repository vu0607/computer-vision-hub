import torch
from torch.nn.utils import prune
from ultralytics import YOLO


def prune_yolo(model):
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Conv2d):
            prune.l1_unstructured(module, name='weight', amount=0.3)  # 30% sparsity
            prune.remove(module, name='weight')
    return model


def load_model(model_path: str):
    model = YOLO(model_path)
    torch_model = model.model
    return torch_model


if __name__ == '__main__':
    model_path = 'yolov8s.pt'
    print(f'Loading model from {model_path}')
    model = load_model(model_path)
    print('Pruning model')
    pruned_model = prune_yolo(model)
    print('Saving pruned model')
    pruned_model.save('pruned_yolov8s.pt')
