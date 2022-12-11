import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def Decider(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    excel = pd.read_excel(r'C:\Users\elifc\Desktop\AgreGood_API-main\AgreGood_API-main\crop.xlsx', header=0)
    print(excel)
    print(excel.shape)

    le = preprocessing.LabelEncoder()
    crop = le.fit_transform(list(excel["CROP"]))

    NITROGEN = list(excel["NITROGEN"])
    PHOSPHORUS = list(excel["PHOSPHORUS"])
    POTASSIUM = list(excel["POTASSIUM"])
    TEMPERATURE = list(excel["TEMPERATURE"])
    HUMIDITY = list(excel["HUMIDITY"])
    PH = list(excel["PH"])
    RAINFALL = list(excel["RAINFALL"])

    features = list(zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))
    features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,RAINFALL])

    features = features.transpose()
    print(features.shape)
    print(crop.shape)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(features,crop)
    plt.model()
    nitrogen_content = nitrogen
    phosphorus_content = phosphorus
    potassium_content = potassium
    temperature_content = temperature
    humidity_content = humidity
    ph_content = ph
    rainfall_content = rainfall

    predict1 = np.array([nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,rainfall_content])
    predict1 - predict1.reshape(1, -1)

    predict1 = model.predict([predict1])

    crop_name = str()
    if predict1 == 0:
        crop_name = 'Apple'
    elif predict1 == 1:
        crop_name = 'Banana'
    elif predict1 == 2:
        crop_name = 'Blackgram'
    elif predict1 == 3:
        crop_name = 'Chickpea'
    elif predict1 == 4:
        crop_name = 'Coconut'
    elif predict1 == 5:
        crop_name = 'Coffee'
    elif predict1 == 6:
        crop_name = 'Cotton'
    elif predict1 == 7:
        crop_name = 'Grapes'
    elif predict1 == 8:
        crop_name = 'Jute'
    elif predict1 == 9:
        crop_name = 'Kidneybeans'
    elif predict1 == 10:
        crop_name = 'Lentil'
    elif predict1 == 11:
        crop_name = 'Maize'
    elif predict1 == 12:
        crop_name = 'Mango'
    elif predict1 == 13:
        crop_name = 'Mothbeans'
    elif predict1 == 14:
        crop_name = 'Mungbeans'
    elif predict1 == 15:
        crop_name = 'Muskmelon'
    elif predict1 == 16:
        crop_name = 'Orange'
    elif predict1 == 17:
        crop_name = 'Papaya'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas'
    elif predict1 == 19:
        crop_name = 'Pomegranate'
    elif predict1 == 20:
        crop_name = 'Rice'
    elif predict1 == 21:
        crop_name = 'Watermelon'

    return crop_name