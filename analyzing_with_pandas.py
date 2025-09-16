# ==========================================
# Giltech Online Cyber Data Analysis Project
# ==========================================
# "Empowering the community with digital access"
# Objective: Load, analyze, and visualize business data
# Libraries
import pandas as pd
import matplotlib.pyplot as plt

# ================================
# Task 1: Load and Explore Dataset
# ================================

try:
    # Simulated dataset: 20 days of cyber services
    data = {
        "Date": pd.date_range(start="2025-09-01", periods=20, freq="D"),
        "Service": ["Printing", "Photocopy", "Browsing", "KRA Services", "Scanning"] * 4,
        "Customers": [20, 15, 30, 12, 8, 25, 18, 35, 10, 6,
                      22, 14, 33, 11, 7, 26, 20, 40, 9, 5],
        "Revenue": [1000, 750, 1500, 1200, 400, 1100, 900, 1750, 1300, 300,
                    1050, 720, 1650, 1250, 350, 1200, 950, 1800, 1150, 280]
    }

    df = pd.DataFrame(data)

    print("✅ Giltech Online Cyber Dataset Loaded Successfully\n")
    print(df.head(10))   # Display first 10 rows for inspection

    # Structure & Missing Values
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values per Column:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("✗ Dataset file not found. Please check the filename or path.")
except Exception as e:
    print(f"✗ An error occurred: {e}")

# ================================
# Task 2: Basic Data Analysis
# ================================

print("\n📊 Statistical Summary of Numerical Columns:")
print(df.describe())

# Grouping: Average revenue per service
avg_revenue = df.groupby("Service")["Revenue"].mean()
print("\n💰 Average Revenue per Service:")
print(avg_revenue)

# Grouping: Average customers per service
avg_customers = df.groupby("Service")["Customers"].mean()
print("\n👥 Average Customers per Service:")
print(avg_customers)

# Business Insights
total_revenue = df["Revenue"].sum()
busiest_day = df.loc[df["Customers"].idxmax()]
top_service = avg_revenue.idxmax()

print(f"\n✨ Business Insights for Giltech Online Cyber:")
print(f"- Total Revenue over 20 days: KES {total_revenue}")
print(f"- Busiest Day: {busiest_day['Date'].date()} with {busiest_day['Customers']} customers")
print(f"- Top Service by Revenue: {top_service} (Avg. {avg_revenue.max():.2f} KES)")

# ================================
# Task 3: Data Visualization
# ================================

plt.style.use("seaborn-v0_8")

# 1. Line Chart - Revenue over Time
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Revenue"], marker='o', linestyle='-', color='blue', label="Daily Revenue")
plt.title("Giltech Online Cyber - Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (KES)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average Revenue per Service
avg_revenue.plot(kind="bar", color="teal", figsize=(8,5))
plt.title("Average Revenue by Service - Giltech Online Cyber")
plt.xlabel("Service")
plt.ylabel("Average Revenue (KES)")
plt.show()

# 3. Histogram - Distribution of Customers per Day
plt.figure(figsize=(8,5))
plt.hist(df["Customers"], bins=8, color="orange", edgecolor="black")
plt.title("Distribution of Daily Customers - Giltech Online Cyber")
plt.xlabel("Number of Customers")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Customers vs Revenue
plt.figure(figsize=(8,5))
plt.scatter(df["Customers"], df["Revenue"], color="green", alpha=0.7)
plt.title("Relationship between Customers & Revenue - Giltech Online Cyber")
plt.xlabel("Number of Customers")
plt.ylabel("Revenue (KES)")
plt.show()

# 5. Stacked Bar - Service Contribution per Day
pivot = df.pivot(index="Date", columns="Service", values="Revenue").fillna(0)
pivot.plot(kind="bar", stacked=True, figsize=(12,6), colormap="Set2")
plt.title("Daily Revenue Contribution by Service - Giltech Online Cyber")
plt.xlabel("Date")
plt.ylabel("Revenue (KES)")
plt.legend(title="Service")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Pie Chart - Revenue Share by Service
plt.figure(figsize=(7,7))
plt.pie(avg_revenue, labels=avg_revenue.index, autopct="%1.1f%%", startangle=90, colors=plt.cm.Paired.colors)
plt.title("Revenue Share by Service - Giltech Online Cyber")
plt.show()