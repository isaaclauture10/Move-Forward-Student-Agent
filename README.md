# Most Valuable Student Agent (MVSA)

## Overview

Most Valuable Student Agent (MVSA) is a productivity assistant built with Python and Streamlit.

The application analyzes tasks based on deadlines, importance, workload, and completion status to help users decide what to focus on next.

MVSA automatically ranks tasks, generates focus recommendations, forecasts workload, and allows users to manage tasks through a simple web interface.

---

## Features

### Task Management

* Add new tasks
* Delete existing tasks
* Store tasks in a CSV database
* Track task status and deadlines

### Priority Engine

* Scores tasks based on urgency
* Scores tasks based on importance
* Detects overdue tasks
* Generates ranked task recommendations

### Productivity Dashboard

* Task count metrics
* Estimated workload hours
* Task ranking table
* Top 3 Focus Plan
* Daily focus recommendation
* Workload forecasting

### Navigation

* Dashboard page
* Tasks page
* About page

---

## Tech Stack

* Python
* Streamlit
* CSV Data Storage

---

## How It Works

MVSA evaluates each task using:

* Due date
* Importance score
* Task status
* Estimated workload

The system generates a priority score and ranks tasks automatically.

Overdue tasks receive additional weighting to encourage recovery planning.

---

## Current MVP Status

### Completed

* Multi-page Streamlit interface
* Task ranking engine
* CSV task storage
* Add task functionality
* Delete task functionality
* Input validation
* Workload forecasting
* Focus recommendations

### Planned Features

* Task editing
* Completion tracking
* User authentication
* Database integration
* AI-powered recommendations
* Calendar integration
* Mobile-friendly interface

---

## Example Use Case

A student enters:

* CIS Assignment
* BUSA Quiz
* Resume Update

MVSA analyzes urgency and importance, then recommends which task should be completed first while generating a Top 3 Focus Plan.

---

## Author

Isaac Lauture

Move Forward.
dictionaries
- Task prioritization using decision logic
- High priority task tracking
- Daily summary generation
- Sample task dataset using CSV
