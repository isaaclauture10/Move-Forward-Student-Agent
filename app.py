import streamlit as st
import csv
from datetime import datetime

tasks = []

tasks = []

with open("tasks.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)

total_hours = 0

for task in tasks:
    total_hours += int(task["estimated_hours"])


st.title("Most Valuable Agent")


st.subheader("AI Productivity Assistant")

st.write(
    "MVSA analyzes deadlines, importance, workload, and task status "
    "to recommend what you should focus on next."
)

st.metric("Tasks Loaded", len(tasks))
st.metric("Estimated Hours", total_hours)

st.subheader("Task List")

st.table(tasks)

st.subheader("Task Hours Chart")

chart_data = {}

for task in tasks:
    chart_data[task["name"]] = int(task["estimated_hours"])

st.bar_chart(chart_data)

from datetime import datetime

ranked_tasks = []

for task in tasks:
    score = 0
    importance = int(task["importance"])
    due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
    today = datetime.today()

    days_until_due = (due_date.date() - today.date()).days

    if days_until_due < 0:
        score += 50
    elif days_until_due <= 1:
        score += 20
    elif days_until_due <= 3:
        score += 10
    elif days_until_due <= 7:
        score += 5

    if task["status"] == "Not Started":
        priority = "HIGH PRIORITY"
        score += 10
    elif task["status"] == "In Progress":
        priority = "MEDIUM PRIORITY"
        score += 5
    else:
        priority = "RECOVERY PLAN"
        score += 20

    score += importance

    ranked_tasks.append({
        "name": task["name"],
        "priority": priority,
        "score": score,
        "importance": importance,
        "due_date": task["due_date"],
        "days_until_due": days_until_due
    })

ranked_tasks.sort(key=lambda x: x["score"], reverse=True)

st.subheader("Ranked Tasks")
st.table(ranked_tasks)

st.subheader("Top 3 Focus Plan")
st.table(ranked_tasks[:3])

top_task = ranked_tasks[0]

st.subheader("Today's Focus")

st.success(
    f"Focus on {top_task['name']} first. "
    f"It currently has the highest priority score ({top_task['score']})."
)



st.subheader("Workload Forecast")

if total_hours >= 8:
    st.warning("Heavy week ahead.")
elif total_hours >= 4:
    st.info("Moderate workload.")
else:
    st.success("Light workload.")
    

st.sidebar.title("Navigation")
st.sidebar.write("Dashboard")
st.sidebar.write("Tasks")
st.sidebar.write("Settings")



