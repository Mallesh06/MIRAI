#import streamlit module
import streamlit as st

#-----------give a title---------
st.title("MIRAI CALCULATOR!")
st.subheader("Mathematics is all we need!")

#select an operation
operation=st.selectbox("Select the operation:",["Addition","Subtraction","Multiplication","Division","Modulus"])

#---------give the first value---------------
num1=st.number_input("Enter first value :",min_value=1, max_value=100)
st.write("You've given ",num1,"!")

#---------give the second value ------------
num2=st.number_input("Enter second value :",min_value=1, max_value=100)
st.write("You've given ",num2,"!")

#-------------result----------------------------
st.subheader("Solution :")
if operation == "Addition":
    st.write("You've choosen Addition :")
    res1= num1+num2
    st.write(f"{num1} + {num2} = {res1} ")
elif operation == "Subtraction":
    st.write ("You've choosen Subtraction :")
    res2=num1-num2
    st.write(f"{num1} - {num2} = {res2}")
elif operation == "Multiplication":
    st.write ("You've choosen Multiplication :")
    res2=num1*num2
    st.write(f"{num1} X {num2} = {res2}")
elif operation == "Division":
    st.write ("You've choosen Division :")
    res2=num1//num2
    st.write(f"{num1} % {num2} = {res2}")
elif operation == "Modulus":
    st.write ("You've choosen Modulus :")
    res2=num1%num2
    st.write(f"{num1} modulo {num2} = {res2}")



