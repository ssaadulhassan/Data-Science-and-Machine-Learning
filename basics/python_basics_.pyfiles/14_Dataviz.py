# Steps involved in Data Viz
# Step1 Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step2 Set a theme
sns.set_theme(style="ticks",color_codes=True)

# Step3 Import Dataset ( You can also import own data)
kashti = sns.load_dataset("titanic")
#print(kashti)  # pura data ajega

# Step4 Plot basic graph with 1 variable (COunt plot me y axis par count auto ata hay)
p=sns.countplot(x='sex',data=kashti)
plt.show()

# Step5 plot Basic  graph with 2 variable (hue means color)
# jese hue me class agae male female ki ticket k hisab se mtlb x ko tor rahaa hay hue apka (LAzmi smjh)
p=sns.countplot(x='sex',hue='who',data=kashti)
plt.show()

# Step6 plot Basic  graph with 2 variable (count plot) with Titles
p=sns.countplot(x='sex',hue='class',data=kashti)
p.set_title("BABA ka count plot for Kashti")
plt.show()
