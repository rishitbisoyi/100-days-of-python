import pandas as pd

df = pd.read_csv("72_DataExploration/salaries_by_college_major.csv")

print(df.head())

print(df.shape)
print(df.columns)
print(df.isna().sum())

print(df["Undergraduate Major"])
print(df["Starting Median Salary"])

print(df.iloc[0])
print(df.iloc[0]["Undergraduate Major"])
print(df.iloc[0]["Starting Median Salary"])

print(df.sort_values("Starting Median Salary", ascending=False).head())

df["Potential"] = (
    df["Mid-Career 90th Percentile Salary"]
    - df["Starting Median Salary"]
)

df["Risk"] = (
    df["Mid-Career 90th Percentile Salary"]
    - df["Mid-Career 10th Percentile Salary"]
)

print(
    df[["Undergraduate Major", "Potential"]]
    .sort_values("Potential", ascending=False)
    .head()
)

print(
    df.groupby("Group")["Starting Median Salary"].mean()
)

print(
    df.pivot_table(
        index="Group",
        values=[
            "Starting Median Salary",
            "Mid-Career Median Salary",
            "Mid-Career 10th Percentile Salary",
            "Mid-Career 90th Percentile Salary"
        ],
        aggfunc="mean"
    )
)