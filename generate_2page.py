import base64
import subprocess
import os

with open('/Users/Admin/Documents/HRM/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV Lê Thị Hoàng Cẩm — Lime Mood 2 Trang Chuyên Sâu</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-page: #FAF8F2;
    --card-bg: #EFECE4;
    --lime: #D4F038;
    --text-black: #111111;
    --text-muted: #4b5563;
    --bar-bg: #DDD9CF;
  }}

  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    font-family: 'Outfit', sans-serif;
    background-color: #cbd5e1;
    color: var(--text-black);
    -webkit-font-smoothing: antialiased;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  .a4-page {{
    width: 210mm;
    height: 297mm;
    margin: 0 auto 12mm auto;
    background: var(--bg-page);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
    padding: 10mm 11mm 8mm 11mm;
    box-shadow: 0 12px 30px rgba(0,0,0,0.12);
  }}

  @media print {{
    body {{ background: none; }}
    .a4-page {{
      box-shadow: none;
      margin: 0;
      width: 210mm;
      height: 297mm;
      page-break-after: always;
    }}
    .a4-page:last-child {{
      page-break-after: avoid;
    }}
  }}

  /* HEADER BENTO (PAGE 1) */
  .hero-bento {{
    display: grid;
    grid-template-columns: 50mm 1fr;
    gap: 7mm;
    align-items: center;
    margin-bottom: 4mm;
  }}
  .avatar-card {{
    width: 48mm;
    height: 52mm;
    background: var(--lime);
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    box-shadow: 0 5px 16px rgba(212, 240, 56, 0.35);
  }}
  .avatar-card img {{
    width: 90%;
    height: 90%;
    object-fit: cover;
    object-position: center top;
    border-radius: 16px;
    background: #fff;
    margin-bottom: 2mm;
  }}
  .doodle-zigzag {{
    position: absolute;
    top: 2mm;
    right: 2mm;
    width: 12mm;
    height: 18mm;
  }}
  .doodle-dot {{
    position: absolute;
    top: 8mm;
    right: 5mm;
    width: 4.5mm;
    height: 4.5mm;
    background: var(--lime);
    border-radius: 50%;
  }}
  .doodle-cross {{
    position: absolute;
    bottom: 5mm;
    right: 13mm;
    font-size: 12pt;
    font-weight: 800;
  }}

  .hero-info {{
    display: flex;
    flex-direction: column;
    gap: 2mm;
  }}
  .role-badge {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--lime);
    color: var(--text-black);
    padding: 3px 11px 3px 5px;
    border-radius: 999px;
    font-size: 8pt;
    font-weight: 800;
    width: fit-content;
  }}
  .role-icon-circle {{
    width: 15px;
    height: 15px;
    background: var(--text-black);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7.5pt;
    font-weight: 900;
  }}
  .hero-heading {{
    font-size: 25pt;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.6px;
  }}

  /* CONTACT BAR */
  .contact-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 2.5mm 5mm;
    margin-top: 1mm;
  }}
  .contact-item {{
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 8.8pt;
    font-weight: 600;
  }}
  .contact-icon {{
    width: 19px;
    height: 19px;
    background: var(--text-black);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 8pt;
    flex-shrink: 0;
  }}
  .contact-item a {{ color: var(--text-black); text-decoration: none; font-weight: 700; }}

  /* SECTION TITLE */
  .section-title {{
    font-size: 11.2pt;
    font-weight: 900;
    letter-spacing: -0.3px;
    margin-bottom: 1.8mm;
    margin-top: 3mm;
    color: var(--text-black);
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 7px;
  }}
  .section-title::after {{
    content: '';
    flex: 1;
    height: 1.5px;
    background: #e2ded5;
  }}

  /* CARD STYLES */
  .card-box {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3.2mm 4.5mm;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}
  .lime-pill {{
    display: inline-block;
    background: var(--lime);
    color: var(--text-black);
    font-size: 7.8pt;
    font-weight: 800;
    padding: 1.8px 8.5px;
    border-radius: 999px;
    width: fit-content;
    font-family: 'Space Grotesk', sans-serif;
  }}

  /* JOB CARD */
  .job-card {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3.5mm 4.5mm;
    display: flex;
    flex-direction: column;
    gap: 1.6mm;
    margin-bottom: 2.8mm;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 5px;
  }}
  .job-role-name {{
    font-size: 11pt;
    font-weight: 900;
    color: var(--text-black);
  }}
  .job-company-name {{
    font-size: 9.2pt;
    font-weight: 700;
    color: var(--text-muted);
  }}
  .job-brand-tag {{
    background: #ffffff;
    padding: 1.8px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 800;
    color: var(--text-black);
    display: inline-block;
  }}
  .job-desc {{
    font-size: 9.4pt;
    color: var(--text-muted);
    line-height: 1.45;
    text-align: justify;
  }}
  .job-desc strong {{ color: var(--text-black); font-weight: 700; }}
  .job-metric-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-top: 0.8mm;
  }}
  .job-metric-tag {{
    font-size: 8.2pt;
    font-weight: 800;
    background: #ffffff;
    color: var(--text-black);
    padding: 2px 8px;
    border-radius: 5px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-family: 'Space Grotesk', sans-serif;
  }}
  .job-metric-tag span.highlight {{ color: #15803d; }}

  /* HIGHLIGHTS STAT ROW */
  .highlights-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 3.5mm;
    margin-top: 2.5mm;
  }}
  .highlight-card {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3mm 3.5mm;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 7px;
    white-space: nowrap;
  }}
  .highlight-circle {{
    width: 25px;
    height: 25px;
    background: var(--lime);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10pt;
    flex-shrink: 0;
  }}
  .highlight-text {{ font-size: 9pt; font-weight: 800; color: var(--text-black); }}

  /* 2-COLUMN GRID (PAGE 2) */
  .p2-grid {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 7mm;
  }}

  /* SKILL BARS */
  .skill-list {{
    display: flex;
    flex-direction: column;
    gap: 2.2mm;
  }}
  .bar-item {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 7px;
  }}
  .bar-label {{
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 8.8pt;
    font-weight: 700;
    min-width: 36mm;
  }}
  .bar-app-icon {{
    width: 18px;
    height: 18px;
    border-radius: 4px;
    background: var(--text-black);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7.2pt;
    font-weight: 800;
    flex-shrink: 0;
  }}
  .bar-track {{
    flex: 1;
    height: 7px;
    background: var(--bar-bg);
    border-radius: 999px;
    overflow: hidden;
  }}
  .bar-fill {{
    height: 100%;
    background: var(--lime);
    border-radius: 999px;
  }}

  .edu-title {{ font-size: 9.8pt; font-weight: 800; line-height: 1.25; }}
  .edu-sub {{ font-size: 8.6pt; color: var(--text-muted); font-weight: 600; line-height: 1.3; }}

  .page-footer {{
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8pt;
    color: #888888;
    border-top: 1px solid #e2ded5;
    padding-top: 2mm;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="a4-page">
  <!-- HERO BENTO -->
  <div class="hero-bento">
    <div style="position: relative;">
      <div class="avatar-card">
        <img src="data:image/png;base64,{avatar_b64}" alt="Lê Thị Hoàng Cẩm">
      </div>
      <svg class="doodle-zigzag" viewBox="0 0 45 70" fill="none" stroke="#111" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M 5,5 L 38,20 L 5,38 L 38,55 L 20,66" />
      </svg>
      <div class="doodle-dot"></div>
      <div class="doodle-cross">✕</div>
    </div>

    <div class="hero-info">
      <div class="role-badge">
        <div class="role-icon-circle">›</div>
        CREATIVE CONTENT CREATOR &amp; DIGITAL MARKETING
      </div>
      <div class="hero-heading">Lê Thị Hoàng Cẩm</div>
      <div class="contact-bar">
        <div class="contact-item">
          <span class="contact-icon">📞</span>
          <a href="tel:0363123121">0363 123 121</a>
        </div>
        <div class="contact-item">
          <span class="contact-icon">✉️</span>
          <a href="mailto:lethihoangcam5@gmail.com">lethihoangcam5@gmail.com</a>
        </div>
        <div class="contact-item">
          <span class="contact-icon">📍</span>
          <span>Bình Tân, TP. Hồ Chí Minh</span>
        </div>
        <div class="contact-item">
          <span class="contact-icon">🔗</span>
          <a href="https://canva.link/kf0t1882b65zzie" target="_blank">canva.link/kf0t1882b65zzie ↗</a>
        </div>
      </div>
    </div>
  </div>

  <!-- ABOUT ME -->
  <div class="section-title">Mục tiêu nghề nghiệp &amp; Định vị bản thân</div>
  <div class="card-box" style="font-size: 9.6pt; line-height: 1.52; color: var(--text-muted); text-align: justify;">
    Chuyên viên Sáng tạo Nội dung &amp; Digital Marketing với hơn 2 năm kinh nghiệm thực chiến trong sản xuất video ngắn viral, xây dựng kịch bản chuyển đổi bán hàng và quản trị truyền thông đa kênh (TikTok, Facebook Fanpage, Instagram Reels). Từng trực tiếp hợp tác và quản lý nội dung cho các nhãn hàng hàng đầu ngành Dược mỹ phẩm &amp; Tiêu dùng như <strong>L’Oréal, Vichy, ColosBaby, Comfort, Gaviscon</strong>. Mục tiêu mang lại tư duy sáng tạo sắc bén, kết hợp phân tích số liệu chuẩn xác để tối đa hóa tương tác thương hiệu và chuyển đổi đơn hàng cho doanh nghiệp.
  </div>

  <!-- EXPERIENCE (PART 1) -->
  <div class="section-title">Kinh nghiệm thực chiến nổi bật</div>

  <!-- JOB 1 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-role-name">Freelance Content Creator</span>
        <span class="job-company-name"> | Làm việc tự do</span>
        <span class="job-brand-tag" style="margin-left: 6px;">L’Oréal • Vichy • Eucerin • SVR</span>
      </div>
      <span class="lime-pill">09/2024 – Hiện tại</span>
    </div>
    <div class="job-desc">
      • Nghiên cứu insight người tiêu dùng, xây dựng concept và kịch bản video ngắn bắt trend cho các dòng sản phẩm Skincare &amp; Dược mỹ phẩm nổi tiếng.<br>
      • Duy trì lượng view ổn định trên <strong>15.000+ views/tháng</strong> trên các kênh social media cá nhân và đối tác.<br>
      • Trực tiếp livestream bán hàng trên nền tảng TikTok Shop, chốt thành công <strong>15–20 đơn hàng/phiên live</strong> với kịch bản tương tác và kích cầu hiệu quả cao.
    </div>
    <div class="job-metric-row">
      <span class="job-metric-tag">🔥 15.000+ Views/tháng</span>
      <span class="job-metric-tag">📦 15–20 Đơn/Phiên Live</span>
      <span class="job-metric-tag"><span class="highlight">↗</span> CTR Tương tác +35%</span>
      <span class="job-metric-tag">🎯 TikTok Shop Creator</span>
    </div>
  </div>

  <!-- JOB 2 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-role-name">Chuyên Viên Sáng Tạo Nội Dung</span>
        <span class="job-company-name"> | Thân Tâm Healthcare</span>
        <span class="job-brand-tag" style="margin-left: 6px;">Comfort • ColosBaby • Gaviscon</span>
      </div>
      <span class="lime-pill">03/2026 – 09/2026</span>
    </div>
    <div class="job-desc">
      • Đạt thành tích sản xuất video viral đạt <strong>98.400 lượt xem</strong> tự nhiên, đưa tỷ lệ tương tác toàn Fanpage tăng trưởng đột biến <strong>+880%</strong> chỉ sau 1 tháng triển khai.<br>
      • Chịu trách nhiệm sáng tạo nội dung đa kênh: từ kịch bản TikTok, bài đăng Fanpage, ấn phẩm banner đến chuỗi video ngắn reels cho 3 thương hiệu chủ lực.<br>
      • Phối hợp chặt chẽ cùng team Media &amp; Design tối ưu hóa hình ảnh sản phẩm, đảm bảo 100% KPI tiến độ và chất lượng từ ban lãnh đạo.
    </div>
    <div class="job-metric-row">
      <span class="job-metric-tag">⭐ Video Viral 98.400 Views</span>
      <span class="job-metric-tag">🚀 Tương tác Fanpage +880%</span>
      <span class="job-metric-tag">📱 Quản trị 4 kênh Social</span>
      <span class="job-metric-tag">💯 100% Đạt KPI</span>
    </div>
  </div>

  <!-- HIGHLIGHTS STATS -->
  <div class="highlights-grid">
    <div class="highlight-card">
      <div class="highlight-circle">⚡</div>
      <div class="highlight-text">98.4K+ Viral View Tự Nhiên</div>
    </div>
    <div class="highlight-card">
      <div class="highlight-circle">🎯</div>
      <div class="highlight-text">15–20 Đơn Hàng/Phiên Live</div>
    </div>
    <div class="highlight-card">
      <div class="highlight-circle">📈</div>
      <div class="highlight-text">+880% Tăng Trưởng Tương Tác</div>
    </div>
  </div>

  <div class="page-footer">
    <span>CV Lê Thị Hoàng Cẩm — Creative Content Creator</span>
    <span>Trang 1 / 2</span>
  </div>
</div>

<!-- ================= PAGE 2 ================= -->
<div class="a4-page">

  <!-- EXPERIENCE (PART 2) -->
  <div class="section-title" style="margin-top: 0;">Kinh nghiệm làm việc (tiếp theo)</div>

  <!-- JOB 3 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-role-name">Digital Marketing &amp; Content Specialist</span>
        <span class="job-company-name"> | OPV Pharma</span>
        <span class="job-brand-tag" style="margin-left: 6px;">Dược phẩm OPV</span>
      </div>
      <span class="lime-pill">12/2024 – 02/2026</span>
    </div>
    <div class="job-desc">
      • Nghiên cứu và sáng tạo nội dung bài viết chuyên sâu về y tế, chăm sóc sức khỏe chuẩn SEO, thúc đẩy mức tăng trưởng tiếp cận tự nhiên <strong>25%–30%</strong> trên website &amp; Fanpage.<br>
      • Lập kế hoạch truyền thông định kỳ hàng tháng cho hơn 15 chiến dịch quảng bá sản phẩm thuốc OTC và dược phẩm kê đơn.<br>
      • Phối hợp cùng đội ngũ Digital Marketing theo dõi các chỉ số CTR, Reach, Engagement để kịp thời điều chỉnh góc tiếp cận nội dung thu hút khách hàng mục tiêu.
    </div>
    <div class="job-metric-row">
      <span class="job-metric-tag">🌿 Tăng trưởng tự nhiên +25–30%</span>
      <span class="job-metric-tag">💊 Chuẩn SEO Y Dược</span>
      <span class="job-metric-tag">📊 15+ Chiến dịch truyền thông</span>
    </div>
  </div>

  <!-- JOB 4 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-role-name">Nhân Viên Tư Vấn &amp; Marketing Dịch Vụ</span>
        <span class="job-company-name"> | Hệ Thống Nha Khoa Kim</span>
        <span class="job-brand-tag" style="margin-left: 6px;">Chuỗi Nha Khoa Kim</span>
      </div>
      <span class="lime-pill">06/2024 – 12/2024</span>
    </div>
    <div class="job-desc">
      • Liên tục duy trì hiệu suất xuất sắc, đạt từ <strong>90%–110% KPI doanh số</strong> cá nhân hàng tháng thông qua tư vấn giải pháp nha khoa trực tiếp tại phòng khám và online.<br>
      • Đóng góp ý tưởng nội dung truyền thông về chăm sóc răng miệng, case study khách hàng thực tế, giúp gia tăng 20% lượng data khách hàng quan tâm dịch vụ thẩm mỹ răng.
    </div>
    <div class="job-metric-row">
      <span class="job-metric-tag">🏆 Đạt 90%–110% KPI Doanh Số</span>
      <span class="job-metric-tag">✨ +20% Khách hàng tiềm năng mới</span>
    </div>
  </div>

  <!-- 2-COLUMN GRID: EDUCATION / CERTS + SKILLS -->
  <div class="p2-grid">
    <!-- LEFT: EDUCATION & CERTS -->
    <div>
      <div class="section-title">Học vấn &amp; Bằng cấp</div>
      <div class="card-box" style="margin-bottom: 2.8mm;">
        <div class="lime-pill">2019 – 2023</div>
        <div class="edu-title">Đại học Sài Gòn</div>
        <div class="edu-sub">Cử nhân Thông Tin – Thư Viện (GPA 3.0/4.0)<br>Thế mạnh: Khai thác, tổ chức dữ liệu &amp; quản trị thông tin chuẩn xác.</div>
      </div>

      <div class="section-title">Chứng chỉ chuyên môn</div>
      <div class="card-box" style="gap: 2mm; margin-bottom: 2.8mm;">
        <div>
          <div class="lime-pill">06/2024</div>
          <div class="edu-title" style="margin-top: 1px;">TOEIC Speaking &amp; Writing</div>
          <div class="edu-sub">Kỹ năng giao tiếp và biên soạn thông điệp quảng cáo song ngữ chuyên nghiệp.</div>
        </div>
        <div style="border-top: 1px solid var(--bar-bg); padding-top: 1.5mm;">
          <div class="lime-pill">06/2023</div>
          <div class="edu-title" style="margin-top: 1px;">Tin Học Văn Phòng MOS</div>
          <div class="edu-sub">Thành thạo Excel báo cáo dữ liệu, Word soạn thảo kịch bản &amp; PowerPoint thuyết trình.</div>
        </div>
      </div>

      <div class="section-title">Phong cách làm việc</div>
      <div class="card-box" style="gap: 1.8mm;">
        <div style="display: flex; gap: 6px; align-items: baseline;">
          <span style="color: #111; font-weight: 900; font-size: 8.5pt;">✓</span>
          <div style="font-size: 8.8pt; color: var(--text-muted); line-height: 1.35;"><strong style="color: var(--text-black);">Nhạy bén xu hướng:</strong> Nắm bắt nhanh thuật toán TikTok/Reels và trend thị trường.</div>
        </div>
        <div style="display: flex; gap: 6px; align-items: baseline;">
          <span style="color: #111; font-weight: 900; font-size: 8.5pt;">✓</span>
          <div style="font-size: 8.8pt; color: var(--text-muted); line-height: 1.35;"><strong style="color: var(--text-black);">Định hướng số liệu:</strong> Sáng tạo kết hợp phân tích tương tác và tỷ lệ chuyển đổi.</div>
        </div>
        <div style="display: flex; gap: 6px; align-items: baseline;">
          <span style="color: #111; font-weight: 900; font-size: 8.5pt;">✓</span>
          <div style="font-size: 8.8pt; color: var(--text-muted); line-height: 1.35;"><strong style="color: var(--text-black);">Chủ động &amp; Cam kết:</strong> Trách nhiệm cao, hoàn thành xuất sắc tiến độ công việc.</div>
        </div>
      </div>
    </div>

    <!-- RIGHT: SKILLS & TOOLS -->
    <div>
      <div class="section-title">Kỹ năng chuyên môn</div>
      <div class="card-box skill-list" style="margin-bottom: 2.8mm;">
        <div class="bar-item">
          <span class="bar-label">Creative Content</span>
          <div class="bar-track"><div class="bar-fill" style="width: 95%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label">Kịch bản TikTok / Reels</span>
          <div class="bar-track"><div class="bar-fill" style="width: 92%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label">Livestream &amp; Bán hàng</span>
          <div class="bar-track"><div class="bar-fill" style="width: 88%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label">Phân tích số liệu Social</span>
          <div class="bar-track"><div class="bar-fill" style="width: 85%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label">Quản trị Fanpage đa kênh</span>
          <div class="bar-track"><div class="bar-fill" style="width: 90%;"></div></div>
        </div>
      </div>

      <div class="section-title">Công cụ &amp; Phần mềm</div>
      <div class="card-box skill-list">
        <div class="bar-item">
          <span class="bar-label"><span class="bar-app-icon">Cp</span> CapCut Video</span>
          <div class="bar-track"><div class="bar-fill" style="width: 95%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label"><span class="bar-app-icon">Cv</span> Canva Graphic</span>
          <div class="bar-track"><div class="bar-fill" style="width: 92%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label"><span class="bar-app-icon">Ad</span> Meta Ads Manager</span>
          <div class="bar-track"><div class="bar-fill" style="width: 85%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label"><span class="bar-app-icon">Ps</span> Adobe Photoshop</span>
          <div class="bar-track"><div class="bar-fill" style="width: 80%;"></div></div>
        </div>
        <div class="bar-item">
          <span class="bar-label"><span class="bar-app-icon">Tt</span> TikTok Creative Hub</span>
          <div class="bar-track"><div class="bar-fill" style="width: 90%;"></div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CV Lê Thị Hoàng Cẩm — Creative Content Creator</span>
    <span>Trang 2 / 2</span>
  </div>
</div>

</body>
</html>
'''

output_path = '/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_Lime_2Trang.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_path} successfully!")
