import glob
import os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory where the data will reside, relative to 'darknet.exe'
path_data = './'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
files = []
for ext in ('images/*/*.jpeg', 'images/*/*.png', 'images/*/*.jpg'):
    files.extend(glob.glob(os.path.join(path_data, ext)))
files = [w.replace('\\', '/') for w in files]
print(files)

# for pathAndFilename in glob.iglob(os.path.join(current_dir, "images/*/*.jpg")):
for pathAndFilename in files:
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        # file_test.write(path_data + title + '.jpg' + "\n")
        file_test.write(pathAndFilename + "\n")
    else:
        # file_train.write(path_data + title + '.jpg' + "\n")
        file_train.write(pathAndFilename + "\n")
        counter = counter + 1
