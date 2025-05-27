import streamlit as st

# Configure the page
st.set_page_config(
    page_title="PT Bách ❤️🔒 Thảo Linh",
    layout="centered"
)

# ---- Title ----
st.title("PT Bách ❤️🔒 Thảo Linh")

# ---- Image Section ----
st.header("Our Favorite Photos")
cols = st.columns(2)

# Replace the paths below with your actual image file paths or URLs
with cols[0]:
    st.image("images/bach.jpg", caption="Bách", use_container_width=True)
with cols[1]:
    st.image("images/linh.jpg", caption="Thảo Linh", use_container_width=True)

# ---- Relationship Summary ----
st.header("Timeline")

st.write(
    """
- **Lần đầu nói chuyện**: 11/04/2025
- **Xóa biệt hiệu**: 01/05/2025
- **Tỏ tình**: 20/05/2025
"""
)

# ---- Footer ----
st.markdown("---")
st.caption("Made with ❤️ by PT Bách for Thảo Linh")
