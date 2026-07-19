# Imaginary Love Story Generator 💌

A fun, interactive, and beautiful choose-your-own-adventure Streamlit web app that generates a funny, stage-by-stage romantic comedy story featuring you and your crush!

## Features
- **Adventure Choices**: 6 multiple-choice questions to shape the narrative.
- **Stage-by-Stage Reveal**: Reveals the story dynamically building suspense.
- **Cheesy & Playful Writing**: Randomized story templates so repeat attempts feel fresh.
- **Compatibility Score**: Calculates a random rating (70-99%) with a personalized message.
- **Data Logging**: Securely logs submissions to a local SQLite database (`love_stories.db`).
- **Premium Aesthetics**: Soft pink-to-purple gradient, glassmorphic layout, and custom typography.

## Project Structure
- `app.py`: Core Streamlit UI, form logic, session state control, and styling.
- `story_generator.py`: Contains story templates and randomization logic.
- `database.py`: Simple SQLite logging wrapper ensuring failures never crash the app.
- `requirements.txt`: Python package dependencies.
- `README.md`: Setup and deployment instructions.

## Local Setup & Run

1. Navigate to the project directory:
   ```bash
   cd C:\Users\VICTUS\.gemini\antigravity\scratch\imaginary_love_story_generator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   streamlit run app.py
   ```

5. Access the app in your browser at `http://localhost:8501`.

## Deployment to Streamlit Community Cloud

Streamlit Community Cloud is a free platform to deploy your applications.

1. **Prepare your GitHub Repository**:
   - Push your code files (`app.py`, `story_generator.py`, `database.py`, and `requirements.txt`) to a public GitHub repository.
   - *Note*: You can exclude or add `love_stories.db` to `.gitignore` to prevent committing your local logs to public GitHub.

2. **Deploy on Streamlit**:
   - Log in to [Streamlit Share](https://share.streamlit.io/).
   - Click **New app**.
   - Select your repository, branch, and specify the main path: `app.py`.
   - Click **Deploy**.

3. **Database Notes**:
   - The app logs submissions to a local SQLite database (`love_stories.db`). On Streamlit Community Cloud, changes to local files are ephemeral (they reset whenever the server restarts or wakes up from sleep).
   - If you require persistent data storage in the cloud, you can connect the app to a persistent database (like PostgreSQL, Supabase, or Google Sheets) using Streamlit's secrets management.
