from wordcloud import WordCloud
import matplotlib.pyplot as plt
filename = "C:\\Users\\dell\\source\\repos\\hello\\yes-minister.txt"
with open(filename) as f:
 mytext = f.read()
print(mytext)
wordcloud = WordCloud().generate(mytext)
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
