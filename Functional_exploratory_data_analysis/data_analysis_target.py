import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


def grab_col_names(dataframe, cat_th = 10, car_th = 20):
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < car_th and df[col].dtypes in ["int64", "float64"]]
    cat_but_car = [col for col in df.columns if df[col].nunique() > cat_th and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"Cat_cols: {len(cat_cols)}")
    print(f"Num_cols: {len(num_cols)}")
    print(f"Cat_but_car: {len(cat_but_car)}")
    print(f"Num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)


# Kategorik degişkenlerle hedef degiskeni inceleme

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, "survived", "sex")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)



# Sayisal degişkenlerle hedef degiskeni inceleme


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}))

for col in num_cols:
    target_summary_with_num(df, "survived", col)

