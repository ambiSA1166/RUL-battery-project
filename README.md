# 🔋 Lithium-Ion Battery Remaining Useful Life (RUL) Predictor

An end-to-end Machine Learning web application that predicts the **Remaining Useful Life (RUL)** of lithium-ion batteries based on cycle-specific operational metrics. Built using an optimized Random Forest architecture and served via a high-performance FastAPI backend, the solution provides real-time inference accompanied by statistical uncertainty metrics (95% Confidence Intervals).

🔗 **Live Application:** [Deploy Link](https://lithium-ion-battery-rul-predictor.onrender.com/)  
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
