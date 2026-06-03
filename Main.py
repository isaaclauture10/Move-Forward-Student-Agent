print("Move Forward Student Agent")

tasks = [
    {"name": "CIS Assignment", "status": "Not Started"},
    {"name": "BUSA Quiz", "status": "In Progress"},
    {"name": "Resume Update", "status": "Missed"}
]
high_priority_count = 0

print("\nTODAY'S TASKS:")

for task in tasks:

    if task["status"] == "Not Started":
        priority = "HIGH PRIORITY"
        high_priority_count += 1

    elif task["status"] == "In Progress":
        priority = "MEDIUM PRIORITY"

    else:
        priority = "RECOVERY PLAN"

    print("-", task["name"], "|", priority)

print(f"\nYou have {high_priority_count} high-priority tasks to complete today.")