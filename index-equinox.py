import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Equinox Explorers",
    page_icon="🌓",
    layout="wide"
)

# Title and description
st.title("🌓 Equinox Explorers")
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
    
    
    #  card
    st.markdown("""
    ### 🔒 Equinox Lockdrop Statistics
    View the total amount of xASTRO committed to the lockdrop and its distribution.
    
    [Launch Dashboard](https://lockdrop-stats.streamlit.app/)
    """)

with col2:
    
    
    # Sixth card
    st.markdown("""
    ### 🍰 Equinox Positions Dashboard
    See what participants have committed to Single Sided vs LP Vaults and the lock periods they have distributed to.
    
    [Launch Dashboard](https://equinox-participation.streamlit.app/)
    """)

# # Footer
# st.markdown("---")
# st.markdown("*Powered by Eclipse Fi Analytics*")
