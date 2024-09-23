import pandas as pd 


#"C:/Users/mahdie/Desktop/important/video/high_imputed"
#"C:/Users/mahdie/Desktop/important/video/high_removed"

import os
import pandas as pd

directory = "C:/Users/mahdie/Desktop/important/video/high_imputed"

length = []

csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]


for file in csv_files:
    df = pd.read_csv(os.path.join(directory, file))
    length.append(len(df))


print(max(length))
print(min(length))
print(median(length))

