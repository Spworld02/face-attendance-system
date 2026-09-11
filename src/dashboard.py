import streamlit as st
import pandas as pd
import os
from datetime import datetime

ATTENDANCE_FILE = "data/attendance.csv"

st.set_page_config(page_title="Attendance Dashboard", layout="wide")
st.title("📋 Face Attendance Dashboard")

if not os.path.exists(ATTENDANCE_FILE):
    st.warning("No attendance records yet. Run recognize.py first.")
    st.stop()

df = pd.read_csv(ATTENDANCE_FILE)
if "Timestamp" not in df.columns or "Name" not in df.columns:
    st.error("Attendance file missing required columns ('Name' and 'Timestamp').")
    st.stop()

df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")
df = df.dropna(subset=["Timestamp"]).copy()
df["Date"] = df["Timestamp"].dt.date

# --- Sidebar filters ---
st.sidebar.header("Filters")

names = ["All"] + sorted(df["Name"].unique().tolist())
selected_name = st.sidebar.selectbox("Filter by name", names)

dates = ["All"] + sorted(df["Date"].astype(str).unique().tolist(), reverse=True)
selected_date = st.sidebar.selectbox("Filter by date", dates)

filtered_df = df.copy()
if selected_name != "All":
    filtered_df = filtered_df[filtered_df["Name"] == selected_name]
if selected_date != "All":
    filtered_df = filtered_df[filtered_df["Date"].astype(str) == selected_date]

# --- Summary metrics ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(filtered_df))
col2.metric("Unique People", filtered_df["Name"].nunique())
col3.metric("Today's Attendance", len(df[df["Date"] == datetime.now().date()]))

# --- Table ---
st.subheader("Attendance Records")
st.dataframe(
    filtered_df[["Name", "Timestamp"]].sort_values("Timestamp", ascending=False),
    use_container_width=True,
)

# --- Download button ---
st.download_button(
    "Download as CSV",
    filtered_df.to_csv(index=False),
    file_name="attendance_export.csv",
    mime="text/csv",
)
