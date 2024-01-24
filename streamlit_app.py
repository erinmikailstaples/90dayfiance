import streamlit as st
import os
from supabase import create_client, Client
from st_supabase_connection import SupabaseConnection
import altair as alt
import numpy as np
import pandas as pd 

# st_supabase_client = st.connection(
#     name="90DAYDATABASE",
#     type=SupabaseConnection,
#     ttl=None,
#     url="SUPABASE_URL",
#     key="SUPABASE_KEY",
# )

# st_supabase_client.query("*", table="90dayfiance", ttl=0).execute()




# # load environment variables + validate SDK Key
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

data = supabase.table("90dayfiance").select("*").execute()


# # #query to get the dang data
def read_data():
    return supabase.from_("90dayfiance").select("*").execute()
    df = pd.DataFrame(response.data)
    return df

df = pd.DataFrame(read_data())
st.dataframe(df)

print(df)

data = supabase.table("90dayfiance").select("*").execute()

df = pd.DataFrame(data)

chart = alt.Chart(df).mark_bar().encode(
    x='partnera',
    y='partnerb'
)
# st.altair_chart(chart, use_container_width=True)