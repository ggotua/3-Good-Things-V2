# 3 Good Things

A daily reflection app to log 3 achievements per day. Based on the "Three Good Things" positive psychology exercise — a simple practice to build gratitude and focus on daily wins.

## What It Does

- **Register / Log in** — Create an account to track your reflections.
- **Log 3 achievements per day** — Each day, write down 3 good things you accomplished. You can edit today's entry anytime.
- **View the last 7 days** — See a history of your recent reflections to look back on your progress.

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: Svelte 5, Vite, Tailwind CSS

## How to Run Locally

### Prerequisites

- Python 3.8+
- Node.js 18+
- pip

### Setup

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd 3-Good-Things-V2
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Install frontend dependencies and build the Svelte app:

   ```bash
   cd frontend
   npm install
   npm run build
   cd ..
   ```

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser to `http://localhost:5000`.

## Planned / Not Yet Built

- Mood tracking
- Resource recommendations
- Mental health support tools

## License

MIT