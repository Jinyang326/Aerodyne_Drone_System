import tkinter as tk
from tkinter import ttk
from math import ceil

# ==========================================
# Crop Monitoring Module
# Analyze crop monitoring mission
# ==========================================

def crop_monitoring(crop_type, land_size):

    if crop_type == "Palm Oil":
        coverage = 12

    elif crop_type == "Paddy":
        coverage = 8

    elif crop_type == "Vegetable":
        coverage = 5

    else:
        coverage = 10

    flights_needed = land_size / coverage

    battery_required = ceil(flights_needed)

    flight_duration = battery_required * 20

    return coverage, battery_required, flight_duration

# ==========================================
# Pest Detection Module
# ==========================================

def pest_detection(pest_level):

    if pest_level == "Low":

        risk = "LOW"
        action = "Routine Monitoring"
        loss = "5%"

    elif pest_level == "Medium":

        risk = "MEDIUM"
        action = "Drone Spraying Recommended"
        loss = "15%"

    elif pest_level == "High":

        risk = "HIGH"
        action = "Immediate Drone Deployment Required"
        loss = "25%"

    else:

        risk = "UNKNOWN"
        action = "No Recommendation"
        loss = "0%"

    return risk, action, loss

# ==========================================
# Flight Planning Module
# ==========================================

def flight_planning(weather):

    if weather == "Sunny":

        status = "APPROVED"
        reason = "Weather conditions are ideal."

    elif weather == "Cloudy":

        status = "APPROVED"
        reason = "Safe for drone operation."

    elif weather == "Windy":

        status = "DELAYED"
        reason = "Strong wind may affect flight stability."

    elif weather == "Rainy":

        status = "CANCELLED"
        reason = "Drone operation is unsafe in rain."

    else:

        status = "UNKNOWN"
        reason = "Weather data unavailable."

    return status, reason

# ==========================================
# Mission Service Module
# ==========================================

def mission_service(mission_type):

    if mission_type == "Crop Monitoring":

        service = "Aerial Crop Monitoring"
        rate = 15

    elif mission_type == "Fertilizer Spraying":

        service = "Precision Fertilizer Spraying"
        rate = 35

    elif mission_type == "Pest Detection":

        service = "AI Pest Detection Analysis"
        rate = 20

    else:

        service = "No Service Selected"
        rate = 0

    return service, rate

# ==========================================
# Cost Estimation Module
# ==========================================

def cost_estimation(land_size, rate):

    total_cost = land_size * rate

    return total_cost

# ==========================================
# Main Analysis Function
# ==========================================

def analyze_mission():

    try:

        crop_type = crop_combo.get()

        land_size_text = land_entry.get()

        if land_size_text == "":

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Please enter a land size."
            )

            return

        land_size = float(land_size_text)

        pest_level = pest_combo.get()

        weather = weather_combo.get()

        mission_type = mission_combo.get()

        if crop_type == "":

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Please select a Crop Type."
            )

            return


        if pest_level == "":

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Please select a Pest Level."
            )

            return


        if weather == "":

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Please select a Weather Condition."
            )

            return


        if mission_type == "":

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Please select a Mission Type."
            )

            return

        if land_size <= 0:

            result_textbox.delete("1.0", tk.END)

            result_textbox.insert(
                tk.END,
                "Invalid land size. Please enter a value greater than 0."
            )

            return

        coverage, battery, duration = crop_monitoring(
            crop_type,
            land_size
        )
        risk, action, loss = pest_detection(
            pest_level
        )

        status, reason = flight_planning(
            weather
        )
        service, rate = mission_service(
            mission_type
        )

        total_cost = cost_estimation(
            land_size,
            rate
        )

        result_text = f"""
MISSION ANALYSIS RESULT

Drone Model:
Aerodyne AGX-100

Coverage Efficiency:
{coverage} ha/flight

Battery Required:
{battery}

Estimated Flight Duration:
{duration} mins

Pest Risk Level:
{risk}

Recommended Action:
{action}

Potential Yield Loss:
{loss}

Mission Status:
{status}

Flight Decision:
{reason}

Mission Type:
{mission_type}

Recommended Service:
{service}

Service Rate:
RM{rate}/ha

Estimated Mission Cost:
RM{total_cost:.2f}
"""

        result_textbox.delete(
            "1.0",
            tk.END
        )

        result_textbox.insert(
            tk.END,
            result_text
        )

    except ValueError:

        result_textbox.delete("1.0", tk.END)

        result_textbox.insert(
            tk.END,
            "Please enter a valid numeric value for land size."
        )

root = tk.Tk()

root.title("Aerodyne Smart Agricultural Drone System")
root.geometry("1100x900")

title_label = tk.Label(
    root,
    text="Aerodyne Smart Agricultural Drone System",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# Crop Type
tk.Label(form_frame, text="Crop Type:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

crop_combo = ttk.Combobox(
    form_frame,
    values=["Palm Oil", "Paddy", "Vegetable"]
)
crop_combo.grid(row=0, column=1)

# Land Size
tk.Label(form_frame, text="Land Size (ha):").grid(row=1, column=0, padx=10, pady=10, sticky="w")

land_entry = tk.Entry(form_frame)
land_entry.grid(row=1, column=1)

# Pest Level
tk.Label(form_frame, text="Pest Level:").grid(row=2, column=0, padx=10, pady=10, sticky="w")

pest_combo = ttk.Combobox(
    form_frame,
    values=["Low", "Medium", "High"]
)
pest_combo.grid(row=2, column=1)

# Weather
tk.Label(form_frame, text="Weather:").grid(row=3, column=0, padx=10, pady=10, sticky="w")

weather_combo = ttk.Combobox(
    form_frame,
    values=["Sunny", "Cloudy", "Windy", "Rainy"]
)
weather_combo.grid(row=3, column=1)

# Mission Type
tk.Label(form_frame, text="Mission Type:").grid(row=4, column=0, padx=10, pady=10, sticky="w")

mission_combo = ttk.Combobox(
    form_frame,
    values=[
        "Crop Monitoring",
        "Fertilizer Spraying",
        "Pest Detection"
    ]
)
mission_combo.grid(row=4, column=1)

analyze_button = tk.Button(
    root,
    text="Analyze Mission",
    width=20,
    command=analyze_mission
)
analyze_button.pack(pady=20)

result_frame = tk.LabelFrame(
    root,
    text="Mission Analysis Result",
    padx=10,
    pady=10
)

result_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_textbox = tk.Text(
    result_frame,
    wrap="word",
    width=70,
    height=20,
    font=("Courier New", 11),
    yscrollcommand=scrollbar.set
)

result_textbox.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.config(
    command=result_textbox.yview
)

root.mainloop()