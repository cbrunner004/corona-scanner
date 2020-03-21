import json 

# Dummy 
# json = get_json()

# CONSTANTS
QUESTION_1 = 'age'
QUESTION_2 = 'symptoms'
QUESTION_3 = 'pre_existing_illness'
QUESTION_4 = 'question_4'
QUESTION_5 = 'question_5'

SORE_THROAT = 'sore_throat'
SNIFFLES = 'sniffles'
FEVER_SMALL = 'small fever'
FEVER_MEDIUM = 'medium fever'
FEVER_LARGE = 'large fever'
SHORT_BREATH = 'short breath'
DYSPNOEA = 'dyspnoea'

CARDIOVASCULAR_DISEASE = 'cardiovascular disease'
DIABETES = 'diabetes'
RESPIRATORY_DISEASES = 'respiratory diseases'
HIGH_BLOOD_PRESSURE = 'high blood pressure'
CANCER = 'cancer'

def get_score_from_age(age: int) -> float:
    age_score_dict = {
        range(80, 120): 14.8,
        range(70, 79): 8,
        range(60, 69): 3.6,
        range(50, 59): 1.3,
        range(40, 49): 0.4,
        range(00, 39): 0.2,
    }

    for key, value in age_score_dict.items():
        if age in key:
            return value


def get_score_from_symptoms(symptoms: list) -> float:
    symptoms_dict = {
        SORE_THROAT: 0.5,
        SNIFFLES: 0.5,
        FEVER_SMALL: 0.5,
        FEVER_MEDIUM: 1,
        FEVER_LARGE: 1.5,
        SHORT_BREATH: 1,
        DYSPNOEA: 1.5
    }
    
    score = 0
    for symptom in symptoms:
        try:
            score += symptoms_dict[symptom]
        except KeyError:
            pass
    
    return score
    

def get_score_from_previous_diseases(previous_diseases: list) -> float:
    previous_disease_dict = {
        CARDIOVASCULAR_DISEASE: 10.5,
        DIABETES: 7.3,
        RESPIRATORY_DISEASES: 6.3,
        HIGH_BLOOD_PRESSURE: 6,
        CANCER: 5.6,
    }
    
    score = 0
    for previous_disease in previous_diseases:
        try:
            score += previous_disease_dict[previous_disease]
        except KeyError:
            pass
    
    return score


print(get_score_from_age(43))
print(get_score_from_symptoms([FEVER_LARGE, SORE_THROAT]))
print(get_score_from_previous_diseases([CARDIOVASCULAR_DISEASE, CANCER]))


