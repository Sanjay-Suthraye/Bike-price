import streamlit as st
import pickle
import numpy as np
import datetime                      
from datetime import date 


pickle_in = open("bike_price_model.pkl","rb")
model=pickle.load(pickle_in)

def prediction():
    st.title("Used Bike price prediction")
    ex_showroom_price=st.text_input("Enter the original Bike price","Type here")
    
    km_driven=st.text_input("Enter the total kilometers driven","Type here")
    
    owner1=st.radio("Number of previous owners",("1st Owner","2nd Owner","3rd Owner"))
    owner=0
    if owner1=="1st Owner":
        owner+=1
    if owner1=="2nd Owner":
        owner+=2
    if owner1=="3rd Owner":
        owner+=3
    
    
    
    year1=st.text_input("Enter the Bike's year of manufacture","Type here")
    

    Seller_type=st.radio("Select seller type",("Dealer","Individual"))
    seller_type_Individual=0
        
    if Seller_type=="Individual":
        
        seller_type_Individual+=1
    
  
    obj1=""
    if st.button("Predict"):
        date=datetime.datetime.now()
        age=date.year-int(year1)
        result=model.predict([[owner,km_driven,ex_showroom_price,age,seller_type_Individual]])
        obj=float(result)
        obj1=round(obj)
    st.success('The Bike price is {}'.format(obj1))
    
    
                   
     
        
if __name__=='__main__':
    prediction()
   