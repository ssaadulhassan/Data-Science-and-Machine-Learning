import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)

titanic = sns.load_dataset("titanic")
print(titanic)
p1=sns.countplot(x='who',hue='alone',data=titanic)
p1.set_title("Plot for counting")
#plt.title("ye kia scene hay?")
plt.show()
