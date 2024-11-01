import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Eclipse Fi Explorers",
    page_icon="🌓",
    layout="wide"
)

# Title and description
st.title("🌓 Eclipse Fi Explorers")
# st.markdown("Welcome to the Eclipse Fi analytics hub. Explore various dashboards and statistics below.")
st.markdown("---")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    # First card
    st.markdown("""
    ### 📈 Staked ECLIP & Cosmic Essence Tracker
    Track all staked ECLIP and Cosmic Essence live from the blockchain.
    
    [Launch Dashboard](https://cosmic-essence.streamlit.app/)
    """)
    
    # Second card
    st.markdown("""
    ### 💰 Eclipse Fi IDO Participation
    Explore participation statistics for Eclipse Fi's IDOs.
    *(Private dashboard)*
    
    [Launch Dashboard](https://ido-dashboards.streamlit.app/Participation)
    """)
    

with col2:
    # card
    st.markdown("""
    ### 📊 Eclipse Fi IDO Tiers
    Analyze the composition of Cosmic Essence holders for each IDO snapshot.
    *(Private dashboard)*
    
    [Launch Dashboard](https://ido-dashboards.streamlit.app/Cosmic_Essence_Flow)
    """)
    
    # card
    st.markdown("""
    ### 🧑 Eclipse Fi IDO Cohort Analysis
    View cohort retention, top participants & country attribution.
    *(Private dashboard)*
    
    [Launch Dashboard](https://ido-dashboards.streamlit.app/Analytics)
    """)
    


# # Footer
# st.markdown("---")
# st.markdown("*Powered by Eclipse Fi Analytics*")
