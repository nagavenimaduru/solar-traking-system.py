import math


def calculate_solar_angle(hour):
    """
    Calculate approximate solar angle based on time.
    Solar noon = 12:00
    """

    if hour < 6 or hour > 18:
        return None

    # 0° at 6 AM, 90° at 12 PM, 180° at 6 PM
    angle = (hour - 6) * 15

    return angle


def calculate_panel_angle(hour):
    """
    Calculate the required panel tracking angle.
    """

    solar_angle = calculate_solar_angle(hour)

    if solar_angle is None:
        return None

    
    panel_angle = solar_angle - 90

    
    panel_angle = max(-90, min(90, panel_angle))

    return panel_angle


print("===================================")
print("     SOLAR TRACKING SYSTEM")
print("===================================")

try:
    hour = float(input("Enter current time (6 to 18 hours): "))

    if hour < 6 or hour > 18:
        print("\nSolar tracking is inactive.")
        print("Tracking operates between 6:00 AM and 6:00 PM.")

    else:
        solar_angle = calculate_solar_angle(hour)
        panel_angle = calculate_panel_angle(hour)

        print("\n--------- Tracking Result ---------")
        print(f"Time              : {hour:.2f} hours")
        print(f"Solar Position    : {solar_angle:.2f}°")
        print(f"Panel Angle       : {panel_angle:.2f}°")

        if panel_angle < 0:
            print("Panel Direction   : East")
        elif panel_angle > 0:
            print("Panel Direction   : West")
        else:
            print("Panel Direction   : Solar Noon")

        print("-----------------------------------")

except ValueError:
    print("Invalid input! Please enter a numeric value.")
