import streamlit as st
import csv
from datetime import datetime

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Tasks", "About"]
)

tasks = []

with open("tasks.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)

total_hours = 0

for task in tasks:
    total_hours += int(task["estimated_hours"])

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

if page == "Dashboard":

    st.title("Most Valuable Agent")

    st.subheader("AI Productivity Assistant")

    st.write(
        "MVSA analyzes deadlines, importance, workload, and task status "
        "to recommend what you should focus on next."
    )

    st.metric("Tasks Loaded", len(tasks))
    st.metric("Estimated Hours", total_hours)

    st.subheader("Task Hours Chart")

    chart_data = {}

    for task in tasks:
        chart_data[task["name"]] = int(task["estimated_hours"])

    st.bar_chart(chart_data)

    st.subheader("Ranked Tasks")
    st.table(ranked_tasks)

    st.subheader("Top 3 Focus Plan")
    st.table(ranked_tasks[:3])

    if len(ranked_tasks) > 0:
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

elif page == "Tasks":

    st.title("Tasks")

    st.subheader("Task List")
    st.table(tasks)

    st.subheader("Delete Task")

    task_to_delete = st.selectbox(
        "Select a task to delete",
        [task["name"] for task in tasks]
    )
    if st.button("Delete Task"):
       updated_tasks = []

       for task in tasks:
        if task["name"] != task_to_delete:
            updated_tasks.append(task)

       with open("tasks.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "status", "due_date", "estimated_hours", "importance"]
        )

        writer.writeheader()
        writer.writerows(updated_tasks)

        st.success("Task deleted! Refresh the page to see it.")




    st.subheader("Add New Task")

    task_name = st.text_input("Task Name")

    hours = st.number_input(
        "Estimated Hours",
        min_value=1,
        max_value=40,
        value=1
    )

    importance = st.slider(
        "Importance",
        min_value=1,
        max_value=10,
        value=5
    )

    due_date = st.date_input("Due Date")

    if st.button("Add Task"):

        if task_name.strip() == "":
            st.error("Please enter a task name.")

        else:
            with open("tasks.csv", "a", newline="") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["name", "status", "due_date", "estimated_hours", "importance"]
                )

                writer.writerow({
                    "name": task_name,
                    "status": "Not Started",
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "estimated_hours": hours,
                    "importance": importance
                })

            st.success("Task added! Refresh the page to see it.")

elif page == "About":

    st.title("About MVSA")

    st.write(
        "MVSA is a productivity assistant that analyzes tasks, deadlines, "
        "importance, workload, and status to recommend what to focus on first."
    )

    st.subheader("Current Features")

    st.write("- Reads tasks from CSV")
    st.write("- Scores tasks by urgency and importance")
    st.write("- Ranks tasks automatically")
    st.write("- Generates a Top 3 Focus Plan")
    st.write("- Forecasts workload")
    st.write("- Adds new tasks from the app")