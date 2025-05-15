import pickle
import streamlit as st

t=st.title("Iris Flower Prediction App")
sl=st.number_input("Enter Sepal Length")
sw=st.number_input("Enter Sepal Width")
pl=st.number_input("Enter Petal Length")
pw=st.number_input("Enter Petal Width")

button = st.button("Predict")
if button:
    dtc=pickle.load(open("iris.pkl","rb"))
    res=dtc.predict([[sl,sw,pl,pw]])[0]
    st.markdown(f"Predicted flower:{res}")


