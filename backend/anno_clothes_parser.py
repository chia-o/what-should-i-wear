"""Script to add sleeve distinctions to clothes_dataset"""

# Parse sleeve attributes from annotation file
import os, shutil, json

"""
attribute_names = [
    'floral', 'graphic', 'striped', 'embroidered', 'pleated', 'solid',
    'lattice', 'long_sleeve', 'short_sleeve', 'sleeveless', 'maxi_length', 'mini_length',
    'no_dress', 'crew_neckline', 'v_neckline', 'square_neckline', 'no_neckline',
    'denim', 'chiffon', 'cotton', 'leather', 'faux', 'knit', 'tight',
    'loose', 'conventional'
]


desired_attrs = ['long_sleeve', 'short_sleeve', 'sleeveless']
desired_attr_indices = [8, 9, 10]

image_labels = {}

with open(attr_file_path, "r") as f:
    lines = f.readlines()

for line in lines[2:]:
    parts = line.strip().split()
    img_name = parts[0]
    attr_values = list(map(int, parts[1:]))

    labels = [attr_values[i] for i in desired_attr_indices]

    if labels.count(1) == 1:
        label = desired_attrs[labels.index(1)]
        image_labels[img_name] = label
"""


# Placing image files into folders



modanet_image_dir = "/Users/chiamakaofonagoro/projects/what-should-i-wear/backend/modanet/images"
modanet_anno_file = "/Users/chiamakaofonagoro/projects/what-should-i-wear/backend/modanet/modanet2018_instances_train.json"
output_dir = "clothes_dataset"

with open(modanet_anno_file, 'r') as f:
    open_file = json.load(f)

# load categories and ids
categories = {cat['id']: cat['name'] for cat in open_file['categories']}

images = {img['id']: img['file_name'] for img in open_file['images']}

image_to_category = {}

# populate categories, ids in image_to_category dict
for annotation in open_file['annotations']:
    img_id = annotation['image_id']
    cat_id = annotation['category_id']

    img_name = images[img_id]
    cat_name = categories[cat_id]

    # Assign category only if not assigned yet (to avoid duplicates)
    if img_name not in image_to_category:
        image_to_category[img_name] = cat_name







# create category folders in clothes_dataset
for cat_name in set(image_to_category.values()):    
    cat_folder = os.path.join(output_dir, cat_name)
    os.makedirs(cat_folder, exist_ok=True) # if category doesnt exist


# copy images into category folders
for img_name, cat_name in image_to_category.items():
    src_path = os.path.join(modanet_image_dir, img_name)
    dst_path = os.path.join(output_dir, cat_name, img_name)

    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
    else:
        print(f"Image not found: {src_path}")

print("Images organized by category successfully")
