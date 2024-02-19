import pandas as pd
import streamlit as st

st.markdown("# :card_index_dividers: Data")
#st.title("Data")
st.write(" ")

st.markdown("""<div style="text-align: center;">
<h3><u>Dataset's Description📜</u></h3>
</div>"""
, unsafe_allow_html=True) 

st.markdown("""<div style="text-align: justify;">

 1. **Age** (*age*): Age of the patient at the time of health checkup 
 2. **Sex** (*sex*): 0 = Female and 1 = Male
 3. **Chest Pain** (*cp*): 1 = Typical angina, 2 = Atypical angina, 3 = Non-anginal pain, 4 = Asymptotic
 4. **Resting Blood Pressure** (*trtbps*): Resting blood pressure value of patient in mmHg (unit) 
 5. **Cholesterol** (*chol*): Cholesterol of patient in mg/dl (unit)
 6. **Fasting Blood Sugar** (*fbs*): 1 = if fbs >120 mg/dl (true), else 0 = if not that (false)
 7. **Resting ECG** (*restecg*): 0 = Normal, 1 = Having ST-T wave abnormality, 2 = Left ventricular hypertrophy
 8. **Max Heart Rate** (*thalachh*): Maximum heart rate achieved by any patient
 9. **Exercise induced angina** (*exng*): 0 = No and 1 = Yes
 10. **oldpeak**: Displays the value of ST depression of any patient induced by exercise with respect to rest (float values) 
 11. **slp**: Describes the peak of exercise during ST segment, 0 = up-slope, 1 = flat, 2 = down-slope
 12. **Number of major vessels** (*caa*): Classified in range 0 to 4 by coloring through fluoroscopy
 13. **Thalassemia** (*thall*): 1 = Normal, 2 = Fixed defect, 3 = Reversible defect
 14. **target**: It's the prediction column for diagnosis of heart attacks. Here, 0 = no possibility of heart attack and 1 = possibilities of heart attack
</div>""", unsafe_allow_html=True)

st.markdown("""<div style="text-align: center;">
<h3><u>Dataset🗂️</u></h3>
</div>"""
, unsafe_allow_html=True) 

st.markdown("""<div style="text-align: center;">
<i>The Data set used for the 
<b>Prediction of Heart Disease Using Machine Learning</b> 
Project</i>
</div>"""
, unsafe_allow_html=True) 

df = pd.read_csv("heart.csv")

df_styled = df.style.apply(lambda x: ['background: #F0F2F6' for i in range(len(x))])

#st.table(df.style.highlight_max(axis=0))

st.table(df_styled)

