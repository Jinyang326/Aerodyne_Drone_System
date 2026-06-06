import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Aerodyne Smart Agricultural Drone System")
root.geometry("900x600")

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
    width=20
)
analyze_button.pack(pady=20)

result_label = tk.Label(
    root,
    text="Mission Result Will Be Displayed Here",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()