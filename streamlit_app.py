import streamlit as st
import os
from supabase import create_client
from st_supabase_connection import SupabaseConnection
import altair as alt
import numpy as np
import pandas as pd 

# load environment variables + validate SDK Key
st.write("supabaseurl:", st.secrets["SUPABASE_URL"])
st.write("supabasekey:", st.secrets["SUPABASE_KEY"])

Client = create_client("supabaseurl", "supabasekey")

# Initialize connection.
conn = st.connection('supabase',type='SupabaseConnection')

# SQL query to get the dang data
query = "SELECT * FROM 90dayfiance"

# Load this dang data into a dataframe

df = pd.read_sql(query, conn)

print(df.head)