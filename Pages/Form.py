import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import psycopg2
import streamlit as st
from datetime import datetime
import utility

# Connection settings
connection_str = utility.connection_str  # Dev connection

# Connect to NeonDB PostgreSQL
conn = psycopg2.connect(connection_str)  
cursor = conn.cursor()

# Ensure the sequence for ID exists and set it as the default for the "ID" column
cursor.execute("""
    CREATE SEQUENCE IF NOT EXISTS gear_vault_schema.equipment_id_seq START 1;
""")

cursor.execute("""
    ALTER TABLE gear_vault_schema.equipment
    ALTER COLUMN "ID" SET DEFAULT nextval('gear_vault_schema.equipment_id_seq');
""")
conn.commit()

# Function to insert data into table
def insert_equipment(data):
    query = """
    INSERT INTO gear_vault_schema.equipment 
    ("CATEGORY", "NAME", "BRAND", "MODEL", "STORE", "SIZE", "UNIT", "PURCHASE_DATE", "NOTES") 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)  # Do not include ID in the data
    conn.commit()

# Streamlit UI
st.title("Gear Vault")

utility.set_background("Assets/background_blur.png")

# Sidebar content using markdown
st.sidebar.markdown("""
### 1. **Protection**
- **Belay Devices**: Devices used by climbers to manage rope slack and catch falls.
- **Carabiners**: Metal loops with spring-loaded gates used for securing ropes and equipment.
- **Climbing Harness**: Worn by climbers for safety and attachment to ropes.
- **Climbing Protection (Nuts, Cams)**: Devices placed in cracks in the rock to protect the climber in case of a fall.
- **Climbing Ropes**: Strong, durable ropes used to secure climbers to anchors, belay devices, or other climbers for safety during ascents and descents.
- **Crash Pads**: Portable pads used for bouldering to protect against falls.
- **Helmets**: Worn to protect the head from falling rocks or bumps.
- **Quickdraws**: A pair of carabiners connected by a sewn sling used to connect rope to anchors.
- **Rope Protectors**: Prevent rope wear when climbing on abrasive surfaces.

### 2. **Footwear**
- **Approach Shoes**: Versatile shoes used for hiking to a climbing site or on easy climbing terrain.
- **Climbing Boots**: High-ankle boots designed for mountaineering or ice climbing.
- **Climbing Shoes**: Shoes designed with rubber soles for optimal grip while climbing.

### 3. **Bags**
- **Chalk Bag**: A small bag for holding chalk, typically worn on a climber's harness.
- **Climbing Backpack**: A backpack designed to carry climbing gear.
- **Climbing Duffel Bag**: A spacious bag for carrying all climbing equipment for travel or storage.
- **Hydration Packs**: Small, wearable water storage bags used for hydration during climbs.
- **Rope Bag**: Used to store and carry climbing ropes to keep them clean and untangled.

### 4. **Nutrition**
- **Electrolyte Tablets**: Used to replenish essential minerals lost during intense activity.
- **Energy Bars**: High-calorie, portable food items to maintain energy during climbs.
- **Hydration Packs**: Water and nutrient-filled packs to stay hydrated and energized.
- **Protein Powder**: For muscle recovery after a strenuous climb.
- **Trail Mix**: A mix of nuts, seeds, and dried fruits providing quick energy.
""")

# Form to add new equipment
with st.form(key="add_equipment"):
    category = st.selectbox("Category", ["Protection", "Footwear", "Bags", "Nutrition", "Certification"])
    name = st.text_input("Name")
    brand = st.text_input("Brand")
    model = st.text_input("Model")
    store = st.text_input("Store")
    size = st.text_input("Size")
    unit = st.number_input("Unit", min_value=0, step=1)
    purchase_date = st.date_input("Purchase Date")
    notes = st.text_area("Notes")

    submit = st.form_submit_button("Add Equipment")

    if submit:
        if name:
            try:
                data = (category, name, brand, model, store, size, unit, purchase_date, notes)
                insert_equipment(data)
                st.success(f"Equipment '{name}' added successfully!")
            except Exception as e:
                st.error(f"Failed to add equipment: {e}")

if st.button(":house: Go Home"):
    st.switch_page("Home.py")


# Close connection on app exit
if conn:
    conn.close()
