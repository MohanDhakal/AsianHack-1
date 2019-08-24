import json
from commons import get_tensor, get_model, get_model_cuisine

with open('cat_to_name.json') as f:
    cat_to_name = json.load(f)

with open('class_to_idx.json') as f:
    class_to_idx = json.load(f)

with open('cuisine_cat_to_name.json') as f:
    cuisine_cat_to_name = json.load(f)

with open('class_to_idx_cuisine.json') as f:
    class_to_idx_cuisine = json.load(f)

idx_to_class = {v: k for k, v in class_to_idx.items()}
idx_to_class_cuisine = {v: k for k, v in class_to_idx_cuisine.items()}
model = get_model("cash_checkpoint_august_24_2019.pth")
model_cuisine = get_model_cuisine("nepali_cuisine_checkpoint_august_23.pth")


def get_cuisine_name(image_bytes):
    tensor = get_tensor(image_bytes)
    model_cuisine.eval()
    outputs = model_cuisine.forward(tensor)
    _, prediction = outputs.max(1)
    category = prediction.item()
    class_idx_cuisine = idx_to_class_cuisine[category]
    cuisine_name = cuisine_cat_to_name[class_idx_cuisine]
    return category, cuisine_name, outputs

def get_cash_name(image_bytes):
    tensor = get_tensor(image_bytes)
    model.eval()
    outputs = model.forward(tensor)
    _, prediction = outputs.max(1)
    category = prediction.item()
    class_idx = idx_to_class[category]
    cash_name = cat_to_name[class_idx]
    return category, cash_name, outputs





