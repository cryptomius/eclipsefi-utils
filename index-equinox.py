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
    # card
    st.markdown("""
    ### 📈 Staked ECLIP & Cosmic Essence Tracker
    Track all staked ECLIP and Cosmic Essence live from the blockchain.
    
    [Launch Dashboard](https://cosmic-essence.streamlit.app/)
    """)
    
    
    # card
    st.markdown("""
    ### 🔒 Equinox Lockdrop Statistics
    View the total amount of xASTRO committed to the lockdrop and its distribution.
    
    [Launch Dashboard](https://lockdrop-stats.streamlit.app/)
    """)

    # card
    st.markdown("""
    ### 📝 Equinox voting behaviour
    View the voting behaviour of Equinox participants per Astroport Epoch.
    
    [Voting Behaviour](https://equinox-votes.streamlit.app/)
    """)

with col2:
    
    
    # card
    st.markdown("""
    ### 🍰 Equinox Position Dashboard
    See what a participant has committed to Single Sided vs LP Vaults and the lock periods they have allocated to.
    
    [Launch Dashboard](https://equinox-positions.streamlit.app/)
    """)

    # card
    st.markdown("""
    ### 📊 Equinox Participation
    Analyze the composition of Equinox participants by vault type and lock period.
    *(Private dashboard)*
    
    [Launch Dashboard](https://ido-dashboards.streamlit.app/Equinox)
    """)

# # Footer
# st.markdown("---")
# st.markdown("*Powered by Eclipse Fi Analytics*")
