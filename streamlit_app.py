import streamlit as st
import streamlit.components.v1 as components
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
st.header("Thơ về cuộc tình")

# Dữ liệu bài thơ chi tiết
poem_data_detailed = [
    {
        "stanza_number": 1,
        "lines": [
            {"text": "Có con ong nhỏ chăm ngoan\nBay đi thụ phấn giữa ngàn bông hoa\nTrong rừng biết mấy loài hoa\nẤy mà nó lại đậu vào Thảo Linh", "annotation":  "Ai hiểu thì hiểu thôi"},
            {"text": "Hàng cây đứng đó cũng như là", "annotation": None},
            {"text": "Bóng mát che riêng đời chúng ta", "annotation": "Sự che chở, gắn bó mật thiết. Tình yêu đôi lứa được ví như bóng mát an lành."},
            {"text": "Ngón tay thon thả ngắt lá đa.", "annotation": "Hành động tinh tế, nhẹ nhàng, thể hiện sự dịu dàng của người con gái."}
        ]
    }
]

# HTML hiển thị thơ và diễn giải
html = "<div style='font-family:serif; font-size:18px;'>"

for stanza in poem_data_detailed:
    html += "<div style='margin-bottom: 20px;'>"
    for idx, line in enumerate(stanza["lines"]):
        line_id = f"stanza{stanza['stanza_number']}_line{idx}"
        annotation = line["annotation"]

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
            html += f"""
            <div style="margin-bottom:8px;">
                <span style="color:#aaaaaa;">{line['text']}</span>
            </div>
            """
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

# Chèn toàn bộ HTML + JS bằng components.html (cho phép <script> chạy)
components.html(html, height=600, scrolling=True)

# ---- Footer ----
st.markdown("---")
st.caption("Made with ❤️ by PT Bách for Thảo Linh")