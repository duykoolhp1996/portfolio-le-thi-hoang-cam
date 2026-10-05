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
<title>CV Lê Thị Hoàng Cẩm — Lime Mood A4 Standard</title>
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
    margin: 0 auto;
    background: var(--bg-page);
    display: flex;
    overflow: hidden;
    position: relative;
    padding: 7.5mm 9.5mm 7mm 9.5mm;
    box-shadow: 0 12px 30px rgba(0,0,0,0.12);
  }}

  @media print {{
    body {{ background: none; }}
    .a4-page {{
      box-shadow: none;
      margin: 0;
      width: 210mm;
      height: 297mm;
      page-break-after: avoid;
    }}
  }}

  .grid-layout {{
    display: grid;
    grid-template-columns: 66mm 1fr;
    gap: 7.5mm;
    width: 100%;
    height: 100%;
  }}

  /* LEFT COLUMN */
  .left-col {{
    display: flex;
    flex-direction: column;
    gap: 2.8mm;
  }}

  /* AVATAR + DOODLE */
  .avatar-block {{
    position: relative;
    padding-top: 1mm;
    margin-bottom: 0.5mm;
  }}
  .avatar-card {{
    width: 44mm;
    height: 46mm;
    background: var(--lime);
    border-radius: 18px;
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    box-shadow: 0 4px 14px rgba(212, 240, 56, 0.35);
  }}
  .avatar-card img {{
    width: 90%;
    height: 90%;
    object-fit: cover;
    object-position: center top;
    border-radius: 14px;
    background: #fff;
    margin-bottom: 2mm;
  }}
  .doodle-zigzag {{
    position: absolute;
    top: 1mm;
    right: 3mm;
    width: 10mm;
    height: 16mm;
  }}
  .doodle-dot {{
    position: absolute;
    top: 6mm;
    right: 6mm;
    width: 3.5mm;
    height: 3.5mm;
    background: var(--lime);
    border-radius: 50%;
  }}
  .doodle-cross {{
    position: absolute;
    bottom: 4mm;
    right: 12mm;
    font-size: 11pt;
    font-weight: 800;
  }}

  /* GREETING */
  .greeting-section {{
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}
  .role-badge {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: var(--lime);
    color: var(--text-black);
    padding: 2.5px 9px 2.5px 5px;
    border-radius: 999px;
    font-size: 7.5pt;
    font-weight: 800;
    width: fit-content;
  }}
  .role-icon-circle {{
    width: 14px;
    height: 14px;
    background: var(--text-black);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7pt;
    font-weight: 900;
  }}
  .hero-heading {{
    font-size: 22pt;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -0.5px;
  }}

  .section-title {{
    font-size: 10.2pt;
    font-weight: 900;
    letter-spacing: -0.2px;
    margin-bottom: 1.2mm;
    color: var(--text-black);
    text-transform: uppercase;
  }}

  .card-box {{
    background: var(--card-bg);
    border-radius: 11px;
    padding: 2.6mm 3.4mm;
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }}
  .lime-pill {{
    display: inline-block;
    background: var(--lime);
    color: var(--text-black);
    font-size: 7.4pt;
    font-weight: 800;
    padding: 1.5px 7px;
    border-radius: 999px;
    width: fit-content;
    font-family: 'Space Grotesk', sans-serif;
  }}
  .edu-title {{ font-size: 9pt; font-weight: 800; line-height: 1.25; }}
  .edu-sub {{ font-size: 8.2pt; color: var(--text-muted); font-weight: 600; line-height: 1.25; }}

  /* SKILL BARS */
  .skill-list {{
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}
  .bar-item {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
  }}
  .bar-label {{
    display: flex;
    align-items: center;
    gap: 4px;
    font-size: 8.3pt;
    font-weight: 700;
    min-width: 29mm;
  }}
  .bar-app-icon {{
    width: 16px;
    height: 16px;
    border-radius: 4px;
    background: var(--text-black);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 6.5pt;
    font-weight: 800;
    flex-shrink: 0;
  }}
  .bar-track {{
    flex: 1;
    height: 6px;
    background: var(--bar-bg);
    border-radius: 999px;
    overflow: hidden;
  }}
  .bar-fill {{
    height: 100%;
    background: var(--lime);
    border-radius: 999px;
  }}

  /* RIGHT COLUMN */
  .right-col {{
    display: flex;
    flex-direction: column;
    gap: 2.5mm;
  }}

  .top-meta-row {{
    display: grid;
    grid-template-columns: 1fr 1.05fr;
    gap: 3.5mm;
  }}
  .meta-title {{ font-size: 10.2pt; font-weight: 900; margin-bottom: 1.2mm; }}
  .meta-contact-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.4mm;
    font-size: 8.5pt;
    font-weight: 600;
  }}
  .contact-item {{ display: flex; align-items: center; gap: 6px; }}
  .contact-icon {{
    width: 17px;
    height: 17px;
    background: var(--text-black);
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7.5pt;
    flex-shrink: 0;
  }}
  .contact-item a {{ color: var(--text-black); text-decoration: none; font-weight: 700; }}

  /* PROFILE CARD */
  .profile-card {{
    background: var(--card-bg);
    border-radius: 11px;
    padding: 2.8mm 4mm;
    font-size: 9.1pt;
    color: var(--text-muted);
    line-height: 1.42;
    text-align: justify;
  }}
  .profile-card strong {{ color: var(--text-black); font-weight: 700; }}

  /* EXPERIENCE CARDS */
  .experience-list {{
    display: flex;
    flex-direction: column;
    gap: 2mm;
  }}
  .job-card {{
    background: var(--card-bg);
    border-radius: 11px;
    padding: 2.4mm 3.8mm;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 4px;
  }}
  .job-role-name {{
    font-size: 10.2pt;
    font-weight: 900;
    color: var(--text-black);
  }}
  .job-company-name {{
    font-size: 8.4pt;
    font-weight: 700;
    color: var(--text-muted);
  }}
  .job-brand-tag {{
    background: #ffffff;
    padding: 1px 7px;
    border-radius: 4px;
    font-size: 7.6pt;
    font-weight: 800;
    color: var(--text-black);
    display: inline-block;
  }}
  .job-desc {{
    font-size: 8.8pt;
    color: var(--text-muted);
    line-height: 1.36;
    text-align: justify;
  }}
  .job-desc strong {{ color: var(--text-black); font-weight: 700; }}
  .job-metric-row {{
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    margin-top: 0.4mm;
  }}
  .job-metric-tag {{
    font-size: 7.8pt;
    font-weight: 800;
    background: #ffffff;
    color: var(--text-black);
    padding: 1.5px 7px;
    border-radius: 4px;
    display: inline-flex;
    align-items: center;
    gap: 3px;
    font-family: 'Space Grotesk', sans-serif;
  }}
  .job-metric-tag span.highlight {{ color: #15803d; }}

  /* HIGHLIGHTS */
  .highlights-row {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 3mm;
    margin-top: 0.6mm;
  }}
  .highlight-card {{
    background: var(--card-bg);
    border-radius: 11px;
    padding: 2.2mm 2.2mm;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 5px;
    white-space: nowrap;
  }}
  .highlight-circle {{
    width: 22px;
    height: 22px;
    background: var(--lime);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 9.5pt;
    flex-shrink: 0;
  }}
  .highlight-text {{ font-size: 8.3pt; font-weight: 800; color: var(--text-black); }}
</style>
</head>
<body>

<div class="a4-page">
  <div class="grid-layout">

    <!-- LEFT COLUMN -->
    <div class="left-col">
      <!-- AVATAR + DOODLE -->
      <div class="avatar-block">
        <div class="avatar-card">
          <img src="data:image/png;base64,{avatar_b64}" alt="Lê Thị Hoàng Cẩm">
        </div>
        <svg class="doodle-zigzag" viewBox="0 0 45 70" fill="none" stroke="#111" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M 5,5 L 38,20 L 5,38 L 38,55 L 20,66" />
        </svg>
        <div class="doodle-dot"></div>
        <div class="doodle-cross">✕</div>
      </div>

      <!-- GREETING & ROLE -->
      <div class="greeting-section">
        <div class="role-badge">
          <div class="role-icon-circle">›</div>
          CREATIVE CONTENT CREATOR
        </div>
        <div class="hero-heading">Lê Thị<br>Hoàng Cẩm</div>
      </div>

      <!-- EDUCATION -->
      <div>
        <div class="section-title">Học vấn</div>
        <div class="card-box">
          <div class="lime-pill">2019 – 2023</div>
          <div class="edu-title">Đại học Sài Gòn</div>
          <div class="edu-sub">Cử nhân Thông Tin – Thư Viện (GPA 3.0/4.0)</div>
        </div>
      </div>

      <!-- CERTIFICATIONS -->
      <div>
        <div class="section-title">Chứng chỉ</div>
        <div class="card-box" style="gap: 1.8mm;">
          <div>
            <div class="lime-pill">06/2024</div>
            <div class="edu-title" style="margin-top: 1px;">TOEIC Speaking & Writing</div>
            <div class="edu-sub">Giao tiếp & biên soạn nội dung chuyên nghiệp</div>
          </div>
          <div style="border-top: 1px solid var(--bar-bg); padding-top: 1.5mm;">
            <div class="lime-pill">06/2023</div>
            <div class="edu-title" style="margin-top: 1px;">Tin học văn phòng MOS</div>
            <div class="edu-sub">Thành thạo ứng dụng văn phòng, báo cáo & dữ liệu</div>
          </div>
        </div>
      </div>

      <!-- SKILLS -->
      <div>
        <div class="section-title">Kỹ năng chuyên môn</div>
        <div class="card-box skill-list">
          <div class="bar-item">
            <span class="bar-label">Creative Content</span>
            <div class="bar-track"><div class="bar-fill" style="width: 95%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label">Kịch bản TikTok / Reels</span>
            <div class="bar-track"><div class="bar-fill" style="width: 92%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label">Phân tích số liệu</span>
            <div class="bar-track"><div class="bar-fill" style="width: 85%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label">Quản trị Fanpage đa kênh</span>
            <div class="bar-track"><div class="bar-fill" style="width: 90%;"></div></div>
          </div>
        </div>
      </div>

      <!-- SOFTWARE -->
      <div>
        <div class="section-title">Công cụ & Phần mềm</div>
        <div class="card-box skill-list">
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Cp</span> CapCut Video</span>
            <div class="bar-track"><div class="bar-fill" style="width: 95%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Cv</span> Canva Design</span>
            <div class="bar-track"><div class="bar-fill" style="width: 90%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Ad</span> Meta Ads Manager</span>
            <div class="bar-track"><div class="bar-fill" style="width: 85%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Ps</span> Adobe Photoshop</span>
            <div class="bar-track"><div class="bar-fill" style="width: 80%;"></div></div>
          </div>
        </div>
      </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right-col">

      <!-- TOP META ROW -->
      <div class="top-meta-row">
        <div>
          <div class="meta-title">Portfolio dự án</div>
          <div class="card-box" style="padding: 2.4mm 3.2mm;">
            <div class="lime-pill" style="font-size: 7pt;">CANVA SHOWCASE</div>
            <div style="font-size: 8.8pt; font-weight: 800; margin-top: 1.5px;">
              <a href="https://canva.link/kf0t1882b65zzie" target="_blank" style="color: var(--text-black); text-decoration: none;">canva.link/kf0t1882b65zzie ↗</a>
            </div>
            <div style="font-size: 7.8pt; color: var(--text-muted); font-weight: 600;">Xem video viral & ấn phẩm mẫu</div>
          </div>
        </div>
        <div>
          <div class="meta-title">Thông tin liên hệ</div>
          <ul class="meta-contact-list">
            <li class="contact-item">
              <span class="contact-icon">📞</span>
              <a href="tel:0363123121">0363 123 121</a>
            </li>
            <li class="contact-item">
              <span class="contact-icon">✉️</span>
              <a href="mailto:lethihoangcam5@gmail.com">lethihoangcam5@gmail.com</a>
            </li>
            <li class="contact-item">
              <span class="contact-icon">📍</span>
              <span>Bình Tân, TP. Hồ Chí Minh</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- ABOUT ME -->
      <div>
        <div class="section-title">Mục tiêu nghề nghiệp</div>
        <div class="profile-card">
          Chuyên viên Sáng tạo Nội dung &amp; Digital Marketing với thế mạnh sản xuất video ngắn viral, xây dựng kịch bản chuyển đổi và livestream bán hàng. Đã thực chiến quản trị truyền thông cho các thương hiệu lớn ngành Dược mỹ phẩm &amp; F&amp;B như <strong>L’Oréal, Vichy, ColosBaby, Gaviscon</strong>. Mục tiêu đóng góp năng lực sáng tạo để thúc đẩy nhận diện thương hiệu và tối ưu hóa doanh số cho doanh nghiệp.
        </div>
      </div>

      <!-- EXPERIENCE -->
      <div>
        <div class="section-title">Kinh nghiệm làm việc</div>
        <div class="experience-list">

          <!-- JOB 1 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Freelance Content Creator</span>
                <span class="job-company-name"> | Tự do</span>
                <span class="job-brand-tag" style="margin-left: 5px;">L’Oréal • Vichy • Eucerin</span>
              </div>
              <span class="lime-pill">09/2024 – Hiện tại</span>
            </div>
            <div class="job-desc">
              • Sáng tạo video viral review sản phẩm Dược mỹ phẩm; duy trì <strong>15.000+ views/tháng</strong>.<br>
              • Trực tiếp livestream bán hàng, chốt <strong>15–20 đơn/phiên live</strong>, kịch bản chuyển đổi cao.
            </div>
            <div class="job-metric-row">
              <span class="job-metric-tag">🔥 15K+ views/tháng</span>
              <span class="job-metric-tag">📦 15-20 đơn/live</span>
              <span class="job-metric-tag"><span class="highlight">↗</span> CTR +35%</span>
              <span class="job-metric-tag">🎯 TikTok Shop</span>
            </div>
          </div>

          <!-- JOB 2 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Chuyên Viên Sáng Tạo Nội Dung</span>
                <span class="job-company-name"> | Thân Tâm Healthcare</span>
                <span class="job-brand-tag" style="margin-left: 5px;">ColosBaby • Gaviscon</span>
              </div>
              <span class="lime-pill">03/2026 – 09/2026</span>
            </div>
            <div class="job-desc">
              • Đạt video viral <strong>98.400 views</strong>, tăng tương tác Fanpage <strong>+880%</strong> sau 1 tháng.<br>
              • Lên kế hoạch và sản xuất nội dung đa kênh (TikTok, Facebook Fanpage, Reels) cho nhãn hàng.
            </div>
            <div class="job-metric-row">
              <span class="job-metric-tag">⭐ Viral 98.4K views</span>
              <span class="job-metric-tag">🚀 Tương tác +880%</span>
              <span class="job-metric-tag">📱 4 kênh MXH</span>
              <span class="job-metric-tag">💯 100% KPI</span>
            </div>
          </div>

          <!-- JOB 3 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Digital Marketing &amp; Content</span>
                <span class="job-company-name"> | OPV Pharma</span>
                <span class="job-brand-tag" style="margin-left: 5px;">Dược phẩm OPV</span>
              </div>
              <span class="lime-pill">12/2024 – 02/2026</span>
            </div>
            <div class="job-desc">
              • Thúc đẩy tăng trưởng tự nhiên <strong>25%–30%</strong> qua chuỗi bài viết chuẩn SEO Y Dược.<br>
              • Triển khai kế hoạch truyền thông đa kênh cho các dòng sản phẩm OTC và thuốc chuyên khoa.
            </div>
            <div class="job-metric-row">
              <span class="job-metric-tag">🌿 Tăng trưởng +25-30%</span>
              <span class="job-metric-tag">💊 Chuẩn SEO Dược</span>
              <span class="job-metric-tag">📊 15+ Chiến dịch</span>
            </div>
          </div>

          <!-- JOB 4 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Nhân Viên Tư Vấn &amp; Marketing</span>
                <span class="job-company-name"> | Nha Khoa Kim</span>
                <span class="job-brand-tag" style="margin-left: 5px;">Chuỗi Nha Khoa Kim</span>
              </div>
              <span class="lime-pill">06/2024 – 12/2024</span>
            </div>
            <div class="job-desc">
              • Đạt <strong>90%–110% KPI doanh số</strong> hàng tháng; tư vấn khách hàng trực tiếp và qua kênh số.<br>
              • Sáng tạo nội dung chăm sóc răng miệng, thu hút khách hàng tiềm năng đến phòng khám.
            </div>
            <div class="job-metric-row">
              <span class="job-metric-tag">🏆 90-110% KPI Doanh số</span>
              <span class="job-metric-tag">✨ +20% Khách tiềm năng</span>
            </div>
          </div>

        </div>
      </div>

      <!-- HIGHLIGHTS -->
      <div class="highlights-row">
        <div class="highlight-card">
          <div class="highlight-circle">⚡</div>
          <div class="highlight-text">98.4K+ Viral View</div>
        </div>
        <div class="highlight-card">
          <div class="highlight-circle">🎯</div>
          <div class="highlight-text">15-20 Đơn/Live</div>
        </div>
        <div class="highlight-card">
          <div class="highlight-circle">📈</div>
          <div class="highlight-text">+880% Tương Tác</div>
        </div>
      </div>

    </div>

  </div>
</div>

</body>
</html>
'''

output_path = '/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_Lime_A4.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_path} successfully!")
