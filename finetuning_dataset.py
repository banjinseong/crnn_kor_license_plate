import random
import os

data_type = 'plate' # made1, made2

# Data Preprocessing
with open(f'./deep-text-recognition-benchmark/plate_data/labels.txt', 'r', encoding='cp949') as f:
    labels = f.readlines()

image_files = os.listdir(f'./deep-text-recognition-benchmark/plate_data/images/')
total = len(image_files)
print(total)

random.shuffle(image_files)

n_train = int(len(image_files) * 0.03)
n_validation = int(len(image_files) * 0.008)
n_test = int(len(image_files) * 0.008)

train_files = image_files[:n_train]
validation_files = image_files[n_train:n_train+n_validation]
test_files = image_files[-n_test:]

save_root_path = f'./deep-text-recognition-benchmark/{data_type}_data/'

gt_test_path = save_root_path + 'gt_test.txt'
gt_validation_path = save_root_path + 'gt_validation.txt'
gt_train_path = save_root_path + 'gt_train.txt'

# Remove existing files if they exist
if os.path.exists(gt_test_path):
    os.remove(gt_test_path)
if os.path.exists(gt_validation_path):
    os.remove(gt_validation_path)
if os.path.exists(gt_train_path):
    os.remove(gt_train_path)

gt_test = open(gt_test_path, 'w')
gt_validation = open(gt_validation_path, 'w')
gt_train = open(gt_train_path, 'w')

for line in labels:
    file_name, annotation = line.split('.png')
    file_name += '.png'


    if file_name in train_files:
        gt_train.write("train/{}\t{}".format(file_name, annotation))
    if file_name in test_files:
        gt_test.write("test/{}\t{}".format(file_name, annotation))
    elif file_name in validation_files:
        gt_validation.write("validation/{}\t{}".format(file_name, annotation))

print('gt_file done')
