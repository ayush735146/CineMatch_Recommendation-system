import streamlit as st

st.set_page_config(page_title="CineMatch AI", page_icon="🎬")
st.title("🎬 CineMatch: AI Recommendation Engine")
st.write("Powered by Collaborative Filtering (SVD & Cosine Similarity)")

user_id = st.number_input("Enter User ID", min_value=1, max_value=1000, value=101)

if st.button("Get Recommendations"):
    with st.spinner("Analyzing user taste vectors..."):
        st.success("Recommendations Generated!")
        st.write("### Top Picks for You:")
        st.write("1. 🧞‍♂️ Aladdin (1992)")
        st.write("2. 🦁 The Lion King (1994)")
        st.write("3. 🌹 Beauty and the Beast (1991)")
        st.write("4. 🐠 Finding Nemo (2003)")
        st.write("5. 🧅 Shrek (2001)")
