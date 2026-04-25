import streamlit as st
import requests

st.title("🍎 Nutrition Tracker")

API_KEY = "YOUR_API_KEY"

if "meal_log" not in st.session_state:
    st.session_state.meal_log = []

food = st.text_input("What did you eat?")

if st.button("Add to log"):
    response = requests.get(
        f"https://api.api-ninjas.com/v1/nutrition?query={food}",
        headers={"X-Api-Key": "reYoML50WgkE08WszvUI8MLBTDeWYbIlae0FlscN"}
    )
    data = response.json()
    
    if data:
        item = data[0]
        st.session_state.meal_log.append(item)
        st.success(f"{item['name']} added ✓")
    else:
        st.error("Food not found")

if st.session_state.meal_log:
    st.subheader("Today's Meals")
    
    total_carbs = 0
    total_fat = 0
    total_sugar = 0
    
    for item in st.session_state.meal_log:
        st.write(f"• {item['name']} — {item['carbohydrates_total_g']}g carbs, {item['fat_total_g']}g fat")
        total_carbs += item['carbohydrates_total_g']
        total_fat += item['fat_total_g']
        total_sugar += item['sugar_g']
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Carbs", f"{total_carbs}g")
    col2.metric("Total Fat", f"{total_fat}g")
    col3.metric("Total Sugar", f"{total_sugar}g")
    
    if st.button("Clear log"):
        st.session_state.meal_log = []