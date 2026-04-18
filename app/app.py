import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Poll Results Dashboard", layout="wide")

st.title("🌍Poll Results Visualizer")

# -----------------------------
# LOAD DATA (FIXED PATH)
# -----------------------------
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "advanced_poll_data.csv")

    if not os.path.exists(file_path):
        return None, file_path

    df = pd.read_csv(file_path)
    return df, file_path

df, file_path = load_data()

# -----------------------------
# ERROR HANDLING (DEBUG INCLUDED)
# -----------------------------
if df is None:
    st.error("❌ Data not found!")
    st.write("📁 Expected file location:", file_path)
    st.write("👉 Run this command in terminal:")
    st.code("python src/data_generator.py")
    st.stop()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

country = st.sidebar.multiselect(
    "🌍 Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

region = st.sidebar.multiselect(
    "🗺 Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

age_group = st.sidebar.multiselect(
    "👤 Age Group",
    options=df["Age_Group"].unique(),
    default=df["Age_Group"].unique()
)

gender = st.sidebar.multiselect(
    "⚧ Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

question = st.sidebar.selectbox(
    "❓ Select Question",
    options=df["Question"].unique()
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df["Country"].isin(country)) &
    (df["Region"].isin(region)) &
    (df["Age_Group"].isin(age_group)) &
    (df["Gender"].isin(gender)) &
    (df["Question"] == question)
]

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(filtered_df.head())

# -----------------------------
# METRICS
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

vote_counts = filtered_df["Option_Selected"].value_counts()

with col1:
    st.metric("Total Responses", len(filtered_df))

with col2:
    if not vote_counts.empty:
        st.metric("Top Choice", vote_counts.idxmax())

with col3:
    st.metric("Countries Selected", len(country))

# -----------------------------
# BAR CHART
# -----------------------------
st.subheader("📊 Vote Distribution")

fig1, ax1 = plt.subplots()
sns.barplot(x=vote_counts.index, y=vote_counts.values, ax=ax1)
ax1.set_xlabel("Options")
ax1.set_ylabel("Votes")
st.pyplot(fig1)

# -----------------------------
# PIE CHART
# -----------------------------
st.subheader("🥧 Percentage Share")

fig2, ax2 = plt.subplots()
ax2.pie(vote_counts.values, labels=vote_counts.index, autopct='%1.1f%%')
st.pyplot(fig2)

# -----------------------------
# REGION ANALYSIS
# -----------------------------
st.subheader("🌍 Region-wise Analysis")

region_data = pd.crosstab(filtered_df["Region"], filtered_df["Option_Selected"])

fig3, ax3 = plt.subplots()
region_data.plot(kind="bar", stacked=True, ax=ax3)
st.pyplot(fig3)

# -----------------------------
# COUNTRY ANALYSIS
# -----------------------------
st.subheader("🌎 Country-wise Analysis")

country_data = pd.crosstab(filtered_df["Country"], filtered_df["Option_Selected"])

fig4, ax4 = plt.subplots()
country_data.plot(kind="bar", stacked=True, ax=ax4)
st.pyplot(fig4)

# -----------------------------
# TREND ANALYSIS
# -----------------------------
st.subheader("📈 Trend Over Time")

trend_data = filtered_df.groupby(
    [pd.Grouper(key="Date", freq="W"), "Option_Selected"]
).size().unstack()

fig5, ax5 = plt.subplots()
trend_data.plot(ax=ax5)
st.pyplot(fig5)

# -----------------------------
# INSIGHTS
# -----------------------------
st.subheader("🧠 Insights")

if not vote_counts.empty:
    st.success(f"🏆 Most Preferred Option: {vote_counts.idxmax()}")
    st.info(f"📊 Total Responses: {len(filtered_df)}")
else:
    st.warning("No data available for selected filters.")