import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_bar(counts):
    plt.figure()
    sns.barplot(x=counts.index, y=counts.values)
    plt.title("Vote Count")
    plt.savefig("outputs/bar_chart.png")
    plt.show()

def plot_pie(counts):
    plt.figure()
    plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
    plt.title("Poll Distribution")
    plt.savefig("outputs/pie_chart.png")
    plt.show()

def plot_region(df):
    region_data = pd.crosstab(df["Region"], df["Option_Selected"])
    region_data.plot(kind="bar", stacked=True)
    plt.title("Region-wise Preferences")
    plt.savefig("outputs/region_chart.png")
    plt.show()