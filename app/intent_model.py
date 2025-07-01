from transformers import pipeline

classifier = pipeline("text-classification", model="joeddav/xlm-roberta-large-xnli")

def predict_intent(text: str) -> str:
    result = classifier(text)[0]
    return result['label']