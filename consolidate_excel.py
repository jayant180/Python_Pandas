import pandas as pd
import os
import glob
from datetime import datetime

path="your/path"
dest="destinationPath"

os.makedirs(store, exist_ok=True)

files = glob.glob(os.path.join(path, "*.xlsx"))
if not files:
    print("No excel files found")
    exit()

all_datas = []

for file in files:
    print(f"Processing: {files}")
    df = pd.read_excel(file)
    all_datas.append(df)

final_df = pd.concat(all_datas, ignore_index = True)
output_file = os.path.join(dest, "consolidate_report.xlsx")
final_df.to_excel(output_file, index=False)
