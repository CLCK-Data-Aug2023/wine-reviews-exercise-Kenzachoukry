# add your code here
import pandas as pd
import zipfile

#Reading the dataset using the compression zip
file = pd.read_csv('wine-reviews-exercise-Kenzachoukry/data/winemag-data-130k-v2.csv.zip',compression='zip')
 
#Displaying the dataset
print(file.head())

# Creating a summary for the requested output
file_stats = file.groupby('country').agg({'points': ['count', 'mean']}).reset_index()

# Naming the columns as requested
file_stats.columns = ['country', 'count', 'points']

#Writing to a new CSV file
file_csv = 'wine-reviews-exercise-Kenzachoukry/data/reviews-per-country.csv'
file_stats.to_csv(file_csv, index=False)

#Sorting the files by average points
print(file_stats)


