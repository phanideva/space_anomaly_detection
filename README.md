# 🚀 Real-Time Space Anomaly Detection & Prediction  
📡 **AI-Powered Satellite Telemetry Monitoring System**  

---

## **🛰️ Project Overview**  
This project is a **real-time space telemetry analysis system** that **simulates, detects, and predicts anomalies** in satellite telemetry data.  

It uses **Machine Learning (ML), Deep Learning (DL), and Dash visualization** to monitor space conditions such as:  

- 🌡 **Temperature fluctuations**  
- ☢ **Radiation exposure**  
- ☀ **Solar flux variations**  
- 🔋 **Battery voltage performance**  
- 🚀 **Thruster system behavior**  

The system **processes live telemetry data**, identifies anomalies using **ML models**, predicts failures using **LSTM-based Deep Learning**, and displays everything on a **real-time interactive dashboard**.

---

## **🎯 Purpose & Problem Statement**
### **🌍 Why is this Important?**
Satellites and space probes operate in **harsh environments** where system failures can lead to **billions of dollars in losses**.  

- **Unexpected temperature fluctuations** can damage onboard instruments.  
- **Radiation surges** can cause electronics to malfunction.  
- **Battery failures** can result in power loss.  
- **Thruster misfires** can impact trajectory adjustments.  

### **🔬 What Does This Project Do?**
✅ **Simulates real-time satellite telemetry data.**  
✅ **Detects anomalies using ML-based Isolation Forest.**  
✅ **Uses Deep Learning (LSTM) to predict potential system failures.**  
✅ **Provides an interactive Dash-based visualization for monitoring.**  

This helps **space agencies** and **aerospace companies** prevent failures **before they happen**.

---

## **🛠️ How It Works (Pipeline Overview)**  

### **✅ Step 1: Data Ingestion (Live Telemetry Simulation)**
- **Script:** `src/data_pipeline.py`  
- **What It Does:**  
  - Generates **random satellite telemetry data**.  
  - Saves it in `data/satellite_telemetry.csv`.  

### **✅ Step 2: Anomaly Detection (Machine Learning)**
- **Script:** `src/anomaly_detection.py`  
- **What It Does:**  
  - Uses **Isolation Forest (ML model)** to detect abnormal behavior.  
  - Marks **anomalies** in the telemetry dataset.  

### **✅ Step 3: Failure Prediction (Deep Learning)**
- **Script:** `src/prediction.py`  
- **What It Does:**  
  - Trains a **Long Short-Term Memory (LSTM) model** to predict failures.  
  - Saves the trained model in `models/lstm_model.h5`.  

### **✅ Step 4: Visualization (Real-Time Monitoring Dashboard)**
- **Script:** `src/visualization.py`  
- **What It Does:**  
  - Starts a **Dash-based web app** to visualize telemetry data.  
  - Updates graphs **every 2 seconds**.  
  - Displays **Temperature, Radiation, Solar Flux, and Battery Voltage trends**.  

### **✅ Step 5: Automate the Entire Workflow**
- **Script:** `run_pipeline.py`  
- **What It Does:**  
  - Runs **all scripts in sequence** with a **single command**.  

---

## **📊 Dash Visualization: How to Interpret the Output**
### **Live Dashboard URL**:  
👉 **http://127.0.0.1:8050/**  

Once `visualization.py` runs, you will see:  

### **1️⃣ Live Graphs of Key Satellite Metrics**
| **Metric**          | **Meaning** |
|---------------------|------------|
| **Temperature**     | Shows **thermal stability** of the satellite. Sudden spikes may indicate an issue. |
| **Radiation**       | Tracks **cosmic radiation exposure**. Extreme values can damage electronics. |
| **Solar Flux**      | Measures **solar panel efficiency**. A sudden drop might indicate **dust accumulation or failure**. |
| **Battery Voltage** | Monitors **battery health**. Low voltage levels can cause power failures. |

Each **graph updates every 2 seconds**, reflecting **real-time telemetry data**.

### **2️⃣ How Anomalies Appear**
- If an **anomaly is detected**, it will be **marked in the dataset**.  
- Future improvements can **highlight anomalies in red** in the dashboard.  

---

## **📥 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/space-anomaly-detection.git
cd space-anomaly-detection
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Pipeline**
Run the full system with:
```bash
python run_pipeline.py
```
or step by step:
```bash
python src/data_pipeline.py    # Generate data
python src/anomaly_detection.py  # Detect anomalies
python src/prediction.py   # Train & predict failures
python src/visualization.py  # Start the real-time dashboard
```

---

## **📡 Future Enhancements**
🚀 **Upgrade the system to use live NASA/SpaceX telemetry API.**  
📡 **Deploy on AWS for real-time monitoring.**  
🛰️ **Enhance ML models with Reinforcement Learning (RL).**  
⚠️ **Send automated alerts (Email/SMS) when anomalies are detected.**  

---

## **👨‍💻 Technologies Used**
✅ **Python** (Data Processing, AI/ML)  
✅ **Dash & Plotly** (Data Visualization)  
✅ **Pandas & Numpy** (Data Handling)  
✅ **Scikit-Learn & TensorFlow** (Machine Learning & Deep Learning)  
✅ **AWS Lambda, S3, DynamoDB (Future Deployment)**  

---

## **📬 Support & Contribution**
Feel free to **fork the repository, open issues, or contribute** to improvements!  
For any questions, **contact**: [phanisaisri@example.com]  

---

# **🚀 Final Thoughts**
With this **AI-powered Space Anomaly Detection System**, we can **improve space mission reliability, reduce failure risks, and enable autonomous monitoring** of **satellites and deep-space probes**.  

### **📡 "The future of space exploration relies on intelligent data-driven decision-making!"** 🚀✨  