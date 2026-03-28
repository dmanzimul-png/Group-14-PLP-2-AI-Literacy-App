# AI Literacy Quiz App
### Group 14 — PLP II

A command-line quiz application that tests users' knowledge of Artificial Intelligence across three topics. Users can register, log in, take quizzes, view their score history, and compete on a leaderboard.

---

## Topics Covered

- What is AI?
- AI Ethics & Responsibility
- AI in Everyday Life

Each topic contains 8 randomly selected and shuffled multiple-choice questions (A–D).

---

## Project Structure

```
Group-14-PLP-II-AI-Literacy-App/
├── Main.py         — Entry point. Wires all modules together and handles menus
├── auth.py         — User registration and login with password hashing
├── Database.py     — SQLite database setup, table creation, and question seeding
├── quiz.py         — Quiz engine, score saving, history, and leaderboard
├── quiz_app.db     — Auto-generated SQLite database (do not commit this)
├── .gitignore      — Excludes generated files from Git
└── README.md       — Project documentation
```

---

## Database Tables

| Table       | Description                                      |
|-------------|--------------------------------------------------|
| `users`     | Stores registered users with hashed passwords   |
| `questions` | Stores all quiz questions seeded at startup      |
| `scores`    | Records every quiz attempt per user              |

---

## Requirements

- Python 3.7 or higher
- No external libraries required — uses Python's built-in `sqlite3`, `hashlib`, `os`, `random`, and `datetime` modules

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Group-14-PLP-II-AI-Literacy-App
   ```

2. Run the app:
   ```bash
   python Main.py
   ```

The database (`quiz_app.db`) is created automatically on first run.

---

## Features

- **Register** — Create an account with a username, email, password, and age group
- **Login** — Secure login with hashed password verification
- **Take a Quiz** — Choose a topic and answer 8 randomised, shuffled questions
- **Score History** — View all your past quiz attempts with scores and dates
- **Leaderboard** — See the top 10 players ranked by their best quiz percentage

---

## Age Groups

When registering, users select one of the following:

1. Under 13
2. 13–17
3. 18–25
4. 26+

---

## How the Quiz Works

1. A topic is selected from the menu
2. 8 questions are randomly pulled from the database for that topic
3. Answer options are shuffled on every attempt so positions change
4. After each answer, feedback and an explanation are shown
5. Final score, percentage, and time taken are displayed at the end
6. Results are saved automatically to the leaderboard

---

## Known Issues

- `quiz_app.db` is generated locally — each team member will have their own copy
- Password hashing uses SHA-256 (functional but not recommended for production — consider upgrading to `bcrypt` or `scrypt`)
- `quiz.py` cursor resources are not explicitly closed after use

---

## .gitignore Recommendation

Add a `.gitignore` file to avoid committing generated or sensitive files:

```
quiz_app.db
__pycache__/
*.pyc
*.pyo
.env
```

---

## Group Members

| Name | Role |
|------|------|
| Joel | auth.py — User Registration & Login |
| Alier | Main.py — Entry Point & Menu Navigation |
| Gibri | Database.py — Database Setup & Question Seeding |
| Elvis | quiz.py — Quiz Engine, Scores & Leaderboard |


