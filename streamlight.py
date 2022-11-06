import pandas as pd
import numpy as np
import pickle
import streamlit as st
import os
# import statsmodels.api as sm




pickle_in=open("modelz.pkl",'rb')

model=pickle.load(pickle_in)
def predict(country,year,status,adult_m,infant_d,alc,percent,hepa,meas,bmi,fived,pol,totexp,diph,hiv,gdp,pop,thin1,thin10,inc,school):
    xyz=np.asarray([year,adult_m,infant_d,alc,percent,hepa,meas,bmi,fived,pol,totexp,diph,hiv,gdp,thin1,thin10,inc,school]).astype(np.float64)
    reshapexyz = xyz.reshape(1,-1)
    prediction=model.predict(reshapexyz)
    print(prediction)
    return prediction


def main():
    st.title("Lifespan")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style = " color : white;text-align:center;">streamlit Life Expectancy ML WEB APP</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    country = st.text_input("Country","Type here")
    year=st.text_input("Year","Type Here")
    status=st.text_input("Status","Type Here")
    adult_m=st.text_input("Adult Mortality","Type Here")
    infant_d=st.text_input("Infant Death","Type Here")
    alc=st.text_input("Alcohol","Type Here")
    percent=st.text_input("Percentage Expenditure","Type Here")
    hepa=st.text_input("Hepatitis B","Type Here")
    meas=st.text_input("Measles","Type Here")
    bmi=st.text_input("BMI","Type Here")
    fived=st.text_input("Under Five Deaths","Type Here")
    pol=st.text_input("Polio","Type Here")
    totexp=st.text_input("Total Expenditure","Type Here")
    diph=st.text_input("Diphtheria","Type Here")
    hiv=st.text_input("HIV/Aids","Type Here")
    gdp=st.text_input("GDP","Type Here")
    pop=st.text_input("Population","Type Here")
    thin1=st.text_input("Thinness 1-19","Type Here")
    thin10=st.text_input("Thinness 5-9","Type Here")
    inc=st.text_input("Income Composition Of Resources","Type Here")
    school=st.text_input("School","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(country,year,status,adult_m,infant_d,alc,percent,hepa,meas,bmi,fived,pol,totexp,diph,hiv,gdp,pop,thin1,thin10,inc,school)
    st.success('The Output Is {}'.format(result))
    if st.button("About"):
        st.text("What we have achieved to do here is create a Linear Reggression model that will")
        st.text("predict the Life Expectancy of a country based on some given factors.")
        st.text("This project was prepared by team Runtime Error- ")
        st.text("1. Ayushman Bhowmik")
        st.text("2. Aryan Debray")
        st.text("3. Roudrak Saha")
        st.text("4. Sampan Basu")
        st.text("5. Shikha Chaturvedi")
if __name__=='__main__':
    main()

    #predict(country,year,status,adult_m,infant_d,alc,percent,hepa,meas,bmi,fived,pol,totexp,diph,hiv,gdp,pop,thin1,thin10,inc,school)