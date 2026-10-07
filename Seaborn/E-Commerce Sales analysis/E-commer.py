import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("E-Commerece.csv")
print(df)


print("=======================================Given Dataset Perform================================")
print("=======Category Has The Highest Total Sales=======")
cate=df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
cate_sales=df.groupby('Category')['Sales'].sum().nlargest(1)
print(cate,cate_sales)

print("=======City Generates the Highest Profit======")
city=df.groupby('City')['Sales'].sum().sort_values(ascending=False)
city_sales=df.groupby('City')['Sales'].sum().nlargest(1)
print(city,city_sales)

print("=======Discount Effect Sales=======")
discount=df.groupby('Discount')['Sales'].sum().sort_values(ascending=False)
print(discount)

print("=======Category Has The Highest Average Rating=======")
rating=df.groupby('Category')['Rating'].mean().sort_values(ascending=False)
avg_rating=df.groupby('Category')['Rating'].mean().nlargest(1)
print(rating,avg_rating)

print("=======The Relationship Between Sales And Profit=======")
sns.scatterplot(x='Sales',y='Profit',data=df)
plt.show()

print("=======Categories With Unusually High Or Low=======")
sales_hl=df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print(sales_hl)

print("========================================Seaborn Charts================================")
print("=======Sales By Category=======")
sns.barplot(x='Sales',y='Category',hue='Category',data=df)
plt.show()

print("=======Profit By City=======")
sns.barplot(x='Profit',y='City',hue='City',data=df)
plt.show()

print("=======Discount Vs Sales=======")
sns.scatterplot(x='Discount',y='Sales',data=df)
plt.show()

print("=======Rating By Category=======")
sns.boxplot(x='Rating',y='Category',data=df)
plt.show()

print("=======Sales Vs Profit======")
sns.scatterplot(x='Sales',y='Profit',data=df)
plt.show()

print("=======Correlation Between Numerical Columns=======")
co=df[['Quantity','Sales','Profit','Discount','Rating']].corr()
sns.heatmap(co,annot=True)
plt.show()

print("========================================Final Output================================")
print("=======Product Quantity=======")
pro=df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(pro)

print("=======Product Discount=======")
disc=df.groupby('Product')['Discount'].count().sort_values(ascending=False)
print(disc)

print("=======City Wise Sales=======")
c=df.groupby('City')['Sales'].sum().sort_values(ascending=False)
print(c)

print("=======City Wise Date======")
print(df[['City','Date']])

print("=======Product Wise Quantity=======")
count=df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(count)

print("=======Improve Sales Profit=======")
improv=df.groupby('Category')[['Sales','Profit']].sum().reset_index()
sns.barplot(data=improv,x='Category',y='Sales')
plt.title("Sales By Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

print("========================================Completed================================")

