import streamlit as st
import requests
import json

def query_cosmic_essence():
    # Neutron blockchain query endpoint
    url = "https://rest.cosmos.directory/neutron/cosmwasm/wasm/v1/contract/neutron19q93n64nyet24ynvw04qjqmejffkmyxakdvl08sf3n3yeyr92lrs2makhx/smart/eyJxdWVyeV9zdGF0ZSI6e319"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Extract the stake state amount
        stake_amount = int(data['data']['stake_state']['total_bond_amount'])
        
        # Extract lock state amounts
        lock_amounts = [int(state['total_bond_amount']) for state in data['data']['lock_states']]
        
        # Calculate total (dividing by 1,000,000 as specified)
        total_essence = (stake_amount + sum(lock_amounts)) / 1_000_000
        
        return total_essence, None
        
    except Exception as e:
        return None, str(e)

def main():
    st.set_page_config(
        page_title="Cosmic Essence Tracker",
        page_icon="🌌",
        layout="centered"
    )
    
    st.title("🌌 Cosmic Essence Tracker")
    
    # Add a refresh button
    if st.button("Refresh Data"):
        st.cache_data.clear()
    
    # Query the data (with caching)
    @st.cache_data(ttl=300)  # Cache for 5 minutes
    def get_cached_data():
        return query_cosmic_essence()
    
    total_essence, error = get_cached_data()
    
    if error:
        st.error(f"Error fetching data: {error}")
    else:
        # Display the total essence with nice formatting
        st.markdown("### Total Cosmic Essence")
        st.markdown(
            f"""
            <div style='background-color: #1E1E1E; padding: 20px; border-radius: 10px; text-align: center;'>
                <h1 style='color: #00FF00; font-size: 48px;'>{total_essence:,.2f}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Add timestamp
        st.caption("Data refreshes every 5 minutes. Click refresh button for immediate update.")

if __name__ == "__main__":
    main()