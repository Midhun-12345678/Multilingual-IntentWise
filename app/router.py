from fastapi import APIRouter
from app.schema import InputText, IntentResponse
from app.language_detect import detect_language 
from app.translator import translate_to_english
from app.intent_model import predict_intent

router = APIRouter()

@router.post("/predict", response_model=IntentResponse)
def predict(input_text: InputText):
    lang = detect_language(input_text.text)
    english_text = translate_to_english(input_text.text, lang)
    intent = predict_intent(english_text)
    return IntentResponse(language=lang, translated_text=english_text, intent=intent)