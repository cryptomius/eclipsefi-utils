import streamlit as st
import requests
import json
import time

def make_api_request(url, max_retries=3):
    """Helper function to make API requests with retries and better error handling"""
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(f"API request failed after {max_retries} attempts: {str(e)}")
            time.sleep(1)  # Wait before retrying
        except json.JSONDecodeError as e:
            if attempt == max_retries - 1:  # Last attempt
                raise Exception(f"Failed to decode JSON response: {str(e)}\nResponse content: {response.text[:200]}")
            time.sleep(1)  # Wait before retrying

def query_staked_eclip():
    url = "https://rest.cosmos.directory/neutron/cosmwasm/wasm/v1/contract/neutron19q93n64nyet24ynvw04qjqmejffkmyxakdvl08sf3n3yeyr92lrs2makhx/smart/eyJxdWVyeV9zdGF0ZSI6e319"
    
    try:
        data = make_api_request(url)
        
        # Extract the stake state amount
        stake_amount = int(data['data']['stake_state']['total_bond_amount'])
        
        # Extract lock state amounts
        lock_amounts = [int(state['total_bond_amount']) for state in data['data']['lock_states']]
        
        # Calculate total and convert to integer
        total_staked = int((stake_amount + sum(lock_amounts)) // 1_000_000)
        
        return total_staked, None
        
    except Exception as e:
        st.error(f"Debug info - URL: {url}")
        return None, f"Error querying staked ECLIP: {str(e)}"

def query_cosmic_essence():
    url = "https://rest.cosmos.directory/neutron/cosmwasm/wasm/v1/contract/neutron19q93n64nyet24ynvw04qjqmejffkmyxakdvl08sf3n3yeyr92lrs2makhx/smart/eyJxdWVyeV90b3RhbF9lc3NlbmNlIjp7fX0="
    
    try:
        data = make_api_request(url)
        
        # Extract the essence value and convert to integer
        total_essence = int(int(data['data']['essence']) // 1_000_000)
        
        return total_essence, None
        
    except Exception as e:
        st.error(f"Debug info - URL: {url}")
        return None, f"Error querying Cosmic Essence: {str(e)}"

def display_metric(label, value, color="#00FF00"):
    st.markdown(f"### {label}")
    st.markdown(
        f"""
        <div style='background-color: #1E1E1E; padding: 20px; border-radius: 10px; text-align: center;'>
            <h1 style='color: {color}; font-size: 48px;'>{int(value):,d}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    st.set_page_config(
        page_title="ECLIP & Cosmic Essence Tracker",
        page_icon="🌌",
        layout="centered"
    )
    
    st.title("🌌 ECLIP & Cosmic Essence Tracker")
    
    # Add a refresh button
    if st.button("Refresh Data"):
        st.cache_data.clear()
    
    # Query the data (with caching)
    @st.cache_data(ttl=300)  # Cache for 5 minutes
    def get_cached_data():
        staked_eclip, eclip_error = query_staked_eclip()
        cosmic_essence, essence_error = query_cosmic_essence()
        return staked_eclip, cosmic_essence, eclip_error, essence_error
    
    staked_eclip, cosmic_essence, eclip_error, essence_error = get_cached_data()
    
    # Display errors if any
    if eclip_error:
        st.error(eclip_error)
    if essence_error:
        st.error(essence_error)
    
    # Create two columns for metrics
    col1, col2 = st.columns(2)
    
    with col1:
        if staked_eclip is not None:
            display_metric("Total Staked ECLIP", staked_eclip, "#00FF00")
            
    with col2:
        if cosmic_essence is not None:
            display_metric("Total Cosmic Essence", cosmic_essence, "#FF00FF")
    
    # Add timestamp
    st.caption("Data refreshes every 5 minutes. Click refresh button for immediate update.")

if __name__ == "__main__":
    main()