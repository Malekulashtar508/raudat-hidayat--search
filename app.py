import streamlit as st
import pandas as pd

# Load Excel file
@st.cache_data
def load_data():
    return pd.read_excel("raudat_hidayat.xlsx")

df = load_data()

st.title("📚 Raudat Hidayat Search Engine")

# Search Option 1: Text Search in hadeeth, kalam or qaul
st.header("🔍 Search in Hadeeth, Kalam or Qaul")
search_query = st.text_input("Enter a word to search:")

if search_query:
    results = df[df['hadeeth, kalam or qaul'].astype(str).str.contains(search_query, case=False, na=False)]
    if not results.empty:
        st.success(f"Found {len(results)} results:")
        st.dataframe(results[['النص']])
    else:
        st.warning("No matches found.")

# Search Option 2: Filter by topic
st.header("📂 Filter by Topic (الموضوع)")
topics = df['الموضوع'].dropna().unique()
selected_topic = st.selectbox("Choose a topic:", sorted(topics))

if selected_topic:
    filtered = df[df['الموضوع'] == selected_topic]
    st.success(f"Found {len(filtered)} results for topic '{selected_topic}':")
    st.dataframe(filtered)
