import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("high_quality_variants.csv")
import numpy as np

df["TYPE"] = np.where(
    (df["REF"].str.len() == 1) & (df["ALT"].str.len() == 1),
    "SNP",
    "INDEL"
)

print(df.sample(5))

# quality scores visualizattion
plt.hist(df["QUAL"],bins=50)
plt.title("Qualty score distributions (HIGH QUALITY VARIENTS)")
plt.xlabel("QUAL")
plt.ylabel("Frequency")
plt.show()

# deapth distribuition
plt.hist(df["DP"],bins=50)
plt.title("Read Depth Distribution")
plt.xlabel("DP")
plt.ylabel("Frequency")
plt.show()

# SNP vs INDEL
df["TYPE"].value_counts().plot(kind="bar")
plt.title("SNP vs INDEL Distribution")
plt.xlabel("Variant Type")
plt.ylabel("Count")
plt.show()

# DP vs QUAL
plt.scatter(df["DP"], df["QUAL"], alpha=0.5)
plt.title("QUAL vs DP")
plt.xlabel("Quality Score (QUAL)")
plt.ylabel("Read Depth (DP)")
plt.show()

plt.hist(df["QUAL"], bins=50)
plt.savefig("qual_distribution.png")
plt.savefig("plots/qual_distribution.png")
plt.close()