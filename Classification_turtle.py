# import os
# import keras 
# from keras.models import load_model
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image 
import tempfile
import base64
import re
import json
import random_responses
import time

#Decoracion de la app
st.set_page_config(page_title="Imagen Classification", 
                   page_icon=":turtle:", 
                   layout="wide",
                   initial_sidebar_state="auto",
                   menu_items=None)

#https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3
markdown = """
Clasificación de imagen de tortuga de estas especies:
- *Gopherus flavomarginatus*
- *Kinosternon flavescens*
- *Terrapene coahuila*
- *Trachemys scripta*

Developed Bruno Rodriguez
"""
st.sidebar.title("INFORMACION \nV.1.0")
st.sidebar.info(markdown)

logo = "./Clicker.jpg"
st.sidebar.image(logo)


st.title("Ask my JORGE")

#Script main chatbot
def load_json(file):
    with open(file) as bot_responses:
        # print(f"Loaded '{file}' succesfully!")
        return json.load(bot_responses)

responses_data = load_json("bot.json")

def get_responses(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []
    
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]
        
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1
        
        if response_score == len(required_words):
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1 
        
        score_list.append(response_score)
        
        
    best_response = max(score_list)
    response_index = score_list.index(best_response)
        
    if input_string == "":
        return "Que quieres saber sobre las tortugas :)"
        
    if best_response != 0:
        return responses_data[response_index]["bot_response"]
        
    return random_responses.random_string()
########

##Clasificacion de imagen
#nombres de las tortugas
turtle_name = ['Ghopherus_flagomagenatus', 'Kinisternon_flavescens', 'Terrapene_coahuila', 'Trachemys_scripta']

#carga del modelo
model = tf.keras.models.load_model('turtle_model_V_1_7.keras')

#######################################
#def classify_images(image_path):
#     input_image = tf.keras.utils.load_img(image_path, target_size= (250, 250))
#     input_image_array = tf.keras.utils.img_to_array(input_image)
#     input_image_exp_dim = tf.expand_dims(input_image_array, 0)

#     prediction = model.predict(input_image_exp_dim)
#     result = tf.nn.softmax(prediction[0])
#     #https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
#     outcome = f"The imagen belog to {turtle_name[np.argmax(result)]} with score {max(result) * 100:.3f}"
#     return outcome
###########################################

def classify_images(image_path):
     input_image = tf.keras.utils.load_img(image_path, target_size= (224, 224))
     input_image_array = tf.keras.utils.img_to_array(input_image)
     input_image_exp_dim = tf.expand_dims(input_image_array, 0)

     prediction = model.predict(input_image_exp_dim)
     result = tf.nn.softmax(prediction[0])
#     # #https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
     # outcome = f"The imagen belog to {turtle_name[np.argmax(result)]} with score {max(result) * 100:.3f}"
     outcome = f"The imagen belog to {turtle_name[np.argmax(result)]}"

#     #Grafico de la distribucion de probabilidades
     class_turtle = ['Gopherus flavomarginatus',
                     'Kinosternon flavescens', 
                     'Terrapene_coahuila', 
                     'Trachemys_scripta']

     fig, ax = plt.subplots()
     y_pos = np.arange(len(class_turtle))
     ax.barh(y_pos, prediction[0], align = 'center')
     ax.set_yticks(y_pos)
     ax.set_yticklabels(class_turtle)
     ax.invert_yaxis()
     ax.set_xlabel("Probality")
     ax.set_title("Turtle Classification")

#     #imprimir la probabilidad de la imagen
     print(outcome)

     return plt.show(fig)

#Carga de la imagen a clasificar
file = st.file_uploader("Porfavor carga una imagen", type = ["jpg","png"])

if file is not None:
    # Create a temporary file to save the uploaded image
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.getbuffer())
        temp_file_path = temp_file.name
    
    image = Image.open(temp_file_path)
    st.image(image, width=200)

    # Classify the image using the temporary file path
    classification_result = classify_images(temp_file_path)
    st.markdown(classification_result)

#auto play de cancion    
#https://discuss.streamlit.io/t/how-to-play-an-audio-file-automatically-generated-using-text-to-speech-in-streamlit/33201/2   
    def autoplay_audio(file_path: str):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                 <audio controls autoplay="true">
                 <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                 </audio>
                 """
            st.markdown(
                  md,
                 unsafe_allow_html=True,
            )

    #st.write("# Auto-playing Audio!")

    autoplay_audio("./Finish.mp3") 
    
#chatbot interface   
# Interfaz de Streamlit
    st.markdown('''### Chatbot de Tortugas 🐢 ''')
    st.markdown('''Ejemplo: 
                    \n- Descripcion de *Gopherus flavomarginatus*
                    \n- Distribucion de *Trachemys scripta*
                ''')
    

    # Caja de texto para entrada del usuario
    user_input = st.text_input("Tú:", "")

    # Mostrar la respuesta del bot
    if user_input:
        bot_response = get_responses(user_input)
        st.text_area("BugNo:", bot_response, height=10, max_chars=None) 
    
else:
    st.text("No has cargado imagen aún!")

# #chatbot interface   
# # Interfaz de Streamlit
# st.markdown('''### Chatbot de Tortugas 🐢 ''')
# st.write("Ejemplo: Distribucion de *Trachemys scripta*")

# # Caja de texto para entrada del usuario
# user_input = st.text_input("Tú:", "")

# # Mostrar la respuesta del bot
# if user_input:
#     bot_response = get_responses(user_input)
#     st.text_area("BugNo:", bot_response, height=10, max_chars=None)
