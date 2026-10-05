import base64
import subprocess
import os
import re
import shutil

with open('/Users/Admin/Documents/HRM/avatar.jpg', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV Lê Thị Hoàng Cẩm — Marketing Executive</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-page: #FAF8F5;
    --card-bg: #F2EFE9;
    --accent: #5B8266;
    --accent-soft: #E8EFE9;
    --accent-text: #264A31;
    --accent-border: #CCDDCF;
    --text-black: #1E2320;
    --text-muted: #4D5750;
    --bar-bg: #DDD7CE;
    --accent-green: #2B693E;
    --brand-icon-bg: #3B5742;
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
    padding: 10mm 12mm 9mm 12mm;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
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

  /* HEADER (PAGE 1) */
  .hero-bento {{
    display: grid;
    grid-template-columns: 48mm 1fr;
    gap: 7mm;
    align-items: center;
    margin-bottom: 3.5mm;
  }}
  .avatar-card {{
    width: 46mm;
    height: 50mm;
    background: linear-gradient(145deg, #E6EFE8 0%, #D5E4D8 100%);
    border: 1.5px solid var(--accent-border);
    border-radius: 20px;
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    box-shadow: 0 4px 14px rgba(91, 130, 102, 0.12);
  }}
  .avatar-card img {{
    width: 90%;
    height: 90%;
    object-fit: cover;
    object-position: center top;
    border-radius: 15px;
    background: #fff;
    margin-bottom: 2mm;
  }}

  .hero-info {{
    display: flex;
    flex-direction: column;
    gap: 2mm;
  }}
  .role-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
    padding: 3.5px 14px 3.5px 7px;
    border-radius: 999px;
    font-size: 8.4pt;
    font-weight: 800;
    width: fit-content;
    letter-spacing: 0.2px;
  }}
  .role-icon-circle {{
    width: 16px;
    height: 16px;
    background: var(--accent);
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
    color: var(--text-black);
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
    font-size: 9pt;
    font-weight: 600;
  }}
  .contact-icon {{
    width: 19px;
    height: 19px;
    background: var(--brand-icon-bg);
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
    letter-spacing: -0.2px;
    margin-bottom: 2mm;
    margin-top: 2.8mm;
    color: var(--text-black);
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .section-title::after {{
    content: '';
    flex: 1;
    height: 1.5px;
    background: #dfdad0;
  }}

  /* CARD STYLES */
  .about-box {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3.2mm 4.5mm;
    border: 1px solid #e7e2d8;
  }}
  .about-text {{
    font-size: 9.4pt;
    line-height: 1.55;
    color: #37413a;
    text-align: justify;
    text-justify: inter-word;
  }}
  .about-text strong {{
    color: var(--text-black);
    font-weight: 700;
  }}

  .card-box {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3.2mm 4.2mm;
    display: flex;
    flex-direction: column;
    gap: 1.6mm;
    border: 1px solid #e7e2d8;
  }}
  .lime-pill {{
    display: inline-block;
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
    font-size: 7.8pt;
    font-weight: 800;
    padding: 2px 9px;
    border-radius: 999px;
    width: fit-content;
    font-family: 'Space Grotesk', sans-serif;
  }}

  /* JOB CARD (EXPANDED TO FULL CONTENT) */
  .job-card {{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 3.5mm 4.5mm;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
    margin-bottom: 2.8mm;
    border: 1px solid #e7e2d8;
  }}
  .job-head {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 4px;
  }}
  .job-company-name {{
    font-size: 10.8pt;
    font-weight: 900;
    color: var(--text-black);
  }}
  .job-role-line {{
    font-size: 9.3pt;
    font-weight: 700;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }}
  .job-brand-tag {{
    background: #ffffff;
    border: 1px solid #d9d3c7;
    padding: 1.5px 8px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 800;
    color: var(--accent-text);
  }}

  .job-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.2mm;
    font-size: 9.2pt;
    color: var(--text-muted);
    line-height: 1.42;
  }}
  .job-bullets li {{
    position: relative;
    padding-left: 4.5mm;
    text-align: justify;
  }}
  .job-bullets li::before {{
    content: "•";
    position: absolute;
    left: 1mm;
    top: -1px;
    color: var(--accent);
    font-weight: 900;
    font-size: 10pt;
  }}
  .job-bullets strong {{ color: var(--text-black); font-weight: 700; }}

  /* ACHIEVEMENT BOX */
  .achievement-box {{
    background: #ffffff;
    border-left: 3.5px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 2.2mm 3.5mm;
    display: flex;
    flex-direction: column;
    gap: 1mm;
    margin-top: 0.5mm;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }}
  .achievement-title {{
    font-size: 8.5pt;
    font-weight: 900;
    color: var(--accent-text);
    text-transform: uppercase;
    letter-spacing: 0.3px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .achievement-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0.8mm;
    font-size: 8.9pt;
    color: var(--text-black);
    line-height: 1.38;
  }}
  .achievement-list li {{
    position: relative;
    padding-left: 4mm;
  }}
  .achievement-list li::before {{
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--accent-green);
    font-weight: 900;
    font-size: 8.5pt;
  }}
  .badge-metric {{
    display: inline-block;
    background: #edf4ee;
    color: #235a34;
    border: 1px solid #d2e4d5;
    font-weight: 800;
    padding: 1px 6px;
    border-radius: 4px;
    font-family: 'Space Grotesk', sans-serif;
  }}

  /* 2-COLUMN GRID (PAGE 2 BOTTOM) */
  .p2-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6.5mm;
    margin-top: 1mm;
  }}

  /* SKILL & TOOL LISTS (DESCRIPTIVE BULLETS) */
  .skill-text-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.8mm;
  }}
  .skill-text-item {{
    display: flex;
    align-items: flex-start;
    gap: 6px;
    font-size: 8.65pt;
    line-height: 1.35;
    color: #444c46;
  }}
  .skill-bullet-check {{
    color: var(--accent-green);
    font-weight: 900;
    font-size: 8.8pt;
    flex-shrink: 0;
    margin-top: 0.5px;
  }}
  .skill-text-item strong {{
    color: var(--text-black);
    font-weight: 700;
  }}

  .tool-row-item {{
    display: flex;
    align-items: flex-start;
    gap: 7px;
    font-size: 8.65pt;
    line-height: 1.35;
    color: #444c46;
  }}
  .tool-app-icon {{
    width: 19px;
    height: 19px;
    border-radius: 4px;
    background: var(--brand-icon-bg);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 7.2pt;
    font-weight: 800;
    flex-shrink: 0;
    margin-top: 1px;
  }}
  .tool-info {{
    flex: 1;
  }}
  .tool-info strong {{
    color: var(--text-black);
    font-weight: 700;
  }}

  /* SOFT SKILLS */
  .soft-skill-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 1.6mm;
  }}
  .soft-skill-item {{
    display: flex;
    align-items: flex-start;
    gap: 6px;
    font-size: 8.7pt;
    line-height: 1.35;
    color: #444c46;
  }}
  .soft-skill-check {{
    color: var(--accent-green);
    font-weight: 900;
    font-size: 8.8pt;
    flex-shrink: 0;
    margin-top: 0.5px;
  }}
  .soft-skill-item strong {{
    color: var(--text-black);
    font-weight: 700;
  }}

  .edu-title {{ font-size: 9.5pt; font-weight: 800; line-height: 1.25; color: var(--text-black); }}
  .edu-sub {{ font-size: 8.5pt; color: var(--text-muted); font-weight: 500; line-height: 1.3; }}

  .page-footer {{
    margin-top: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.2pt;
    color: #727a74;
    border-top: 1px solid #dfdad0;
    padding-top: 2mm;
  }}
