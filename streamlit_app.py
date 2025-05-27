import streamlit as st

# Configure the page
st.set_page_config(
    page_title="PT Bách ❤️ Thảo Linh",
    layout="centered"
)

# ---- Title ----
st.title("PT Bách ❤️ Thảo Linh")

# ---- Image Section ----
st.header("Our Favorite Moments")
cols = st.columns(2)

# Replace the paths below with your actual image file paths or URLs
with cols[0]:
    st.image("images/bach.jpg", caption="Bách", use_column_width=True)
with cols[1]:
    st.image("images/linh.jpg", caption="Thảo Linh", use_column_width=True)

# ---- Relationship Summary ----
st.header("Our Journey Together")

st.write(
    """
**Tóm tắt**

From the moment we first met, our connection has grown stronger every day. We share laughter, support each other through challenges, and continue to build beautiful memories together.
"""
)

st.write(
    """
**Chi tiết**

- **Lần đầu nói chuyện**:
- **Xóa biệt hiệu**:
- **Tỏ tình**:
"""
)

# ---- Footer ----
st.markdown("---")
st.caption("Made with ❤️ by PT Bách for Thảo Linh")
