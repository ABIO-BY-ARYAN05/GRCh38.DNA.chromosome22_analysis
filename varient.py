# data handling and preprocessing for the varient analysis
print("--data handling and preprocessing for the varient analysis--")
import pandas as pd
import numpy as np

df=pd.read_csv("variants_table.csv",header=None)

df=df[0].str.split("\t",expand=True)

df.columns=["CHROM", "POS", "ID", "REF", "ALT",
    "QUAL", "FILTER", "INFO", "FORMAT", "SAMPLE"]
print(df.sample(5))
print(df.shape)