# step4_report.py
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os

# --- Setup Paths ---
os.makedirs("outputs", exist_ok=True)

# Load matrices
distance_df = pd.read_csv("data/distance_matrix.csv", index_col=0)
time_df = pd.read_csv("data/time_matrix.csv", index_col=0)

# Optimized route (from Step 3 output)
# If you got the route printed earlier, put it here:
optimized_route = ["Warehouse", "Customer_1", "Customer_3", "Customer_4", "Warehouse"]

total_distance, total_time = 0, 0
cost_per_km = 20  # ₹ per km

# Route breakdown table
route_details = []
for i in range(len(optimized_route) - 1):
    start, end = optimized_route[i], optimized_route[i+1]
    distance = distance_df.loc[start, end]
    time = time_df.loc[start, end]
    total_distance += distance
    total_time += time
    route_details.append([start, end, f"{distance:.2f} km", f"{time:.2f} min"])

total_cost = total_distance * cost_per_km

# --- Generate PDF Report ---
pdf_file = "outputs/Final_Optimization_Report.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# Title Section
c.setFont("Helvetica-Bold", 18)
c.drawString(50, height - 50, "Delivery Route Optimization Report")
c.setFont("Helvetica", 12)
c.drawString(50, height - 80, "Internship Task 4 - Codetech IT Solutions")
c.drawString(50, height - 100, "Name: Swara Rajesh Redij | ID: CITS0D734")
c.drawString(50, height - 120, "Domain: Data Science | Duration: 6 weeks")

# Insert the route map image (from Step 3)
route_img = "outputs/optimized_route.png"
if os.path.exists(route_img):
    c.drawImage(route_img, 50, height - 400, width=300, preserveAspectRatio=True, mask='auto')
else:
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 400, "[Route map not found. Run step3_optimization.py first]")

# Add Route Table
data = [["From", "To", "Distance", "Time"]] + route_details
table = Table(data, colWidths=[100, 100, 100, 100])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 0), (-1, -1), 10)
]))
table.wrapOn(c, width, height)
table.drawOn(c, 50, height - 500)

# Summary Section
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 530, f"Total Optimized Distance: {total_distance:.2f} km")
c.drawString(50, height - 550, f"Total Estimated Time: {total_time:.2f} minutes")
c.drawString(50, height - 570, f"Estimated Delivery Cost: ₹{total_cost:.2f}")

c.setFont("Helvetica-Oblique", 10)
c.drawString(50, height - 600, "Generated automatically as part of Internship Task 4 submission.")

c.save()
print(f"PDF Report Generated: {pdf_file}")
