import csv
print("Move Forward Student Agent")

tasks = []

with open("tasks.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)
        
high_priority_count = 0
ranked_tasks = []
total_hours = 0

print("\nTODAY'S TASKS:")

for task in tasks:

    score = 0
    total_hours += int(task["estimated_hours"])

    if task["status"] == "Not Started":
        priority = "HIGH PRIORITY"
        score += 10
        high_priority_count += 1

    elif task["status"] == "In Progress":
        priority = "MEDIUM PRIORITY"
        score += 5

    else:
        priority = "RECOVERY PLAN"
        score += 20
      
    ranked_tasks.append({
    "name": task["name"],
    "priority": priority,
    "score": score,
    "due_date": task["due_date"]
    })

    print("-", task["name"], "|", priority, "| Score:", score, "| Due:", task["due_date"])
    for task in tasks:
    # scoring logic
    # ranked_tasks.append(...)
     print(...)

ranked_tasks.sort(key=lambda x: x["score"], reverse=True)

print("\nRANKED TASKS")

for task in ranked_tasks:
    print("-", task["name"], "|", task["priority"], "| Score:", task["score"], "| Due:", task["due_date"])
print("\nTOP 3 FOCUS PLAN")

for task in ranked_tasks[:3]:
    print("-", task["name"], "|", task["priority"], "| Score:", task["score"])
print("\nDAILY WORKLOAD")

if high_priority_count >= 2:
    print("Heavy workload today. Focus on urgent tasks first.")
elif high_priority_count == 1:
    print("Moderate workload today. Stay consistent.")
else:
    print("Light workload today. Good time for planning.")
print("\nSUMMARY")
print(f"You have {high_priority_count} high-priority tasks to complete today.")
print(f"Total tasks loaded: {len(tasks)}")
print(f"Total estimated hours: {total_hours}")
print("\nWORKLOAD FORECAST")

if total_hours >= 8:
    print("Heavy week ahead.")
elif total_hours >= 4:
    print("Moderate workload.")
else:
    print("Light workload.")
    