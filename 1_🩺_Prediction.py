import streamlit as st
import pandas as pd
import joblib




df = pd.read_csv('heart.csv')

st.set_page_config(
  page_title="Prediction of Heart Disease",
  page_icon="♥️",
)


st.markdown("# :stethoscope: Prediction of Heart Disease :bar_chart:")
#st.title("Prediction of Heart Disease using Machine Learning")
st.markdown("""<div style="text-align: center;">
<h6><i>This project predicts the heart disease of an individual using machine learning.
</i></h6></div>""", unsafe_allow_html=True)

st.write(" ")
#st.image('image.png', width=None)
st.video('mainpageheart.mp4', format="video/mp4")
#col1, col2, col3 = st.columns(3)

#with col2:
    #st.image("image.png")

st.header(' ')
st.markdown("""<div style="text-align: center;">
<h2>Enter the Data</h2></div>""", unsafe_allow_html=True) 


x = df.drop(['target'], axis=1)
y = df['target']


sex_dictionary = {'Male':1, 'Female':0}
fasting_dictionary = {'true':1, 'false':0}
ex_dict = {'yes':1, 'no':0}

#st.write("Refer here to know more about the data: [Link](http://localhost:8501/Data)")

def user_report():
  age = st.slider('Age', 25,95, 30)
  #st.write('You selected:', age)
  #sex = st.slider('Sex (Male=1, Female=0)', 0, 1, 0 )
  #sex = st.selectbox('Sex (Male=1, Female=0)', (1, 0))
  sex = st.radio('Sex (Male=1, Female=0)', [0,1])
  #st.write('You Selected:', sex)
  #cp = st.slider('Chest Pain Type (4 values)', 0,3, 1 )
  c1, c2 = st.columns(2)
  cp = c1.selectbox('Chest Pain Type (4 values)', (0,1,2,3))
  #cp = st.selectbox('Chest Pain Type (4 values)', (0,1,2,3))
  trtbps = st.slider('Resting Blood Pressure (in mmHg units on admission to the hospital)', 94,200, 120 )
  chol = st.slider('Serum Cholesterol in mg/dl',126, 564, 200)
  #fbs = st.slider('fasting blood sugar &gt; 120 mg/dl (True = 1, False=0)', 0,1 ,0)
  fbs = st.radio('Fasting Blood Sugar &gt; 120 mg/dl (True = 1, False=0)', [0,1])
  #st.write('You Selected:',fbs)
  r1, r2 = st.columns(2)
  restecg = r1.selectbox('Resting Electrocardiographic Results (values= 0,1,2)', (0,1,2) )
  #restecg = st.selectbox('Resting Electrocardiographic Results (values= 0,1,2)', (0,1,2) )
  thalachh = st.slider('Maximum Heart Rate achieved (bpm)', 71,202, 110)
  exng = st.radio('Exercise induced angina (Yes=1, No=0)', [0,1] )
  oldpeak = st.slider('Oldpeak = ST depression induced by exercise relative to rest', 0.0,6.0, 2.0 )
  s1, s2 = st.columns(2)
  slp = s1.selectbox('The slope of the peak exercise ST segment', (0,1,2))
  #slp = st.selectbox('The slope of the peak exercise ST segment', (0,1,2))
  caa = st.slider('Number of major vessels colored by flourosopy', 0, 4, 0)
  t1, t2 = st.columns(2)
  thall = t1.selectbox('Thal: 1 = Normal; 2 = Fixed defect; 3 = Reversable defect', (0,1,2,3))
  #thall = st.selectbox('Thal: 3 = normal; 6 = fixed defect; 7 = reversable defect', (0,1,2,3))



  user_report_data = {
	  'age': age,
	  'sex': sex,
	  'cp': cp,
	  'trtbps': trtbps,
	  'chol': chol,
	  'fbs': fbs,
	  'restecg': restecg,
	  'thalachh': thalachh,
	  'exng': exng,
	  'oldpeak': oldpeak,
	  'slp': slp,
	  'caa': caa,
	  'thall': thall
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data





user_data = user_report()
st.subheader(' ')
st.markdown("""<div style="text-align: center;">
    <h2>Data Entered</h2></div>""", unsafe_allow_html=True)
st.table(user_data)

#kn = LogisticRegression()
#kn.fit(x, y)
#user_result = kn.predict(user_data)

loaded_model = joblib.load("model.pkl")
user_result = loaded_model.predict(user_data)





# OUTPUT
st.write(' ')
output=''

if st.button(label="Predict"):
    st.markdown("""<div><h2>Your Report:</h2></div>""", unsafe_allow_html=True)
    if user_result[0]==0:
      col1, col2, col3 = st.columns(3)
      with col1:
        st.success("Output: 0")
      output = 'You are in Good Condition :slightly_smiling_face:'
    else:
      #output = 'You Have a chance of getting Heart Disease :pensive:'
      col1, col2, col3 = st.columns(3)
      with col1:
        st.error("Output: 1")
      output = 'You have an elevated risk of developing heart disease:pensive:'
    st.subheader(output)





























#st.subheader('Accuracy: ')
#st.write(str(accuracy_score(y, loaded_model.predict(x))*100)+'%')





