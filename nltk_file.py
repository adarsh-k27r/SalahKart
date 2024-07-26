import nltk
import matplotlib.pyplot as plt

nltk.download()
text = " Hey, My name is Adarsh Kumar, skills are python, java and web-scraping. Rest, I am a writer."

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist

word_tokenized = word_tokenize(text)
sent_tokenized = sent_tokenize(text)

fd = FreqDist(word_tokenized)
print(fd.most_common(3))

fd.plot(10, cumulative=False)
plt.show()

