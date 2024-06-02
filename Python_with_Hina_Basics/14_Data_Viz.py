#Steps involved indata visuatization
#step-1 Import libararies
import seaborn as sns
import matplotlib.pyplot as plt

#step-2 seta theme
sns.set_theme(style="ticks", color_codes= True)

#step-3 import data set you can also import your own data
kashti =sns.load_dataset("titanic")
# print(kashti)

#step-4 plot basic graph simple countplot
p=sns.countplot(x="sex", data=kashti)
plt.show()

#step-5 plot basic graph with 2 variables
p=sns.countplot(x="sex", data=kashti,hue="class")
plt.show()

#step-6 plot basic graph with 2 variables with title
p=sns.countplot(x="sex", data=kashti,hue="class")
p.set_title("Count plot for kashti")
plt.show()