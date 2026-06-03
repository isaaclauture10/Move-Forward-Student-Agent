print("Move Forward Student Agent")

tasks = [
    {"name": "CIS Assignment", "status": "Not Started"},
    {"name": "BUSA Quiz", "status": "In Progress"},
    {"name": "Resume Update", "status": "Missed"}
]

print("\nTODAY'S TASKS:")

for task in tasks:
    print("-", task["name"], "|", task["status"])