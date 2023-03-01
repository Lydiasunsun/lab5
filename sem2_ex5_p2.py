
# initilize the dictionary and list
wordcount = {}
words = []
# open the file
fin = open('sampleinput.txt', 'r')
# read each line
for line in fin:
    # split line into words lists
    splitword = line.split()

    # read each word in the list and change to lower case ( now they are words,not lists)
    for word_original in splitword:
        word = word_original.lower()
        # add all words into one list:words
        words.append(word)


# count each word in the list

for keys in words:
    count = words.count(keys)


# add the key and count value into the wordcount
    wordcount[keys] = count
print(wordcount)
