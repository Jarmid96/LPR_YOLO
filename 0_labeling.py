file_labels = open('zdjecia/labels.txt', 'r')
index = 0
WIDTH = 512
HEIGHT = 384
# Loop through the file line by line
for line in file_labels:
    index += 1

    data = line.split()

    name = data[0][0:-4]
    y1 = int(data[1])
    y2 = int(data[2])
    x1 = int(data[3])
    x2 = int(data[4])

    if y1 != 0 or y2 != 0 or x1 != 0 or x2 != 0:
        x = ((x1+x2)/2)/WIDTH
        y = ((y1+y2)/2)/HEIGHT
        height = (y2-y1)/HEIGHT
        width = (x2-x1)/WIDTH

        label_name = 'zdjecia/data/labels/' + name + '.txt'
        file = open(label_name, 'a')
        file.write('{} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format('0', x, y, width, height))
        file.close()
    else:
        label_name = 'zdjecia/data/labels/' + name + '.txt'
        file = open(label_name, 'a')
        file.close()

# closing text file
file_labels.close()
