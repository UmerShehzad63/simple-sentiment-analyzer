# Simple Sentiment Analyzer

A premium, modern web-based tool for analyzing the sentiment of any text. Built with precision and a stunning glassmorphism interface.

## Features
- **Real-time Analysis**: Get instant polarity and subjectivity scores.
- **Modern Interface**: Beautiful, responsive design with smooth animations.
- **Powered by NLTK**: Reliable and accurate sentiment analysis core.

## Getting Started

### Prerequisites
- Python 3.9+
- Pip

### Installation
1. Clone this project.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   pip install flask
   ```

### Running the GUI
Start the local server:
```bash
python gui_server.py
```
Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Deployment

### Why not GitHub Pages?
GitHub Pages is designed for **static** websites (pure HTML/CSS/JS). Because this project uses a **Python (Flask)** backend to run the sentiment logic, you need a platform that supports server-side code.

### Recommended: Render.com (Free Tier)
1. Create a free account on [Render.com](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub repository.
4. Render will automatically detect the `render.yaml` or you can use these settings:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt && pip install -e .`
   - **Start Command**: `gunicorn gui_server:app`
5. Click **Deploy**.

## Project Structure
- `src/simple_sentiment_analyzer/`: Core logic and analysis engine.
- `static/`: Frontend assets (HTML, CSS, JS).
- `gui_server.py`: Backend Flask application.
- `pyproject.toml`: Modern project configuration.
- `render.yaml`: Deployment configuration for Render.
