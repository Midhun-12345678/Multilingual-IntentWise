from pydantic import BaseModel

class InputText(BaseModel):
    text: str

class IntentResponse(BaseModel):
    language: str
    translated_text: str
    intent: str