from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import matplotlib.pyplot as plt
import jieba
from scipy.misc import imread

with open(r'text1.txt','r',encoding='utf-8') as f:
	txt=f.read()
txt=txt.replace('，','').replace(' ','').replace('？','')
wordlist=jieba.cut(txt,cut_all=False)
space_splite=''.join(wordlist)
back_coloring=plt.imread('img/test5.jpg')
my_wordcloud=WordCloud(background_color='black',
				# font_path=font,
				mask=back_coloring,
				stopwords=STOPWORDS,
				max_font_size=60,
				random_state=30,
               )
wc=my_wordcloud.generate(space_splite)
image_colors = ImageColorGenerator(back_coloring)
plt.imshow(wc)
plt.axis('off')
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(back_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()

