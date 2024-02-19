import streamlit as st
import pickle

st.markdown("# :coffin: Death Rate")
st.markdown("""<div style="text-align: center;">
<h6><i>Statistics of the Deaths Caused due to Heart Diseases over the years in several countries.
</i></h6></div>""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.write("_Data Source: [Link](https://ourworldindata.org/grapher/cardiovascular-disease-death-rates?tab=table)_")

st.write(" ")


st.markdown("""<div style="text-align: center;"><h2><u>Heart Disease Deaths</u></h2></div>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    country = st.text_input("Enter the Country Name:")


pickle_in = open("C:\\Users\\king of lenovo\\Desktop\\Btech-final-project\\Deaths.pkl", "rb")
entity = pickle.load(pickle_in)



entity_country = entity["entity"]
# entity_df = entity_country.get_group(country)
# entity_df
if st.button("Enter"):

    if country in entity_country.groups.keys():
        df = entity_country.get_group(country)
        st.markdown(f"""<div style="text-align: center;"><h2><u>{country}</u></h2></div>""", unsafe_allow_html=True)
        st.write("Number of Deaths from cardiovascular disease per 100,000 people")
        st.write("Sex - Both(Male,Female)")

        tab = df.loc[:,["Year","Deaths"]]
        tab = tab.reset_index()
        tab.drop(columns=["index"], inplace=True)
        tab = tab.set_index("Year")
        st.bar_chart(tab)
        st.line_chart(tab)
        col1, col2, col3 = st.columns(3)
        with col2:
            df_styled = tab.style.apply(lambda x: ['background: #F0F2F6' for i in range(len(x))])
            st.table(df_styled)
    else:
        st.warning("Please Enter Vaild Country Name")
    
    # fig = px.bar(df, x=df["Year"], y=df["Deaths"])
    # fig.show()
    