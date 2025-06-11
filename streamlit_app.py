# import streamlit as st

# # Configure the page
# st.set_page_config(
#     page_title="PT Bách ❤️🔒 Thảo Linh",
#     layout="centered"
# )

# # ---- Title ----
# st.title("PT Bách ❤️🔒 Thảo Linh")

# # ---- Image Section ----
# st.header("Our Favorite Photos")
# cols = st.columns(2)

# # Replace the paths below with your actual image file paths or URLs
# with cols[0]:
#     st.image("images/bach.jpg", caption="Bách", use_container_width=True)
# with cols[1]:
#     st.image("images/linh.jpg", caption="Thảo Linh", use_container_width=True)

# # ---- Relationship Summary ----
# st.header("Timeline")

# st.write(
#     """
# - **Lần đầu nói chuyện**: 11/04/2025
# - **Xóa biệt hiệu**: 01/05/2025
# - **Tỏ tình**: 20/05/2025
# """
# )

# # ---- Footer ----
# st.markdown("---")
# st.caption("Made with ❤️ by PT Bách for Thảo Linh")

import streamlit as st

# 1. Nhập bài thơ
st.title("📜 Viết & Diễn giải Thơ")

input_text = st.text_area("✍️ Viết bài thơ của bạn vào đây:", height=200)

# 2. Tách câu thơ theo dòng
lines = input_text.strip().split("\n") if input_text else []

st.write("---")
st.subheader("📖 Bài thơ của bạn:")

# 3. Tạo selector và hiển thị diễn giải
if lines:
    selected_line = st.radio("👉 Chọn một dòng thơ để xem diễn giải:", lines)

    # 4. Diễn giải thủ công hoặc gợi ý
    explanations = {
        line: f"Diễn giải cho câu: “{line}”"  # bạn có thể viết cụ thể hơn hoặc dùng AI để sinh
        for line in lines
    }

    st.info(explanations[selected_line])
