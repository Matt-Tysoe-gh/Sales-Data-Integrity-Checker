import pandas as pd
import os
from itertools import combinations

base_file_path = r""

excel_files = [f for f in os.listdir(base_file_path) if f.endswith((".xlsx", "xls"))]

file_data = {
    file_name: pd.read_excel(os.path.join(base_file_path, file_name))
    for file_name in excel_files
}

def compare_files(file_name1: str, df1: pd.DataFrame, file_name2: str, df2: pd.DataFrame) -> None:

    store_ids1 = set(df1["Store ID"].unique())
    store_ids2 = set(df2["Store ID"].unique())

    if store_ids1 == store_ids2:
        print(f"{file_name1} and {file_name2}: Store IDs match")

        sellout_by_store1 = df1.groupby("Store ID")["Sell Out"].sum()
        sellout_by_store2 = df2.groupby("Store ID")["Sell Out"].sum()

        for store_id in sellout_by_store1.index:
            sum1 = sellout_by_store1.loc[store_id]
            sum2 = sellout_by_store2.loc[store_id]
            if sum1 == sum2:
                print(f"Store {store_id}: Sell Out matches ({sum1:,})")
            else:
                print(f"Mismatch for store {store_id}: {file_name1} = {sum1:,} vs {file_name2} = {sum2:,}")

    else:
        print(f"{file_name1} and {file_name2}: Store IDs do not match")

    total_sellout1 = df1["Sell Out"].sum()
    total_sellout2 = df2["Sell Out"].sum()

    if total_sellout1 == total_sellout2:
        print(f"{file_name1} and {file_name2}: Overall Sell Out matches ({total_sellout1:,})")
    else:
        print(f"{file_name1} and {file_name2}: Overall Sell Out mismatch ({total_sellout1:,} vs {total_sellout2:,})")
    print("-" * 60)

for (name1, df1), (name2, df2) in combinations(file_data.items(), 2):
    compare_files(name1, df1, name2, df2)
