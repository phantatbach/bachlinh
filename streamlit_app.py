import streamlit as st
import streamlit.components.v1 as components

# Configure the page
st.set_page_config(
    page_title="Bách ❤️🔒 Thảo Linh",
    layout="centered"
)

# ---- Title ----
st.title("Bách ❤️🔒 Thảo Linh")

# ---- Image Section ----
st.header("Ảnh của chúng ta ❤️")
cols = st.columns(2)

# Replace the paths below with your actual image file paths or URLs
with cols[0]:
    st.image("images/bach.jpg", caption="Bách", use_container_width=True)
with cols[1]:
    st.image("images/linh.jpg", caption="Thảo Linh", use_container_width=True)

st.header("Những khoảnh khắc đáng nhớ ❤️")
cols = st.columns(2)

# Replace the paths below with your actual image file paths or URLs
with cols[0]:
    st.image("images/cute-vid-call.jpg", caption="Những cuộc trò chuyện hằng đêm.", use_container_width=True)
with cols[1]:
    st.image("images/texting.jpg", caption="Những lời chúc đều đặn.", use_container_width=True)

# ---- Relationship Summary ----
st.header("Cuộc tình của chúng ta ❤️")

# Dữ liệu bài thơ chi tiết
poem_data_detailed = [
    {
        "stanza_number": 1,
        "lines": [
            {"text": "xsCó con ong nhỏ chăm ngoan,<br>Bay đi thụ phấn giữa ngàn bông hoa.<br>Trong rừng biết mấy loài hoa,<br>Ấy mà nó lại đậu vào Thảo Linh. ❤️ ", "annotation":  "Ai hiểu thì hiểu thôi! - 11/04/2025"}
        ]
    },
    {
        "stanza_number": 2,
        "lines": [
            {"text": "Đầu tiên hỏi chuyện linh tinh:<br>Học hành, công việc, dự định tương lai.<br>Câu chuyện cứ thế kéo dài,<br>Lái sang câu chuyện gia tài cô Vân.<br>Mặc dù vất vả muôn phần,<br>Chăm ba đứa nhỏ, gian truân nặng nề.<br>Ấy mà cô cũng chẳng nề,<br>Nuôi ba đứa lớn, đề huề đó nha.<br>Linh-đầu, Ngọc-thứ, Gấu-ba.<br>Rồi sang câu chuyện mẹ cha ngọt ngào. ❤️", "annotation": "Dù chỉ mới quen nhưng cả hai đã có những cuộc trò chuyện đều đặn."},
        ]        
    },
    {
        "stanza_number": 3,
        "lines": [
            {"text": "Thời gian cứ thế ào ào,<br>Cả hai dính chặt lúc nào không hay!<br>Thế mà Linh vẫn loay hoay<br>Nên yêu hay bỏ, nghĩ ngày nghĩ đêm.<br>Nghĩ về trò chuyện hằng đêm,<br>Nghĩ về những lúc yếu mềm cô đơn,<br>Nghĩ về cái thiệt cái hơn,<br>Yêu xa là khổ, giận hờn vu vơ. 😔", "annotation": "Mặc dù có cảm tình, Linh vẫn không chắc chắn liệu có nên tiến xa hơn không. Điều đó khiến Linh giữ một khoảng cách nhất định với Bách."},
        ]        
    },
    {
        "stanza_number": 4,
        "lines": [
            {"text": "Bách thì mong mỏi đợi chờ<br>Những dòng tin nhắn lập lờ từ Linh.<br>Đôi khi chỉ nói linh tinh<br>Mà vui như Tết, một mình đã lâu<br>Ấy mà đời đẹp vậy đâu!<br>Sóng yên bể lặng, u sầu than ai!<br>Đợi chờ cứ thế kéo dài<br>Thích nhau rồi cũng nhạt phai đôi phần.<br>Chịu không nổi, cứ lần chần<br>Bách đành chủ động xoá dần chữ si. 👋", "annotation": "Mặc dù có cảm tình với Linh và cũng biết Linh có cảm tình với mình, nhưng thấy Linh vẫn chần chừ và không chắc chắn, Bách đành ... xóa biệt hiệu. - 01/05/2025"},
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
                    style="cursor:pointer; color:#d16e94; font-weight:500;">
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
st.caption("Made with ❤️ by Bách for Thảo Linh")