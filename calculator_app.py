import streamlit as st
import math

# Custom CSS for gradient text
st.markdown("""
    <style>
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #FF6B6B, #FFD93D, #6BCB77);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with gradient text and subtitle with emoji
st.markdown('<h1 class="gradient-text">Scientific Calculator</h1>', unsafe_allow_html=True)
st.subheader("🧮 This was created by M.Saad Zia 🎉")

# Input fields for calculator operations
operation = st.selectbox("Select Operation ✨", ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide", "💪 Power", "√ Square Root", "🌞 Sin", "🌙 Cos", "📐 Tan"])

if operation in ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide", "💪 Power"]:
    num1 = st.number_input("Enter first number 🔢")
    num2 = st.number_input("Enter second number 🔢")
else:
    num = st.number_input("Enter the number 🔢")

# Perform the calculation when button is clicked
if st.button("Calculate 💻"):
    if operation == "➕ Add":
        result = num1 + num2
    elif operation == "➖ Subtract":
        result = num1 - num2
    elif operation == "✖️ Multiply":
        result = num1 * num2
    elif operation == "➗ Divide":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    elif operation == "💪 Power":
        result = num1 ** num2
    elif operation == "√ Square Root":
        result = math.sqrt(num)
    elif operation == "🌞 Sin":
        result = math.sin(math.radians(num))
    elif operation == "🌙 Cos":
        result = math.cos(math.radians(num))
    elif operation == "📐 Tan":
        result = math.tan(math.radians(num))

    st.write(f"📊 Result: {result}")
