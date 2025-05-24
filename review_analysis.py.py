import pandas as pd

# Safely load with low_memory=False
df = pd.read_csv('C:\\Users\\uifsa\\OneDrive\\Desktop\\PROJECTS\\reviews.csv', low_memory=False)


# Strip extra spaces from column names
df.columns = df.columns.str.strip()
# See actual column names
print(df.columns.tolist())
print(df.head())
df.columns = df.columns.str.strip()  # Remove extra spaces

# Rename columns for easier use
df.rename(columns={
    'name': 'product_name',
    'reviews.text': 'review_text',
    'reviews.didPurchase': 'verified_purchase'
    'reviews.date ':'reviews_date'
}, inplace=True)

print(df.columns.tolist())  # Confirm the rename worked

df =df[['product_name','reviews.rating','reviews_text','categories','reviews.date','reviews.didPurchase']]
print(df.head())

#taking top 10 hig rated products
top_rated =df.groupby('product_name')['reviews.rating'].mean().sort_values(ascending=True).head(10)
print("top rated products",top_rated)

#top 10 most reviewed products \
most_reviewed = df['product_name'].value_counts().head(10)
print("the most reviwed products",most_reviewed)

#average rating by category
average_category =df.groupby('categories')['reviews.rating'].mean().sort_values(ascending=False)
print("average rating of categories",average_category)

#verified vs non-verified rating comparsion
verified_rating =df.groupby('reviews.didPurchase')['reviews.rating'].mean()
print("verified rating vs non  ",verified_rating)

#now making the graphs for visualization
import matplotlib.pyplot as plt

# Top 10 most reviewed
most_reviewed = df['product_name'].value_counts().head(10)

plt.figure(figsize=(12, 6))  # Wider chart
most_reviewed.plot(kind='bar', color='blue')
plt.title("Top 10 Most Reviewed Products", fontsize=16)
plt.ylabel("Review Count", fontsize=12)
plt.xticks(rotation=30, ha='right', fontsize=10)  # Angled x-axis labels
plt.tight_layout()
plt.show()



# Average rating by category
average_category = df.groupby('categories')['reviews.rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(14, 7))
average_category.plot(kind='bar', color='orange')
plt.title("Average Rating by Category (Top 20)", fontsize=16)
plt.ylabel("Average Rating", fontsize=12)
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.tight_layout()
plt.show()

# Verified vs Non-Verified
verified_rating = df.groupby('reviews.didPurchase')['reviews.rating'].mean()

plt.figure(figsize=(6, 4))
verified_rating.plot(kind='bar', color='green')
plt.title("Verified vs Non-Verified Purchase Rating", fontsize=14)
plt.ylabel("Average Rating", fontsize=12)
plt.xticks(rotation=0, fontsize=10)
plt.tight_layout()
plt.show()
print(df['reviews.didPurchase'].unique())

