# data frame and analysis
import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\hp\biotechnology stuff\automation projects\varient_analysis\variants_table.csv",header=None)

df=df[0].str.split("\t",expand=True)

df.columns=["CHROM", "POS", "ID", "REF", "ALT",
    "QUAL", "FILTER", "INFO", "FORMAT", "SAMPLE"]

print(df["FILTER"].value_counts())

# QUALITY DISTRIBUTION
print("--QUALITY DISTRIBUTION--")
df["QUAL"]=df["QUAL"].astype(float)
print(df["QUAL"].describe())

# EXTRACT OF DEPTH FROM INFO
print("--EXTRACT OF DEPTH FROM INFO--")
df["DP"]=df["INFO"].str.extract(r"DP=(\d+)").astype(float)
print(df["DP"].describe())

# QUALITY FILTER FOR VARIENT
print("--QUALITY FILTER FOR VARIENT--")
filtered_df=df[(df["QUAL"]>50) & (df["DP"]>10)]
print('original:',df.shape)
print('filtered:',filtered_df.shape)

# SNP VS INDEL
print("--SNP VS INDEL--")
df["TYPE"] = df.apply(
    lambda x: "SNP" if len(x["REF"]) == 1 and len(x["ALT"]) == 1 else "INDEL",
    axis=1
)
print(df["TYPE"].value_counts())


# QUALITY BEFORE AND AFTER
print("-- QUALITY BEFORE AND AFTER--")
print("Before QUAL mean:", df["QUAL"].mean())
print("After QUAL mean:", filtered_df["QUAL"].mean())

# VARIANT REMOVED
print("--VARIANT REMOVED--")
removed=df.shape[0]-filtered_df.shape[0]
print("varient removed:",removed)

# DEPTH BEFORE AND AFTER
print("-- DEPTH BEFORE AND AFTER--")
print("Before DP mean:", df["DP"].mean())
print("After DP mean:", filtered_df["DP"].mean())


# result save
filtered_df.to_csv("high_quality_variants.csv", index=False)