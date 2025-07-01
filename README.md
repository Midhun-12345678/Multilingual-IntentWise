# 🌍 IntentWise: Multilingual Intent Detection API

**IntentWise** is a fast, scalable, and intelligent multilingual intent detection API powered by FastAPI and Hugging Face transformers. This app detects the language of any input text, translates it to English, and predicts the intent in real-time using a robust transformer model. It also comes with a modern Gradio-based demo UI for quick interaction and testing.

---

# Project Structure

```
MULTILINGUAL_INTENT_APP/
├── app/
│   ├── main.py             # FastAPI entry
│   ├── router.py           # API routing
│   ├── intent_model.py     # Intent prediction logic
│   ├── language_detect.py  # Language detection util
│   ├── translator.py       # Translation logic
├── gradio_app.py           # Gradio demo UI
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

##  Run Locally

```bash
# Clone the repository
git clone https://github.com/Midhun-12345678/Multilingual-IntentWise.git
cd Multilingual-IntentWise

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload --port 8000

# Optionally run Gradio demo
python gradio_app.py
```


---

##License

MIT License. Use it freely, but give credit if you build on top of it 
