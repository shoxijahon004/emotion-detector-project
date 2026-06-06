import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP API manzili (To'liq ko'rinishi)
    url = 'https://skills.network'
    
    # API uchun sarlavha
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Yuboriladigan matn ma'lumoti
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # API'ga so'rov yuborish
    response = requests.post(url, json=myobj, headers=headers)
    
    # Agar so'rov muvaffaqiyatli bo'lsa, natijani qaytarish
    if response.status_code == 200:
        return response.text
    else:
        return None
