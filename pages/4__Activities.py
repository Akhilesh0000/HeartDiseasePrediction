import streamlit as st

st.markdown("# :man_in_lotus_position: Activities")
st.write(" ")

st.markdown('<div style="text-align: center;"><h2><u>Common Activities</u></h2></div>', unsafe_allow_html=True) 


st.markdown("""<div style="text-align: justify;">
<p>
Exercise is an important component of managing heart disease, but it's essential to consult with a healthcare provider before starting any exercise program. 
The type and intensity of exercise recommended for heart disease patients may vary depending on their individual condition, and their healthcare provider can help determine what exercises are safe and appropriate for them. 
However, here are some general exercises that are often recommended for heart disease patients:</p>
<ol>
<li>Walking 🚶🏽</li>
<li>Cycling 🚴🏽</li>
<li>Swimming 🏊🏽</li>
<li>Resistance Training 🏋🏽</li>
<li>Yoga and Stretching 🧘🏽</li>
</ol>
<p>It's essential to start slowly and gradually increase the intensity and duration of exercise as tolerated. 
It's also crucial to stop exercising and seek medical attention if any chest pain, dizziness, or shortness of breath occurs during exercise.</p>
</div>""", unsafe_allow_html=True)

st.write(' ')
st.markdown('<div style="text-align: center;"><h2><u>Walking🚶🏽</u></h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
#with col2:
 #   st.video("walking.mp4", format="video/mp4")
with col1:
    st.image("walking.png", width=None)
with col3:
    st.image("walking1.png", width=None)
st.markdown("""<div style="text-align: justify;">
<p>
Walking is a low-impact exercise that can help improve cardiovascular health. 
Start with short walks and gradually increase the duration and intensity as tolerated.</p>
</div>""",unsafe_allow_html=True)

st.write(' ')
st.markdown('<div style="text-align: center;"><h2><u>Cycling🚴🏽</u></h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("inbike.png", width=None)
with col2:
    st.image("biking.png", width=None)
with col3:
    st.image("outbike.png", width=None)
st.markdown("""<div style="text-align: justify;">
<p>
Cycling is a low-impact exercise that can improve cardiovascular health and strengthen leg muscles. 
Start with a stationary bike or a low-resistance setting on an outdoor bike and gradually increase the duration and intensity.</p>
</div>""",unsafe_allow_html=True)

st.write(' ')
st.markdown('<div style="text-align: center;"><h2><u>Swimming🏊🏽</u></h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.image("swimming.png", width=None)
st.markdown("""<div style="text-align: justify;">
<p>
Swimming is a low-impact exercise that can improve cardiovascular health and provide a full-body workout. 
However, it's important to avoid swimming alone and to make sure the pool has a lifeguard on duty.</p>
</div>""",unsafe_allow_html=True)

st.write(' ')
st.markdown('<div style="text-align: center;"><h2><u>Resistance training🏋🏽</u></h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.image("training.png", width=None)
st.markdown("""<div style="text-align: justify;">
<p>
Resistance training with light weights or resistance bands can help strengthen muscles and improve overall fitness. 
However, it's essential to start with light weights and to avoid lifting heavy weights that could strain the heart.</p>
</div>""",unsafe_allow_html=True)

st.write(' ')
st.markdown('<div style="text-align: center;"><h2><u>Yoga and stretching🧘🏽</u></h2></div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.image("yoga.png", width=None)
st.markdown("""<div style="text-align: justify;">
<p>
Yoga and stretching exercises can help improve flexibility, balance, and relaxation, which can benefit heart health. 
However, it's important to avoid poses that require holding the breath or that put excessive strain on the heart.</p>
</div>""",unsafe_allow_html=True)






