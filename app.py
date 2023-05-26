import streamlit as st
import joblib


def main():
   
    st.title("StatisticaM")

    file = "Nuovomodel.pkl"
    model = joblib.load(file)

    AdultMortality= st.number_input('Adult Mortality',0,10,5)
    infantdeaths= st.number_input('infant deaths',0,10,5)
    HepatitisB	= st.number_input('Hepatitis B	',0,10,5)
    Measles= st.number_input('Measles',0,10,5)
    BMI= st.number_input('BMI',0,10,5)
    underfivedeaths= st.number_input('under-five deaths',0,10,5)
    Polio= st.number_input('Polio',0,10,5)
    Diphtheria= st.number_input('Diphtheria',0,10,5)
    HIVAIDS= st.number_input('HIV/AIDS',0,10,5)
    thinness119years= st.number_input('thinness 1-19 years',0,10,5)
    thinness59years= st.number_input('thinness 5-9 years',0,10,5)
    Incomecompositionofresources= st.number_input('Income composition of resources',0,10,5)
    Schooling= st.number_input('Schooling',0,10,5)
    


    res= model.predict([[AdultMortality,infantdeaths,HepatitisB,Measles,BMI,underfivedeaths,Polio,Diphtheria,HIVAIDS,thinness119years,thinness59years,Incomecompositionofresources,Schooling]])
    st.write(f"il risultato è {res[0]}")


if __name__ == "__main__":
    main()