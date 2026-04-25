import requests

API_KEY = "YOUR_API_KEY"
daily_log = []

while True:
    food = input("\nWhat did you eat? (or type 'done' to finish) ")
    
    if food == "done":
        break
    
    response = requests.get(
        f"https://api.api-ninjas.com/v1/nutrition?query={food}",
        headers={"X-Api-Key": "reYoML50WgkE08WszvUI8MLBTDeWYbIlae0FlscN"}
    )
    
    data = response.json()
    
    if data:
        item = data[0]
        daily_log.append(item)
        print(f"{item['name']} logged ✓")
    else:
        print("Food not found, try again")

print("\n--- YOUR DAY ---")
for item in daily_log:
    print(f"{item['name']} — {item['carbohydrates_total_g']}g carbs, {item['fat_total_g']}g fat")
