# ⚡ Kenya EV Charging Infrastructure Dashboard

A comprehensive **web app (Streamlit) dashboard** analyzing the growth, distribution, and insights of **Electric Vehicle (EV) charging infrastructure in Kenya**.  
This project visualizes EV station data, provider networks, county-level accessibility, and user feedback. 

The key output: **downloadable sample dataset** mapping EV chargings stations in Kenya

<p align="center">
  <img src="Visuals\EV Dashboard overview.png" width="700">
</p>


---

## 📖 Project Overview
The dashboard offers a multi-tab view into Kenya’s emerging EV ecosystem; helping users understand where charging stations are located, which providers dominate, and how users perceive the current infrastructure.

**Tabs included:**
1. **Overview** – Executive summary of Kenya’s EV growth trends.
2. **Visualizations** – Interactive data visualizations and trend charts.
3. **Stations** – Mapping charging stations based on location and EV Brand.
4. **Brands** – Breakdown of EV brands in Kenya and respective charging stations' charger compatibility.
5. **Counties** – County-level distribution and comparative insights.
6. **Reviews** – Customer feedback and sentiment highlights.
7. **Insights** – Key findings and next steps.

---

## 🧩 Key Features
- Interactive Streamlit dashboard
- Folium-based county and station mapping
- Provider- and county-level filtering
- Searchable provider summaries
- Downloadable CSV datasets per provider
- Consistent tab layout with clean inline styling

<p align="center">
  <img src="Visuals\EV Stations Map.png" alt="Charging Stations Map" width="700">
</p>


---

## 📊 Dataset Details

The dataset captures EV charging stations across multiple Kenyan counties.  
Below is the data dictionary describing key variables used in the dataset of the project.

| **Column Name** | **Description** |
|------------------|------------------|
| `Station Name` | Name of the EV charging station |
| `Provider` | Charging service provider or operator |
| `County` | County where the charging station is located |
| `Location` | Specific area or address of the station |
| `Coordinates` | Latitude and longitude for mapping |
| `Charger Types` | Supported charger types (e.g., DC Fast, AC Type 2) |
| `Number of Ports` | Total number of charging ports available |
| `Pricing` | Cost of charging per kWh or per session |
| `Payment Methods` | Accepted payment methods (e.g., MPESA, Card) |
| `Car Models Supported` | Compatible vehicle models for the chargers |
| `Motorcycle Support` | Indicates if the station supports e-motorcycles |
| `Operating Hours` | Station’s daily operating schedule |
| `Status` | Whether the station is operational or planned |
| `Average Rating` | Average user rating for the station |


---

## 🧮 Data Sources
- Government of Kenya EV policy reports
- Kenya Power pilot network news reports
- Private EV providers newsletters announcements
- Google maps/my business directory

---

## ⚙️ Tech Stack
- **Frontend:** Streamlit
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Plotly, Altair
- **Styling:** Inline CSS (embedded per tab)
- **Export:** CSV/JSON download capability

---

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/kenya-ev-charging-dashboard.git
   cd kenya-ev-charging-dashboard
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

5. Once it starts, Streamlit will open a local URL (Open your browser) at [http://localhost:8501](http://localhost:8501).

---

## 🗂️ Project Structure

```
kenya-ev-charging-dashboard/
│
├── app.py                      # Main Streamlit  application
├── data/
│   └── charging_stations dataframe   # Example dataset
├── visuals #images folder
├── README.md
└── requirements.txt
```

---

## 📈 Example of Web App Visuals

<p align="center">
  <img src="Visuals\Ev dashborad overview 2.png" alt="Overview Tab" width="30%" style="margin-right:10px;">
  <img src="Visuals\EV Charging stations.png" alt="Insights Tab" width="30%" style="margin-right:10px;">
  <img src="Visuals\Ev visuals .png" alt="Map Tab" width="30%">
</p>

<p align="center">
  <b>Figure:</b> Overview | EV Charging Stations | Visualized Insights
</p>


---

## 🧑‍💻 Author

**Authored by Collins Ogombo**  
📧 collinsogomboochiko@gmail.com  
🌐 https://github.com/Ogombo-collins

---

## ⚖️ License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with attribution.

```
MIT License

Copyright (c) 2025 Collins Ogombo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
