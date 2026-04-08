import pandas as pd 
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt 
import seaborn as sns 

def generate_plots() : 

 df = pd.read_csv("unbiased_student_performance.csv")

 # 1. Distribution of Marks :-
 plt.figure()
 sns.histplot(df['Marks'],bins=20)
 plt.savefig("static/plots/marks_distribution.png")
 plt.close()

 # 2. Study Vs Marks :-
 plt.figure()
 sns.scatterplot(x='Study_Hours', y='Marks', data=df)
 plt.savefig("static/plots/study_vs_marks.png")
 plt.close()

 # 3. Internet Usage Vs Marks 
 plt.figure()
 sns.scatterplot(x='Internet_Usage', y='Marks', data=df)
 plt.savefig("static/plots/internet_vs_marks.png")
 plt.close()
