# Flask Task Manager

A simple task manager built with Flask, allowing users to create and manage tasks with deadlines and dependencies. The project supports hierarchical task visualization and prioritization based on deadlines.

## Features
- Add and delete tasks with descriptions and deadlines
- Support for hierarchical task dependencies (subtasks)
- Display tasks as a list sorted by deadline
- Display tasks as a tree for dependency visualization
- Persistent data storage with SQLite
- Docker support for easy deployment
- Automated testing with GitHub Actions
- Continuous Deployment (CD) via Railway

---

## Technologies Used
- Flask – Web framework for Python
- Flask-SQLAlchemy – ORM for database management
- SQLite – Embedded SQL database for data storage
- Bootstrap – UI styling for a clean interface
- Docker – Containerization for easy deployment
- GitHub Actions – CI/CD automation
- Railway – Hosting and deployment platform

---

## Installation & Running Locally

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python app.py
   ```
5. Open your browser and go to:  
   🔹 http://127.0.0.1:5000/tasks

---

## Deploying with Docker

1. Build the Docker image:
   ```sh
   docker build -t flask-task-manager .
   ```
2. Run the container:
   ```sh
   docker run -p 8080:8080 flask-task-manager
   ```
3. Open in browser:  
   🔹 http://127.0.0.1:8080/tasks

---

## Deployment on Railway (CD)

The project is configured for automatic deployment via GitHub Actions and Railway.

---

## Running Tests
To ensure everything works correctly, you can run automated tests:
```sh
pytest tests/
```
GitHub Actions runs tests automatically on every push.
