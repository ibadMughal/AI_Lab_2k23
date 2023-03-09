# import csv
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Job 1: Read keyword column and assign data to a data-structure(list)
keywordsList = []

# Method 1
file = open('dataset-medical.csv', "r", encoding="utf-8")
for line in file:
    keywordsList.append(line.rstrip().split(",")[1])
    
# Method 2    
# with open('dataset-medical.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # skip header row
#     for row in reader:
#         keywords_list.append(row[1])

# Job 2: Separate words using ';' separator
keywords = []
for words in keywordsList:
    element = [word.upper() for word in words.split(";")]
    keywords.extend(element)

print(keywords)
# Job 3: Count Frequency of each word (occurrence of word in entire dataset)
word_freq = {}
for word in keywords:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# just checking that my logic is correct or not using Counter class?
# print(word_freq == Counter(keywords))


# # Job 4: Create wordcloud from word frequency dictionary using WordCloud library
wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(Counter(keywords))

# Job 5: Display wordcloud using matplotlib
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()


    
    
