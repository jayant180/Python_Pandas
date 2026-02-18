import pandas as pd
import glob
import os

files_path="C:/Users/admin/Documents"
output_file="C:/Users/admin/Documents/MainData.xlsx"

files = glob.glob(os.path.join(files_path, "*.xlsx"))
with pd.ExcelWriter(output_file) as writer:
    for file in files:
        df = pd.read_excel(file)
        sheet_name = os.path.basename(file.replace(".xlsx",""))
        df.to_excel(writer, sheet_name=sheet_name, index=False)
print("Merged the file into one file as a sheet")
