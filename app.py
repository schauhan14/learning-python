import streamlit as st
import requests

st.title("🍎 Nutrition Tracker")

API_KEY = "YOUR_NEW_API_KEY"

food = st.text_input("What did you eat?")

if st.button("Search"):
    response = requests.get(
        f"https://api.api-ninjas.com/v1/nutrition?query={food}",
        headers={"X-Api-Key": "reYoML50WgkE08WszvUI8MLBTDeWYbIlae0FlscN"}
    )
    data = response.json()
    
    if data:
        item = data[0]
        st.subheader(item['name'].upper())
        col1, col2, col3 = st.columns(3)
        col1.metric("Carbs", f"{item['carbohydrates_total_g']}g")
        col2.metric("Fat", f"{item['fat_total_g']}g")
        col3.metric("Sugar", f"{item['sugar_g']}g")
    else:
        st.error("Food not found")