import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import jieba
from scipy.misc import imread
from myStopWords import *
import sys
 
text_from_file_with_apath = open(sys.argv[1]).read()
 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

img = imread('b.jpg')

 
my_wordcloud = WordCloud(font_path = './simyou.ttf', 
                        random_state = 30,
                        mask = img,
                        max_font_size = 180,
                        stopwords = myStopWords(),
                        background_color="white").generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()