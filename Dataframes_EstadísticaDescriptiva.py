
import pandas as pd

df = pd.read_csv("archivo.csv")

print(df["year"].mean())
print(df["condition"].max())
print(df["odometer"].min())
print(df["condition"].median())
print(df["sellingprice"].describe())
print(df[df["year"]>2012])
dfColor = df[df["color"]=="black"]
print(dfColor)
dfFabricante = df[df["make"]=="Kia"]
print(dfFabricante)

