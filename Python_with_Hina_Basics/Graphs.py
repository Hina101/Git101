# #Bar plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks" , color_codes=True)
# titanic= sns.load_dataset("titanic")
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# plt.show()


#Count plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks" , color_codes=True)
# titanic= sns.load_dataset("titanic")
# p1=sns.countplot(x="sex", data=titanic, hue="class")
# p1.set_title("Plot for counting")
# plt.show()

#Scatter plot
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks" , color_codes=True)
# titanic= sns.load_dataset("titanic")
# g=sns.FacetGrid(titanic, row="sex",hue="alone")
# g=g.map(plt.scatter,"age", "fare").add_legend()
# plt.show()