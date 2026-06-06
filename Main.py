import csv
print("Move Forward Student Agent")

tasks = []

with open("tasks.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)
        
high_priority_count = 0
ranked_tasks = []

print("\nTODAY'S TASKS:")

for task in tasks:

    score = 0

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

print("\nSUMMARY")
print(f"You have {high_priority_count} high-priority tasks to complete today.")
print(f"Total tasks loaded: {len(tasks)}")