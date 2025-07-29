# deliveryRootOptimization
Company: Codetech IT Solutions 
Name: Swara Rajesh Redij 
Internship ID: CITS0D734 
Internship Duration: 6 Weeks (Starting 14 June 2025) 
Mentor: Neela Santosh

description:
This project focuses on optimizing the delivery route for a warehouse serving multiple customers using Python-based data analysis and operations research techniques. The primary objective was to minimize total travel distance, time, and delivery cost while generating a professional, automated report.
The solution was implemented in four structured steps:
1. Step 1 – Location Setup & Visualization:
Defined warehouse and customer coordinates on a 2D map. Visualized all delivery points with a labeled scatter plot to understand their spatial distribution.
2. Step 2 – Distance and Time Matrices:
Generated a distance matrix (in kilometers) and travel time matrix (in minutes) for all location pairs using Euclidean distance and estimated travel times considering random delays. Both matrices were stored in CSV format for reuse.
3. Step 2.5 – Heatmap Analysis:
Created a distance heatmap using Seaborn to highlight shortest and longest routes, enabling better insights into delivery patterns.
4. Step 3 – Route Optimization (TSP Solver):
Applied linear programming (using PuLP) to solve a Traveling Salesman Problem (TSP), determining the most efficient delivery route covering all customers and returning to the warehouse. The optimized route was visualized and saved as optimized_route.png.
5. Step 4 – Automated PDF Report:
Generated a professional PDF report summarizing the optimized route, total distance, estimated time, and delivery cost (₹20 per km). The report includes the route map, detailed metrics, and a summary table for presentation.
The project automates every stage — from data preparation and route analysis to final reporting, providing a scalable solution that can be adapted for larger logistics networks.
![Image](https://github.com/user-attachments/assets/54734af9-82fc-4642-92f5-c76b249514d2)

![Image](https://github.com/user-attachments/assets/8012533e-432d-48e8-8ec7-dac572f3ab9d)
![Image](https://github.com/user-attachments/assets/b16efa4d-84e5-44ab-9ac1-ac1f23a5faad)
