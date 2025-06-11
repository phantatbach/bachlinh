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

st.set_page_config(page_title="📜 Thơ & Diễn giải", layout="centered")

# Dữ liệu bài thơ chi tiết
poem_data_detailed = [
    {
        "stanza_number": 1,
        "lines": [
            {"text": "Áo em trắng quá nhìn không ra", "annotation": "Gợi hình ảnh trong sáng, tinh khôi. Màu áo trắng tượng trưng cho sự thuần khiết."},
            {"text": "Hàng cây đứng đó cũng như là", "annotation": None},
            {"text": "Bóng mát che riêng đời chúng ta", "annotation": "Sự che chở, gắn bó mật thiết. Tình yêu đôi lứa được ví như bóng mát an lành."},
            {"text": "Ngón tay thon thả ngắt lá đa.", "annotation": "Hành động tinh tế, nhẹ nhàng, thể hiện sự dịu dàng của người con gái."}
        ]
    }
]

st.title("📖 Bài thơ có chú giải")

# HTML hiển thị thơ và diễn giải
html = "<div style='font-family:serif; font-size:18px;'>"

for stanza in poem_data_detailed:
    html += "<div style='margin-bottom: 20px;'>"
    for idx, line in enumerate(stanza["lines"]):
        line_id = f"stanza{stanza['stanza_number']}_line{idx}"
        annotation = line["annotation"]

        # Nếu có chú giải
        if annotation:
            html += f"""
            <div style="margin-bottom:8px;">
                <span onclick="toggleExplanation('{line_id}')" 
                      style="cursor:pointer; color:#1f77b4; font-weight:500;">
                    {line['text']}
                </span>
                <div id="{line_id}" style="display:none; margin-left:20px; color:#444; font-style:italic; margin-top:4px;">
                    {annotation}
                </div>
            </div>
            """
        else:
            # Nếu không có chú giải
            html += f"<div style='margin-bottom:8px;'>{line['text']}</div>"

    html += "</div>"

html += "</div>"

# Inject JS
html += """
<script>
function toggleExplanation(id) {
  var x = document.getElementById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
</script>
"""

st.markdown(html, unsafe_allow_html=True)
