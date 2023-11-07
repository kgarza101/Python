import pandas as pd
import matplotlib.pyplot as plt 

# Load the data
# df = DataFrame
df = pd.read_csv("C:/Users/xxsco/Downloads/silly ahh goofy/Python/W9/titanic.csv", sep=",")

# show an abbreviated version of the dataframe
#print(df)

# show the first few rows of the dataframe
print(df.head())

# show the columns of the dataframe
print(df.columns)

# show a summary of this dataframe
print(df.info())

# fliter our dataframe
print(df["Sex"] == "male")

# make a new dataframe from the fliter
m_data = df[df["Sex"] == "male"]

# show summary of the m_data dataframe
print(m_data.info())

# preview the first few rows
print(m_data.head())

# make a dataframe for females
f_data = df[df["Sex"] == "female"]
print(f_data.info())
print(f_data.head())

# find the total number of survivors in the m_data
totalSurvM = m_data["Survived"].sum()
print(totalSurvM)

# find number of f_data survivors
totalSurF = f_data["Survived"].sum()
print(totalSurF)

# count the number of rows in each dataframe
totalF = f_data.shape[0] # number of rows
totalM = m_data.shape[0]
print(totalM, totalF)

print(f"Percentage of Male Survivors: {totalSurvM / totalM * 100:.2f} %" )
print(f"Percentage of Female Survivors: {totalSurF / totalF * 100:.2f} %" )

# find the average fair price, males and females separately
print(f"Male average fare: ${m_data['Fare'].mean():.2f}")
print(f"Female average fare: ${f_data['Fare'].mean():.2f}")

# display max and min fare
# lowest
print(f"Lowest fare: ${df['Fare'].min()}")

# highest
print(f"Highest fare: ${df['Fare'].max():.2f}")

# sort the dataframe by Fare
print(df.sort_values('Fare', ascending=False))

# draw a plot of all Fares
plt.scatter(df.index, df.Fare)
plt.show()

