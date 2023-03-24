import streamlit as st
import streamlit.components.v1 as stc
import requests
import json
import pydeck as pdk
import pandas as pd




# Utilisez une chaîne de caractères formatée pour définir le style du cadre et du titre
title_style = "<h1 style='color: #fea347; text-align: center;'>TAXI FARE PREDICTION</h1>"
frame_style = "<div style='background-color: #757474; padding: 20px; border-radius: 30px;'>{}</div>".format(title_style)

# Affichez le titre encadré en utilisant st.markdown()
st.markdown(frame_style, unsafe_allow_html=True)

# Ajoutez du contenu à votre application ci-dessous
# st.write("Bienvenue dans mon application !")
st.write("")
st.write("")


# Créer trois colonnes avec st.columns()
col1, col2, col3 = st.columns(3)

# Ajoutez une cellule d'entrée pour la date dans la première colonne
col1.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Date de départ</h4>"
    f"</div>",
    unsafe_allow_html=True
)
date = col1.date_input("")


# Ajoutez une cellule d'entrée pour l'heure de départ dans la deuxième colonne
col2.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Heure de départ</h4>"
    f"</div>",
    unsafe_allow_html=True
)
time = col2.time_input("")

# Ajoutez une cellule d'entrée pour le nombre de passagers avec une liste déroulante allant de 1 à 8
# passenger_count = col3.selectbox("Nombre de passagers", range(1, 9))
col3.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Nbr passagers</h4>"
    f"</div>",
    unsafe_allow_html=True
)
passenger_count = col3.selectbox("", range(1, 9))


# Créez deux lignes avec deux colonnes chacune
pickup_col1, pickup_col2 = st.columns(2)
dropoff_col1, dropoff_col2 = st.columns(2)

# Ajoutez les cellules d'entrée pour la longitude et la latitude du point de ramassage sur la première ligne
pickup_col1.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Départ : Longitude</h4>"
    f"</div>",
    unsafe_allow_html=True
)
pickup_longitude = pickup_col1.text_input("", key="pickup_longitude")

pickup_col2.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Départ : Latitude</h4>"
    f"</div>",
    unsafe_allow_html=True
)
pickup_latitude = pickup_col2.text_input("", key="pickup_latitude")

# Ajoutez les cellules d'entrée pour la longitude et la latitude de la destination sur la deuxième ligne
dropoff_col1.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Destination : Longitude</h4>"
    f"</div>",
    unsafe_allow_html=True
)
dropoff_longitude = dropoff_col1.text_input("", key="dropoff_longitude")

dropoff_col2.write(
    f"<div style='background-color: #fea347; padding: 0px; border-radius: 15px; text-align: center;'>"
    f"<h4 style='color: white;'>Destination : Latitude</h4>"
    f"</div>",
    unsafe_allow_html=True
)
dropoff_latitude = dropoff_col2.text_input("", key="dropoff_latitude")




# Ajouter un bouton de validation pour appeler l'API
if st.button("Obtenir la prédiction du prix"):

    # Construire un dictionnaire contenant les paramètres de l'API
    params = {
        "pickup_datetime": f"{date} {time}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # URL de l'API
    url = 'https://taxifare.lewagon.ai/predict'

    try:
        # Appeler l'API et récupérer la réponse
        response = requests.get(url, params=params)
        response.raise_for_status()
        prediction = round(response.json()['fare'], 2)
        with st.container():
            st.write(
                f"<div style='background-color: #fea347; padding: 10px; border-radius: 5px; text-align: center;'>"
                f"<h4 style='color: #white;'>Le prix de la course devrait être d'environ : {prediction} $</h4>"
                f"</div>",
                unsafe_allow_html=True
            )

    except requests.exceptions.HTTPError as e:
        st.error(f"Merci de remplir correctement tous les champs")

    except (requests.exceptions.RequestException, json.JSONDecodeError):
        st.error("Une erreur s'est produite lors de la récupération des données de l'API.")


CSS = """
h1 {
    color: red;
}
.stApp {
    background-image: url(https://i.pinimg.com/originals/d1/af/8b/d1af8b50b2d19f24ec34a055048e25ff.jpg);
    background-size: cover;
}
"""

st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
