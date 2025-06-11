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

st.set_page_config(layout="centered", page_title="Bài Thơ Tương Tác (Tooltip)", initial_sidebar_state="expanded")

# Dữ liệu bài thơ với chú giải chi tiết từng dòng/đoạn
poem_data_detailed = [
    {
        "stanza_number": 1,
        "lines": [
            {"text": "Áo em trắng quá nhìn không ra", "annotation": "Gợi hình ảnh trong sáng, tinh khôi."},
            {"text": "Hàng cây đứng đó cũng như là", "annotation": None}, # Không có chú giải cho dòng này
            {"text": "Bóng mát che riêng đời chúng ta", "annotation": "Sự che chở, gắn bó mật thiết."},
            {"text": "Ngón tay thon thả ngắt lá đa.", "annotation": "Hành động tinh tế, nhẹ nhàng."}
        ]
    },
    {
        "stanza_number": 2,
        "lines": [
            {"text": "Chiều nay tiếng hát vẳng trong mưa", "annotation": "Không gian lãng mạn, hơi buồn."},
            {"text": "Anh nhớ em nhiều biết mấy cho vừa", "annotation": "Nỗi nhớ sâu sắc, da diết."},
            {"text": "Em ơi thôi nhé đừng buồn nữa", "annotation": "Lời an ủi, vỗ về."},
            {"text": "Phía cuối con đường vẫn có ta.", "annotation": "Sự hứa hẹn, đồng hành."}
        ]
    },
    {
        "stanza_number": 3,
        "lines": [
            {"text": "Trăng vàng hiu hắt giữa không gian", "annotation": "Cảnh vật tĩnh lặng, có chút u hoài."},
            {"text": "Gió thoảng hương xưa thổi nhẹ nhàng", "annotation": "Gợi nhớ kỷ niệm, cảm xúc xưa cũ."},
            {"text": "Ngỡ ngàng bỗng thấy bao la lắm", "annotation": "Cảm giác ngỡ ngàng trước sự bao la của vũ trụ."},
            {"text": "Cuộc đời này vẫn đẹp vô vàn.", "annotation": "Thông điệp lạc quan về vẻ đẹp của cuộc sống."}
        ]
    }
]

st.title("Bài Thơ Tương Tác: Áo Trắng (Tooltip)")
st.write("Di chuột (hover) vào các dòng thơ được gạch chân để xem chú giải!")

