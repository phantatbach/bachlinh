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

st.set_page_config(layout="centered", page_title="Bài Thơ Tương Tác (Tooltip Dòng)", initial_sidebar_state="expanded")

# Dữ liệu bài thơ với chú giải chi tiết từng dòng/đoạn
poem_data_detailed = [
    {
        "stanza_number": 1,
        "lines": [
            {"text": "Áo em trắng quá nhìn không ra", "annotation": "Gợi hình ảnh trong sáng, tinh khôi. Màu áo trắng tượng trưng cho sự thuần khiết."},
            {"text": "Hàng cây đứng đó cũng như là", "annotation": None}, # Không có chú giải cho dòng này
            {"text": "Bóng mát che riêng đời chúng ta", "annotation": "Sự che chở, gắn bó mật thiết. Tình yêu đôi lứa được ví như bóng mát an lành."},
            {"text": "Ngón tay thon thả ngắt lá đa.", "annotation": "Hành động tinh tế, nhẹ nhàng, thể hiện sự dịu dàng của người con gái."}
        ]
    },
    {
        "stanza_number": 2,
        "lines": [
            {"text": "Chiều nay tiếng hát vẳng trong mưa", "annotation": "Không gian lãng mạn, hơi buồn. Tiếng hát trong mưa mang lại cảm xúc sâu lắng."},
            {"text": "Anh nhớ em nhiều biết mấy cho vừa", "annotation": "Nỗi nhớ sâu sắc, da diết, không thể đong đếm được."},
            {"text": "Em ơi thôi nhé đừng buồn nữa", "annotation": "Lời an ủi, vỗ về từ người yêu."},
            {"text": "Phía cuối con đường vẫn có ta.", "annotation": "Sự hứa hẹn, đồng hành, niềm tin vào tương lai."}
        ]
    },
    {
        "stanza_number": 3,
        "lines": [
            {"text": "Trăng vàng hiu hắt giữa không gian", "annotation": "Cảnh vật tĩnh lặng, có chút u hoài, gợi suy tư về vũ trụ."},
            {"text": "Gió thoảng hương xưa thổi nhẹ nhàng", "annotation": "Gợi nhớ kỷ niệm, cảm xúc xưa cũ. Hương xưa mang theo những ký ức ngọt ngào."},
            {"text": "Ngỡ ngàng bỗng thấy bao la lắm", "annotation": "Cảm giác ngỡ ngàng trước sự rộng lớn, vô tận của vũ trụ."},
            {"text": "Cuộc đời này vẫn đẹp vô vàn.", "annotation": "Thông điệp lạc quan về vẻ đẹp tiềm ẩn của cuộc sống, dù có lúc khó khăn."}
        ]
    }
]

st.title("Bài Thơ Tương Tác: Áo Trắng (Tooltip Theo Dòng)")
st.write("Di chuột (hover) vào các dòng thơ **được gạch chân** để xem chú giải!")

