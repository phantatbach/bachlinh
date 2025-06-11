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

st.set_page_config(layout="centered", page_title="Bài Thơ Tương Tác", initial_sidebar_state="expanded") # Thêm initial_sidebar_state

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

st.title("Bài Thơ Tương Tác: Áo Trắng")
st.write("Click vào mỗi khổ thơ để xem chú giải!")

# --- CSS mới để xử lý Dark Mode và màu chữ ---
st.markdown("""
<style>
/* Đảm bảo màu chữ hiển thị rõ ràng trên cả light/dark mode */
body {
    color: var(--text-color); /* Sử dụng biến màu chữ của Streamlit */
}

.stanza-container {
    cursor: pointer;
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid var(--primary-color); /* Sử dụng màu chính của Streamlit */
    border-radius: 8px;
    transition: all 0.2s ease-in-out;
    background-color: var(--secondary-background-color); /* Nền phụ của Streamlit */
    color: var(--text-color); /* Đảm bảo màu chữ trong container */
}
.stanza-container:hover {
    background-color: var(--hover-color, #e6f7ff); /* Streamlit hover color hoặc fallback */
    border-color: var(--primary-color-light, #91d5ff); /* Màu sáng hơn của primary */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.stanza-container p {
    color: var(--text-color); /* Đảm bảo màu chữ cho đoạn thơ */
}

.annotation-box {
    display: none; /* Mặc định ẩn */
    margin-top: 10px;
    padding: 15px;
    background-color: var(--annotation-bg-color, #fffacd); /* Màu nền chú giải */
    border-left: 5px solid var(--annotation-border-color, #ffcc00);
    border-radius: 5px;
    font-style: italic;
    color: var(--annotation-text-color, #333); /* Màu chữ chú giải */
    animation: fadeIn 0.3s ease-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Các biến màu Streamlit có sẵn (hoặc bạn có thể tự định nghĩa nếu cần) */
/*
:root {
    --text-color: #31333F;
    --background-color: #FFFFFF;
    --secondary-background-color: #F0F2F6;
    --primary-color: #FF4B4B;
    --primary-color-light: #FF7B7B;
    --hover-color: #E6F7FF;
}

[data-baseweb="dark"] {
    --text-color: #FAFAFA;
    --background-color: #0E1117;
    --secondary-background-color: #1A1C20;
    --primary-color: #FF4B4B;
    --primary-color-light: #FF7B7B;
    --hover-color: #3F444E;
}
*/
/* Định nghĩa màu sắc riêng cho chú giải để kiểm soát tốt hơn ở cả hai chế độ */
:root { /* Light Mode default */
    --annotation-bg-color: #fffacd; /* light goldenrod yellow */
    --annotation-border-color: #ffcc00; /* gold */
    --annotation-text-color: #333;
}

[data-baseweb="dark"] { /* Dark Mode specific colors */
    --annotation-bg-color: #3a3a2d; /* darker goldenrod yellow */
    --annotation-border-color: #ffd700; /* gold */
    --annotation-text-color: #e0e0e0;
}


</style>
""", unsafe_allow_html=True)

# Hiển thị các khổ thơ và chú giải
for i, item in enumerate(poem_data):
    # Sử dụng div với id để dễ dàng thao tác bằng JavaScript
    # Thêm sự kiện onclick trực tiếp vào div
    # Đảm bảo ID là duy nhất và không trùng lặp
    st.markdown(f"""
    <div class="stanza-container" id="stanza-{i}" onclick="toggleAnnotation('annotation-{i}')">
        <p style="white-space: pre-line;">{item['stanza']}</p>
        <div class="annotation-box" id="annotation-{i}">
            <strong>Chú giải:</strong> {item['annotation']}
        </div>
    </div>
    """, unsafe_allow_html=True)

# JavaScript để xử lý việc hiển thị/ẩn chú giải
# Đặt script này ở cuối cùng để đảm bảo DOM đã được load
st.markdown("""
<script>
function toggleAnnotation(annotationId) {
    console.log("Clicked! Toggling annotation: " + annotationId); // Debugging
    var annotationBox = document.getElementById(annotationId);
    if (annotationBox) { // Kiểm tra xem phần tử có tồn tại không
        if (annotationBox.style.display === "none" || annotationBox.style.display === "") {
            annotationBox.style.display = "block";
        } else {
            annotationBox.style.display = "none";
        }
    } else {
        console.error("Annotation box not found: " + annotationId); // Debugging
    }
}
</script>
""", unsafe_allow_html=True)

st.sidebar.header("Thông Tin")
st.sidebar.info("Ứng dụng này giúp bạn tương tác với bài thơ bằng cách click vào từng khổ để xem chú giải chi tiết.")