# --- CSS cho Tooltip và định dạng bài thơ ---
st.markdown("""
<style>
/* Streamlit theme variables */
:root { /* Light Mode default */
    --text-color: #31333F;
    --background-color: #FFFFFF;
    --secondary-background-color: #F0F2F6;
    --primary-color: #FF4B4B;
    --tooltip-bg-color: #333;
    --tooltip-text-color: #f9f9f9;
    --highlight-text-color: #007bff; /* Color for underlined text */
    --highlight-underline-color: #007bff; /* Underline color */
}

[data-baseweb="dark"] { /* Dark Mode specific colors */
    --text-color: #FAFAFA;
    --background-color: #0E1117;
    --secondary-background-color: #1A1C20;
    --primary-color: #FF4B4B;
    --tooltip-bg-color: #555;
    --tooltip-text-color: #FAFAFA;
    --highlight-text-color: #4CAF50; /* Green for dark mode highlights */
    --highlight-underline-color: #4CAF50;
}

body {
    color: var(--text-color);
}

.poem-container {
    font-size: 1.1em;
    line-height: 1.8;
    margin-bottom: 30px;
    padding: 20px;
    border-radius: 8px;
    background-color: var(--secondary-background-color);
    color: var(--text-color);
}

.stanza {
    margin-bottom: 25px;
}

.annotated-line {
    /* Mặc định màu chữ của dòng thơ */
    color: var(--text-color);
    position: relative; /* Quan trọng để tooltip định vị tương đối */
    cursor: help; /* Con trỏ chuột hình dấu hỏi */
    text-decoration: underline; /* Gạch chân để dễ nhận biết */
    text-decoration-color: var(--highlight-underline-color);
    text-underline-offset: 3px; /* Khoảng cách gạch chân */
    text-decoration-thickness: 1px;
    /* Optional: highlight text color for annotated lines */
    /* color: var(--highlight-text-color); */
}

/* Tooltip style */
.custom-tooltip {
    display: none; /* Hidden by default */
    position: absolute;
    z-index: 1000; /* Đảm bảo tooltip nằm trên cùng */
    padding: 10px 15px;
    background-color: var(--tooltip-bg-color);
    color: var(--tooltip-text-color);
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    font-size: 0.9em;
    line-height: 1.4;
    max-width: 250px; /* Giới hạn chiều rộng tooltip */
    text-align: left;
    white-space: normal; /* Cho phép chú giải xuống dòng */
    opacity: 0;
    transition: opacity 0.2s ease-in-out;
}

.custom-tooltip.show {
    opacity: 1;
    display: block;
}

/* CSS để giấu tooltip mặc định của trình duyệt cho title attribute */
[data-annotation]:hover::before,
[data-annotation]:hover::after {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

# --- Hiển thị bài thơ với các dòng được đánh dấu ---
html_content = ""
for stanza_idx, stanza in enumerate(poem_data_detailed):
    html_content += f'<div class="stanza" id="stanza-{stanza_idx}">'
    for line_idx, line_data in enumerate(stanza["lines"]):
        line_text = line_data["text"]
        annotation = line_data["annotation"]

        if annotation:
            # Đánh dấu dòng cần chú giải bằng class và data-annotation
            # Thêm id để có thể định vị chính xác bằng JavaScript
            html_content += f'<p><span class="annotated-line" id="line-{stanza_idx}-{line_idx}" data-annotation="{annotation}">{line_text}</span></p>'
        else:
            html_content += f'<p>{line_text}</p>'
    html_content += '</div>'

# Thêm container cho tooltip, sẽ được quản lý bởi JavaScript
html_content += '<div id="customPoemTooltip" class="custom-tooltip"></div>'

st.markdown(f'<div class="poem-container">{html_content}</div>', unsafe_allow_html=True)

# --- JavaScript để xử lý Tooltip (onmouseover/onmouseout) ---
# Đặt script này ở cuối cùng để đảm bảo DOM đã được load hoàn chỉnh
js_code = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const annotatedLines = document.querySelectorAll('.annotated-line');
    const tooltip = document.getElementById('customPoemTooltip');

    annotatedLines.forEach(line => {
        line.addEventListener('mouseover', function(event) {
            const annotationText = this.getAttribute('data-annotation');
            if (annotationText) {
                tooltip.innerHTML = annotationText;
                tooltip.classList.add('show');

                // Lấy vị trí của dòng thơ
                const rect = this.getBoundingClientRect();
                const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
                const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

                // Tính toán vị trí của tooltip
                // Đặt tooltip phía trên và giữa dòng
                let tooltipX = rect.left + scrollLeft + (rect.width / 2) - (tooltip.offsetWidth / 2);
                let tooltipY = rect.top + scrollTop - tooltip.offsetHeight - 10; // 10px above the line

                // Đảm bảo tooltip không bị tràn ra ngoài màn hình bên trái
                if (tooltipX < scrollLeft) {
                    tooltipX = scrollLeft + 5; // 5px padding from left edge
                }
                // Đảm bảo tooltip không bị tràn ra ngoài màn hình bên phải
                if (tooltipX + tooltip.offsetWidth > window.innerWidth + scrollLeft) {
                    tooltipX = window.innerWidth + scrollLeft - tooltip.offsetWidth - 5; // 5px padding from right edge
                }
                // Đảm bảo tooltip không bị tràn ra ngoài màn hình phía trên
                if (tooltipY < scrollTop) {
                    tooltipY = rect.bottom + scrollTop + 10; // If no space above, put it below
                }


                tooltip.style.left = tooltipX + 'px';
                tooltip.style.top = tooltipY + 'px';
            }
        });

        line.addEventListener('mouseout', function() {
            tooltip.classList.remove('show');
            tooltip.innerHTML = ''; // Clear content
        });
    });
});
</script>
"""

st.markdown(js_code, unsafe_allow_html=True)

st.sidebar.header("Thông Tin")
st.sidebar.info("Di chuột vào các dòng thơ được gạch chân để xem chú giải chi tiết cho từng dòng.")