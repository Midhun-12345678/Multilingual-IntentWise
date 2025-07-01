import gradio as gr
from app.intent_model import predict_intent
from app.translator import translate_to_english
from app.language_detect import detect_language

def intent_demo(text):
    # Step 1: Detect language
    lang = detect_language(text)

    # Step 2: Translate to English
    translated = translate_to_english(text, lang)

    # Step 3: Predict intent on translated text
    prediction = predict_intent(translated)

    # Step 4: Extract intent and confidence
    if isinstance(prediction, list) and isinstance(prediction[0], dict):
        pred = prediction[0]
        intent = pred['label']
        confidence = f"{float(pred['score']) * 100:.2f} %"
    else:
        intent = str(prediction)
        confidence = "N/A"

    # ✅ Return all 4 outputs in order
    return lang, translated, intent, confidence

# Gradio UI definition
demo = gr.Interface(
    fn=intent_demo,
    inputs=gr.Textbox(lines=3, placeholder="Type any query in any language..."),
    outputs=[
        gr.Textbox(label="Detected Language"),
        gr.Textbox(label="Translated Text"),
        gr.Textbox(label="Predicted Intent"),
        gr.Textbox(label="Confidence Score"),
    ],
    title="🌍 Multilingual Intent Detection",
    description="Test multilingual input to detect intent with real-time language detection and translation."
)

if __name__ == "__main__":
    demo.launch(share=True)
