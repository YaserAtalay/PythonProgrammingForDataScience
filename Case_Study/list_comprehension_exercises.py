import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

# Görev1

["NUM" + col.upper() if df[col].dtypes != "O" else col.upper() for col in df.columns]

# Görev2

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Görev3

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]
