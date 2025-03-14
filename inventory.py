import warnings
warnings.filterwarnings("ignore")

import psycopg2
import streamlit as st
from datetime import datetime
import utility

# Connection settings
connection_str = utility.connection_str  # Dev connection

# Connect to NeonDB PostgreSQL
conn = psycopg2.connect(connection_str)  
cursor = conn.cursor()

# Function to load data from table
def load_equipment():
    cursor.execute('SELECT "ID", "CATEGORY", "NAME", "BRAND", "MODEL", "STORE", "SIZE", "UNIT", "PURCHASE_DATE", "NOTES" FROM gear_vault_schema.equipment')
    return cursor.fetchall()

# Function to insert data into table
def insert_equipment(data):
    query = """
    INSERT INTO gear_vault_schema.equipment 
    ("CATEGORY", "NAME", "BRAND", "MODEL", "STORE", "SIZE", "UNIT", "PURCHASE_DATE", "NOTES") 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)  # Include CATEGORY in the tuple
    conn.commit()

# Streamlit UI
st.title("Gear Vault Equipment Manager")

# Form to add new equipment
with st.form(key="add_equipment"):
    category = st.selectbox("Category", ["Gear", "Protection", "Footwear", "Bags", "Nutrition"])
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

# Display existing equipment in a table
if st.button("Load Equipment"):
    equipment = load_equipment()
    if equipment:
        st.write("### Current Equipment:")
        st.dataframe(equipment, hide_index=True)
    else:
        st.write("No equipment found.")

# Close connection on app exit
if conn:
    conn.close()
