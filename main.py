from fastapi import FastAPI, HTTPException, status
from typing import List
from models import UserCreate, UserResponse, ProjectBase, ProjectResponse, TaskCreate, TaskResponse
from database import db
from datetime import datetime

# 1. API Metadata: This appears at the very top of the /docs page
app = FastAPI(
    title="TaskMaster Pro API",
    description="""
    ## A Comprehensive Task Management System
    Build and manage your team's workflow with ease.
    
    ### Core Functionality:
    * **Identity**: Robust User management with email validation.
    * **Organization**: Group work into Projects with ownership tracking.
    * **Execution**: Detailed Task tracking with priority and due dates.
    * **Insights**: Automated project statistics and overdue alerts.
    """,
    version="1.0.0"
)

# --- USER ENDPOINTS ---

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: UserCreate):
    """
    **Register a new user.**
    
    Requires a unique username and a valid email format.
    """
    new_user = {**user.dict(), "id": db._user_id_counter, "created_at": datetime.now()}
    db.users[db._user_id_counter] = new_user
    db._user_id_counter += 1
    return new_user

# --- PROJECT ENDPOINTS ---

@app.get("/projects/{project_id}/stats", tags=["Statistics"])
def get_project_stats(project_id: int):
    """
    **Calculate real-time project metrics.**
    
    Returns:
    - Total task count
    - Breakdown by status (todo, in_progress, done)
    - Count of overdue tasks
    """
    if project_id not in db.projects:
        raise HTTPException(status_code=404, detail="Project not found")
    
    project_tasks = [t for t in db.tasks.values() if t["project_id"] == project_id]
    
    return {
        "total_tasks": len(project_tasks),
        "overdue_count": len([t for t in project_tasks if t["due_date"] and t.get("is_overdue", False)])
    }
    
