# num1=float(input("Enter the no 1: "))
# num2=float(input("Enter the no 2: "))
# operator=input("Enter the operator: ")
# if operator=="+":
#     print(num1+num2)
# elif operator=="-":
#     print(num1-num2)
# elif operator=="*":
#     print(num1*num2)
# elif operator=="/":
#     print(num1/num2)


import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Operator selection
operator = st.selectbox("Select Operator", ["+", "-", "*", "/"])

# Calculate result on button click
if st.button("Calculate"):
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        st.success(f"Result: {result}")
    except ZeroDivisionError:
        st.error("❌ Cannot divide by zero!")
