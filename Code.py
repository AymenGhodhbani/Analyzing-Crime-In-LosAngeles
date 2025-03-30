# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("Data/crimes.csv", dtype={"TIME OCC": str})
crimes.head()

crimes["HOUR OCC"] = crimes["TIME OCC"].str[:2].astype(int)

peak_crime_hour = crimes["HOUR OCC"].mode()[0]
print(f"{peak_crime_hour} is the hour that has the highest frequency of crimes.")

night_crimes = crimes[crimes["HOUR OCC"].isin([22,23,0,1,2,3])]
peak_night_crime_location = night_crimes["AREA NAME"].mode()[0]
print(f"{peak_night_crime_location} is the location with the largest frequence of night crimes.")

sns.countplot(data=crimes, x= "HOUR OCC")
plt.show()

group_labels =["0-17", "18-25", "26-34", "35-44","45-54", "55-64", "65+"] 
age_groups  = [0, 17, 25, 34, 44, 54, 64, np.inf]
crimes["Age Groups"] = pd.cut(crimes["Vict Age"], bins = age_groups, labels = group_labels)

victim_ages = crimes["Age Groups"].value_counts()
print(victim_ages)