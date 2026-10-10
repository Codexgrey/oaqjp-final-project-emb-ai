import requests, json

def emotion_detector(text_to_analyze):
    ''' funtion to analyze text using ibm's Watson AI and its NLP capabilities
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)
    
    # prepare output dict - formatting response with json, then extracting
    if response.status_code == 200:
        # parse API response
        res = json.loads(response.text)
        anger_score = res["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = res["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = res["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = res["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = res["emotionPredictions"][0]["emotion"]["sadness"]
    
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
    
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None


    # score dictionary
    scores = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score
    }
    
    # get name of dominant emotion
    dominant = max(scores, key=scores.get)

    # return output dict
    return {**scores, 'dominant_emotion' : dominant }
