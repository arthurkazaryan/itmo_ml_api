import pickle
from pathlib import Path
from typing import Tuple

import numpy as np


def load_scalers(folder_path: Path):
    scalers = []
    for scaler_path in folder_path.iterdir():
        scalers.append(pickle.load(open(scaler_path, 'rb')))
    return scalers


def load_label_encoders(folder_path: Path):
    l_encoders = []
    for l_enc_path in folder_path.iterdir():
        l_encoders.append(pickle.load(open(l_enc_path, 'rb')))
    return l_encoders


def preprocess_input(n_days: int, drug: str, age: int, sex: str, ascites: str, hepatomegaly: str, spiders: str,
                     edema: str, bilirubin: float, cholesterol: float, albumin: float, copper: float, alk_phos: float,
                     sgot: float, tryglicerides: float, platelets: float, prothrombin: float, stage: float) -> Tuple[float]:

    n_days = s_n_days.transform([[n_days]])[0][0]
    drug = l_drug.transform([drug])[0]
    age = s_age.transform([[age]])[0][0]
    sex = l_sex.transform([sex])[0]
    ascites = l_ascites.transform([ascites])[0]
    hepatomegaly = l_hepatomegaly.transform([hepatomegaly])[0]
    spiders = l_spiders.transform([spiders])[0]
    edema = l_edema.transform([edema])[0]
    bilirubin = s_bilirubin.transform([[bilirubin]])[0][0]
    cholesterol = s_cholesterol.transform([[cholesterol]])[0][0]
    albumin = s_albumin.transform([[albumin]])[0][0]
    copper = s_copper.transform([[copper]])[0][0]
    alk_phos = s_alk_phos.transform([[alk_phos]])[0][0]
    sgot = s_sgot.transform([[sgot]])[0][0]
    tryglicerides = s_tryglicerides.transform([[tryglicerides]])[0][0]
    platelets = s_platelets.transform([[platelets]])[0][0]
    prothrombin = s_prothrombin.transform([[prothrombin]])[0][0]

    vector = [n_days, drug, age, sex, ascites, hepatomegaly, spiders, edema, bilirubin, cholesterol, albumin, copper,
              alk_phos, sgot, tryglicerides, platelets, prothrombin, stage]
    array = np.expand_dims(vector, axis=0)
    return array


s_age, s_albumin, s_alk_phos, s_bilirubin, s_cholesterol, \
    s_copper, s_n_days, s_platelets, s_prothrombin, s_sgot, s_tryglicerides = load_scalers(Path("celery_app/dump/scaler"))

l_ascites, l_drug, l_edema, l_hepatomegaly, l_sex, l_spiders = load_label_encoders(Path("celery_app/dump/l_encoder"))

