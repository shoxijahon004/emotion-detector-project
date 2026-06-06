import requests
import json

def emotion_detector(text_to_analyze):
    # Rasmiy va to'g'ri URL manzil
    url = 'https://github.com/shoxijahon004/emotion-detector-project'
    
    # API sarlavhasi
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Yuboriladigan ma'lumot
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # API'ga so'rov yuborish
    response = requests.post(url, json=myobj, headers=headers)
    
    # Javob muvaffaqiyatli kelganda (Status 200)
    if response.status_code == 200:
        # Natijani JSON formatga o'tkazish
        formatted_response = json.loads(response.text)
        
        # Emotsiyalarni ajratib olish (Haqiqiy kalit so'zlar)
        emotion_predictions = formatted_response['emotion_predictions'][0]['emotion']
        anger_score = emotion_predictions['anger']
        disgust_score = emotion_predictions['disgust']
        fear_score = emotion_predictions['fear']
        joy_score = emotion_predictions['joy']
        sadness_score = emotion_predictions['sadness']
        
        # Eng yuqori balli emotsiyani aniqlash
        emotions_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions_dict, key=emotions_dict.get)
        
        # Yakuniy javob formati
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return result
    else:
        return None
