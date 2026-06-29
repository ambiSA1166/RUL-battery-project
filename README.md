# 🔋 Lithium-Ion Battery Remaining Useful Life (RUL) Predictor

An end-to-end Machine Learning web application that predicts the **Remaining Useful Life (RUL)** of lithium-ion batteries based on cycle-specific operational metrics. Built using an optimized Random Forest architecture and served via a high-performance FastAPI backend, the solution provides real-time inference accompanied by statistical uncertainty metrics (95% Confidence Intervals).

🔗 **Live Application:** [Deploy Link Vercel](https://rul-battery-project.vercel.app)  
🔗 **Live Application:** [Deploy Link Render](https://battery-rul-docker.onrender.com)  
🐳 **Docker Image:** [`ambika1166/battery-predictor-app` on Docker Hub](https://hub.docker.com/r/ambika1166/battery-predictor-app)

---
## software and tools requirement
1. [GithubAccount](https://github.com)
2. [VScodeIDE](https://code.visualstudio.com/)
3. [Docker](https://hub.docker.com/)
4. [Render](https://render.com/)
   
create a new environment
```
conda create -p venv python==3.9 -y
```

---

## 🚀 Key Features

* **Robust Core Engine:** Utilizes an optimized Random Forest Regressor to output cycle counts based on specific charge/discharge characteristics.
* **Confidence Interval Analytics:** Quantifies real-time prediction uncertainty by polling individual tree estimators to construct an approximate 95% Confidence Interval limit ($1.96 \times \sigma$).
* **High Performance API:** Powered by **FastAPI** with rigid Pydantic validation rules guaranteeing reliable data ingestion.
* **Production Deployment:** Containerized using lightweight multi-stage cached Docker files and deployed seamlessly via Render.

---

## 🛠️ Tech Stack & Tools

* **Language:** Python (3.11)
* **Machine Learning / Data Processing:** Scikit-learn, Joblib, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Web Framework & Server:** FastAPI, Uvicorn, Jinja2 Templates (HTML rendering)
* **Containerization & DevOps:** Docker, Render Cloud

---

## 📂 Project Architecture & File Structure

```text
├── templates/
│   └── index.html                 # Frontend user interface
├── battery_rul_champion_rf.pkl    # Serialized Random Forest model artifact
├── Dockerfile                     # Multi-stage optimized Docker deployment build
├── eda and model.ipynb            # Interactive notebook for EDA, model tracking & evaluation
├── main.py                        # Core ASGI application setup & prediction pipeline
├── requirements.txt               # explicit python environment requirements
└── README.md                      # Documentation
```
---

## File Breakdown
* `main.py`: Declares FastAPI app schema, initializes Pydantic features models, extracts model.estimators_ variance to quantify predictive volatility, and interfaces with UI components.

* `eda and model.ipynb`: Conducts correlation matrix analysis, structural checks, scaling, and processes the final champion .pkl pipeline export using joblib.

* `Dockerfile`: Builds a python:3.11-slim image, implementing strict layered caching optimization strategies (copying requirements and resolving runtime dependencies before mounting context layers).

## 🛠️ Local Environment Setup

### Method 1: Using Python Virtual Environment
* **Clone the Repository**
  ```
  git clone [https://github.com/YOUR_GITHUB_USERNAME/RUL-battery-project.git](https://github.com/YOUR_GITHUB_USERNAME/RUL-battery-project.git) cd RUL-battery-project
  ```
* **Initialize Environment & Install Dependencies**
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
* **Spin Up Server Locally**
  ```
  uvicorn main:app --reload --host 127.0.0.1 --port 8000
  ```
  Access the interactive UI layout at http://127.0.0.1:8000 or navigate to /docs for swagger interface details.

### Method 2: Running with Docker
* **Build Container Image**
  ```
  docker build -t battery-predictor-app .
  ```
* **Run Local Container Instance**
  ```
  docker run -p 8000:8000 battery-predictor-app
  ```
* **Pull Directly From Registry**
  ```
  docker pull ambika1166/battery-predictor-app:latest
  ```
---

## API Endpoint Reference

1. `POST /predict`
   Processes real-time telemetry inputs to project remaining cycle lifespan metrics.
   * Sample Payload Schema:
     ```
     {
     "discharge_time": 2150.0,
     "decrement_range": 1150.0,
     "max_voltage_discharge": 3.95,
     "min_voltage_charge": 3.52,
     "time_at_voltage_threshold": 150.2,
     "time_constant_current": 650.4,
     "charging_time": 3200.0
     }
     ```
   * Sample Structural Response:
     ```
     {
     "Predicted RUL": 412.55,
     "Confidence Analytics": {
     "Margin of Error (cycles)": 14.22,
     "95% Confidence Interval": [398.33, 426.77]
     }
     }
     ```

2. `GET /health`
   Returns system status diagnostics to track endpoint load capacity or node verification checks.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
