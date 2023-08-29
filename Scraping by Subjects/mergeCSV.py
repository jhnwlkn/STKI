import pandas as pd
import os

cats_raw = os.listdir('D:/John/STKI/Scraping by Subject/CSVFile/')
cats = [x[:-5] for x in cats_raw]

data_frames = []

for i in cats:
    cat_folder = f"D:/John/STKI/Scraping by Subject/CSVFile/{i}.json/"
    for file in os.listdir(cat_folder):
        if file.endswith(".csv"):
            csv_path = os.path.join(cat_folder, file)
            df = pd.read_csv(csv_path)
            data_frames.append(df)

merged_df = pd.concat(data_frames, ignore_index=True)
output_csv_path = "merged_data.csv"
merged_df.to_csv(output_csv_path, index=False)