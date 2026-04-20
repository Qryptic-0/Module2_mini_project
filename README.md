# Module2_mini_project
**TASK FLOW MANAGEMENT API DOCUMENTATION**


**TaskFlow Management API**
***A Robust Backend System for Team Productivity***
*Project Overview*
In modern development environments, task fragmentation is a major bottleneck. TaskFlow is a RESTful API designed to bridge the gap between high-level project management and granular task execution. By providing a centralized source of truth, it ensures that users, projects, and deadlines are always in sync.
*Tech Stack*
1. Framework: FastAPI (High performance, Python 3.9+)
2. Data Validation: Pydantic (Schema enforcement & Data integrity)
3. Standard: OpenAPI 3.1.0 / JSON Schema
4. Server: Uvicorn (ASGI server for high-speed delivery)
*Core Features*
1. User Management: Create and retrieve team members with unique identity validation.
2. Project Organization: Group tasks under specific projects with ownership tracking.
3. Task Lifecycle Tracking: Full CRUD operations for tasks, including status transitions (todo → in_progress → done).
4. Intelligent Statistics: Automated calculation of project health, including task counts by status and overdue task detection.
5. Data Guardrails: Strict length requirements for strings and range-bound priority levels.
   
**This project is built with a "Documentation First" approach. By leveraging FastAPI’s native integration with the OpenAPI (Swagger) standard, the API is designed to be self-documenting and strictly validated.**
*Interactive Documentation (Swagger UI)*
Although the environment is currently staged for deployment, the API is configured to automatically generate an interactive playground at /docs.
*Automatic Schema Generation*: Every Pydantic model in models.py translates into a JSON Schema that defines exactly what data the API expects.
*Visual Endpoints*: The documentation categorizes actions (Users, Projects, Tasks) and provides "Try it out" functionality to test logic without external tools like Postman.

Example Validation Flow:
Request: A user tries to create a task with a priority of 10.
Process: The TaskCreate Pydantic model intercepts the request.
Validation: The ge=1, le=5 constraint fails.
Response: The API automatically returns a 422 Unprocessable Entity status code with a clear JSON error message explaining that the priority is out of range.


Data Integrity & Validation
To ensure the system is "crash-proof," I implemented multi-layered validation using Pydantic:
a. Type Safety: Ensures IDs are integers, names are strings, and dates follow the ISO 8601 format.
b.Constraint Validation: 
i. Usernames must be between 3-50 characters.
ii. Task priorities are strictly locked between 1 and 5.
iii. Status updates only accept specific values (todo, in_progress, done) via Python Enums.
c. Custom Logic: I included a custom validator to ensure that due_date cannot be set in the past, preventing logical errors in task scheduling.


⚙️ Installation & Setup
To run this project locally, follow these steps:
**1. Install Dependencies:**
     pip install fastapi uvicorn pydantic[email]

**2. Launch the Server:**
     uvicorn main:app --reload

**3. Access the API:**
    The server will start at http://127.0.0.1:8000.


**Testing the API**

To test this API, I have implemented full OpenAPI documentation. run the server and navigate to/docs to interact with all the endpoints, see data schemas and verify validation rules

-*To test the API logic without external tools:*
1. Navigate to http://127.0.0.1:8000/docs.
2. Locate the endpoint you wish to test.
3. Click "Try it out", fill in the parameters, and click "Execute".
4. Observe the Response Body and Status Code to verify successful execution or validation errors.

***Project Structure***
📂 mini-project-2/
├── main.py          # Entry point & API endpoints
├── models.py        # Pydantic schemas & Enums
├── database.py      # In-memory storage logic
├── requirements.txt # Dependency list
└── README.md        # Project documentation


