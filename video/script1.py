import os
import pandas as pd

directory = "C:/Users/mahdie/Desktop/important/video/high"

csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

for file in csv_files:
    df = pd.read_csv(os.path.join(directory, file))
    
    df['Label'] = 1 
    df.to_csv(os.path.join(directory, file), index=False)
