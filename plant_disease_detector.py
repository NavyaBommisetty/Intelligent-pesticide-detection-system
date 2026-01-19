
# --- Import Required Libraries ---
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload Image from Local System (Colab Environment) 
uploaded = files.upload()

# This function generates a thermal image from the grayscale leaf image
# and estimates the stress level based on brightness (pixel intensity).
# The stress helps identify early disease risk or confirmed infections.
def analyze_stress(image, infection_status):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)                                                                               
    thermal = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    stress_index = np.mean(gray)

    # Classify stress based on brightness intensity
    if stress_index > 170:
        stress_status = "High Stress → Already infected (not visible yet)"
    elif 120 < stress_index <= 170:
        stress_status = "Low Stress → Early signs, possible risk"
    else:
        stress_status = "No Stress → Healthy plant"

    # Override status if infection already detected
    if infection_status in ["Medium Pest Infection", "High Pest Infection"]:
        stress_status = "High Stress → Confirmed pest infection"
    return thermal, stress_status

# Processing Each Uploaded Image
for filename in uploaded.keys():
    print(f"\nProcessing {filename} ...")

    #  Read and convert image 
    img = cv2.imread(filename)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color threshold for pest infection detection 
    lower = np.array([10, 40, 40])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    #Find infected regions and count
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    infected_area = np.sum(mask > 0) / (mask.shape[0] * mask.shape[1]) * 100
    spot_count = len(contours)

    # Classify infection level & spray intensity 
    if infected_area < 0.5:
        infection_status = "Healthy"
        spray_pressure = "No Spray Needed"
    elif infected_area < 2.0:
        infection_status = "Low Pest Infection"
        spray_pressure = "Low Pressure"
    elif infected_area < 5.0:
        infection_status = "Medium Pest Infection"
        spray_pressure = "Medium Pressure"
    else:
        infection_status = "High Pest Infection"
        spray_pressure = "High Pressure"

    #  Perform stress analysis 
    thermal_img, stress_status = analyze_stress(img, infection_status)

    # Annotate output image with results ---
    annotated = img_rgb.copy()
    cv2.putText(annotated, f"{infection_status}", (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
    cv2.putText(annotated, f"Spray: {spray_pressure}", (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    #Display Results (Original, Mask, Annotated, Thermal) 
    plt.figure(figsize=(18,6))
    plt.subplot(1,4,1)
    plt.imshow(img_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,4,2)
    plt.imshow(mask, cmap="gray")
    plt.title("Detected Spots")
    plt.axis("off")

    plt.subplot(1,4,3)
    plt.imshow(annotated)
    plt.title(f"{infection_status}\nSpray: {spray_pressure}")
    plt.axis("off")

    plt.subplot(1,4,4)
    plt.imshow(cv2.cvtColor(thermal_img, cv2.COLOR_BGR2RGB))
    plt.title(f"Thermal Scan\n{stress_status}")
    plt.axis("off")

    plt.show()

    #Print results in console
    print(f" {filename} → {infection_status} ({infected_area:.2f}% area, {spot_count} spots)")
    print(f" Spray Action → {spray_pressure}")
    print(f" Thermal Analysis → {stress_status}")
