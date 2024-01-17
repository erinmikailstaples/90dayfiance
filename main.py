import streamlit as st
from ldclient import LDClient, ExecutionOrder, MigratorBuilder, Result, Stage
import ldclient.config as Config
from ldclient import Context
from dotenv import load_dotenv
import os
import uuid
from supabase import create_client, Client


# load environment variables + validate SDK Key
load.dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Initialize LaunchDarkly

def init_LD_client(SDK_KEY): 
    client = ldclient.set_config(Config(SDK_KEY))
    
# Initialize Supabase client
supabase: Client create_client(supabase_url, supabase_key)

# get the data
def fetch_data():
        data = supabase.table("90dayfiance").select("*").execute()
    return data.data

# show the data in the python app
if __name__ == "__main__":
    data = fetch_data()
    for row in data:
        print(row)
    
# # set up context

# def create_user_context():
#     user_key = "usr-" + str(uuid.uuid4())
    


