import base64

with open('/Users/Admin/Documents/HRM/avatar.png', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV Lê Thị Hoàng Cẩm — Lime Mood Clean Minimal</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-page: #FAF8F2;
    --card-bg: #EFECE4;
    --lime: #D4F038;
    --text-black: #111111;
    --text-muted: #555555;
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
    padding: 10mm 11mm 10mm 11mm;
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
    gap: 8.5mm;
    width: 100%;
    height: 100%;
  }}

  /* LEFT COLUMN */
  .left-col {{
    display: flex;
    flex-direction: column;
    gap: 4.8mm;
  }}

  /* AVATAR + DOODLE */
  .avatar-block {{
    position: relative;
    padding-top: 1mm;
    margin-bottom: 1mm;
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
    box-shadow: 0 4px 14px rgba(212, 240, 56, 0.35);
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
    top: 1mm;
    right: 2mm;
    width: 11mm;
    height: 17mm;
  }}
  .doodle-dot {{
    position: absolute;
    top: 7mm;
    right: 5mm;
    width: 4mm;
    height: 4mm;
    background: var(--lime);
    border-radius: 50%;
  }}
  .doodle-cross {{
    position: absolute;
    bottom: 5mm;
    right: 12mm;
    font-size: 12pt;
    font-weight: 800;
  }}

  /* GREETING */
  .greeting-section {{
    display: flex;
    flex-direction: column;
    gap: 1.5mm;
  }}
  .role-badge {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--lime);
    color: var(--text-black);
    padding: 3px 10px 3px 5px;
    border-radius: 999px;
    font-size: 7.8pt;
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
    line-height: 1.06;
    letter-spacing: -0.5px;
  }}

  .section-title {{
    font-size: 10.5pt;
    font-weight: 900;
    letter-spacing: -0.2px;
    margin-bottom: 1.8mm;
    color: var(--text-black);
  }}

  .card-box {{
    background: var(--card-bg);
    border-radius: 13px;
    padding: 3.8mm 4.2mm;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}
  .lime-pill {{
    display: inline-block;
    background: var(--lime);
    color: var(--text-black);
    font-size: 7.5pt;
    font-weight: 800;
    padding: 1.8px 8px;
    border-radius: 999px;
    width: fit-content;
    font-family: 'Space Grotesk', sans-serif;
  }}
  .edu-title {{ font-size: 9.2pt; font-weight: 800; line-height: 1.25; }}
  .edu-sub {{ font-size: 8.2pt; color: var(--text-muted); font-weight: 500; line-height: 1.25; }}

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
    font-size: 8.5pt;
    font-weight: 700;
    min-width: 30mm;
  }}
  .bar-app-icon {{
    width: 17px;
    height: 17px;
    border-radius: 4px;
    background: var(--text-black);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 6.8pt;
    font-weight: 800;
    flex-shrink: 0;
  }}
  .bar-track {{
    flex: 1;
    height: 6.5px;
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
    gap: 4mm;
  }}

  .top-meta-row {{
    display: grid;
    grid-template-columns: 1fr 1.05fr;
    gap: 4mm;
  }}
  .meta-title {{ font-size: 10.5pt; font-weight: 900; margin-bottom: 1.5mm; }}
  .meta-contact-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
    font-size: 8.6pt;
    font-weight: 600;
  }}
  .contact-item {{ display: flex; align-items: center; gap: 7px; }}
  .contact-icon {{
    width: 18px;
    height: 18px;
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

  /* PROFILE CARD */
  .profile-card {{
    background: var(--card-bg);
    border-radius: 13px;
    padding: 3.5mm 4.5mm;
    font-size: 9.3pt;
    color: var(--text-muted);
    line-height: 1.5;
    text-align: justify;
  }}
  .profile-card strong {{ color: var(--text-black); font-weight: 700; }}

  /* EXPERIENCE CARDS */
  .experience-list {{
    display: flex;
    flex-direction: column;
    gap: 3.2mm;
  }}
  .job-card {{
    background: var(--card-bg);
    border-radius: 13px;
    padding: 3.5mm 4.5mm;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .job-role-name {{
    font-size: 10.8pt;
    font-weight: 900;
    color: var(--text-black);
  }}
  .job-company-name {{
    font-size: 8.6pt;
    font-weight: 700;
    color: var(--text-muted);
  }}
  .job-brand-tag {{
    display: inline-block;
    background: #fff;
    padding: 1.5px 8px;
    border-radius: 4px;
    font-size: 7.8pt;
    font-weight: 800;
    color: var(--text-black);
  }}
  .job-desc {{
    font-size: 9pt;
    color: var(--text-muted);
    line-height: 1.45;
  }}
  .job-desc strong {{ color: var(--text-black); font-weight: 700; }}

  /* HOBBY & VALUE ROW (MATCHING REFERENCE) */
  .hobby-row {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 3.5mm;
  }}
  .hobby-card {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 2.8mm 3mm;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.5mm;
  }}
  .hobby-circle {{
    width: 28px;
    height: 28px;
    background: var(--lime);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12pt;
  }}
  .hobby-label {{
    font-size: 8.4pt;
    font-weight: 800;
    color: var(--text-black);
  }}
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
            <span class="bar-label">Livestream Bán Hàng</span>
            <div class="bar-track"><div class="bar-fill" style="width: 88%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label">Quản trị Fanpage đa kênh</span>
            <div class="bar-track"><div class="bar-fill" style="width: 90%;"></div></div>
          </div>
        </div>
      </div>

      <!-- TOOLS -->
      <div>
        <div class="section-title">Công cụ &amp; Phần mềm</div>
        <div class="card-box skill-list">
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Cp</span> CapCut Video</span>
            <div class="bar-track"><div class="bar-fill" style="width: 95%;"></div></div>
          </div>
          <div class="bar-item">
            <span class="bar-label"><span class="bar-app-icon">Cv</span> Canva Design</span>
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
        </div>
      </div>

      <!-- CERTIFICATION -->
      <div>
        <div class="section-title">Chứng chỉ</div>
        <div class="card-box" style="gap: 1.5mm;">
          <div style="font-size: 8.6pt; font-weight: 800;">TOEIC Speaking &amp; Writing (06/2024)</div>
          <div style="font-size: 8.6pt; font-weight: 800; border-top: 1px solid var(--bar-bg); padding-top: 1.5mm;">Tin học văn phòng MOS (06/2023)</div>
        </div>
      </div>

    </div>

    <!-- RIGHT COLUMN -->
    <div class="right-col">

      <!-- TOP META ROW -->
      <div class="top-meta-row">
        <div>
          <div class="meta-title">Portfolio dự án</div>
          <div class="card-box" style="padding: 2.8mm 3.5mm;">
            <div class="lime-pill" style="font-size: 7.2pt;">CANVA SHOWCASE</div>
            <div style="font-size: 9pt; font-weight: 800; margin-top: 1.5px;">
              <a href="https://canva.link/kf0t1882b65zzie" target="_blank" style="color: var(--text-black); text-decoration: none;">canva.link/kf0t1882b65zzie ↗</a>
            </div>
            <div style="font-size: 8pt; color: var(--text-muted); font-weight: 500;">Video ngắn viral &amp; ấn phẩm truyền thông</div>
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
        <div class="section-title">Giới thiệu bản thân</div>
        <div class="profile-card">
          Chuyên viên Sáng tạo Nội dung &amp; Digital Marketing với thế mạnh sản xuất video ngắn viral, xây dựng kịch bản chuyển đổi bán hàng và livestream thực chiến. Từng trực tiếp quản trị và triển khai truyền thông cho các thương hiệu hàng đầu ngành Dược mỹ phẩm &amp; F&amp;B như <strong>L’Oréal, Vichy, ColosBaby, Comfort, Gaviscon</strong>.
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
              </div>
              <span class="lime-pill">09/2024 – Hiện tại</span>
            </div>
            <div>
              <span class="job-brand-tag">L’Oréal • Vichy • Eucerin • SVR</span>
            </div>
            <div class="job-desc">
              Sáng tạo video ngắn viral review sản phẩm Dược mỹ phẩm, duy trì đều đặn <strong>15.000+ views/tháng</strong>. Trực tiếp livestream bán hàng trên TikTok Shop, đạt doanh số <strong>15–20 đơn hàng/phiên live</strong> với kịch bản tương tác tự nhiên và chuyển đổi cao.
            </div>
          </div>

          <!-- JOB 2 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Chuyên Viên Sáng Tạo Nội Dung</span>
                <span class="job-company-name"> | Thân Tâm Healthcare</span>
              </div>
              <span class="lime-pill">03/2026 – 09/2026</span>
            </div>
            <div>
              <span class="job-brand-tag">Comfort • ColosBaby • Gaviscon</span>
            </div>
            <div class="job-desc">
              Sản xuất video viral đạt <strong>98.400 lượt xem</strong> tự nhiên, thúc đẩy mức tương tác Fanpage tăng trưởng đột biến <strong>+880%</strong> sau 1 tháng. Lên kế hoạch và sản xuất nội dung đa kênh (TikTok, Fanpage, Reels) cho 3 thương hiệu lớn.
            </div>
          </div>

          <!-- JOB 3 -->
          <div class="job-card">
            <div class="job-head">
              <div>
                <span class="job-role-name">Digital Marketing &amp; Content</span>
                <span class="job-company-name"> | OPV Pharma</span>
              </div>
              <span class="lime-pill">12/2024 – 02/2026</span>
            </div>
            <div>
              <span class="job-brand-tag">Dược phẩm OPV</span>
            </div>
            <div class="job-desc">
              Xây dựng chuỗi bài viết chuyên sâu chuẩn SEO Y Dược, thúc đẩy tiếp cận tự nhiên tăng <strong>25%–30%</strong>. Phối hợp triển khai kế hoạch truyền thông cho hơn 15 chiến dịch quảng bá sản phẩm thuốc OTC và thực phẩm chức năng.
            </div>
          </div>

        </div>
      </div>

      <!-- HIGHLIGHTS / HOBBY & VALUES (EXACT MOOD AS REFERENCE) -->
      <div>
        <div class="section-title">Điểm nổi bật &amp; Phong cách</div>
        <div class="hobby-row">
          <div class="hobby-card">
            <div class="hobby-circle">🎬</div>
            <div class="hobby-label">Video Viral</div>
          </div>
          <div class="hobby-card">
            <div class="hobby-circle">🛍️</div>
            <div class="hobby-label">Live Selling</div>
          </div>
          <div class="hobby-card">
            <div class="hobby-circle">📈</div>
            <div class="hobby-label">Data Driven</div>
          </div>
        </div>
      </div>

    </div>

  </div>
</div>

</body>
</html>
'''

output_path = '/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_Lime_Clean.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_path} successfully!")
