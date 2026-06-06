import csv
print("Move Forward Student Agent")

tasks = []

with open("tasks.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        tasks.append(row)
        
high_priority_count = 0


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
        
    print("-", task["name"], "|", priority, "| Score:", score, "| Due:", task["due_date"])
print("\nSUMMARY")
print(f"You have {high_priority_count} high-priority tasks to complete today.")
print(f"Total tasks loaded: {len(tasks)}")