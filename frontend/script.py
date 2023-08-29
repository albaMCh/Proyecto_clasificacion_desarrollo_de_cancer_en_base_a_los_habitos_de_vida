
import requests
import os
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def classify_person(data):
    """
    Sends a request to the backend with the image data
    to perform a classification on the image.
    """
    # Retrieve the URL of the backend from the environment variables
    #url_backend = os.environ["URL_BACKEND"]

    url_backend = 'https://fastapi-yefgqxi25a-uc.a.run.app/predict'
    
    # Send a GET request to the backend with the image data as a JSON payload
    request = requests.post(url_backend, json=data)
    # Retrieve the predicted probabilities from the response
    answer = request.json()
   
    prob = answer["prediction"]

    #st.info(np.array(prob));
    return np.array(prob)


     

def main():
    st.set_page_config(page_title="Test predicción desarrollo de Cáncer")
    st.title("Test predictivo de desarrollo de cáncer basado en ciertos habitos de vida")

    st.caption("Este tests nos sirve de herramienta para predecir, según los hábitos de vida y ciertos factores médicos la probabilidad de desarrollar cáncer y como cambiando algunos habitos podemos bajar su probabilida")
    st.caption("Rellene todos los campos del test, para ello, debes de seleccionar el valor que mejor se corresponda.")
    st.caption(" Siendo 0: Nada y 8: Bastante")
    st.divider()

    with st.form("mi_formulario", clear_on_submit=True):
        age = st.slider('¿Cuál es su edad?', 0, 99, 25)

        st.divider()
        genre = st.slider(
        "Seleccione su género (1: Hombre, 2: Mujer)", 1, 1, 2)
        st.divider()
        contaminacion = st.slider('¿Cuál es el nivel de contaminación del aire dónde vives?', 0, 8, 4)
        st.divider()
        alcohol= st.slider('¿Cuál es su consumo de alcohol?', 0, 8, 4)
        st.divider()
        alergia_polvo = st.slider(
        "¿Tienes alergía al polvo?", 0, 8, 4)
        st.divider()
        enfermedad_trabajo = st.slider(
        "¿Presentas alguna enfermedad relacionada con su puesto de trabajo?", 0, 8, 4)
        st.divider()

        geneticos = st.slider(
        "¿Existen en su familia antecendentes genéticos de desarrollo de cáncer?",0, 8, 4)
        st.divider()
        enfermedad_cronica = st.slider(
        "¿Padece alguna enfermedad crónica?",0, 8, 4)
        st.divider()
        dieta_equi = st.slider(
        "¿Tienes una dieta equilibrada?",0, 8, 4)
        st.divider()
        obesidad = st.slider(
        "¿Tienes obesidad?", 0, 8, 4)
        st.divider()

        Tabaco= st.slider('¿Fumas?', 0, 8, 4)
        st.divider()
        fumador_pas = st.slider(
        "¿Eres fumador pasivo?",0, 8, 4)
        st.divider()
        dolor_pecho = st.slider(
        "¿Tienes habitualmente dolor de pecho?", 0, 8, 4)
        st.divider()
        coagulacion = st.slider(
        "¿Tienes algun problema de coagulación sanguínea?",0, 8, 4)
        st.divider()
        fatiga = st.slider(
        "¿Tienes fatiga tras realizar cualquier actividad?",0, 8, 4)
        st.divider()

        perdida_peso = st.slider(
        "¿Has perdido peso en los ultimos meses de forma repentina?",0, 8, 4)
        st.divider()
        dicultad_respirar = st.slider(
        "¿Sientes dificultad para respirar?",0, 8, 4)
        st.divider()

        sivilancia = st.slider(
        "¿Tienes sivilancias(ruidos respiratorios) de forma habitual?",0, 8, 4)
        st.divider()
        dificultad_tragar = st.slider(
        "¿Tienes dificultad para tragar?",0, 8, 4)
        st.divider()
        dedos_palillos = st.slider(
        "¿Presentas dedos en forma de palillo de tambor?",0, 8, 4)
        st.divider()

        resfriado = st.slider(
        "¿Te sueles resfriar con frecuencia?",0, 8, 4)
        st.divider()
        tos_seca = st.slider(
        "¿Tienes tos seca?",0, 8, 4)
        st.divider()
        ronca = st.slider(
        "¿Roncas de forma habitual?",0, 8, 4)
        st.divider()

        form = st.form_submit_button("Enviar informacion");

        result = None
        
        if form:
            # Anadir todas las propiedades con su valor correspondiente
            result = classify_person({
                'Age': age,
                'Gender': genre, 
                'Air Pollution': contaminacion, 
                'Alcohol use': alcohol, 
                'Dust Allergy': alergia_polvo, 
                'OccuPational Hazards': enfermedad_trabajo, 
                'Genetic Risk': geneticos, 
                'chronic Lung Disease': enfermedad_cronica, 
                'Balanced Diet': dieta_equi, 
                'Obesity': obesidad, 
                'Smoking': Tabaco, 
                'Passive Smoker': fumador_pas, 
                'Chest Pain': dolor_pecho, 
                'Coughing of Blood': coagulacion, 
                'Fatigue': fatiga, 
                'Weight Loss': perdida_peso, 
                'Shortness of Breath': dicultad_respirar, 
                'Wheezing': sivilancia, 
                'Swallowing Difficulty': dificultad_tragar, 
                'Clubbing of Finger Nails': dedos_palillos, 
                'Frequent Cold': resfriado, 
                'Dry Cough': tos_seca, 
                'Snoring': ronca
            });

        
        if result == 'Low':
            st.success('¡Enhorabuena tu probabilidad de desarrollar cáncer es baja, sigue manteniendo esos habitos de vida saludables!')

        elif result == 'Medium':
            st.warning(' Su probabilidad de desarrollar cáncer es media. Le recomendamos cambiar algunos habitos de vida para poder bajar la probabilidad de desarrollar cáncer. Recuerda: Evitar el consumo excesivo de alcohol y tabaco, llevar una dieta equilibrada, realizar alguna actividad física, e intenta reducir su peso, todos estos consejos pueden ayudarle para ganar calidad de vida'  )


        elif result == 'High':
            st.error('La probabilidad de desarrollar cáncer es alta. Le recomendamos mejorar ciertos hábitos de vida para reducirlo, como por ejemplo reducir el consumo de alcohol y tabaco, realizar ejercicio físico y llevar unos habitos de alimentación saludables, reducir el consumo de ultraprocesados y comida basura, reducir en la medida de lo posible su peso, y si presenta algun problema de salud hablar con su médico')


        if result != None:
            st.info('Como puedes ver en el gráfico se muestran los hábitos que más nos puede afectar a la hora de desarrollar cáncer como son: la obesidad, el tabaco, el ser fumador pasivo, no llevar una dieta equilibrada, el consumo de alcohol, entre otras por lo que recomendamos cambiar si tienes algunos de estos hábitos. Un dato muy significativo es la mayor relevancia que tiene por ejemplo la obesidad frente al tabaco y aunque parezca contradictorio es así, hoy en día y si se mantienen estos hábitos de vida, la obesidad aumenta de manera considerable los casos de cáncer frente al tabaco.')

            df = pd.read_excel('cancer_patient_data_sets.xlsx')
            df.head()
            from sklearn.feature_selection import SelectKBest #Feature Selector
            from sklearn.feature_selection import f_classif #F-ratio statistic for categorical values
            #Feature Selection
            X=df.drop(['Level','Patient Id'], axis=1)
            Y=df['Level']
            bestfeatures = SelectKBest(score_func=f_classif, k='all')
            fit = bestfeatures.fit(X,Y)
            dfscores = pd.DataFrame(fit.scores_)
            dfcolumns = pd.DataFrame(X.columns)
            #concat two dataframes for better visualization
            featureScores = pd.concat([dfcolumns,dfscores],axis=1)
            featureScores.columns = ['Feature','Score']  #naming the dataframe columns

            #Visualize the feature scores
            fig, ax=plt.subplots(figsize=(7,7))
            plot=sns.barplot(data=featureScores, x='Score', y='Feature', palette='viridis',linewidth=0.5, saturation=2, orient='h')
            st.pyplot(fig)




def onClick():
    st.info('Clic recibido');    
  

if __name__ == "__main__":
    main()
