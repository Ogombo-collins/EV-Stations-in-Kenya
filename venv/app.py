
# LIBRARIES
import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Kenya's EV Charging Infrastructure Dataset",
    page_icon="⚡",
    layout="wide",
)

# =====================================================
# GLOBAL CSS (Light theme: white background, muted blue headers, soft gray cards)
# =====================================================
st.markdown(
    """
    <style>
    /* Page background & typography */
    .reportview-container, .main {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        color: #111827;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    h1, h2, h3, h4, h5 {
        color: #1f2937;
    }
    /* Tabs spacing */
    .stTabs [data-baseweb="tab-list"] {
        gap: 18px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        padding-left: 18px;
        padding-right: 18px;
        font-weight: 600;
    }
    /* Cards */
    .metric-card, .station-card, .review-card, .insight-box {
        background: white;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 6px 18px rgba(15,23,42,0.04);
    }
    .metric-card h2 {
        margin: 0;
    }
    .small-muted {
        color: #6b7280;
        font-size: 0.92rem;
    }
    .pill {
        display:inline-block;
        padding:6px 10px;
        border-radius: 999px;
        font-size: 0.85rem;
    }
    a {
        color: #2563eb;
    }
    /* Responsive tweaks */
    @media (max-width: 600px) {
        .stTabs [data-baseweb="tab"] {
            height: 44px;
            font-size: 14px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# DATA: Main dataset
# =====================================================
charging_stations = [
    # NAIROBI & ENVIRONS STATIONS
    {
        "id": 1,
        "name": "Stima Plaza",
        "provider": "Kenya Power",
        "county": "Nairobi",
        "location": "Parklands, Nairobi",
        "coordinates": "-1.2641, 36.8161",
        "charger_types": ["50kW DC Fast Charger", "22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "Free",
        "payment_methods": ["RFID Card"],
        "car_models": ["BYD e6", "Hyundai Kona Electric", "Nissan Leaf", "Renault Zoe", "All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.5,
        "reviews": [
            {"user": "John K.", "rating": 5, "comment": "Fast charging, no cost. Great initiative by Kenya Power!"},
            {"user": "Mary N.", "rating": 4, "comment": "Convenient location but sometimes busy during peak hours"},
            {"user": "Peter M.", "rating": 5, "comment": "The DC fast charger is excellent. Charged my Nissan Leaf in under an hour"},
            {"user": "Grace W.", "rating": 4, "comment": "Need to get RFID card first which takes a bit of time"}
        ]
    },
    {
        "id": 2,
        "name": "Ruaraka Depot",
        "provider": "Kenya Power",
        "county": "Nairobi",
        "location": "Ruaraka, Nairobi",
        "coordinates": "-1.2567, 36.8833",
        "charger_types": ["50kW DC Fast Charger", "22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "Free",
        "payment_methods": ["RFID Card"],
        "car_models": ["BYD e6", "Hyundai Kona Electric", "Nissan Leaf", "Renault Zoe", "All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.3,
        "reviews": [
            {"user": "Sarah L.", "rating": 4, "comment": "Good location for those in Eastlands. Free charging is a bonus"},
            {"user": "James K.", "rating": 5, "comment": "Never had to wait. Always available"},
            {"user": "Faith M.", "rating": 4, "comment": "Great facility but signage could be better"},
            {"user": "Michael T.", "rating": 4, "comment": "Consistent service. Appreciate the free access"}
        ]
    },
    {
        "id": 3,
        "name": "Donholm Depot",
        "provider": "Kenya Power",
        "county": "Nairobi",
        "location": "Donholm, Nairobi",
        "coordinates": "-1.2937, 36.9006",
        "charger_types": ["50kW DC Fast Charger", "22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "Free",
        "payment_methods": ["RFID Card"],
        "car_models": ["BYD e6", "Hyundai Kona Electric", "Nissan Leaf", "Renault Zoe", "All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.2,
        "reviews": [
            {"user": "Melisa L.", "rating": 4, "comment": "Nice to have charging port for those in Eastlands. Free charging is a bonus"},
            {"user": "Mwangi K.", "rating": 5, "comment": "Charging is fast."},
            {"user": "Otieno M.", "rating": 4, "comment": "Loved the experience."},
            {"user": "Wafula T.", "rating": 4, "comment": "Appreciate the free cost."}
        ]
    },
    {
        "id": 4,
        "name": "Ragati Depot",
        "provider": "Kenya Power",
        "county": "Nairobi",
        "location": "Ragati - Upperhill, Nairobi",
        "coordinates": "-1.29558, 36.81281",
        "charger_types": ["50kW DC Fast Charger", "22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "Free",
        "payment_methods": ["RFID Card"],
        "car_models": ["BYD e6", "Hyundai Kona Electric", "Nissan Leaf", "Renault Zoe", "All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.1,
        "reviews": [
            {"user": "Sam L.", "rating": 4, "comment": "I love that I's free."},
            {"user": "Wairimu K.", "rating": 5, "comment": "Charging is convenient for me, easily acessible from where I live."},
            {"user": "Omondi M.", "rating": 5, "comment": "Fast charging."},
            {"user": "Neksesa T.", "rating": 4, "comment": "Good customer service."}
        ]
    },
    {
        "id": 5,
        "name": "TotalEnergies-Roam Hub Lusaka Road",
        "provider": "TotalEnergies | Roam-electric",
        "county": "Nairobi",
        "location": "Lusaka Road, Nairobi",
        "coordinates": "-1.30124, 36.83284",
        "charger_types": ["22kW AC Charger", "Battery Swap for motorcycles"],
        "number_of_ports": 2,
        "pricing": "KSh 20-50 per kWh (varies by time)",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.3,
        "reviews": [
            {"user": "George Ooko", "rating": 5, "comment": "Nice battery service"},
            {"user": "Felix Mesa", "rating": 4, "comment": "Works only for electric bikes none for cars yet."},
            {"user": "Alex Tobosore", "rating": 5, "comment": "Best customer service and fastest #roam"},
            {"user": "Naomi Adhiambo", "rating": 4, "comment": "Easy to use"}
        ]
    },
    {
        "id": 6,
        "name": "TotalEnergies-Roam Hub Waiyaki Way",
        "provider": "TotalEnergies | Roam-electric",
        "county": "Nairobi",
        "location": "Waiyaki Way, Nairobi",
        "coordinates": "-1.25789, 36.78216",
        "charger_types": ["22kW AC Charger", "Battery Swap for motorcycles"],
        "number_of_ports": 2,
        "pricing": "KSh 20-50 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available at the hub"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.7,
        "reviews": [
            {"user": "Kelvin Khalakuli", "rating": 5, "comment": "Easy charging"},
            {"user": "James Chege", "rating": 5, "comment": "Very good services. Excellent!"}
        ]
    },
    {
        "id": 7,
        "name": "TotalEnergies - Ampersand Dagoretti Swap Station",
        "provider": "TotalEnergies | Ampersand-energy",
        "county": "Nairobi",
        "location": "Dagoretti, Nairobi",
        "coordinates": "-1.29547, 36.75867",
        "charger_types": ["Battery Swap for motorcycles"],
        "number_of_ports": 0,
        "pricing": "KSh 200 - 300 for 90-110 km of range",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "7:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": [{"user": "Kenedy Munene", "rating": 5, "comment": "Succesful charge"}]
    },
    {
        "id": 8,
        "name": "TotalEnergies - Ampersand Mountain View Swap Station",
        "provider": "TotalEnergies | Ampersand-energy",
        "county": "Nairobi",
        "location": "Mountain View - Kangemi, Nairobi",
        "coordinates": "-1.26081, 36.73841",
        "charger_types": ["Battery Swap for motorcycles"],
        "number_of_ports": 0,
        "pricing": "KSh 200 - 300 for 90-110 km of range",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "7:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 0,
        "reviews": []
    },
    {
        "id": 9,
        "name": "TotalEnergies - Ampersand Starehe Swap Station",
        "provider": "TotalEnergies | Ampersand-energy",
        "county": "Nairobi",
        "location": "Starehe, Nairobi",
        "coordinates": "-1.27739, 36.83708",
        "charger_types": ["Battery Swap for motorcycles"],
        "number_of_ports": 3,
        "pricing": "KSh 200 - 300 for 90-110 km of range",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "7:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": [{"user": "Maxwell Murigi", "rating": 5, "comment": "Succesful charge"}]
    },
    {
        "id": 10,
        "name": "TotalEnergies - Ampersand Hurlingham Swap Station",
        "provider": "TotalEnergies | Ampersand-energy",
        "county": "Nairobi",
        "location": "Hurligham, Nairobi",
        "coordinates": "-1.28874, 36.80090",
        "charger_types": ["Battery Swap for motorcycles"],
        "number_of_ports": 3,
        "pricing": "KSh 200 - 300 for 90-110 km of range",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "7:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 1.0,
        "reviews": []
    },
    {
        "id": 11,
        "name": "TotalEnergies Roam Hub Karambe",
        "provider": "TotalEnergies | Roam-electric",
        "county": "Nairobi",
        "location": "Total Energies Karambe, Juja Road, Nairobi",
        "coordinates": "-1.25930, 36.84510",
        "charger_types": ["22kW AC Charger", "Battery Swap for motorcycles"],
        "number_of_ports": 3,
        "pricing": "KSh 20-50 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available at the hub. Charging for Roam's electric buses takes place at Roam warehouse"],
        "motorcycle_support": True,
        "operating_hours": "6:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": [
            {"user": "Hezron Gitundu", "rating": 5, "comment": "Good service"},
            {"user": "Melisa wamathai", "rating": 4, "comment": "Fast charging"}
        ]
    },
    {
        "id": 12,
        "name": "TotalEnergies - Roam Shop Machakos",
        "provider": "TotalEnergies | Roam-electric",
        "county": "Machakos",
        "location": "TotalEnergies Mua View Service Station, Machakos",
        "coordinates": "-1.52769, 37.20937",
        "charger_types": ["22kW AC Charger", "Battery Swap for motorcycles"],
        "number_of_ports": 3,
        "pricing": "KSh 20-50 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available at the hub"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": []
    },
    {
        "id": 13,
        "name": "BasiGo Buru Buru",
        "provider": "BasiGo",
        "county": "Nairobi",
        "location": "Buru Buru, Nairobi",
        "coordinates": "-1.3142, 36.8875",
        "charger_types": ["DC Fast Charger (Multiple)", "CCS-2 Compatible"],
        "number_of_ports": 6,
        "pricing": "Subscription-Based",
        "payment_methods": ["Corporate Account", "M-Pesa"],
        "car_models": ["Electric Buses", "Electric Vans(Matatus)",  "All CCS compatible Persenger Cars & Trucks"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.6,
        "reviews": [
            {"user": "Salim Ngoma", "rating": 5, "comment": "🔌 very efficient..."},
            {"user": "Stephen Murithi", "rating": 5, "comment": "Buru...nice n safe"},
            {"user": "Apiyo Malcolm", "rating": 4, "comment": "Successful charge"}
        ]
    },
    {
        "id": 14,
        "name": "BasiGo Depot - Embakasi",
        "provider": "BasiGo",
        "county": "Nairobi",
        "location": "Embakasi, Nairobi",
        "coordinates": "-1.3167, 36.9167",
        "charger_types": ["DC Fast Charger", "CCS-2"],
        "number_of_ports": 4,
        "pricing": "Subscription-Based",
        "payment_methods": ["Corporate Account", "M-Pesa"],
        "car_models": ["Electric Buses", "Electric Vans(Matatus)", "All CCS compatible Persenger Cars & Trucks"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": [
            {"user": "Moses Nderitu", "rating": 5, "comment": "Get your EV charged here"},
            {"user": "Felix Muendo", "rating": 3, "comment": "How much for a full charge?"}
        ]
    },
    {
        "id": 15,
        "name": "BasiGo Charging Station Kikuyu",
        "provider": "BasiGo",
        "county": "Kiambu",
        "location": "Kikuyu, Kiambu County (Greater Nairobi)",
        "coordinates": "-1.2417, 36.6667",
        "charger_types": ["DC Fast Charger", "CCS-2"],
        "number_of_ports": 4,
        "pricing": "Subscription-Based",
        "payment_methods": ["Corporate Account", "M-Pesa"],
        "car_models": ["Electric Buses", "Electric Vans(Matatus)", "All CCS compatible Persenger Cars & Trucks"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.5,
        "reviews": [
            {"user": "Faith Kamau", "rating": 5, "comment": "Finding charger very easy"},
            {"user": "Joseph M.", "rating": 4, "comment": "Clean and efficient service"}
        ]
    },
    {
        "id": 16,
        "name": "Roam Hub - Suguta Center",
        "provider": "Roam Electric",
        "county": "Nairobi",
        "location": "Kileleshwa, inside Suguta Center, Nairobi",
        "coordinates": "-1.28590, 36.77855",
        "charger_types": ["AC Charger for motorcycles", "Battery Swap"],
        "number_of_ports": 2,
        "pricing": "Subscription-based for motorcycles",
        "payment_methods": ["M-Pesa", "Roam App", "Debit/Credit Card"],
        "car_models": ["Limited car support"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.0,
        "reviews": [
            {"user": "Benedict", "rating": 5, "comment": "Successful charge"},
            {"user": "Michael Otieno", "rating": 5, "comment": "Convenient access."}
        ]
    },
    {
        "id": 17,
        "name": "Roam Hub - Kayole",
        "provider": "Roam Electric",
        "county": "Nairobi",
        "location": "Kayole Spine Road, Nairobi",
        "coordinates": "-1.28145, 36.90510",
        "charger_types": ["AC Charger for motorcycles", "Battery Swap"],
        "number_of_ports": 2,
        "pricing": "Subscription-based for motorcycles",
        "payment_methods": ["M-Pesa", "Roam App", "Debit/Credit Card"],
        "car_models": ["Limited car support"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.7,
        "reviews": [
            {"user": "George Ooko", "rating": 5, "comment": "Great services done here"},
            {"user": "Seth Busolo", "rating": 3, "comment": "Wait time up to 10 minutes"}
        ]
    },
    {
        "id": 18,
        "name": "Roam Hub - Quickmart Roysambu",
        "provider": "Roam Electric | Quickmart",
        "county": "Nairobi",
        "location": "QuickMart Roysambu, Nairobi",
        "coordinates": "-1.20784, 36.89363",
        "charger_types": ["AC Charger for motorcycles", "Battery Swap"],
        "number_of_ports": 2,
        "pricing": "Subscription-based for motorcycles",
        "payment_methods": ["M-Pesa", "Roam App", "Debit/Credit Card"],
        "car_models": ["Limited car support"],
        "motorcycle_support": True,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.2,
        "reviews": [
            {"user": "Clive Mudavadi", "rating": 5, "comment": "Quick. No wait time."},
            {"user": "Phillip Kuria", "rating": 1, "comment": "There are not enough betters, we ask that we be given better, and the changes are already there, let's not reduce the changes to make it better."},
            {"user": "Livingstone Wagura", "rating": 5, "comment": "Successful charge."}
        ]
    },
    {
        "id": 19,
        "name": "Ampersand - Kangundo Road Swap",
        "provider": "Ampersand",
        "county": "Nairobi",
        "location": "Kangundo Rd, Nairobi",
        "coordinates": "-1.27358, 36.88287",
        "charger_types": ["Battery Swap for motorcycles"],
        "number_of_ports": 3,
        "pricing": "KSh 200 - 300 for 90-110 km of range",
        "payment_methods": ["M-Pesa", "Credit Card", "Debit Card"],
        "car_models": ["Not available"],
        "motorcycle_support": True,
        "operating_hours": "7:00 AM - 10:00 PM",
        "status": "Operational",
        "avg_rating": 3.7,
        "reviews": [{"user": "Onormous G.", "rating": 5, "comment": "You should be 24hrs."},
            {"user": "Cliff", "rating": 5, "comment": "Successful charge"}]
    },
    {
        "id": 20,
        "name": "Waterfront Mall EVChaja",
        "provider": "EVChaja",
        "county": "Nairobi",
        "location": "Waterfront Mall, Karen",
        "coordinates": "-1.3311, 36.7122",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 25-40 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "EVChaja App"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False,
        "operating_hours": "9:00 AM - 9:00 PM (Mall hours)",
        "status": "Operational",
        "avg_rating": 4.3,
        "reviews": [
            {"user": "Joash Mayaka", "rating": 5, "comment": "Good place to be"},
            {"user": "Felix Otieno", "rating": 3, "comment": "It's free"}
        ]
    },
    {
        "id": 21,
        "name": "Adlife Plaza EVChaja",
        "provider": "EVChaja",
        "county": "Nairobi",
        "location": "Adlife Plaza, Kilimani",
        "coordinates": "-1.29135, 36.78602",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 25-40 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "EVChaja App"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False,
        "operating_hours": "9:00 AM - 9:00 PM (Mall hours)",
        "status": "Operational",
        "avg_rating": 4.3,
        "reviews": []
    },
    {
        "id": 22,
        "name": "Two Rivers Mall EVChaja",
        "provider": "EVChaja",
        "county": "Nairobi",
        "location": "Two Rivers Mall, Limuru Rd Ruaka",
        "coordinates": "-1.20760, 36.79377",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 25-40 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "EVChaja App"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 5.0,
        "reviews": [ {"user": "Dancun Mutuku", "rating": 5, "comment": "Nice one"},
            {"user": "James Ngala", "rating": 5, "comment": "Succesful charge"}]
    },
    {
        "id": 23,
        "name": "The Hub Nairobi",
        "provider": "Independent",
        "county": "Nairobi",
        "location": "The Hub, Karen",
        "coordinates": "-1.3186, 36.7031",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 30-45 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf"],
        "motorcycle_support": False,
        "operating_hours": "8:00 AM - 8:00 PM",
        "status": "Operational",
        "avg_rating": 4.2,
        "reviews": [
            {"user": "Simon P.", "rating": 4, "comment": "Nice ambiance while charging. A bit pricey"},
            {"user": "Linda M.", "rating": 4, "comment": "Good service but can be busy"}
        ]
    },
    # Kisumu / Mombasa / Highway & Planned entries
    {
        "id": 24,
        "name": "Kenya Power Kisumu",
        "provider": "Kenya Power",
        "county": "Kisumu",
        "location": "Kisumu Town (Exact location TBD)",
        "coordinates": "-0.0917, 34.7680",
        "charger_types": ["DC Fast Charger (Planned)"],
        "number_of_ports": 2,
        "pricing": "To be announced",
        "payment_methods": ["TBD"],
        "car_models": ["All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "TBD",
        "status": "Planned (2025-2026)",
        "avg_rating": None,
        "reviews": []
    },
    {
        "id": 25,
        "name": "TotalEnergies Kisumu",
        "provider": "TotalEnergies",
        "county": "Kisumu",
        "location": "Kisumu (Station expansion planned)",
        "coordinates": "-0.0917, 34.7680",
        "charger_types": ["22kW AC Charger (Planned)"],
        "number_of_ports": 2,
        "pricing": "Similar to Nairobi rates expected",
        "payment_methods": ["M-Pesa", "Credit Card (Expected)"],
        "car_models": ["All Type 2 compatible"],
        "motorcycle_support": True,
        "operating_hours": "TBD",
        "status": "Planned (2025)",
        "avg_rating": None,
        "reviews": []
    },
    {
        "id": 26,
        "name": "Megacity Mall EvChaja",
        "provider": "EVChaja",
        "county": "Kisumu",
        "location": "Kisumu",
        "coordinates": "-0.10621, 34.77050",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 25-40 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "EVChaja App"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False,
        "operating_hours": "8:30 AM - 8:30 PM",
        "status": "Operational",
        "avg_rating": 4.0,
        "reviews": [ {"user": "FG", "rating": 5, "comment": "Very convenient, free to use and located right at the new entrance."}]
    },
    {
        "id": 27,
        "name": "Kenya Power Mombasa",
        "provider": "Kenya Power",
        "county": "Mombasa",
        "location": "Mombasa Town (Exact location TBD)",
        "coordinates": "-4.0435, 39.6682",
        "charger_types": ["DC Fast Charger (Planned)"],
        "number_of_ports": 3,
        "pricing": "To be announced",
        "payment_methods": ["TBD"],
        "car_models": ["All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "TBD",
        "status": "Planned (2025-2026)",
        "avg_rating": None,
        "reviews": []
    },
    {
        "id": 28,
        "name": "Highway Charging - Mtito Andei",
        "provider": "Kenya Power",
        "county": "Makueni",
        "location": "Mtito Andei (Nairobi-Mombasa Highway)",
        "coordinates": "-2.6908, 38.1667",
        "charger_types": ["DC Fast Charger (Planned)"],
        "number_of_ports": 4,
        "pricing": "To be announced",
        "payment_methods": ["M-Pesa", "RFID Card (Expected)"],
        "car_models": ["All CCS compatible EVs"],
        "motorcycle_support": False,
        "operating_hours": "24/7 (Planned)",
        "status": "Planned (2025-2026)",
        "avg_rating": None,
        "reviews": []
    },
    {
        "id": 29,
        "name": "City Mall EvChaja",
        "provider": "EVChaja",
        "county": "Mombasa",
        "location": "City Mall Exit Gate, Malindi Road Mombasa",
        "coordinates": "-4.01975, 39.72048",
        "charger_types": ["22kW AC Charger"],
        "number_of_ports": 2,
        "pricing": "KSh 25-40 per kWh",
        "payment_methods": ["M-Pesa", "Credit Card", "EVChaja App"],
        "car_models": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False,
        "operating_hours": "24/7",
        "status": "Operational",
        "avg_rating": 4.0,
        "reviews": [ {"user": "TJ", "rating": 5, "comment": "Very convenient for me."}]
    },
]

# =====================================================
# PROVIDER SUMMARY 
# =====================================================
provider_summary = {
    "Kenya Power": {
        "total_stations": 7,
        "total_ports": 17,
        "counties": ["Nairobi", "Kisumu", "Mombasa", "Makueni"],
        "operational": 4,
        "planned": 45,
        "avg_rating": 2.4,
        "price_range": "Free",
        "car_support": ["BYD e6", "Hyundai Kona Electric", "Nissan Leaf", "Renault Zoe", "All CCS compatible"],
        "motorcycle_support": False
    },
    "Roam Electric": {
        "total_stations": 2,
        "total_ports": 4,
        "counties": ["Nairobi"],
        "operational": 2,
        "planned": 0,
        "avg_rating": 4.4,
        "price_range": "Subscription-Based",
        "car_support": ["Limited car support"],
        "motorcycle_support": True
    },
    "Ampersand": {
        "total_stations": 1,
        "total_ports": 3,
        "counties": ["Nairobi", "Kiambu"],
        "operational": 1,
        "planned": 0,
        "avg_rating": 4.2,
        "price_range": "KSh 200 - 300 for 90-110 km of range",
        "car_support": ["Not available"],
        "motorcycle_support": True
    },
    "TotalEnergies | Ampersand-energy": {
        "total_stations": 4,
        "total_ports": 6,
        "counties": ["Nairobi"],
        "operational": 4,
        "planned": 0,
        "avg_rating": 2.8,
        "price_range": "KSh 200 - 300 for 90-110 km of range",
        "car_support": ["Not available"],
        "motorcycle_support": True
    },
    "TotalEnergies | Roam-electric": {
        "total_stations": 4,
        "total_ports": 10,
        "counties": ["Nairobi", "Machakos"],
        "operational": 4,
        "planned": 1,
        "avg_rating": 4.8,
        "price_range": "KSh 20-50 per kWh",
        "car_support": ["Not available"],
        "motorcycle_support": True
    },
    "TotalEnergies": {
        "total_stations": 4,
        "total_ports": 11,
        "counties": ["Nairobi", "Kisumu"],
        "operational": 3,
        "planned": 1,
        "avg_rating": 4.2,
        "price_range": "KSh 20-50 per kWh",
        "car_support": ["BYD e6", "Nissan Leaf", "MG ZS EV", "All Type 2"],
        "motorcycle_support": True
    },
    "BasiGo": {
        "total_stations": 3,
        "total_ports": 14,
        "counties": ["Nairobi"],
        "operational": 3,
        "planned": 16,
        "avg_rating": 4.7,
        "price_range": "Subscription-Based",
        "car_support": ["Electric Buses", "Electric Vans(Matatus)",  "All CCS compatible Cars & Trucks"],
        "motorcycle_support": False
    },
    "Roam Electric | Quickmart": {
        "total_stations": 1,
        "total_ports": 2,
        "counties": ["Nairobi"],
        "operational": 1,
        "planned": 0,
        "avg_rating": 4.2,
        "price_range": "Subscription-Based",
        "car_support": ["Limited car support"],
        "motorcycle_support": True
    },
    "EVChaja": {
        "total_stations": 5,
        "total_ports": 2,
        "counties": ["Nairobi", "Kisumu", "Mombasa"],
        "operational": 5,
        "planned": 0,
        "avg_rating": 4.3,
        "price_range": "KSh 25-40 per kWh",
        "car_support": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False
    },
    "Independent": {
        "total_stations": 1,
        "total_ports": 2,
        "counties": ["Nairobi"],
        "operational": 1,
        "planned": 0,
        "avg_rating": 4.2,
        "price_range": "KSh 30-45 per kWh",
        "car_support": ["NETA V", "BYD e6", "Nissan Leaf", "All Type 2"],
        "motorcycle_support": False
    }
}

# =====================================================
# COUNTY STATISTICS 
# =====================================================
county_stats = {
    "Nairobi": {"total_stations": 21, "operational_stations": 21, "total_ports": 48, "avg_rating": 4.1},
    "Kisumu": {"total_stations": 3, "operational_stations": 1, "total_ports": 6, "avg_rating": 1.3},
    "Machakos": {"total_stations": 1, "operational_stations": 1, "total_ports": 3, "avg_rating": 5.0},
    "Kiambu": {"total_stations": 1, "operational_stations": 1, "total_ports": 4, "avg_rating": 4.5},
    "Makueni": {"total_stations": 1, "operational_stations": 0, "total_ports": 3, "avg_rating": 0.0},
    "Mombasa": {"total_stations": 2, "operational_stations": 1, "total_ports": 5, "avg_rating": 2.0},
}

# =====================================================
# HELPER FUNCTIONS 
# =====================================================
def convert_to_dataframe(stations):
    """Convert charging stations list to pandas DataFrame"""
    df_data = []
    for station in stations:
        df_data.append({
            'Station Name': station.get('name'),
            'Provider': station.get('provider'),
            'County': station.get('county'),
            'Location': station.get('location'),
            'Coordinates': station.get('coordinates'),
            'Charger Types': ', '.join(station.get('charger_types', [])),
            'Number of Ports': station.get('number_of_ports'),
            'Pricing': station.get('pricing'),
            'Payment Methods': ', '.join(station.get('payment_methods', [])),
            'Car Models Supported': ', '.join(station.get('car_models', [])),
            'Motorcycle Support': station.get('motorcycle_support'),
            'Operating Hours': station.get('operating_hours'),
            'Status': station.get('status'),
            'Average Rating': station.get('avg_rating') if station.get('avg_rating') is not None else 'N/A'
        })
    return pd.DataFrame(df_data)


def get_filtered_stations(county_filter, provider_filter):
    """Filter stations based on county and provider"""
    filtered = charging_stations
    if county_filter and county_filter != "All Counties":
        filtered = [s for s in filtered if s.get('county') == county_filter]
    if provider_filter and provider_filter != "All Providers":
        filtered = [s for s in filtered if s.get('provider') == provider_filter]
    return filtered


def create_provider_distribution_chart(stations):
    """Create provider distribution pie chart for operational stations"""
    provider_counts = {}
    for station in stations:
        if station.get('status') and 'Operational' in station.get('status'):
            provider = station.get('provider', 'Unknown')
            provider_counts[provider] = provider_counts.get(provider, 0) + 1

    labels = list(provider_counts.keys())
    values = list(provider_counts.values())

    # safe fallback if no data
    if not labels:
        labels = ['No Operational Stations']
        values = [1]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_traces(textinfo='percent')
    fig.update_layout(title_text="Segmenting Operational Stations by Provider", height=420, showlegend=True)
    return fig


def create_ports_by_county_chart(county_stats_dict):
    """Create grouped bar chart of ports and operational stations by county"""
    counties = list(county_stats_dict.keys())
    ports = [county_stats_dict[c]['total_ports'] for c in counties]
    operational = [county_stats_dict[c]['operational_stations'] for c in counties]

    fig = go.Figure(data=[
        go.Bar(name='Total Ports', x=counties, y=ports),
        go.Bar(name='Operational Stations', x=counties, y=operational)
    ])
    fig.update_layout(title_text="Number of EV Charging Stations by County", barmode='group', height=420,
                      xaxis_title="County", yaxis_title="Count")
    return fig


def create_rating_distribution(stations):
    """Create histogram of station ratings (exclude None)"""
    ratings = [s.get('avg_rating') for s in stations if s.get('avg_rating') is not None]
    if not ratings:
        ratings = [0]
    fig = go.Figure(data=[go.Histogram(x=ratings, nbinsx=10, opacity=0.8)])
    fig.update_layout(title_text="Charging Stations' Rating Distribution", xaxis_title="Rating",
                      yaxis_title="Number of Stations", height=360)
    return fig


def create_map_visualization(stations):
    """Create interactive scatter mapbox visualization using plotly"""
    operational_stations = [s for s in stations if s.get('status') and 'Operational' in s.get('status')]
    lats, lons, names, providers, ratings = [], [], [], [], []
    for stn in operational_stations:
        coords = stn.get('coordinates', '')
        # handle splitting when comma+space or comma
        parts = [p.strip() for p in coords.split(',') if p.strip()]
        if len(parts) == 2:
            try:
                lats.append(float(parts[0])); lons.append(float(parts[1]))
            except ValueError:
                continue
            names.append(stn.get('name'))
            providers.append(stn.get('provider'))
            ratings.append(stn.get('avg_rating') if stn.get('avg_rating') is not None else 0)

    df_map = pd.DataFrame({'lat': lats, 'lon': lons, 'name': names, 'provider': providers, 'rating': ratings})
    if df_map.empty:
        # Return a placeholder empty figure
        fig = go.Figure()
        fig.update_layout(title="No operational station coordinates available", height=420)
        return fig

    fig = px.scatter_mapbox(df_map, lat='lat', lon='lon', hover_name='name',
                            hover_data={'provider': True, 'rating': True, 'lat': False, 'lon': False},
                            color='provider', size='rating', size_max=16, zoom=9, height=500)
    fig.update_layout(mapbox_style="open-street-map", margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def render_review_card(review, show_station_info=True):
    """Return HTML for a single review card."""
    station_info_html = ""
    if show_station_info:
        station_info_html = f"<p class='small-muted' style='margin: 0 0 8px 0;'>{review.get('station_name', '')}{(' • ' + review.get('county')) if review.get('county') else ''}</p>"
    user = review.get('user', 'Anonymous')
    rating = review.get('rating', 'N/A')
    comment = review.get('comment', '')
    return f"""
        <div class='review-card'>
            <div style='display:flex; justify-content:space-between; margin-bottom:8px;'>
                <strong style='color:#111827'>{user}</strong>
                <span style='color:#fbbf24;'>★ {rating}</span>
            </div>
            {station_info_html}
            <p style='color:#4b5563; margin:0;'>{comment}</p>
        </div>
    """


# =====================================================
# MAIN APP
# =====================================================
def main():
    # -----------------------------
    # DYNAMIC METRICS
    # -----------------------------
    total_stations = len(charging_stations)
    operational_stations = len([s for s in charging_stations if s.get('status') and 'Operational' in s.get('status')])
    total_ports = sum((s.get('number_of_ports') or 0) for s in charging_stations)
    active_ports = sum((s.get('number_of_ports') or 0) for s in charging_stations if s.get('status') and 'Operational' in s.get('status'))
    counties_covered = len(county_stats.keys())
    rated_stations = [s.get('avg_rating') for s in charging_stations if s.get('avg_rating') is not None]
    avg_rating = round(sum(rated_stations) / len(rated_stations), 1) if rated_stations else "N/A"

    # -----------------------------
    # Header Tab
    # -----------------------------
    st.markdown(
        """
        <div style='background: white; padding: 24px; border-radius: 12px; box-shadow: 0 8px 24px rgba(15,23,42,0.04);'>
            <h1 style='margin: 0 0 6px 0;'>⚡ Kenya's EV Charging Infrastructure</h1>
            <p class='small-muted' style='margin:0;'>Mapping a Sample of ~29 EV Charging Stations Across Kenya as at October 2025</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")  

    # -----------------------------
    # Download Buttons(CSV + JSON Format)
    # -----------------------------
    col_a, col_b, col_c = st.columns([1, 1, 4])
    df_full = convert_to_dataframe(charging_stations)

    with col_a:
        csv = df_full.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download CSV", data=csv, file_name="kenya_ev_charging_infrastructure.csv", mime="text/csv")

    with col_b:
        json_data = {
            "metadata": {
                "title": "Kenya's EV Charging Infrastructure Sample Dataset",
                "date": "October 2025",
                "source": "Compiled from Kenya Power, Ampersand, TotalEnergies, BasiGo, Roam, EVChaja",
                "total_stations": total_stations,
                "operational_stations": operational_stations
            },
            "stations": charging_stations,
            "provider_summary": provider_summary,
            "county_statistics": county_stats
        }
        json_str = json.dumps(json_data, indent=2)
        st.download_button(label="📥 Download JSON", data=json_str, file_name="kenya_ev_charging_infrastructure.json", mime="application/json")

    # -----------------------------
    # TABS 
    # -----------------------------
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🔢 Overview",
        "📈 Visualizations",
        "🔌 Stations",
        "🔋 Brands",
        "🏙️ Counties",
        "⭐ Reviews",
        "💡 Insights"
    ])

    # =====================================================
    # TAB 1: OVERVIEW
    # =====================================================
    with tab1:
        st.markdown("### Key Metrics", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f"<div class='metric-card'><h2 style='color:#10b981'>{total_stations}</h2><p class='small-muted'>Total Stations<br><span style='font-size:12px; color:#9ca3af'>{operational_stations} Operational</span></p></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='metric-card'><h2 style='color:#3b82f6'>{total_ports}</h2><p class='small-muted'>Charging Ports<br><span style='font-size:12px; color:#9ca3af'>{active_ports} Active</span></p></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='metric-card'><h2 style='color:#8b5cf6'>{counties_covered}</h2><p class='small-muted'>Counties Covered<br><span style='font-size:12px; color:#9ca3af'>Nairobi, Kisumu, Mombasa, Kiambu, Makueni, Machakos</span></p></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='metric-card'><h2 style='color:#f97316'>{avg_rating}</h2><p class='small-muted'>Average Rating<br><span style='font-size:12px; color:#9ca3af'>From user reviews</span></p></div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Dataset Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                "<div class='station-card'><h4 style='margin:0 0 8px 0;'>Coverage</h4>"
                "<ul style='color:#4b5563; line-height:1.7;'>"
                "<li><strong>Nairobi:</strong> 21 operational stations with detailed locations and reviews</li>"
                "<li><strong>Kisumu:</strong> 1 operational station, and 2 planned stations</li>"
                "<li><strong>Mombasa:</strong> 1 operational station, and 1 planned station</li>"
                "<li><strong>Kiambu, Makueni & Machakos:</strong> Kiambu and Machakos have 1 operational station, while Makueni has 1 planned station</li>"
                "</ul></div>",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                "<div class='station-card'><h4 style='margin:0 0 8px 0;'>Data Points Included</h4>"
                "<ul style='color:#4b5563; line-height:1.7;'>"
                "<li>Exact GPS coordinates for all stations</li>"
                "<li>Number and types of charging ports</li>"
                "<li>Pricing information (where available)</li>"
                "<li>Compatible car models and EV brands</li>"
                "<li>User ratings and sample reviews</li>"
                "<li>Payment methods accepted</li>"
                "</ul></div>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown(
            "<div style='background:linear-gradient(135deg,#eef2ff 0%,#f0f9ff 100%); padding:14px; border-radius:10px;'>"
            "<strong>Data Sources & Methodology:</strong> Compiled from Kenya Power, Ampersand, TotalEnergies Kenya, BasiGo, Roam Electric, and EVChaja in October 2025."
            "</div>", unsafe_allow_html=True
        )

    # =====================================================
    # TAB 2: VISUALIZATIONS
    # =====================================================
    with tab2:
        st.markdown("### Visualizations")
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            st.plotly_chart(create_provider_distribution_chart(charging_stations), use_container_width=True)
        with r1c2:
            st.plotly_chart(create_ports_by_county_chart(county_stats), use_container_width=True)

        st.markdown("### Rating distribution")
        st.plotly_chart(create_rating_distribution(charging_stations), use_container_width=True)

        st.markdown("### Provider Comparison")
        comparison_data = []
        for provider, data in provider_summary.items():
            comparison_data.append({
                'Provider': provider,
                'Stations': data.get('total_stations', 0),
                'Ports': data.get('total_ports', 0),
                'Operational': data.get('operational', 0),
                'Avg Rating': data.get('avg_rating', 'N/A'),
                'Motorcycle Support': '✓' if data.get('motorcycle_support') else '✗',
                'Price Range': data.get('price_range', 'N/A'),
            })
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, use_container_width=True, hide_index=True)

        st.markdown("### Operational Stations' Locations (Map)")
        st.plotly_chart(create_map_visualization(charging_stations), use_container_width=True)

    # =====================================================
    # TAB 3: STATIONS
    # =====================================================
    with tab3:
        st.markdown("### Charging Stations")
        # Filters
        county_options = ["All Counties"] + sorted(list({s.get('county') for s in charging_stations if s.get('county')}))
        provider_options = ["All Providers"] + sorted(list(provider_summary.keys()))
        col_f1, col_f2 = st.columns([2, 3])
        with col_f1:
            county_filter = st.selectbox("Filter by County", county_options)
        with col_f2:
            provider_filter = st.selectbox("Filter by Provider", provider_options)

        # Filter + Search
        filtered = get_filtered_stations(county_filter, provider_filter)
        st.markdown(f"**Showing {len(filtered)} station(s)**")

        # Download filtered
        df_filtered = convert_to_dataframe(filtered)
        st.download_button(label="📥 Download Filtered CSV", data=df_filtered.to_csv(index=False).encode('utf-8'),
                           file_name="filtered_stations.csv", mime="text/csv")

        # Display station cards
        for stn in filtered:
            status_label = stn.get('status', 'Unknown')
            status_color = "#10b981" if "Operational" in status_label else "#f97316"
            st.markdown(
                f"<div class='station-card' style='margin-bottom:12px;'>"
                f"<div style='display:flex; justify-content:space-between; align-items:flex-start;'>"
                f"<div><h4 style='margin:0;'>{stn.get('name')}</h4><div class='small-muted'>{stn.get('provider')}</div></div>"
                f"<div style='text-align:right;'><span class='pill' style='background:#f3f4f6; color:{status_color};'>{status_label}</span><div style='font-size:14px; margin-top:8px;'>"
                f"{'★ ' + str(stn.get('avg_rating')) if stn.get('avg_rating') is not None else ''}</div></div>"
                f"</div><div style='display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:12px;'>"
                f"<div><strong>📍 Location:</strong> {stn.get('location')}<br><strong>🌍 Coordinates:</strong> {stn.get('coordinates')}<br><strong>⚡ Chargers:</strong> {', '.join(stn.get('charger_types', []))}</div>"
                f"<div><strong>💰 Pricing:</strong> {stn.get('pricing')}<br><strong>💳 Payments:</strong> {', '.join(stn.get('payment_methods', []))}<br><strong>🏍️ Motorcycle:</strong> {'✓' if stn.get('motorcycle_support') else '✗'}</div>"
                f"</div></div>",
                unsafe_allow_html=True
            )

    # =====================================================
    # TAB 4: BRANDS (Providers)
    # =====================================================
    with tab4:
        st.markdown("### Provider Analysis")
        # Provider search / filter
        providers_list = sorted(list(provider_summary.keys()))
        chosen_provider = st.selectbox("Select Provider to view details", ["All Providers"] + providers_list)

        def _render_provider_card(brand, data):
            counties_text = ', '.join(data.get('counties', []))
            return f"""
            <div class='station-card' style='margin-bottom:12px;'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <h3 style='margin:0'>{brand}</h3>
                        <div class='small-muted'>{data.get('operational',0)} operational, {data.get('planned',0)} planned</div>
                    </div>
                    <div style='text-align:right;'>
                        <div style='background:#fff7ed; padding:8px 12px; border-radius:10px;'><strong style='font-size:18px;'>★ {data.get('avg_rating','N/A')}</strong></div>
                    </div>
                </div>
                <div style='display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-top:12px;'>
                    <div><strong>Infrastructure</strong><p class='small-muted' style='margin:6px 0 0 0;'>Stations: {data.get('total_stations')}</p><p class='small-muted' style='margin:6px 0 0 0;'>Total Ports: {data.get('total_ports')}</p><p class='small-muted' style='margin:6px 0 0 0;'>Counties: {counties_text}</p></div>
                    <div><strong>Pricing</strong><p class='small-muted' style='margin:6px 0 0 0;'>{data.get('price_range')}</p><p style='margin-top:12px;'><strong>Motorcycle Support</strong></p><p class='small-muted'>{'✓ Available' if data.get('motorcycle_support') else '✗ Not available'}</p></div>
                    <div><strong>Supported Vehicles</strong><p class='small-muted' style='margin:6px 0 0 0;'>{', '.join(data.get('car_support', []))}</p></div>
                </div>
            </div>
            """

        if chosen_provider == "All Providers":
            for brand, data in provider_summary.items():
                st.markdown(_render_provider_card(brand, data), unsafe_allow_html=True)
            # full providers table + download
            df_providers = pd.DataFrame([{
                "Provider": k,
                "Stations": v.get('total_stations'),
                "Ports": v.get('total_ports'),
                "Operational": v.get('operational'),
                "Planned": v.get('planned'),
                "Avg Rating": v.get('avg_rating'),
                "Price Range": v.get('price_range'),
                "Motorcycle Support": v.get('motorcycle_support')
            } for k, v in provider_summary.items()])
            st.download_button(label="📥 Download Providers CSV", data=df_providers.to_csv(index=False).encode('utf-8'),
                               file_name="provider_summary.csv", mime="text/csv")
            st.dataframe(df_providers, use_container_width=True)
        else:
            data = provider_summary.get(chosen_provider)
            if data:
                st.markdown(_render_provider_card(chosen_provider, data), unsafe_allow_html=True)
                # list stations for provider + download
                provider_stations = [s for s in charging_stations if s.get('provider') == chosen_provider]
                st.markdown(f"**Stations for {chosen_provider}: {len(provider_stations)}**")
                df_provider = convert_to_dataframe(provider_stations)
                st.dataframe(df_provider, use_container_width=True)
                st.download_button(label=f"📥 Download {chosen_provider} Stations", data=df_provider.to_csv(index=False).encode('utf-8'),
                                   file_name=f"{chosen_provider.replace(' ','_')}_stations.csv", mime="text/csv")
            else:
                st.info("No data available for the selected provider.")

    # =====================================================
    # TAB 5: COUNTIES
    # =====================================================
    with tab5:
        for county, stats in county_stats.items():
                st.markdown(f"""
                    <div class='station-card'>
                        <h3 style='color: #1f2937; margin-bottom: 20px;'>{county}</h3>
                        <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 20px;'>
                            <div style='background: #dbeafe; padding: 15px; border-radius: 8px;'>
                                <h4 style='color: #3b82f6; margin: 0; font-size: 24px;'>{stats['total_stations']}</h4>
                                <p style='color: #6b7280; margin: 5px 0 0 0; font-size: 13px;'>Total Stations</p>
                            </div>
                            <div style='background: #d1fae5; padding: 15px; border-radius: 8px;'>
                                <h4 style='color: #10b981; margin: 0; font-size: 24px;'>{stats['operational_stations']}</h4>
                                <p style='color: #6b7280; margin: 5px 0 0 0; font-size: 13px;'>Operational</p>
                            </div>
                            <div style='background: #e9d5ff; padding: 15px; border-radius: 8px;'>
                                <h4 style='color: #8b5cf6; margin: 0; font-size: 24px;'>{stats['total_ports']}</h4>
                                <p style='color: #6b7280; margin: 5px 0 0 0; font-size: 13px;'>Charging Ports</p>
                            </div>
                            <div style='background: #fef3c7; padding: 15px; border-radius: 8px;'>
                                <h4 style='color: #f59e0b; margin: 0; font-size: 24px;'>{stats['avg_rating'] if stats['avg_rating'] else 'N/A'}</h4>
                                <p style='color: #6b7280; margin: 5px 0 0 0; font-size: 13px;'>Avg Rating</p>
                            </div>
                        <!-- intentionally not closing the grid div or station-card div to avoid extra </div> -->
                """, unsafe_allow_html=True)
                
                # Stations in county
                county_stations = [s for s in charging_stations if s['county'] == county]
                
                st.markdown(f"<p style='font-weight: 600; color: #374151; margin: 15px 0 10px 0;'>Stations in {county}:</p>", unsafe_allow_html=True)
                
                cols = st.columns(2)
                for idx, station in enumerate(county_stations):
                    with cols[idx % 2]:
                        status_color = "#10b981" if station['status'] == "Operational" else "#f97316"
                        status_bg = "#d1fae5" if station['status'] == "Operational" else "#fed7aa"
                        
                        st.markdown(f"""
                            <div style='border: 1px solid #e5e7eb; padding: 12px; border-radius: 8px; margin-bottom: 10px;'>
                                <p style='font-weight: 600; color: #1f2937; margin: 0 0 3px 0;'>{station['name']}</p>
                                <p style='color: #6b7280; font-size: 13px; margin: 0 0 5px 0;'>{station['provider']}</p>
                                <p style='color: #9ca3af; font-size: 12px; margin: 0 0 8px 0;'>{station['location']}</p>
                                <div>
                                    <span style='background: {status_bg}; color: {status_color}; padding: 3px 8px; border-radius: 12px; font-size: 11px;'>
                                        {station['status']}
                                    </span>
                                    {f"<span style='color: #fbbf24; margin-left: 8px;'>★</span> <span style='font-size: 12px;'>{station['avg_rating']}</span>" if station['avg_rating'] else ""}
                                
                        """, unsafe_allow_html=True)
                
                if county != "Nairobi":
                    st.markdown(f"""
                        <div style='background: #fed7aa; border: 1px solid #fb923c; padding: 15px; border-radius: 8px; margin-top: 15px;'>
                            <p style='color: #9a3412; margin: 0; font-size: 14px;'>
                                <strong>Note:</strong> {county} stations are part of Kenya Power's / Private EV's planned expansion 
                                scheduled for 2025-2026. Full operational details will be available upon launch.
                            </p>
                        
                    """, unsafe_allow_html=True)
        


    # =====================================================
    # TAB 6: REVIEWS
    # =====================================================
    with tab6:
        st.markdown("### User Reviews")
        # Reviews by County
        city_colors = {
            "Nairobi": "#3b82f6",
            "Kisumu": "#10b981",
            "Mombasa": "#f97316",
            "Kiambu": "#8b5cf6",
            "Machakos": "#ef4444",
            "Makueni": "#6366f1"
        }

        for county, stats in county_stats.items():
            county_stations = [s for s in charging_stations if s.get('county') == county and s.get('reviews')]
            all_reviews = []
            for s in county_stations:
                for r in s.get('reviews', []):
                    all_reviews.append({**r, 'station_name': s.get('name'), 'county': s.get('county')})

            tile_color = city_colors.get(county, "#f3f4f6")
            if not all_reviews:
                st.markdown(f"<div class='station-card' style='background:{tile_color}; margin-bottom:12px;'><h4 style='margin:0;'>{county}</h4><p class='small-muted' style='margin:6px 0 0 0;'>No reviews available yet (stations planned/under development)</p></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='station-card' style='background:{tile_color}; margin-bottom:12px;'><div style='display:flex; align-items:center; gap:10px;'><h4 style='margin:0;'>{county}</h4><div style='background:#fff7ed; padding:6px 10px; border-radius:20px;'>★ <strong>{stats.get('avg_rating')}</strong></div></div></div>", unsafe_allow_html=True)
                cols = st.columns(2)
                for idx, review in enumerate(all_reviews[:10]):
                    with cols[idx % 2]:
                        st.markdown(render_review_card(review, show_station_info=True), unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### Reviews by Provider")
        provider_colors = {
            "Kenya Power": "#10b981",
            "TotalEnergies | Ampersand-energy": "#f97316",
            "TotalEnergies": "#3b82f6",
            "BasiGo": "#8b5cf6",
            "TotalEnergies | Roam-electric": "#ef4444",
            "Roam Electric": "#6366f1",
            "Roam Electric | Quickmart": "#fbbf24",
            "EVChaja": "#06b6d4",
            "Independent": "#E3E1EF",
            "Ampersand": "#ec4899"
        }

        for brand, data in provider_summary.items():
            brand_stations = [s for s in charging_stations if s.get('provider') == brand and s.get('reviews')]
            all_reviews = []
            for s in brand_stations:
                for r in s.get('reviews', []):
                    all_reviews.append({**r, 'station_name': s.get('name'), 'county': s.get('county')})
            tile_color = provider_colors.get(brand, "#f3f4f6")
            if all_reviews:
                st.markdown(f"<div class='station-card' style='background:{tile_color}; margin-bottom:12px;'><div style='display:flex; align-items:center; gap:10px;'><h4 style='margin:0;'>{brand}</h4><div style='background:#fff7ed; padding:6px 10px; border-radius:20px;'>★ <strong>{data.get('avg_rating')}</strong></div></div></div>", unsafe_allow_html=True)
                cols = st.columns(2)
                for idx, review in enumerate(all_reviews[:10]):
                    with cols[idx % 2]:
                        st.markdown(render_review_card(review, show_station_info=True), unsafe_allow_html=True)

    # =====================================================
    # TAB 7: INSIGHTS
    # =====================================================
    with tab7:
        st.markdown("### Insights & Takeaways")
        # Pricing Structure
        st.markdown(
            "<div class='insight-box' style='border-left:4px solid #8b5cf6;'>"
            "<h4 style='margin:0 0 8px 0;'>Pricing Structure</h4>"
            "<ul style='color:#4b5563; line-height:1.7;'>"
            "<li>Kenya Power offers free charging at select pilot stations.</li>"
            "<li>Commercial rates commonly range between KSh 20-50 per kWh (approx $0.15 - $0.38).</li>"
            "<li>E-mobility tariff pilots indicate KSh 8-16 per kWh depending on peak/off-peak.</li>"
            "<li>Charging cost comparison: ~KSh <a href='https://www.utucars.africa/blog/4' target='_blank'>4/km vs KSh 14/km</a> for petrol (approx 71.4% savings).</li>"
            "</ul></div>", unsafe_allow_html=True
        )

        # Vehicle compatibility
        st.markdown(
            "<div class='insight-box' style='border-left:4px solid #f97316; margin-top:12px;'>"
            "<h4 style='margin:0 0 8px 0;'>Vehicle Compatibility</h4>"
            "<ul style='color:#4b5563; line-height:1.7;'>"
            "<li>Popular models: Hyundai Kona Electric, BYD e6, Nissan Leaf.</li>"
            "<li>CCS is the dominant standard for DC fast charging; Type 2 is common for AC.</li>"
            "<li>Motorcycle charging commonly offered by: TotalEnergies + Roam/Ampersand.</li>"
            "<li>Motorcycle charging and battery swap models are active in select urban hubs.</li>"
            "</ul></div>", unsafe_allow_html=True
        )

        # Geographic gaps & opportunities
        st.markdown(
            "<div class='insight-box' style='border-left:4px solid #ef4444; margin-top:12px;'>"
            "<h4 style='margin:0 0 8px 0;'>Geographic Gaps & Opportunities</h4>"
            "<ul style='color:#4b5563; line-height:1.7;'>"
            "<li>Kisumu and Mombasa show early rollout activity (planned 2025-2026); more coverage needed for secondary cities.</li>"
            "<li>Highway corridor charging (Nairobi-Mombasa, etc.) is critical for intercity EV adoption.</li>"
            "<li>Motorcycle/boda-boda segment shows strong growth potential.</li>"
            "<li>Renewable energy integration (Kenya's largely renewable grid is advantage)</li>"
            "<li>Residential charging, workplace charging, and motorcycle segments are promising growth areas.</li>"
            "</ul></div>", unsafe_allow_html=True
        )

        # User experience highlights
        st.markdown(
            "<div class='insight-box' style='border-left:4px solid #6366f1; margin-top:12px;'>"
            "<h4 style='margin:0 0 8px 0;'>User Experience Highlights</h4>"
            "<ul style='color:#4b5563; line-height:1.7;'>"
            "<li>Overall average rating across sample: 4.3/5 (from stations that have ratings).</li>"
            "<li>Payment convenience (e.g., M-Pesa integration) is a consistent positive factor.</li>"
            "<li>Common challenges: insufficient ports during peak times and signage/navigation.</li>"
            "<li>Overall user sentiment is positive, with many users appreciating fast charging speeds, and free charging.</li>"
            "</ul></div>", unsafe_allow_html=True
        )

        # Footer
        st.markdown(
            "<div style='background:white; padding:16px; border-radius:10px; margin-top:14px;'>"
            "<p class='small-muted' style='margin:0;'><strong>Data Compiled:</strong> October 2025 | <strong>Sources:</strong> Kenya Power, TotalEnergies, BasiGo, Roam Electric, EVChaja, News Outlets Reportings, and Industry Reports</p>"
            "<p class='small-muted' style='margin:6px 0 0 0;'>This sample dataset is intended for learning and prototyping. For real-time availability, use providers' official apps.</p>"
            "</div>", unsafe_allow_html=True
        )

# =====================================================
# RUNNING APP
# =====================================================
if __name__ == "__main__":
    main()
