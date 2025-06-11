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

st.set_page_config(layout="centered", page_title="Bài Thơ Tương Tác")

# Dữ liệu bài thơ và chú giải
poem_data = [
    {
        "stanza": "Áo em trắng quá nhìn không ra\nHàng cây đứng đó cũng như là\nBóng mát che riêng đời chúng ta\nNgón tay thon thả ngắt lá đa.",
        "annotation": "Khổ thơ này gợi lên hình ảnh trong sáng của người con gái và sự gắn bó giữa hai người. Đây là một đoạn thơ mở đầu nhẹ nhàng, tạo không khí thơ mộng."
    },
    {
        "stanza": "Chiều nay tiếng hát vẳng trong mưa\nAnh nhớ em nhiều biết mấy cho vừa\nEm ơi thôi nhé đừng buồn nữa\nPhía cuối con đường vẫn có ta.",
        "annotation": "Khổ thơ thứ hai thể hiện nỗi nhớ nhung và sự an ủi, hứa hẹn của nhân vật trữ tình. Nó mang đến thông điệp về sự hy vọng và sự đồng hành trong cuộc sống."
    },
    {
        "stanza": "Trăng vàng hiu hắt giữa không gian\nGió thoảng hương xưa thổi nhẹ nhàng\nNgỡ ngàng bỗng thấy bao la lắm\nCuộc đời này vẫn đẹp vô vàn.",
        "annotation": "Khổ thơ này tả cảnh trăng và gió, gợi lên cảm giác về sự rộng lớn của vũ trụ và vẻ đẹp tiềm ẩn của cuộc sống, dù có lúc hiu hắt."
    }
]

st.title("Bài Thơ Tương Tác  thơ 'Áo Trắng'")
st.write("Click vào mỗi khổ thơ để xem chú giải!")

# CSS để ẩn/hiện popup và định dạng
st.markdown("""
<style>
.stanza-container {
    cursor: pointer;
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    transition: all 0.2s ease-in-out;
    background-color: #f9f9f9;
}
.stanza-container:hover {
    background-color: #e6f7ff;
    border-color: #91d5ff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.annotation-box {
    display: none; /* Mặc định ẩn */
    margin-top: 10px;
    padding: 15px;
    background-color: #fffacd; /* Màu vàng nhạt */
    border-left: 5px solid #ffcc00;
    border-radius: 5px;
    font-style: italic;
    color: #333;
    animation: fadeIn 0.3s ease-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

# Hiển thị các khổ thơ và chú giải
for i, item in enumerate(poem_data):
    # Sử dụng div với id để dễ dàng thao tác bằng JavaScript
    # Thêm sự kiện onclick trực tiếp vào div
    st.markdown(f"""
    <div class="stanza-container" id="stanza-{i}" onclick="toggleAnnotation('annotation-{i}')">
        <p style="white-space: pre-line;">{item['stanza']}</p>
        <div class="annotation-box" id="annotation-{i}">
            <strong>Chú giải:</strong> {item['annotation']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# JavaScript để xử lý việc hiển thị/ẩn chú giải
st.markdown("""
<script>
function toggleAnnotation(annotationId) {
    var annotationBox = document.getElementById(annotationId);
    if (annotationBox.style.display === "none" || annotationBox.style.display === "") {
        annotationBox.style.display = "block";
    } else {
        annotationBox.style.display = "none";
    }
}
</script>
""", unsafe_allow_html=True)

st.sidebar.header("Thông Tin")
st.sidebar.info("Ứng dụng này giúp bạn tương tác với bài thơ bằng cách click vào từng khổ để xem chú giải chi tiết.")