</style>
</head>
<body>

<!-- ================= PAGE 1 ================= -->
<div class="a4-page">
  <!-- HERO BENTO -->
  <div class="hero-bento">
    <div>
      <div class="avatar-card">
        <img src="data:image/jpeg;base64,{avatar_b64}" alt="Lê Thị Hoàng Cẩm">
      </div>
    </div>

    <div class="hero-info">
      <div class="role-badge">
        <div class="role-icon-circle">›</div>
        MARKETING EXECUTIVE • CONTENT &amp; DIGITAL MARKETING
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
      </div>
    </div>
  </div>

  <!-- ABOUT ME -->
  <div class="section-title">Mục tiêu nghề nghiệp &amp; Định vị bản thân</div>
  <div class="about-box">
    <p class="about-text">
      Chuyên viên <strong>Marketing Executive</strong> với hơn <strong>3 năm kinh nghiệm</strong> thực chiến, sở hữu năng lực toàn diện về <strong>Content Marketing</strong> và <strong>Digital Marketing</strong> đa nền tảng (Facebook, TikTok, Reels, Threads, Website). Thế mạnh nổi trội trong mảng <strong>Healthcare Marketing (Y tế &amp; Dược phẩm)</strong> và <strong>Beauty/FMCG</strong>, có kinh nghiệm triển khai dự án B2B kết nối nhãn hàng lớn với bệnh viện. Thành thạo quy trình từ nghiên cứu insight, sáng tạo nội dung, chạy chiến dịch quảng cáo đa kênh đến phân tích hiệu suất và tối ưu tỷ lệ chuyển đổi.
    </p>
  </div>

  <!-- EXPERIENCE (PART 1) -->
  <div class="section-title">Kinh nghiệm làm việc thực chiến (Phần 1)</div>

  <!-- JOB 1 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-company-name">Freelance Marketing Executive &amp; Content Creator</span>
      </div>
      <span class="lime-pill">09/2024 – HIỆN TẠI</span>
    </div>
    <div class="job-role-line">
      <span>Chiến dịch Content &amp; Digital Marketing Đa kênh • KOC</span>
      <span class="job-brand-tag">L’Oréal • Vichy • Eucerin • SVR</span>
    </div>
    <ul class="job-bullets">
      <li>Lên ý tưởng, viết kịch bản chi tiết, tự chủ quay chụp và dựng video/ảnh ngắn chất lượng cao trên đa nền tảng (Facebook, TikTok, Threads, Instagram), luôn đảm bảo đúng deadline và tiến độ.</li>
      <li>Hợp tác sản xuất video trải nghiệm/cảm nhận sản phẩm theo brief từ các nhãn hàng, nắm bắt nhanh xu hướng thịnh hành của giới trẻ để tối ưu hóa tương tác tự nhiên.</li>
    </ul>
    <div class="achievement-box">
      <div class="achievement-title">
        <span>🏆 Kết quả &amp; Thành tựu nổi bật:</span>
      </div>
      <ul class="achievement-list">
        <li>Được các thương hiệu mỹ phẩm hàng đầu (<strong>L’Oréal, Vichy, Eucerin, SVR,...</strong>) gửi lời mời tham dự sự kiện ra mắt độc quyền và sản xuất video review tại sự kiện.</li>
        <li>Kênh cá nhân đạt trung bình <span class="badge-metric">15.000 lượt hiển thị/tháng (+30%)</span> và <span class="badge-metric">800 lượt truy cập profile (+20%)</span>.</li>
      </ul>
    </div>
  </div>

  <!-- JOB 2 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-company-name">Công ty TNHH Đào tạo &amp; Chăm sóc Sức khỏe Thân Tâm</span>
      </div>
      <span class="lime-pill">03/2026 – 09/2026</span>
    </div>
    <div class="job-role-line">
      <span>Chuyên viên Digital Marketing</span>
      <span class="job-brand-tag">Healthcare &amp; Media • Kênh MEDTV</span>
    </div>
    <ul class="job-bullets">
      <li>Lên ý tưởng, viết kịch bản, quay dựng chuỗi Reels/TikTok giáo dục sức khỏe và xây dựng thương hiệu; trực tiếp quản trị 2 Fanpage trọng điểm: <strong>MEDDC</strong> và <strong>Thân Tâm - CSKH Tại Nhà</strong>.</li>
      <li>Triển khai dự án <strong>B2B Healthcare Marketing</strong> kết nối nhãn hàng lớn (<strong>Comfort, ColosBaby, Gaviscon...</strong>) với các bệnh viện đầu ngành (BV Nhi Đồng 1, BV Thủ Đức, BV 175) qua kênh <strong>MEDTV</strong>.</li>
    </ul>
    <div class="achievement-box">
      <div class="achievement-title">
        <span>🏆 Kết quả &amp; Thành tựu nổi bật:</span>
      </div>
      <ul class="achievement-list">
        <li>Đạt <span class="badge-metric">98.474 lượt xem</span> và <span class="badge-metric">37.417 người tiếp cận</span> chỉ trong 28 ngày qua chiến lược Reels đánh trúng insight.</li>
        <li>Tăng trưởng <span class="badge-metric">+880,5% tương tác</span> và tăng <span class="badge-metric">+547% người theo dõi (+110 organic followers)</span> trong 28 ngày.</li>
      </ul>
    </div>
  </div>

  <div class="page-footer">
    <span>CV Lê Thị Hoàng Cẩm — Marketing Executive (Content &amp; Digital Marketing)</span>
    <span>Trang 1 / 2</span>
  </div>
