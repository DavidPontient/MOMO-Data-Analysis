Perfect! You now have a complete working project with:

* ✅ Backend (`Flask` + `SQLite`)
* ✅ Frontend HTML
* ✅ CSS styling
* ✅ JavaScript interactivity + chart visualizations

---

# 📊 MTN MoMo SMS Dashboard

An interactive dashboard to analyze and visualize MTN MoMo transaction data. Built with **Flask**, **SQLite**, and **JavaScript**, it helps users explore financial transactions by filtering, charting, and inspecting the data.

---

## ✨ Features

* 🔍 Filter transactions by **category** and **amount range**
* 📊 View totals per **category** in a bar chart
* 📋 Inspect individual transactions in a detailed table
* ⚡ Fast and responsive with no frameworks — just Flask + vanilla JS + Chart.js

---

## 📁 Project Structure

```
MOMO-Data-Analysis/
├── Backend/
│   ├── data_parsing.py
│   ├── db_setup.py
│   └── server.py
├── Data/
│   ├── modified_sms_v2.xml   
├── Frontend/
│   ├── app.js       
│   ├── index.html         
│   └── main.css            
└── README.md            
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone MOMO-Data-Analysis
cd Backend
```

### 2. Install dependencies

Make sure you have Python 3 installed. Then run:

```bash
pip install flask
```

### 3. Initialize the database

If the database doesn't exist yet, create it with:

```bash
python db_setup.py
```

This creates `transactions.db` and the required `transactions` table.

```bash
python data_parsing.py
```

This creates `unprocessed_logs.txt` 

### 4. Run the Flask server

```bash
python server.py
```

Then visit:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔗 API Overview

| Endpoint | Method | Description                          |
| -------- | ------ | ------------------------------------ |
| `/`      | GET    | Serves the frontend dashboard        |
| `/data`  | GET    | Returns all transaction data as JSON |

---

## 🖼️ Demo video 

> *You can optionally add images or animated GIFs of the dashboard here.*

---

## 🛠 Technologies Used

* **Python + Flask** – lightweight backend
* **SQLite** – simple embedded database
* **HTML + CSS** – responsive UI
* **JavaScript + Chart.js** – interactivity and visualizations

---

## 📄 License

MIT License — open for educational and personal use.

---
