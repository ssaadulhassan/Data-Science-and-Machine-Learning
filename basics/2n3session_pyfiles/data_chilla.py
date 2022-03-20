# import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step2 Set a theme
sns.set_theme(style="ticks",color_codes=True)

# import data from file
chilla = pd.read_csv("data_viz.csv")
print(chilla)

# Step6 plot Basic  graph with 2 variable (count plot) with Titles
p=sns.countplot(x='Gender',hue='Age',data=chilla)
p.set_title("BABA ka Attendance lene ka tariqa")
plt.show()