import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from tensorflow.keras.models import load_model

# loading the saved models

# diabetes_model = pickle.load(open('C:\\Users\\nisha\\OneDrive\\Desktop\\projects\\Multiple diseases\\diabetes.sav','rb'))

heart_disease_model = pickle.load(open('C:\\Users\\nisha\\OneDrive\\Desktop\\projects\\Multiple diseases\\heartdisease.sav','rb'))

# kidney_disease_model = pickle.load(open('C:\\Users\\nisha\\OneDrive\\Desktop\\projects\\Multiple diseases\\kidneydisease.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Chronic Kidney Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')

    def main():
    
    
        st.title('Prediction')
        preg=int(st.text_input("Pregnancies", 6))
        glucose=int(st.text_input("Glucose", 148))
        bp=int(st.text_input("BloodPressure", 72))
        skin=int(st.text_input("SkinThickness",35))
        insulin=int(st.text_input("Insulin",0))
        bmi=float(st.text_input("BMI", 33.6))
        dpf=float(st.text_input("DiabetesPedigreeFunction", 0.627))
        age=int(st.text_input("Age",50))

        if st.button(label="Predict"):
            pred=model.predict([[preg,glucose,bp,skin,insulin,bmi,dpf,age]])
            print(pred[0][0])
            if pred[0][0] > 0.5 :
                st.error("Person is Diabetic")
            else:
                st.success("Person is non-diabetic")
            


    if __name__== "__main__" :
        model= load_model("model.h5")
        main()
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


if (selected == 'Chronic Kidney Disease Prediction'):
    
#     # page title
    st.title('Chronic Kidney Disease Prediction')
    def main():
    
    
        st.title('Prediction')
        sg=float(st.text_input("specific gravity", 1.02))
        al=int(st.text_input("albumin level", 1))
        sc=float(st.text_input("Serum-Creatinine level", 1.2))
        hemo=float(st.text_input("haemoglobin level",15.4))
        pcv=int(st.text_input("packed cell volume",44))
        wc=float(st.text_input("white blood cell count", 7800))
        rc=float(st.text_input("red blood cell count", 5.2))
        htn=int(st.text_input("Does the patient suffer from hyper tension - 1 if yes, 0 if no",-1))

        if st.button(label="Predict"):
            pred=model.predict([[sg, al, sc, hemo, pcv, wc, rc, htn]])
            # print(pred[0][0])
            if pred[0][0] == 1 :
                st.success("Congratulations you are safe from Chronic Kidney Disease!!")
                
            else:
                st.error("I am sorry to inform you, you suffer from chronic Kidney Disease. Please contact your family doctor immediately and acquire some medications. Get well soon!")
                
            


    if __name__== "__main__" :
        model= load_model("ckdmodel.h5")
        main()    