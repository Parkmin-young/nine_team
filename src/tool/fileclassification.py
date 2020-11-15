import os
import random
import shutil

__PATH = os.path.dirname(os.path.abspath(__file__)) 
__PAHT_ORIGNAL_ROOT = __PATH + "/../../data/original"
__PATH_TRAIN_ROOT = __PATH + "/../../data/train"
__PATH_TEST_ROOT = __PATH + "/../../data/test"

def __load_images(path):
    images = []
    for filename in os.listdir(path):
        if ((filename == "readme.md") or filename.startswith(".")):
            continue

        images.append(filename)
    
    return images

def __copy_image(original, destination):
    shutil.copy(original, destination)

def __clear_dir(path):
    for filename in os.listdir(path):
        if ((filename == "readme.md") or filename.startswith(".")):
            continue
        os.remove(os.path.join(path, filename))
        

knu_path = __PAHT_ORIGNAL_ROOT + "/knu"
none_knu_path = __PAHT_ORIGNAL_ROOT + "/none-knu"

knu_images = __load_images(knu_path)
none_knu_images = __load_images(none_knu_path)

random.shuffle(knu_images)
random.shuffle(none_knu_images)


TRAIN_RARIO = 0.75

knu_index = int(len(knu_images) * TRAIN_RARIO)
none_knu_index = int(len(none_knu_images) * TRAIN_RARIO)



__clear_dir(__PATH_TRAIN_ROOT + "/knu")
__clear_dir(__PATH_TRAIN_ROOT + "/none-knu")
__clear_dir(__PATH_TEST_ROOT + "/knu")
__clear_dir(__PATH_TEST_ROOT + "/none-knu")


# train 용 이미지
for file in knu_images[:knu_index]:
    original_path = __PAHT_ORIGNAL_ROOT + "/knu"
    train_path = __PATH_TRAIN_ROOT + "/knu"

    __copy_image(original_path + "/" + file, train_path + "/" + file)

for file in none_knu_images[:none_knu_index]:
    original_path = __PAHT_ORIGNAL_ROOT + "/none-knu"
    train_path = __PATH_TRAIN_ROOT + "/none-knu"

    __copy_image(original_path + "/" + file, train_path + "/" + file)

# test 용 이미지
for file in knu_images[knu_index:]:
    original_path = __PAHT_ORIGNAL_ROOT + "/knu"
    test_path = __PATH_TEST_ROOT + "/knu"

    __copy_image(original_path + "/" + file, test_path + "/" + file)

for file in none_knu_images[none_knu_index:]:
    original_path = __PAHT_ORIGNAL_ROOT + "/none-knu"
    test_path = __PATH_TEST_ROOT + "/none-knu"

    __copy_image(original_path + "/" + file, test_path + "/" + file)
