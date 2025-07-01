from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

def translate_to_english(text: str, source_lang: str) -> str:
    try:
        return translator(text)[0]['translation_text']
    except:
        return text  # fallback