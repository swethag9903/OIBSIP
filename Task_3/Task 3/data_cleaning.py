import pandas as pd

csv_data = pd.read_csv("T3_S1_NYC.csv")
json_data = pd.read_json("T3_S2_Trendingyoutube.json")

csv_data = csv_data.astype(str)
json_data = json_data.astype(str)

csv_data = csv_data.drop_duplicates()
json_data = json_data.drop_duplicates()

csv_data.to_csv("Cleaned_T3_S1_NYC.csv", index=False)
json_data.to_json("Cleaned_T3_S2_Trendingyoutube.json", orient="records", lines=True)

print("Cleaning completed. Cleaned files saved.")
