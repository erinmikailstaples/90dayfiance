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

#query to get the dang data
response = supabase.table('90dayfiance').select('partnera').execute()

data = supabase.table("90dayfiance").select("*").execute

df = pd.DataFrame(data.data)

chart = alt.Chart(df).mark_bar().encode(
    x='partnera',
    y='partnerb'
)

st.altair_chart(chart, use_container_width=True)