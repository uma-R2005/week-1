import time

# Inputs
occupied = input("Is the room occupied? (yes/no): ").lower() == "yes"
time_of_day = input("What time is it? (day/night): ").lower()
weather = input("What's the weather? (sunny/cloudy): ").lower()
manual_override = input("Manual override? (on/off/none): ").lower()
sleep_mode = input("Sleep mode active? (yes/no): ").lower() == "yes"
emergency_alert = input("Emergency alert? (yes/no): ").lower() == "yes"

# Step 1: Automatic control logic
if occupied:
    if time_of_day == "night":
        light_action = "Turn lights ON 💡 (Bright)"
    elif weather == "cloudy":
        light_action = "Turn lights ON 💡 (Dim)"
    else:
        light_action = "Lights remain OFF"
else:
    light_action = "Lights remain OFF (room is empty)"

# Step 2: Manual override applied
if manual_override == "on":
    light_action = "Lights forced ON 💡 (Manual override)"
elif manual_override == "off":
    light_action = "Lights forced OFF (Manual override)"

# Step 3: Emergency alert overrides everything
if emergency_alert:
    light_action = "⚠️ EMERGENCY! Lights ON FULL BRIGHTNESS and flashing!"

# Step 4: Sleep mode applied last (lowest priority override)
elif sleep_mode:
    print(light_action)  # Show current action before sleep dimming
    print("Sleep mode activated. Gradually dimming lights...")
    # Simulate gradual dimming
    for dim_level in range(100, 0, -20):
        print(f"Light intensity: {dim_level}%")
        time.sleep(1)  # wait 1 second per step
    light_action = "Lights OFF. Good night!"

print(f"Action: {light_action}")
