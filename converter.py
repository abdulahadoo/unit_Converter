#Project 02: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit

import streamlit as st
st.markdown(
    """
     <style>
    body {
        background-color:rgb(7, 29, 73);
        color:rgb(243, 233, 233);

    }
    .stApp{
        background: linear-gradient(135deg,rgb(255, 255, 255),rgb(17, 8, 65)); 
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 10px 15px rgba(0,0,0,0.3);   
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg,rgb(22, 72, 82),rgb(245, 9, 9))
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgb(240, 242, 243)
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color:black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgb(45, 27, 87);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgb(240, 242, 243);
        color: white;
    }
    .footer{
        text-align: center;
        font-size: 14px;
        margin-top: 50px;
        color: black;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
#Title and description
st.markdown("<h1>⭕ Unit Converter </h1>",unsafe_allow_html=True)
st.write(" Easily convert between different units of length, temperature, and weight.")

#sidebar
conversion_type = st.selectbox("Choose conversion type",["lenght","weight","temperature"])
value = st.number_input("Enter the value to convert",value=0.0,min_value=0.0,step=0.1)
col1,col2 = st.columns(2)

if conversion_type == "lenght":
    with col1:
        from_unit = st.selectbox("From",["meters","kilometers","miles","yards","feet","inches","millimeters","centimeters"])
    with col2:
        to_unit = st.selectbox("To",["meters","kilometers","miles","yards","feet","inches","millimeters","centimeters"])
elif conversion_type == "weight":
    with col1:
       from_unit = st.selectbox("From",["kilograms","grams","milligrams","pounds","ounces"])
    with col2:
        to_unit = st.selectbox("To",["kilograms","grams","milligrams","pounds","ounces"])
elif conversion_type == "temperature":
    with col1:
        from_unit = st.selectbox("From",["celsius","fahrenheit","kelvin"])
    with col2:
        to_unit = st.selectbox("To",["celsius","fahrenheit","kelvin"])

#converted function
def lenght_convertor(value,from_units,to_unit):
    lenght_units = {
        "meters":1,
        "kilometers":0.001,
        "miles":1609.34,
        "yards":0.9144,
        "feet":3.28084,
        "inches":39.3701,
        "millimeters":1000,
        "centimeters":100,
        "grams":1000,
    }
    return (value / lenght_convertor[from_units]) * lenght_convertor[to_unit]

def weight_convertor(value,from_unit,to_unit):
    weight_units = {
        "kilograms":1,
        "grams":1000,
        "milligrams":1000000,
        "pounds":2.20462,
        "ounces":35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value,from_unit,to_unit):
    if from_unit == "celsius":
        return (value * 9/5 + 32 ) if to_unit == "fahrenheit" else value + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "fahrenheit":
        return (value - 32) * 5/9 if to_unit == "celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "kelvin" else value
    elif from_unit == "kelvin":
        return value - 273.15 if to_unit == "celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "fahrenheit" else value
    return value
#button for conversion
if st.button("❄_Convert_❄"):
    if conversion_type == "Lenght":
        result = lenght_convertor(value,from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_convertor(value,from_unit, to_unit)
    elif conversion_type == "temperature":
        result = temperature_convertor(value,from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result:.4} {to_unit}</div>" , unsafe_allow_html= True) 
    st.markdown("<div class='footer'>Developed by Abdul Ahad 🥵</div>",unsafe_allow_html=True) 


