import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models


heart_disease_model = pickle.load(open('C:/Users/Shree/OneDrive/Desktop/mini project/mini project/heart_disease_model.sav','rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction'
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Male/Female')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease \n1. Follow Medical Advice: Medications: Take prescribed medications exactly as directed. Do not skip doses or stop taking medication without consulting your doctor. Regular Check-ups: Keep all scheduled appointments with your healthcare provider for ongoing assessment and management. \n2. Healthy Diet: Balanced Diet: Consume a heart-healthy diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats (such as those from fish, nuts, and olive oil). Limit Sodium: Reduce sodium intake to help manage blood pressure. Avoid Trans Fats and Saturated Fats: Minimize the intake of foods high in unhealthy fats, such as fried foods and processed snacks. Monitor Portion Sizes: Be mindful of portion sizes to maintain a healthy weight. \n3. Exercise Regularly: Moderate Physical Activity: Aim for at least 150 minutes of moderate-intensity aerobic activity each week, such as walking, swimming, or cycling. Strength Training: Incorporate strength training exercises at least two days a week. Consult Your Doctor: Before starting any new exercise regimen, discuss it with your healthcare provider to ensure it iss safe for you. \n4. Quit Smoking: Smoking Cessation: Seek support to quit smoking, as it significantly reduces the risk of heart disease complications. Avoid Secondhand Smoke: Stay away from environments where you might be exposed to secondhand smoke. \n5. Limit Alcohol: Moderate Consumption: If you drink alcohol, do so in moderation. This typically means up to one drink per day for women and up to two drinks per day for men. \n6. Manage Stress: Stress Reduction Techniques: Practice stress-reducing activities such as meditation, yoga, deep breathing exercises, or hobbies you enjoy. Adequate Sleep: Ensure you get 7-9 hours of quality sleep each night.'
        else:
          heart_diagnosis = 'The person does not have any heart disease \n1. Eat a Balanced Diet: Fruits and Vegetables: Aim for at least five servings per day. Whole Grains: Choose whole grains over refined grains. Lean Proteins: Include sources like fish, poultry, beans, and nuts. Healthy Fats: Use olive oil, avocados, and nuts, and limit saturated and trans fats. Limit Salt and Sugar: Reduce intake of added sugars and salt to maintain healthy blood pressure and glucose levels. \n2. Aerobic Exercise: Engage in at least 150 minutes of moderate-intensity or 75 minutes of high-intensity aerobic activity per week (e.g., brisk walking, running, cycling). Strength Training: Include muscle-strengthening activities at least two days a week. Stay Active: Reduce sedentary behavior by incorporating more physical activity into daily routines, such as taking the stairs instead of the elevator. \n3. Achieve and maintain a healthy weight through a combination of diet and exercise to reduce the risk of heart disease. Don’t Smoke and Avoid Secondhand Smoke: \n4. Quitting smoking greatly reduces the risk of heart disease, and avoiding secondhand smoke is also important. Limit Alcohol Intake: \n5. Drink alcohol in moderation, if at all. This generally means up to one drink per day for women and up to two drinks per day for men.'
        
    st.success(heart_diagnosis)
        
    
    




