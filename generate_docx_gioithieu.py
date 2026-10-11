import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls
import os
import shutil
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

doc = docx.Document()

# Page Margins: 1 inch (25.4mm)
for section in doc.sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)

# Brand Colors
COLOR_DARK_GREEN = RGBColor(38, 74, 49)      # #264A31
COLOR_ACCENT_GREEN = RGBColor(43, 105, 62)   # #2B693E
COLOR_TEXT_MAIN = RGBColor(30, 35, 32)       # #1E2320
COLOR_TEXT_MUTED = RGBColor(85, 95, 88)      # #555F58
HEX_BG_CALLOUT = "F2EFE9"
HEX_BORDER_GREEN = "5B8266"
HEX_LIGHT_GREEN = "E8EFE9"

def set_run_font(run, name="Arial", size_pt=10.5, color=COLOR_TEXT_MAIN, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.color.rgb = color
    run.bold = bold
    run.italic = italic

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    set_run_font(run, name="Arial", size_pt=14, color=COLOR_DARK_GREEN, bold=True)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    set_run_font(run, name="Arial", size_pt=12, color=COLOR_ACCENT_GREEN, bold=True)
    return p

def add_body_paragraph(doc, text="", space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.25
    if text:
        run = p.add_run(text)
        set_run_font(run, name="Arial", size_pt=10.5, color=COLOR_TEXT_MAIN)
    return p

def add_callout_box(doc, text_list, bg_color=HEX_LIGHT_GREEN, border_color=HEX_BORDER_GREEN):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.7)
    
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
    tcPr.append(shd)
    
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.25
    
    for i, t in enumerate(text_list):
        if i > 0:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.25
        run = p.add_run(t)
        set_run_font(run, name="Arial", size_pt=10.5, color=COLOR_TEXT_MAIN)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

# ==================== DOCUMENT HEADER ====================
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(2)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
t_run = title_p.add_run("TÀI LIỆU GIỚI THIỆU BẢN THÂN & HỒ SƠ PHỎNG VẤN")
set_run_font(t_run, name="Arial", size_pt=18, color=COLOR_DARK_GREEN, bold=True)

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_before = Pt(2)
sub_p.paragraph_format.space_after = Pt(14)
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
s_run = sub_p.add_run("Ứng viên: Lê Thị Hoàng Cẩm — Marketing Executive (Content & Digital Marketing)\nSố điện thoại: 0363 123 121 | Email: lethihoangcam5@gmail.com | Khu vực: TP. Hồ Chí Minh")
set_run_font(s_run, name="Arial", size_pt=9.5, color=COLOR_TEXT_MUTED, italic=True)

# Divider line
hr_p = doc.add_paragraph()
hr_p.paragraph_format.space_after = Pt(10)
pPr = hr_p._p.get_or_add_pPr()
pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="1" w:color="{HEX_BORDER_GREEN}"/></w:pBdr>')
pPr.append(pBdr)

# ==================== PHẦN 1 ====================
add_heading_1(doc, "PHẦN 1: CÁC PHIÊN BẢN GIỚI THIỆU BẢN THÂN (ELEVATOR PITCH)")

# --- Version 1 ---
add_heading_2(doc, "1. Phiên bản Đi Phỏng Vấn Trực Tiếp (~1 đến 1.5 Phút)")
add_body_paragraph(doc, "Mục đích: Dùng khi người phỏng vấn mở lời: 'Em hãy giới thiệu ngắn gọn về bản thân mình'. Phong thái: Tự tin, nụ cười thân thiện, giọng nói rõ ràng, điểm nhấn sắc sảo vào năng lực tự chủ Media và kết quả thực tế.")

pitch_v1 = [
    "\"Dạ em chào Anh/Chị, em là Hoàng Cẩm, là một Marketing Executive với hơn 3 năm kinh nghiệm thực chiến chuyên sâu về Content Marketing và Digital Marketing đa nền tảng (Facebook, TikTok, Reels, Website).",
    "Thế mạnh nổi bật nhất của em là khả năng tự chủ 100% quy trình sản xuất Media — từ nghiên cứu insight khách hàng, lên ý tưởng, viết kịch bản phân cảnh, tự quay dựng video ngắn chuẩn xu hướng cho đến trực tiếp vận hành Paid-Ads và đo lường hiệu suất.",
    "Về kinh nghiệm thực tế, em có 3 điểm nổi bật chính:",
    "• Thứ nhất, tại Chăm sóc sức khỏe Thân Tâm: Em trực tiếp quản trị và phát triển nội dung cho kênh chính của công ty. Đặc biệt, khi công ty mở rộng dự án truyền thông số y tế MEDDC, em là người trực tiếp xây dựng kênh mới này từ con số 0. Bằng chuỗi Reels giáo dục sức khỏe kết nối nhãn hàng lớn (Comfort, ColosBaby) với bác sĩ BV Nhi Đồng 1 & 175, chỉ sau 28 ngày kênh mới đã bứt phá đạt hơn 98.400 lượt xem, tăng trưởng +880% tương tác và tăng +547% follower.",
    "• Thứ hai, với vai trò KOC & Content Creator cá nhân: Em vừa hợp tác review cùng các nhãn hàng da liễu hàng đầu (L’Oréal, Vichy, Eucerin, SVR), vừa trực tiếp vận hành mô hình Social Commerce / Affiliate trên chính kênh của mình, mang về doanh thu GMV hơn 239 triệu VNĐ với hơn 3.300 đơn hàng.",
    "• Thứ ba, tại Dược phẩm OPV: Em phụ trách Content & Quản trị Fanpage, chuyên sâu về sản xuất bài viết chuẩn SEO Y Dược và trực tiếp quản lý, chăm sóc Fanpage OPV, tương tác cộng đồng giúp tăng tiếp cận tự nhiên (Reach) 25–30%.",
    "Em định vị mình là nhân sự Marketing vừa có sự nhạy bén sáng tạo bắt trend, vừa có tư duy thực chiến và tối ưu số liệu chuyển đổi. Em rất tự tin kinh nghiệm thực chiến này sẽ giúp em đóng góp hiệu quả và nhanh chóng vào các mục tiêu truyền thông của Quý công ty ạ.\""
]
add_callout_box(doc, pitch_v1, bg_color="F2EFE9", border_color="2B693E")

# Breakdown cấu trúc bài nói
p_struct = add_body_paragraph(doc)
r = p_struct.add_run("💡 Phân tích cấu trúc đắt giá của bài nói trên:")
set_run_font(r, name="Arial", size_pt=10, color=COLOR_DARK_GREEN, bold=True)
bullets_struct = [
    ("Bước 1 - Lời chào & Định vị (15s): ", "Nêu rõ chức danh 'Marketing Executive' + 3 năm kinh nghiệm thực chiến Content & Digital đa nền tảng."),
    ("Bước 2 - Thế mạnh tự chủ Media (20s): ", "Nhấn mạnh 'Tự chủ 100% quy trình Media A-Z' — tự quay dựng, không phụ thuộc agency, tiết kiệm tối đa chi phí cho công ty."),
    ("Bước 3 - Ba trụ cột kinh nghiệm (45s): ", "Kênh chính Thân Tâm + tài năng build kênh mới MEDDC từ số 0 (+880% tương tác, 98.4K views) | KOC kiêm Creator Affiliate (239M GMV) | Dược phẩm OPV (Quản trị Fanpage & SEO Y Dược)."),
    ("Bước 4 - Cam kết đóng góp (15s): ", "Khẳng định sự kết hợp giữa Sáng tạo bắt trend + Tư duy số liệu chuyển đổi, sẵn sàng tạo kết quả cho doanh nghiệp.")
]
for title, desc in bullets_struct:
    bp = doc.add_paragraph()
    bp.paragraph_format.left_indent = Inches(0.25)
    bp.paragraph_format.space_before = Pt(2)
    bp.paragraph_format.space_after = Pt(2)
    r1 = bp.add_run("• " + title)
    set_run_font(r1, name="Arial", size_pt=9.5, color=COLOR_TEXT_MAIN, bold=True)
    r2 = bp.add_run(desc)
    set_run_font(r2, name="Arial", size_pt=9.5, color=COLOR_TEXT_MUTED)

# --- Version 2 ---
add_heading_2(doc, "2. Phiên bản Cover Letter / Email Ứng Tuyển / Tóm Tắt LinkedIn")
add_body_paragraph(doc, "Mục đích: Sử dụng trong thư ứng tuyển gửi nhà tuyển dụng hoặc đặt ở phần 'Giới thiệu' trên trang LinkedIn cá nhân.")

pitch_v2 = [
    "\"Tôi là Lê Thị Hoàng Cẩm, chuyên viên Marketing Executive sở hữu hơn 3 năm kinh nghiệm thực chiến trong việc hoạch định và triển khai chiến lược Content & Digital Marketing đa kênh (Facebook, TikTok, Reels, Website).",
    "Với thế mạnh vượt trội về sáng tạo video ngắn (Short-form Video) và khả năng tự chủ 100% quy trình sản xuất Media từ khâu kịch bản đến quay dựng và quản trị tương tác kênh, tôi có kinh nghiệm thực tế đa dạng:",
    "• Quản lý truyền thông cho Chăm sóc sức khỏe Thân Tâm, đồng thời trực tiếp xây dựng thành công từ con số 0 kênh truyền thông số y tế MEDDC kết nối nhãn hàng lớn (Comfort, ColosBaby) với BV Nhi Đồng 1 & BV 175, đạt 98.4K+ lượt xem và tăng trưởng +880% tương tác chỉ sau 28 ngày.",
    "• Hoạt động với vai trò KOC & Content Creator cá nhân (Creator và KOC là một), hợp tác review cùng các thương hiệu da liễu lớn (L'Oréal, Vichy, Eucerin), kết hợp vận hành Affiliate đạt doanh thu GMV hơn 239M VNĐ với 3.300+ đơn hàng xuất bán.",
    "• Trực tiếp quản trị và chăm sóc Fanpage Dược phẩm OPV kết hợp xây dựng hệ thống nội dung bài viết chuẩn SEO Y Dược, thúc đẩy lượng tiếp cận tự nhiên tăng 25–30%.",
    "Tôi hướng tới mục tiêu đồng hành cùng doanh nghiệp xây dựng những chiến dịch truyền thông chạm đúng insight, tối ưu chi phí và tạo ra tác động định lượng đo lường được.\""
]
add_callout_box(doc, pitch_v2, bg_color="F9FBF9", border_color="5B8266")

# --- Version 3 ---
add_heading_2(doc, "3. Phiên bản Ngắn Gọn (Quick Bio 30 Giây / Đoạn Tóm Tắt Đầu CV)")
add_body_paragraph(doc, "Mục đích: Dành cho phần 'Mục tiêu nghề nghiệp' ở đầu CV hoặc khi người phỏng vấn yêu cầu 'Nói ngắn gọn về em trong 3 câu'.")

pitch_v3 = [
    "\"Tôi là Hoàng Cẩm — Marketing Executive với hơn 3 năm kinh nghiệm thực chiến về Content Marketing và Digital Marketing đa nền tảng. Thế mạnh cốt lõi của tôi là tự chủ sản xuất Short-form video A-Z, sở hữu kinh nghiệm quản lý kênh chính Thân Tâm và xây mới từ số 0 kênh y tế MEDDC (98.4K views, +880% tương tác trong 28 ngày), đồng thời vận hành hiệu quả kênh KOC/Creator cá nhân đạt GMV 239M+ VNĐ. Tôi luôn hướng đến việc kết hợp giữa sáng tạo nội dung bắt trend và tư duy tối ưu số liệu chuyển đổi thực tế.\""
]
add_callout_box(doc, pitch_v3, bg_color="F2EFE9", border_color="2B693E")

# ==================== PHẦN 2 ====================
doc.add_page_break()
add_heading_1(doc, "PHẦN 2: BỘ CÂU HỎI PHỎNG VẤN MỞ RỘNG VỀ BẢN THÂN & CÁCH TRẢ LỜI ĐẮT GIÁ")
add_body_paragraph(doc, "Các câu hỏi nhà tuyển dụng thường xoáy sâu sau phần giới thiệu bản thân, bám sát các trải nghiệm thực tế của bạn:")

qa_list = [
    (
        "Câu hỏi 1: 'Kênh chính em quản lý là Thân Tâm, vậy cơ duyên nào em tạo và phát triển kênh MEDDC đạt 98.4K views?'",
        "Gợi ý trả lời sắc sảo:",
        "\"Dạ, tại công ty, trách nhiệm cốt lõi của em là quản trị và phát triển kênh Chăm sóc sức khỏe Thân Tâm — tập trung vào dịch vụ điều dưỡng và chăm sóc y tế tại gia. Khi em mới gia nhập công ty, dự án MEDDC bắt đầu được định hình như một kênh truyền thông số y tế kết nối các bệnh viện công (BV Nhi Đồng 1, BV 175) với các nhãn hàng tài trợ. Em được giao trọng trách xây dựng kênh này từ vạch xuất phát số 0.\nNhờ nghiên cứu kỹ insight phụ huynh cần kiến thức nhi khoa chuẩn xác từ bác sĩ, em đã lên kịch bản chuỗi Reels 45-60 giây, áp dụng công thức Hook 3 giây đầu giữ chân người xem và lồng ghép tự nhiên thông điệp của nhãn hàng (Comfort, ColosBaby). Kết quả chỉ sau 28 ngày đầu tiên, kênh MEDDC mới tạo đã đạt 98.474 lượt xem, tương tác tăng vọt +880,5% và lượng người theo dõi tăng +547%. Trải nghiệm này chứng minh em vừa có khả năng vận hành ổn định kênh chính, vừa có năng lực 'khởi nghiệp' build kênh mới từ số 0 một cách bài bản.\""
    ),
    (
        "Câu hỏi 2: 'Em là KOC Reviewer hay là TikTok Shop Creator? Hai vai trò này hỗ trợ nhau như thế nào?'",
        "Gợi ý trả lời sắc sảo:",
        "\"Dạ, thực tế với em, KOC và Content Creator là MỘT thể thống nhất trên cùng kênh cá nhân của em. Khi làm việc với các nhãn hàng mỹ phẩm lớn như L’Oréal, Vichy hay Eucerin, em đóng vai trò là KOC Reviewer trải nghiệm thực tế và truyền tải thông điệp thương hiệu uy tín đến người theo dõi. Nhưng thay vì chỉ nhận thù lao booking đơn thuần, em tận dụng chính nội dung review chất lượng đó để gắn link giỏ hàng TikTok Shop Affiliate. Nhờ sự kết hợp này, kênh của em vừa có uy tín thương hiệu để được mời dự sự kiện ra mắt độc quyền, vừa tạo ra hiệu quả chuyển đổi thực tế với doanh thu GMV đạt hơn 239.9 triệu VNĐ và hơn 3.300 đơn hàng. Điều này giúp em rèn luyện tư duy Performance Marketing: Nội dung hay phải đi đôi với doanh số bán hàng.\""
    ),
    (
        "Câu hỏi 3: 'Tại Dược phẩm OPV, công việc cụ thể của em là gì, có làm Brand Marketing không?'",
        "Gợi ý trả lời sắc sảo:",
        "\"Dạ, tại Dược phẩm OPV, em không làm Brand Marketing và cũng không phụ trách quảng cáo Paid-Ads, mà vai trò chính của em là Chuyên viên Content & Quản trị Fanpage. Trọng tâm công việc hàng ngày của em là trực tiếp quản lý, chăm sóc Fanpage OPV, tương tác và giải đáp người theo dõi; đồng thời lên kế hoạch và biên soạn chuỗi bài viết chuẩn SEO Y Dược cung cấp kiến thức bệnh học hữu ích cho người đọc, phối hợp cùng Designer làm ảnh. Nhờ tối ưu hóa chất lượng nội dung và chăm sóc tương tác sát sao, độ tiếp cận tự nhiên (Organic Reach) của trang đã tăng trưởng 25-30% và tốc độ tăng follower duy trì ổn định ở mức 7-8%.\""
    ),
    (
        "Câu hỏi 4: 'Mục tiêu nghề nghiệp trong 1 đến 2 năm tới của em tại công ty là gì?'",
        "Gợi ý trả lời sắc sảo:",
        "\"Dạ, trong năm đầu tiên, em muốn đóng góp toàn bộ năng lực tự chủ Media A-Z để nâng cao hiệu suất nội dung của công ty, xây dựng các kênh truyền thông đạt lượng tương tác tự nhiên cao và tối ưu chi phí quảng cáo. Trong 2 đến 3 năm tới, khi đã am hiểu sâu sắc sản phẩm và văn hóa công ty, em đặt mục tiêu phát triển lên vị trí Senior Marketing Executive hoặc Content Lead, chịu trách nhiệm quản lý đội ngũ sáng tạo nội dung, chuẩn hóa quy trình sản xuất Media và đồng hành cùng Ban lãnh đạo trong các chiến dịch truyền thông đa kênh lớn hơn.\""
    )
]

for q, tag, a in qa_list:
    qp = doc.add_paragraph()
    qp.paragraph_format.space_before = Pt(8)
    qp.paragraph_format.space_after = Pt(2)
    qr = qp.add_run(q)
    set_run_font(qr, name="Arial", size_pt=10.5, color=COLOR_DARK_GREEN, bold=True)
    
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.cell(0, 0)
    cell.width = Inches(6.7)
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="FAF8F5"/>'))
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="16" w:space="0" w:color="{HEX_BORDER_GREEN}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(3)
    cp.paragraph_format.space_after = Pt(3)
    cp.paragraph_format.line_spacing = 1.2
    
    r_tag = cp.add_run(tag + "\n")
    set_run_font(r_tag, name="Arial", size_pt=9.5, color=COLOR_ACCENT_GREEN, bold=True)
    r_ans = cp.add_run(a)
    set_run_font(r_ans, name="Arial", size_pt=10, color=COLOR_TEXT_MAIN)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

# ==================== PHẦN 3 ====================
add_heading_1(doc, "PHẦN 3: BẢNG SỐ LIỆU MINH CHỨNG (CHEAT SHEET ĐI PHỎNG VẤN)")
add_body_paragraph(doc, "Bảng tra cứu số liệu chuẩn xác theo đúng thực tế công việc của Hoàng Cẩm:")

# Table of Metrics
table_metrics = doc.add_table(rows=5, cols=3)
table_metrics.alignment = WD_TABLE_ALIGNMENT.CENTER
table_metrics.autofit = False

headers = ["Dự án / Doanh nghiệp", "Vai trò & Bản chất công việc", "Chỉ số & Kết quả thực tế"]
col_widths = [Inches(1.8), Inches(2.5), Inches(2.4)]

# Header formatting
hdr_cells = table_metrics.rows[0].cells
for i, title in enumerate(headers):
    hdr_cells[i].width = col_widths[i]
    p = hdr_cells[i].paragraphs[0]
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(5)
    run = p.add_run(title)
    set_run_font(run, name="Arial", size_pt=10, color=RGBColor(255, 255, 255), bold=True)
    tcPr = hdr_cells[i]._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{HEX_BORDER_GREEN}"/>'))

metrics_data = [
    (
        "Chăm Sóc Sức Khỏe Thân Tâm\n(03/2026 – 09/2026)",
        "KÊNH CHÍNH QUẢN LÝ:\nVận hành Fanpage chính Thân Tâm (Y tế gia đình & Điều dưỡng tại nhà). Tự chủ kịch bản, quay dựng storyboard, thu âm mic Rode.",
        "• 100% tự chủ quy trình sản xuất Media nội bộ\n• Nâng cao uy tín thương hiệu dịch vụ tại TP.HCM\n• Tăng tỷ lệ inbox tư vấn đặt lịch khám điều dưỡng"
    ),
    (
        "Kênh Mới: MEDDC (MEDTV)\n(Truyền Thông Số BV)",
        "KÊNH MỚI XÂY TỪ SỐ 0:\nKhi mới vào công ty thì kênh được thành lập. Hoàng Cẩm tự tay sản xuất chuỗi Reels kết nối nhãn hàng (Comfort, ColosBaby) với BV Nhi Đồng 1 & 175.",
        "• 98.474 lượt xem video\n• +880,5% tương tác chỉ sau 28 ngày\n• +547% follower mới (+110 organic)\n• 37.417 người tiếp cận tự nhiên"
    ),
    (
        "KOC Reviewer & Creator\n(Kênh Cá Nhân Đa Kênh)",
        "CREATOR & KOC LÀ 1:\nVừa làm KOC Reviewer da liễu (L’Oréal, Vichy, Eucerin, SVR), vừa trực tiếp gắn link TikTok Shop Affiliate trên cùng một kênh.",
        "• GMV 239.9M VNĐ (+4,000%)\n• 3.300+ đơn hàng xuất bán thành công\n• 1.3M lượt hiển thị, 34.7K click\n• Kênh đạt 15K views/tháng (+30%)"
    ),
    (
        "Dược Phẩm OPV\n(12/2024 – 02/2026)",
        "CONTENT & QUẢN TRỊ FANPAGE:\nKhông làm Brand Mkt. Trực tiếp quản lý và chăm sóc Fanpage OPV, tương tác cộng đồng và sản xuất bài viết chuẩn SEO Y Dược.",
        "• Tiếp cận tự nhiên tăng 25 – 30%\n• Tăng trưởng follower trang 7 – 8%\n• Tối ưu tương tác cộng đồng người theo dõi\n• Phối hợp nâng cấp website doanh nghiệp"
    )
]

for row_idx, data in enumerate(metrics_data, start=1):
    row_cells = table_metrics.rows[row_idx].cells
    bg_row = "FFFFFF" if row_idx % 2 == 1 else "F9FBF9"
    for col_idx in range(3):
        row_cells[col_idx].width = col_widths[col_idx]
        p = row_cells[col_idx].paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(data[col_idx])
        set_run_font(run, name="Arial", size_pt=9.5, color=COLOR_TEXT_MAIN)
        tcPr = row_cells[col_idx]._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_row}"/>'))
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="DFDAD0"/>
                <w:left w:val="none"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="DFDAD0"/>
                <w:right w:val="none"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)

# Save Document locally
target_hrm = "/Users/Admin/Documents/HRM/Gioi_Thieu_Ban_Than_Le_Thi_Hoang_Cam.docx"
target_desktop = "/Users/Admin/Desktop/Gioi_Thieu_Ban_Than_Le_Thi_Hoang_Cam.docx"

doc.save(target_hrm)
shutil.copyfile(target_hrm, target_desktop)
print(f"Generated successfully: {target_hrm} and {target_desktop}")

# Update directly into the live Google Doc (ID: 1c_h95zxQLxH_tVO1Vq44yWotZSCF8qeNTmSnZVAd-8Y)
token_path = '/Users/Admin/Documents/KIngblue/API/token.json'
creds = Credentials.from_authorized_user_file(token_path)
drive_service = build('drive', 'v3', credentials=creds)

file_id = '1c_h95zxQLxH_tVO1Vq44yWotZSCF8qeNTmSnZVAd-8Y'
media = MediaFileUpload(target_hrm, mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document', resumable=True)

updated_file = drive_service.files().update(
    fileId=file_id,
    media_body=media,
    fields='id, name, webViewLink'
).execute()

print(f"Successfully updated live Google Doc: {file_id}")
print(f"URL: https://docs.google.com/document/d/{file_id}/edit")
