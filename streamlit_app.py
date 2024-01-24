import streamlit as st
import os
from supabase import create_client, Client
from st_supabase_connection import SupabaseConnection
import altair as alt
import numpy as np
import pandas as pd 

# load environment variables + validate SDK Key
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

Client = create_client("supabaseurl", "supabasekey")

# Initialize connection.
# conn = st.connection('supabase',type='SupabaseConnection')

# SQL query to get the dang data
response = supabase.table('90dayfiance').select('partnera').execute()

# # Load this dang data into a dataframe

# df = pd.read_sql(query, conn)

# print(df.head)