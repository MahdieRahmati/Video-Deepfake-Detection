import os
import pandas as pd


directory = "C:/Users/mahdie/Desktop/important/video/high"

csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

files_with_imputations = []

for file in csv_files:
    df = pd.read_csv(os.path.join(directory, file))
    if (df == -1).any().any():

        files_with_imputations.append(file)
        df.replace(-1, pd.NA, inplace=True)
        df.fillna(method='ffill', inplace=True)

    df.to_csv(os.path.join(directory, file), index=False)


if files_with_imputations:
    print("Files with values imputed:")
    for file in files_with_imputations:
        print(file)
else:
    print("No files had values imputed.")


#high_104.csv
# high_139.csv
# high_143.csv
# high_145.csv
# high_15.csv 
# high_152.csv
# high_154.csv
# high_156.csv
# high_157.csv
# high_159.csv
# high_163.csv
# high_170.csv
# high_171.csv
# high_174.csv
# high_188.csv
# high_192.csv
# high_194.csv
# high_222.csv
# high_250.csv
# high_255.csv
# high_260.csv
# high_312.csv
# high_52.csv
# high_56.csv
# high_61.csv
# high_90.csv

# 26 videos imputed 