</div>

<!-- ================= PAGE 2 ================= -->
<div class="a4-page">

  <!-- EXPERIENCE (PART 2) -->
  <div class="section-title" style="margin-top: 0;">Kinh nghiệm làm việc thực chiến (Tiếp theo)</div>

  <!-- JOB 3 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-company-name">Công ty Cổ phần Dược phẩm OPV</span>
      </div>
      <span class="lime-pill">12/2024 – 02/2026</span>
    </div>
    <div class="job-role-line">
      <span>Chuyên viên Content &amp; Digital Marketing</span>
      <span class="job-brand-tag">Pharmaceutical Brand</span>
    </div>
    <ul class="job-bullets">
      <li>Lập kế hoạch &amp; sản xuất content đa kênh (Facebook, TikTok, Web), tối ưu hóa SEO và báo cáo hiệu suất; phối hợp cùng Designer và IT sản xuất tư liệu và tối ưu giao diện website.</li>
      <li>Thiết lập và vận hành chiến dịch quảng cáo paid-ads (Facebook Ads, TikTok Ads, Instagram Ads) gia tăng độ nhận diện cho các dòng sản phẩm dược phẩm mới.</li>
    </ul>
    <div class="achievement-box">
      <div class="achievement-title">
        <span>🏆 Kết quả &amp; Thành tựu nổi bật:</span>
      </div>
      <ul class="achievement-list">
        <li>Tăng <span class="badge-metric">25 – 30% view &amp; tương tác tự nhiên</span> sau 2 tháng triển khai chiến dịch nội dung mới.</li>
        <li>Thúc đẩy tỷ lệ tăng trưởng người theo dõi đa nền tảng từ <strong>2-3% lên 7-8%</strong> ổn định.</li>
      </ul>
    </div>
  </div>

  <!-- JOB 4 -->
  <div class="job-card">
    <div class="job-head">
      <div>
        <span class="job-company-name">Hệ thống Nha Khoa Kim</span>
      </div>
      <span class="lime-pill">06/2024 – 12/2024</span>
    </div>
    <div class="job-role-line">
      <span>Chuyên viên Chăm sóc &amp; Trải nghiệm Khách hàng</span>
      <span class="job-brand-tag">Dịch vụ Khách hàng</span>
    </div>
    <ul class="job-bullets">
      <li>Hướng dẫn, giải đáp quy trình điều trị y tế chuyên sâu; quản lý thông tin khách hàng và phối hợp với bác sĩ tối ưu quy trình đón tiếp giúp giảm thiểu thời gian chờ khám của khách hàng.</li>
    </ul>
    <div class="achievement-box">
      <div class="achievement-title">
        <span>🏆 Kết quả &amp; Thành tựu nổi bật:</span>
      </div>
      <ul class="achievement-list">
        <li>Tiếp đón và hỗ trợ chu đáo <span class="badge-metric">10 – 15 khách/ngày</span>, xuất sắc đạt <span class="badge-metric">90 – 110% KPI</span> chất lượng dịch vụ được giao.</li>
        <li>Duy trì tỷ lệ khách hàng cũ quay lại tái khám và tỷ lệ khách hài lòng dịch vụ ở mức cao.</li>
      </ul>
    </div>
  </div>

  <!-- 2-COLUMN GRID (BOTTOM PAGE 2) -->
  <div class="p2-grid">
    <!-- LEFT: EDUCATION, CERTS, WORK STYLE -->
    <div style="display: flex; flex-direction: column; gap: 2.2mm;">
      <div>
        <div class="section-title" style="margin-top: 1mm;">Học vấn &amp; Bằng cấp</div>
        <div class="card-box" style="padding: 2.8mm 3.5mm;">
          <div class="lime-pill">2019 – 2023</div>
          <div class="edu-title">Đại học Sài Gòn</div>
          <div class="edu-sub">Cử nhân Thông Tin – Thư Viện<br>Thế mạnh: Khai thác, cấu trúc dữ liệu &amp; quản trị thông tin chuẩn xác.</div>
        </div>
      </div>

      <div>
        <div class="section-title" style="margin-top: 1mm;">Chứng chỉ chuyên môn</div>
        <div class="card-box" style="padding: 2.8mm 3.5mm; gap: 1.5mm;">
          <div>
            <div class="lime-pill">06/2024</div>
            <div class="edu-title" style="margin-top: 1px;">TOEIC Speaking &amp; Writing</div>
            <div class="edu-sub">Kỹ năng giao tiếp và biên soạn thông điệp quảng cáo chuyên nghiệp.</div>
          </div>
          <div style="border-top: 1px solid var(--bar-bg); padding-top: 1.5mm;">
            <div class="lime-pill">06/2023</div>
            <div class="edu-title" style="margin-top: 1px;">Tin Học Văn Phòng MOS</div>
            <div class="edu-sub">Thành thạo Excel báo cáo dữ liệu, Word kịch bản &amp; PowerPoint.</div>
          </div>
        </div>
      </div>

      <div>
        <div class="section-title" style="margin-top: 1mm;">Kỹ năng bổ trợ</div>
        <div class="card-box" style="padding: 2.8mm 3.5mm;">
          <ul class="soft-skill-list">
            <li class="soft-skill-item">
              <span class="soft-skill-check">✓</span>
              <div><strong>Bắt trend nhạy bén:</strong> Nắm bắt nhanh thuật toán TikTok/Reels &amp; xu hướng thị hiếu giới trẻ.</div>
            </li>
            <li class="soft-skill-item">
              <span class="soft-skill-check">✓</span>
              <div><strong>Thấu hiểu khách hàng:</strong> Khéo léo, am hiểu sâu tâm lý và hành vi người tiêu dùng đa độ tuổi.</div>
            </li>
            <li class="soft-skill-item">
              <span class="soft-skill-check">✓</span>
              <div><strong>Cam kết tiến độ:</strong> Trách nhiệm cao, kỷ luật deadline và phối hợp nhịp nhàng đa phòng ban.</div>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- RIGHT: SKILLS & TOOLS (DESCRIPTIVE BULLETS) -->
    <div style="display: flex; flex-direction: column; gap: 2.2mm;">
      <div>
        <div class="section-title" style="margin-top: 1mm;">Kỹ năng chuyên môn</div>
        <div class="card-box" style="padding: 2.8mm 3.5mm;">
          <ul class="skill-text-list">
            <li class="skill-text-item">
              <span class="skill-bullet-check">✓</span>
              <div><strong>Short-form Video:</strong> Lên ý tưởng, kịch bản, quay dựng video ngắn Reels/TikTok bắt trend.</div>
            </li>
            <li class="skill-text-item">
              <span class="skill-bullet-check">✓</span>
              <div><strong>Content &amp; Copywriting:</strong> Sáng tạo nội dung đa kênh, kịch bản video/Reels, bài PR truyền thông.</div>
            </li>
            <li class="skill-text-item">
              <span class="skill-bullet-check">✓</span>
              <div><strong>Digital Marketing &amp; Ads:</strong> Thiết lập và vận hành chiến dịch Facebook Ads, TikTok Ads.</div>
            </li>
            <li class="skill-text-item">
              <span class="skill-bullet-check">✓</span>
              <div><strong>Nội dung chuẩn SEO:</strong> Tối ưu bài viết Y Dược/Sản phẩm chuẩn SEO On-page, quản trị website.</div>
            </li>
            <li class="skill-text-item">
              <span class="skill-bullet-check">✓</span>
              <div><strong>Quản trị Social Media:</strong> Theo dõi hiệu suất kênh, phân tích báo cáo và tối ưu tỷ lệ chuyển đổi.</div>
            </li>
          </ul>
        </div>
      </div>

      <div>
        <div class="section-title" style="margin-top: 1mm;">Công cụ &amp; Ứng dụng AI</div>
        <div class="card-box" style="padding: 2.8mm 3.5mm;">
          <ul class="skill-text-list" style="gap: 2mm;">
            <li class="tool-row-item">
              <span class="tool-app-icon">Cp</span>
              <div class="tool-info"><strong>CapCut Pro:</strong> Dựng video ngắn đa nền tảng, hiệu ứng &amp; âm nhạc xu hướng.</div>
            </li>
            <li class="tool-row-item">
              <span class="tool-app-icon">Cv</span>
              <div class="tool-info"><strong>Canva Pro:</strong> Thiết kế ấn phẩm social, infographic, banner &amp; tư liệu pitching.</div>
            </li>
            <li class="tool-row-item">
              <span class="tool-app-icon">AI</span>
              <div class="tool-info"><strong>GenAI (Gemini, ChatGPT):</strong> Khai thác insight, nghiên cứu ý tưởng &amp; tối ưu bài viết.</div>
            </li>
            <li class="tool-row-item">
              <span class="tool-app-icon">Ad</span>
              <div class="tool-info"><strong>Facebook &amp; TikTok Ads:</strong> Thiết lập nhóm quảng cáo, target tệp &amp; đo lường CPC.</div>
            </li>
            <li class="tool-row-item">
              <span class="tool-app-icon">Ps</span>
              <div class="tool-info"><strong>Photoshop / Premiere:</strong> Xử lý đồ họa, chỉnh sửa ảnh sản phẩm &amp; cắt ghép media.</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <div class="page-footer">
    <span>CV Lê Thị Hoàng Cẩm — Marketing Executive (Content &amp; Digital Marketing)</span>
    <span>Trang 2 / 2</span>
  </div>
</div>

</body>
</html>
'''

output_html = '/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_A4_2Trang.html'
output_pdf = '/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf'
output_preview = '/Users/Admin/Desktop/cv_preview_a4_2trang.png'
output_desktop_pdf = '/Users/Admin/Desktop/CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf'

with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated {output_html} successfully!")

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Print to PDF
subprocess.run([
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    f"--print-to-pdf={output_pdf}",
    "--no-pdf-header-footer",
    f"file://{output_html}"
], check=True)

print(f"Exported PDF to {output_pdf}")

# Copy to Desktop
shutil.copyfile(output_pdf, output_desktop_pdf)
print(f"Copied PDF to {output_desktop_pdf}")

# Check page count
with open(output_pdf, 'rb') as f:
    pdf_bytes = f.read()
pages = len(re.findall(rb'/Type\s*/Page\b', pdf_bytes))
print(f"Verified PDF page count: {pages} pages")

# Screenshot
subprocess.run([
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    f"--screenshot={output_preview}",
    "--window-size=1200,2400",
    f"file://{output_html}"
], check=True)

print(f"Exported preview screenshot to {output_preview}")
