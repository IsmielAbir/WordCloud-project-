from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = open("c.txt", mode="r", encoding="utf-8").read()

wc= WordCloud(
    background_color= "white",
)

wc.generate(text)
wc.to_file("test.png")