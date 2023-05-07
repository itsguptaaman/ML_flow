import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")

scaler = pickle.load(open("pickle_files\scaler.pkl", "rb"))
LR_cls = pickle.load(open("pickle_files\LR_cls.pkl", "rb"))

form = st.form(key='my_form')
age = form.number_input('Enter your Age')
sex = form.number_input('Enter your Sex')
cp = form.number_input('Enter your cp')
trestbps = form.number_input('Enter your trestbps')
chol = form.number_input('Enter your chol')
fbs = form.number_input('Enter your fbs')
restecg = form.number_input('Enter your restecg')
thalach = form.number_input('Enter your thalach')
exang = form.number_input('Enter your exang')
oldpeak = form.number_input('Enter your oldpeak')
slope = form.number_input('Enter your slope')
ca = form.number_input('Enter your ca')
thal = form.number_input('Enter your thal')
submit_button = form.form_submit_button(label='Submit')



record = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
data = scaler.transform([record])
if all(i == 0 for i in record):
    result = None
else:
    result = LR_cls.predict(data)
    print(result)

if result == 0:
    st.write("Negative!!! you dont have heart deases!!!")
elif result == 1:
    st.write("You detected Positive! Please go to a Doctor and do a proper Checkup!!!")
else:
    st.write("Lets Start the prediction")