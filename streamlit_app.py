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
            {"text": "Có con ong nhỏ chăm ngoan<br>Bay đi thụ phấn giữa ngàn bông hoa<br>Trong rừng biết mấy loài hoa<br>Ấy mà nó lại đậu vào Thảo Linh", "annotation":  "Ai hiểu thì hiểu thôi"}
        ]
    },
    {
        "stanza_number": 2,
        "lines": [
            {"text": "Đầu tiên hỏi chuyện linh tinh<br>Học hành, công việc, dự định tương lai<br>Câu chuyện cứ thế kéo dài<br>Lái sang câu chuyện gia tài cô Vân<br>Mặc dù vất vả muôn phần<br>Chăm ba đứa nhỏ, gian truân nặng nề<br>Ấy mà cô cũng chẳng nề<br>Nuôi ba đứa lớn, đề huề đó nha<br>Linh-đầu, Ngọc-thứ, Gấu-ba<br>Rồi sang câu chuyện mẹ cha ngọt ngào", "annotation": None},
        ]        
    },
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