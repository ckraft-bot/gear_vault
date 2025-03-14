import warnings
warnings.filterwarnings("ignore")

import psycopg2
import streamlit as st
import random
from datetime import datetime
import pytz  

connection_str = st.secrets["postgres"]["connection_str"]

# Connect to NeonDB PostgreSQL
conn = psycopg2.connect(connection_str)  
cursor = conn.cursor()

# Function to load gear_vault_schema.equipment
def load_messages():
    cursor.execute("SELECT ID, NAME, BRAND, MODEL, STORE, SIZE, UNIT, PURCHASE_DATE, NOTES FROM gear_vault_schema.equipment")
    return cursor.fetchall()