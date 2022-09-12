file_labels = open('data/labels.txt', 'r')

label_name = 'data/labels_ocr_new.txt'
file_labels_ocr = open(label_name, 'a')

# Loop through the file line by line
index = 0
for line in file_labels:
    index += 1
    data = line.split()
    name = data[0]
    file_labels_ocr.write('{} \n'.format(name))

# closing text file
file_labels.close()
file_labels_ocr.close()
