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

Streamlit Cloud (Easiest)
- **Status**: Completely Free.
- **Pros**: One-click deployment, great for data apps.
- **Cons**: Public by default on the free tier.
- **Setup**: 
    1. Sign in to [share.streamlit.io](https://share.streamlit.io/).
    2. Connect your GitHub.
    3. Select your repo and branch (`main`).
    4. Set **Main file path** to `streamlit_app.py`.
    5. Click **Deploy**.

## Project Structure
- `src/simple_sentiment_analyzer/`: Core logic and analysis engine.
- `static/`: Frontend assets (HTML, CSS, JS).
- `gui_server.py`: Backend Flask application.
- `pyproject.toml`: Modern project configuration.
- `render.yaml`: Deployment configuration for Render.
