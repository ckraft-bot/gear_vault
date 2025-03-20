import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import psycopg2
import streamlit as st
from datetime import datetime
import utility

# Connection settings
# connection_str = utility.connection_str  # Dev connection
connection_str = st.secrets["postgres"]["connection_str"]  # Prod connection

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

# Function to load data from table, ordered by purchase date in ascending order
def load_equipment():
    cursor.execute('''
        SELECT "ID", "CATEGORY", "NAME", "BRAND", "MODEL", "STORE", "SIZE", "UNIT", "PURCHASE_DATE", "NOTES" 
        FROM gear_vault_schema.equipment
        ORDER BY "PURCHASE_DATE" ASC
    ''')
    return cursor.fetchall()

# Display existing equipment in a table
if st.button("Load Equipment"):
    equipment = load_equipment()
    if equipment:
        # Convert the list of tuples to a DataFrame
        columns = ["ID", "CATEGORY", "NAME", "BRAND", "MODEL", "STORE", "SIZE", "UNIT", "PURCHASE_DATE", "NOTES"]
        df = pd.DataFrame(equipment, columns=columns)  # Create the DataFrame with column names
        st.write("### Current Equipment:")
        st.dataframe(df, hide_index=True)  # Display the DataFrame in Streamlit
    else:
        st.write("No equipment found.")

if st.button(":house: Go Home"):
    st.switch_page("App/Pages/Home.py")
    
# Close connection on app exit
if conn:
    conn.close()
