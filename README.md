🚀 Smart Task Analyzer

AI-powered Task Scoring, Prioritization & Strategy Engine
Assignment Submission – Kiran Sanap

📌 Overview

Smart Task Analyzer is an AI-inspired tool that analyzes user tasks and assigns:
✔ Score
✔ Priority (High / Medium / Low)
✔ Explanation
✔ Top 3 Suggested Tasks

Based on:

Importance

Deadlines

Estimated hours

Dependencies

Strategy selected

It includes a Django REST API backend + Animated Premium Frontend UI.

🧩 Tech Stack

🔹 Backend (Django + DRF)

Django 5

Django REST Framework

django-cors-headers

Custom scoring engine

API endpoints for task analysis & suggestions

🔹 Frontend (HTML + CSS + JS)

Animated gradient background

Glassmorphism cards

Poppins font

Smooth fade animations

Responsive layout

Stylish interactive UI

🎨 Frontend Features

Add tasks dynamically

Auto validation

Beautiful UI transitions

Animated buttons

Real-time display of results

Top 3 recommendations

Modern UX with glass effect

⚙️ Backend API Endpoints

🔥 POST /api/tasks/analyze/

Analyzes all tasks & returns detailed priority info.

Request:

{
"tasks": [...],
"strategy": "smart_balance"
}

Response:

{
"results": [
{
"title": "Complete Assignment",
"score": 46,
"priority": "High",
"explanation": "Due in 1 day..."
}
]
}

⭐ POST /api/tasks/suggest/

Returns top 3 tasks sorted by selected strategy.

Request:

{
"tasks": [...],
"strategy": "fastest_wins"
}

📁 Project Structure

project/
│
├── backend/
│ ├── manage.py
│ ├── task_analyzer/
│ └── tasks/
│
└── frontend/
├── index.html
├── styles.css
└── script.js

🛠 Installation Guide

⬛ Backend Setup

cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend runs at:
👉 http://127.0.0.1:8000/

🟦 Frontend Setup

cd frontend
python -m http.server 5500

Frontend runs at:
👉 http://localhost:5500/

📸 Screenshots to Include in Submission

You should provide:

✔ Frontend UI Home
✔ Add Task Screenshot
✔ Analyze Result Screenshot
✔ Top 3 Screenshot
✔ Backend runserver screenshot
✔ Folder structure screenshot

🏁 Conclusion

This assignment demonstrates:

API development

Custom scoring algorithm

Beautiful UI design

Frontend–Backend integration

CORS handling

Priority logic

Real-time task rendering

Submitted by:
🧑‍💻 Pratik Gobade
📅 2025
