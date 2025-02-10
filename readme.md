# **Real-Time Google Play Store Data Analytics**

## **Project Overview**
This project focuses on analyzing and visualizing real-time Google Play Store data using Python. It involves dynamic filtering, interactive dashboards, and time-based data visualization techniques.

### **Live Project & Repository**
- **Live Dashboard**: [View Dashboard](https://elaborate-marzipan-5b573c.netlify.app/)
- **GitHub Repository**: [View Code](https://github.com/sowmiyaM-1/GooglePlayStoreDataAnalysis)

## **Features & Objectives**
✅ Interactive visualizations for Google Play Store data  
✅ Advanced filtering and data cleaning  
✅ Time-restricted dashboards (specific time slots)  
✅ Python-based data analysis using Pandas, Matplotlib, Seaborn, and Plotly  

## **Tasks & Implementations**

### **Task 1: Scatter Plot - Revenue vs Installs**
- Visualizes correlation between revenue and installs for paid apps  
- Color-coded based on app categories  

### **Task 2: Dual-Axis Chart - Free vs Paid Apps**
- Compares installs and revenue for the top 3 categories  
- Filters applied (minimum installs, revenue, app size, Android version, etc.)  
- Display restricted to **1 PM - 2 PM IST**  

### **Task 3: Choropleth Map - Global Installs by Category**
- Displays installs for the top 5 categories  
- Excludes categories starting with "A", "C", "G", or "S"  
- Display restricted to **6 PM - 8 PM IST**  

### **Task 4: Time Series Line Chart - Install Trends**
- Highlights significant growth periods (>20% MoM)  
- Filters applied (content rating = Teen, app name starts with "E", installs >10K)  
- Display restricted to **6 PM - 9 PM IST**  

### **Task 5: Violin Plot - Rating Distribution**
- Shows rating distribution per category  
- Filters applied (category with >50 apps, app name contains "C", reviews >10, rating <4.0)  
- Display restricted to **4 PM - 6 PM IST**  

## **Challenges & Solutions**
🚀 **Multi-condition filtering**: Implemented advanced Pandas filtering techniques  
⏰ **Time-restricted graphs**: Used Python's datetime module to manage dashboard visibility  

## **Outcome**
🎯 Developed dynamic and interactive dashboards  
📊 Improved data analysis and visualization skills  
🔍 Gained insights into Google Play Store app performance  

## **How to Run**
1. Clone the repository:  
   ```bash
   git clone https://github.com/sowmiyaM-1/GooglePlayStoreDataAnalysis.git
   cd GooglePlayStoreDataAnalysis
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the scripts to generate visualizations (e.g., `python Task2.py`)  
4. Open `dashboard.html` to view the output  

## **Technologies Used**
- **Python** (Pandas, Matplotlib, Seaborn, Plotly)  
- **Netlify** (For deployment)  

---