# --- CSS và JavaScript được đặt trong một khối duy nhất để quản lý tốt hơn ---
st.markdown(f"""
<style>
/* Reset một số margin/padding mặc định để kiểm soát bố cục tốt hơn */
p {{ margin: 0; padding: 0; }}

/* Streamlit theme variables (tùy chỉnh màu sắc) */
:root {{ /* Light Mode default */
    --text-color: #31333F;
    --background-color: #FFFFFF;
    --secondary-background-color: #F0F2F6;
    --primary-color: #FF4B4B;

    --poem-bg-color: var(--secondary-background-color);
    --poem-text-color: var(--text-color);

    --tooltip-bg-color: #333;
    --tooltip-text-color: #f9f9f9;
    --highlight-underline-color: #007bff; /* Underline color */
    --highlight-text-color-light: #007bff; /* Color for underlined text in light mode */
}}

[data-baseweb="dark"] {{ /* Dark Mode specific colors */
    --text-color: #FAFAFA;
    --background-color: #0E1117;
    --secondary-background-color: #1A1C20;
    --primary-color: #FF4B4B;

    --poem-bg-color: var(--secondary-background-color);
    --poem-text-color: var(--text-color);

    --tooltip-bg-color: #555;
    --tooltip-text-color: #FAFAFA;
    --highlight-underline-color: #4CAF50; /* Green for dark mode highlights */
    --highlight-text-color-dark: #4CAF50; /* Color for underlined text in dark mode */
}}

/* Định dạng chung cho body */
body {{
    color: var(--text-color);
}}

/* Container chính bao quanh toàn bộ bài thơ */
.poem-container {{
    font-family: 'Times New Roman', Times, serif; /* Font chữ thơ */
    font-size: 1.2em; /* Tăng kích thước chữ */
    line-height: 1.8;
    margin-bottom: 30px;
    padding: 25px;
    border-radius: 8px;
    background-color: var(--poem-bg-color);
    color: var(--poem-text-color);
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}

/* Định dạng cho từng khổ thơ */
.stanza {{
    margin-bottom: 2em; /* Khoảng cách giữa các khổ thơ */
    padding-top: 1em; /* Khoảng cách trên đầu khổ thơ */
}}

/* Định dạng cho các dòng thơ có chú giải */
.annotated-line {{
    position: relative; /* Quan trọng cho việc định vị tooltip */
    cursor: help; /* Con trỏ chuột hình dấu hỏi */
    text-decoration: underline; /* Gạch chân để dễ nhận biết */
    text-decoration-color: var(--highlight-underline-color);
    text-underline-offset: 3px;
    text-decoration-thickness: 1px;
    /* Điều chỉnh màu chữ riêng cho dòng được highlight */
    color: var(--text-color); /* Mặc định theo theme */
    /* Khi ở Light Mode, áp dụng màu highlight riêng */
    [data-baseweb="light"] & {{
        color: var(--highlight-text-color-light);
    }}
    /* Khi ở Dark Mode, áp dụng màu highlight riêng */
    [data-baseweb="dark"] & {{
        color: var(--highlight-text-color-dark);
    }}
}}

/* Tooltip style */
.custom-tooltip {{
    display: none; /* Ẩn mặc định */
    position: absolute;
    z-index: 1000; /* Đảm bảo tooltip nằm trên cùng */
    padding: 10px 15px;
    background-color: var(--tooltip-bg-color);
    color: var(--tooltip-text-color);
    border-radius: 5px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    font-size: 0.9em;
    line-height: 1.4;
    max-width: 280px; /* Giới hạn chiều rộng tooltip */
    text-align: left;
    white-space: normal; /* Cho phép chú giải xuống dòng */
    opacity: 0;
    transition: opacity 0.2s ease-in-out;
}}

.custom-tooltip.show {{
    opacity: 1;
    display: block;
}}

/* Ngăn trình duyệt hiển thị tooltip mặc định cho title attribute (nếu có) */
[data-annotation]:hover::before,
[data-annotation]:hover::after {{
    display: none !important;
}}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {{
    const annotatedLines = document.querySelectorAll('.annotated-line');
    let tooltip = document.getElementById('customPoemTooltip');

    // Nếu tooltip chưa tồn tại (ví dụ Streamlit refresh), tạo nó
    if (!tooltip) {{
        tooltip = document.createElement('div');
        tooltip.id = 'customPoemTooltip';
        tooltip.classList.add('custom-tooltip');
        document.body.appendChild(tooltip); // Thêm vào body để dễ định vị tuyệt đối
        console.log("Tooltip element created and appended.");
    }} else {{
        // Reset tooltip để tránh lỗi nếu Streamlit refresh
        tooltip.classList.remove('show');
        tooltip.innerHTML = '';
        console.log("Existing tooltip element found and reset.");
    }}


    annotatedLines.forEach(line => {{
        line.addEventListener('mouseenter', function(event) {{ // Dùng mouseenter để tránh bubbling
            const annotationText = this.getAttribute('data-annotation');
            if (annotationText) {{
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
                if (tooltipX < scrollLeft + 5) {{ // 5px padding from left edge
                    tooltipX = scrollLeft + 5;
                }}
                // Đảm bảo tooltip không bị tràn ra ngoài màn hình bên phải
                if (tooltipX + tooltip.offsetWidth > window.innerWidth + scrollLeft - 5) {{ // 5px padding from right edge
                    tooltipX = window.innerWidth + scrollLeft - tooltip.offsetWidth - 5;
                }}
                // Đảm bảo tooltip không bị tràn ra ngoài màn hình phía trên
                if (tooltipY < scrollTop + 5) {{ // If no space above, put it below
                    tooltipY = rect.bottom + scrollTop + 10;
                }}

                tooltip.style.left = tooltipX + 'px';
                tooltip.style.top = tooltipY + 'px';
                console.log("Tooltip displayed for line:", this.id);
            }}
        }});

        line.addEventListener('mouseleave', function() {{ // Dùng mouseleave
            tooltip.classList.remove('show');
            tooltip.innerHTML = ''; // Clear content
            console.log("Tooltip hidden for line:", this.id);
        }});
    }});
}});
</script>
""", unsafe_allow_html=True)


# --- Hiển thị bài thơ với các dòng được đánh dấu ---
html_poem_structure = ""
for stanza_idx, stanza in enumerate(poem_data_detailed):
    html_poem_structure += f'<div class="stanza" id="stanza-{stanza_idx}">'
    for line_idx, line_data in enumerate(stanza["lines"]):
        line_text = line_data["text"]
        annotation = line_data["annotation"]

        # Sử dụng f-string để escape dấu ngoặc kép trong annotation nếu cần (JSON.stringify)
        # Hoặc đảm bảo chú giải không chứa dấu ngoặc kép không được escape
        escaped_annotation = annotation.replace('"', '&quot;') if annotation else ''

        if annotation:
            # Bọc dòng thơ cần chú giải trong <span> với class và data-annotation
            # Mỗi dòng đều nằm trong thẻ <p> riêng để dễ kiểm soát layout
            html_poem_structure += f'<p><span class="annotated-line" id="line-{stanza_idx}-{line_idx}" data-annotation="{escaped_annotation}">{line_text}</span></p>'
        else:
            html_poem_structure += f'<p>{line_text}</p>'
    html_poem_structure += '</div>'

# Thêm container cho toàn bộ bài thơ và tooltip element
# Việc thêm customPoemTooltip vào body trong JS sẽ giúp nó định vị chính xác hơn
st.markdown(f'<div class="poem-container">{html_poem_structure}</div>', unsafe_allow_html=True)

st.sidebar.header("Thông Tin")
st.sidebar.info("Di chuột vào các dòng thơ được gạch chân để xem chú giải chi tiết cho từng dòng.")