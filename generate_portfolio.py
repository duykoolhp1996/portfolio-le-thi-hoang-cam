import base64
import os
import subprocess
import shutil

# Read avatar image
with open('/Users/Admin/Documents/HRM/avatar.jpg', 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

portfolio_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lê Thị Hoàng Cẩm — Marketing Executive Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-main: #FAF8F5;
    --bg-card: #FFFFFF;
    --bg-card-sub: #F3EFE9;
    --accent: #5B8266;
    --accent-dark: #3F5E48;
    --accent-soft: #E8EFE9;
    --accent-text: #264A31;
    --accent-border: #CCDDCF;
    --text-primary: #1E2320;
    --text-secondary: #525D56;
    --text-muted: #7A857E;
    --border-color: #E6E1D8;
    --shadow-sm: 0 2px 8px rgba(91, 130, 102, 0.05);
    --shadow-md: 0 8px 24px rgba(91, 130, 102, 0.08);
    --shadow-lg: 0 16px 40px rgba(91, 130, 102, 0.12);
    --radius-sm: 10px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --radius-full: 9999px;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  html {{
    scroll-behavior: smooth;
    font-size: 16px;
  }}

  body {{
    font-family: 'Outfit', sans-serif;
    background-color: var(--bg-main);
    color: var(--text-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }}

  a {{
    text-decoration: none;
    color: inherit;
  }}

  /* CONTAINER */
  .container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
  }}

  /* HEADER / NAVBAR */
  .navbar {{
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    background: rgba(250, 248, 245, 0.88);
    border-bottom: 1px solid var(--border-color);
    transition: all 0.3s ease;
  }}
  .nav-inner {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 72px;
  }}
  .brand-logo {{
    display: flex;
    align-items: center;
    gap: 12px;
    font-weight: 800;
    font-size: 1.15rem;
    letter-spacing: -0.3px;
  }}
  .brand-badge {{
    width: 36px;
    height: 36px;
    border-radius: var(--radius-sm);
    background: var(--accent);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 0.95rem;
  }}
  .nav-menu {{
    display: flex;
    align-items: center;
    gap: 28px;
    list-style: none;
  }}
  .nav-link {{
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-secondary);
    transition: color 0.2s ease;
    position: relative;
    padding: 6px 0;
  }}
  .nav-link:hover, .nav-link.active {{
    color: var(--accent-dark);
  }}
  .nav-link::after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0%;
    height: 2px;
    background: var(--accent);
    transition: width 0.25s ease;
    border-radius: var(--radius-full);
  }}
  .nav-link:hover::after {{
    width: 100%;
  }}
  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: var(--radius-full);
    font-size: 0.92rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s ease;
    border: none;
    font-family: inherit;
  }}
  .btn-primary {{
    background: var(--accent);
    color: #ffffff;
    box-shadow: 0 4px 14px rgba(91, 130, 102, 0.25);
  }}
  .btn-primary:hover {{
    background: var(--accent-dark);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(91, 130, 102, 0.35);
  }}
  .btn-secondary {{
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
  }}
  .btn-secondary:hover {{
    background: #dde8df;
    transform: translateY(-2px);
  }}
  .btn-outline {{
    background: transparent;
    color: var(--text-primary);
    border: 1.5px solid var(--border-color);
  }}
  .btn-outline:hover {{
    border-color: var(--accent);
    color: var(--accent-dark);
    transform: translateY(-2px);
  }}

  /* HERO SECTION */
  .hero-section {{
    padding: 70px 0 60px 0;
    position: relative;
  }}
  .hero-grid {{
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 48px;
    align-items: center;
  }}
  .hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
    padding: 6px 16px;
    border-radius: var(--radius-full);
    font-size: 0.86rem;
    font-weight: 800;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }}
  .hero-badge-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent);
    display: inline-block;
  }}
  .hero-title {{
    font-size: 3.2rem;
    font-weight: 900;
    line-height: 1.12;
    letter-spacing: -1.2px;
    color: var(--text-primary);
    margin-bottom: 20px;
  }}
  .hero-title .highlight {{
    color: var(--accent);
    position: relative;
    display: inline-block;
  }}
  .hero-desc {{
    font-size: 1.1rem;
    color: var(--text-secondary);
    line-height: 1.65;
    margin-bottom: 32px;
    max-width: 580px;
  }}
  .hero-cta-group {{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 16px;
    margin-bottom: 40px;
  }}
  .hero-stats-row {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    padding-top: 24px;
    border-top: 1px solid var(--border-color);
  }}
  .stat-card {{
    display: flex;
    flex-direction: column;
  }}
  .stat-num {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.85rem;
    font-weight: 800;
    color: var(--accent-dark);
    line-height: 1.1;
  }}
  .stat-label {{
    font-size: 0.84rem;
    font-weight: 600;
    color: var(--text-muted);
    margin-top: 4px;
  }}

  /* HERO AVATAR CARD */
  .hero-avatar-wrap {{
    position: relative;
    display: flex;
    justify-content: center;
  }}
  .hero-avatar-card {{
    position: relative;
    width: 100%;
    max-width: 380px;
    border-radius: var(--radius-lg);
    background: linear-gradient(160deg, #E6EFE8 0%, #D8E6DB 100%);
    padding: 12px;
    border: 1.5px solid var(--accent-border);
    box-shadow: var(--shadow-lg);
    transition: transform 0.4s ease;
  }}
  .hero-avatar-card:hover {{
    transform: translateY(-4px);
  }}
  .hero-avatar-img {{
    width: 100%;
    height: 440px;
    object-fit: cover;
    object-position: center top;
    border-radius: calc(var(--radius-lg) - 4px);
    display: block;
    background: #fff;
  }}
  .status-floating-pill {{
    position: absolute;
    bottom: -16px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(12px);
    border: 1px solid var(--accent-border);
    padding: 8px 18px;
    border-radius: var(--radius-full);
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: var(--shadow-md);
    white-space: nowrap;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-primary);
  }}
  .status-pulse {{
    width: 9px;
    height: 9px;
    background: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.2);
  }}

  /* SECTION BASICS */
  .section {{
    padding: 90px 0;
  }}
  .section-alt {{
    background: var(--bg-card-sub);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
  }}
  .section-header {{
    text-align: center;
    max-width: 680px;
    margin: 0 auto 54px auto;
  }}
  .section-tag {{
    display: inline-block;
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
    padding: 4px 14px;
    border-radius: var(--radius-full);
    font-size: 0.8rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }}
  .section-title {{
    font-size: 2.25rem;
    font-weight: 900;
    letter-spacing: -0.6px;
    color: var(--text-primary);
    margin-bottom: 12px;
  }}
  .section-subtitle {{
    font-size: 1.05rem;
    color: var(--text-secondary);
  }}

  /* ABOUT BENTO GRID */
  .about-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
  }}
  .bento-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 32px 28px;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
  }}
  .bento-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--shadow-md);
    border-color: var(--accent-border);
  }}
  .bento-card-span2 {{
    grid-column: span 2;
  }}
  .bento-icon {{
    width: 48px;
    height: 48px;
    border-radius: var(--radius-sm);
    background: var(--accent-soft);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    margin-bottom: 20px;
  }}
  .bento-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 10px;
    letter-spacing: -0.2px;
  }}
  .bento-desc {{
    font-size: 0.95rem;
    color: var(--text-secondary);
    line-height: 1.6;
  }}

  /* PORTFOLIO / CASE STUDIES */
  .portfolio-filter {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 40px;
  }}
  .filter-btn {{
    padding: 8px 20px;
    border-radius: var(--radius-full);
    font-size: 0.88rem;
    font-weight: 700;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.25s ease;
    font-family: inherit;
  }}
  .filter-btn:hover, .filter-btn.active {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
    box-shadow: 0 4px 12px rgba(91, 130, 102, 0.25);
  }}

  .case-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 28px;
  }}
  .case-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
  }}
  .case-card:hover {{
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-border);
  }}
  .case-card-top {{
    padding: 24px 28px 16px 28px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}
  .case-category-tag {{
    font-size: 0.78rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--accent-text);
    background: var(--accent-soft);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    border: 1px solid var(--accent-border);
  }}
  .case-timeline {{
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-muted);
    font-family: 'Space Grotesk', sans-serif;
  }}
  .case-card-body {{
    padding: 0 28px 20px 28px;
    flex: 1;
  }}
  .case-title {{
    font-size: 1.35rem;
    font-weight: 800;
    line-height: 1.3;
    color: var(--text-primary);
    margin-bottom: 8px;
  }}
  .case-brands {{
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .case-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
    font-size: 0.92rem;
    color: var(--text-secondary);
    margin-bottom: 20px;
  }}
  .case-bullets li {{
    position: relative;
    padding-left: 20px;
  }}
  .case-bullets li::before {{
    content: "•";
    position: absolute;
    left: 4px;
    color: var(--accent);
    font-weight: 900;
  }}
  .case-metrics-banner {{
    background: var(--accent-soft);
    border-left: 3px solid var(--accent);
    padding: 12px 16px;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    align-items: center;
  }}
  .metric-item {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--accent-text);
  }}
  .metric-badge {{
    background: #fff;
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Space Grotesk', sans-serif;
    color: var(--accent-dark);
    font-weight: 800;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }}

  /* SKILLS & ECOSYSTEM */
  .skills-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 32px;
  }}
  .skill-box {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 32px;
    box-shadow: var(--shadow-sm);
  }}
  .skill-box-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .skill-list-items {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .skill-list-item {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 0.95rem;
    color: var(--text-secondary);
  }}
  .skill-check-icon {{
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--accent-soft);
    color: var(--accent-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: 900;
    flex-shrink: 0;
    margin-top: 2px;
  }}

  /* TOOL CHIPS GRID */
  .tools-pill-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 14px;
  }}
  .tool-chip {{
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    border-radius: var(--radius-sm);
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    transition: all 0.25s ease;
  }}
  .tool-chip:hover {{
    background: #fff;
    border-color: var(--accent-border);
    transform: translateY(-2px);
    box-shadow: var(--shadow-sm);
  }}
  .tool-icon-square {{
    width: 32px;
    height: 32px;
    border-radius: 6px;
    background: var(--accent-dark);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.8rem;
    font-weight: 800;
    flex-shrink: 0;
  }}
  .tool-name {{
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-primary);
  }}
  .tool-role {{
    font-size: 0.78rem;
    color: var(--text-muted);
  }}

  /* TIMELINE SECTION */
  .timeline-wrap {{
    max-width: 820px;
    margin: 0 auto;
    position: relative;
    padding-left: 32px;
  }}
  .timeline-wrap::before {{
    content: '';
    position: absolute;
    top: 10px;
    bottom: 10px;
    left: 8px;
    width: 2px;
    background: var(--border-color);
  }}
  .timeline-item {{
    position: relative;
    margin-bottom: 36px;
  }}
  .timeline-dot {{
    position: absolute;
    left: -32px;
    top: 6px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--accent);
    border: 4px solid var(--bg-main);
    box-shadow: 0 0 0 2px var(--accent-border);
  }}
  .timeline-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 24px;
    box-shadow: var(--shadow-sm);
  }}
  .timeline-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 6px;
  }}
  .timeline-role {{
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
  }}
  .timeline-date {{
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--accent-text);
    background: var(--accent-soft);
    padding: 2px 10px;
    border-radius: var(--radius-full);
    font-family: 'Space Grotesk', sans-serif;
  }}
  .timeline-company {{
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 10px;
  }}

  /* CONTACT SECTION */
  .contact-card {{
    background: linear-gradient(145deg, #FAF8F5 0%, #EFF4F0 100%);
    border: 1.5px solid var(--accent-border);
    border-radius: var(--radius-lg);
    padding: 56px 48px;
    box-shadow: var(--shadow-md);
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    align-items: center;
  }}
  .contact-title {{
    font-size: 2.2rem;
    font-weight: 900;
    color: var(--text-primary);
    line-height: 1.2;
    margin-bottom: 16px;
  }}
  .contact-desc {{
    font-size: 1.05rem;
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 28px;
  }}
  .contact-info-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }}
  .contact-info-item {{
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 1rem;
    font-weight: 600;
  }}
  .contact-info-icon {{
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--accent);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
  }}
  .contact-actions-box {{
    background: #fff;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 32px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    box-shadow: var(--shadow-sm);
  }}

  /* FOOTER */
  .footer {{
    background: #fff;
    border-top: 1px solid var(--border-color);
    padding: 32px 0;
    text-align: center;
    font-size: 0.9rem;
    color: var(--text-muted);
  }}

  /* RESPONSIVE */
  @media (max-width: 992px) {{
    .hero-grid {{
      grid-template-columns: 1fr;
      text-align: center;
      gap: 40px;
    }}
    .hero-desc {{
      margin: 0 auto 32px auto;
    }}
    .hero-cta-group {{
      justify-content: center;
    }}
    .hero-stats-row {{
      justify-content: center;
    }}
    .about-grid {{
      grid-template-columns: 1fr;
    }}
    .bento-card-span2 {{
      grid-column: span 1;
    }}
    .case-grid {{
      grid-template-columns: 1fr;
    }}
    .skills-grid {{
      grid-template-columns: 1fr;
    }}
    .contact-card {{
      grid-template-columns: 1fr;
      padding: 36px 24px;
    }}
  }}

  @media (max-width: 768px) {{
    .hero-title {{
      font-size: 2.3rem;
    }}
    .nav-menu {{
      display: none;
    }}
    .tools-pill-grid {{
      grid-template-columns: 1fr;
    }}
  }}
</style>
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar">
  <div class="container nav-inner">
    <a href="#" class="brand-logo">
      <div class="brand-badge">HC</div>
      <div>
        <div>LÊ THỊ HOÀNG CẨM</div>
        <div style="font-size: 0.72rem; font-weight: 700; color: var(--accent); letter-spacing: 0.5px;">MARKETING EXECUTIVE</div>
      </div>
    </a>
    <ul class="nav-menu">
      <li><a href="#about" class="nav-link">Về tôi</a></li>
      <li><a href="#projects" class="nav-link">Dự án thực chiến</a></li>
      <li><a href="#skills" class="nav-link">Kỹ năng &amp; AI</a></li>
      <li><a href="#experience" class="nav-link">Hành trình</a></li>
      <li><a href="#contact" class="nav-link">Liên hệ</a></li>
    </ul>
    <div class="nav-actions">
      <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary">
        <span>📄 Tải CV PDF</span>
      </a>
    </div>
  </div>
</nav>

<!-- HERO SECTION -->
<section class="hero-section">
  <div class="container hero-grid">
    <div>
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        MARKETING EXECUTIVE • CONTENT &amp; DIGITAL MARKETING
      </div>
      <h1 class="hero-title">
        Sáng tạo nội dung chạm <span class="highlight">insight</span>, tối ưu chuyển đổi đa kênh.
      </h1>
      <p class="hero-desc">
        Chào bạn! Mình là <strong>Lê Thị Hoàng Cẩm</strong>, chuyên viên Marketing Executive với hơn <strong>3 năm kinh nghiệm thực chiến</strong> bao quát từ Content Strategy, Short-form Video, Social Media Ads đến Healthcare &amp; FMCG Marketing.
      </p>
      <div class="hero-cta-group">
        <a href="#projects" class="btn btn-primary" style="padding: 12px 28px; font-size: 1rem;">
          <span>Khám phá Dự án</span>
          <span>↓</span>
        </a>
        <a href="tel:0363123121" class="btn btn-secondary" style="padding: 12px 24px; font-size: 1rem;">
          <span>📞 0363 123 121</span>
        </a>
        <a href="#contact" class="btn btn-outline" style="padding: 12px 24px;">
          <span>Kết nối ngay</span>
        </a>
      </div>
      <div class="hero-stats-row">
        <div class="stat-card">
          <span class="stat-num">3+ Năm</span>
          <span class="stat-label">Kinh nghiệm thực chiến</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">98.4K+</span>
          <span class="stat-label">Views chiến dịch Healthcare</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">+880%</span>
          <span class="stat-label">Tăng trưởng tương tác Reels</span>
        </div>
      </div>
    </div>

    <!-- AVATAR CARD -->
    <div class="hero-avatar-wrap">
      <div class="hero-avatar-card">
        <img class="hero-avatar-img" src="data:image/jpeg;base64,{avatar_b64}" alt="Lê Thị Hoàng Cẩm — Marketing Executive">
        <div class="status-floating-pill">
          <span class="status-pulse"></span>
          <span>Sẵn sàng cho cơ hội mới</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT SECTION -->
<section id="about" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Về Bản Thân</span>
      <h2 class="section-title">Định vị &amp; Giá trị Cốt lõi</h2>
      <p class="section-subtitle">Kết hợp tư duy dữ liệu chuẩn xác và khả năng sáng tạo câu chuyện thương hiệu chạm đến cảm xúc khách hàng.</p>
    </div>

    <div class="about-grid">
      <div class="bento-card bento-card-span2">
        <div class="bento-icon">💡</div>
        <h3 class="bento-title">Chiến lược Content &amp; Insight Đa Nền Tảng</h3>
        <p class="bento-desc">
          Xuất thân từ chuyên ngành <strong>Thông Tin – Thư Viện (Đại học Sài Gòn)</strong>, mình sở hữu thế mạnh vượt trội trong việc khai thác dữ liệu thị trường, phân tích hành vi người dùng và cấu trúc thông tin mạch lạc. Mình không chỉ tạo ra nội dung bắt trend mà luôn đảm bảo nội dung đó phục vụ trực tiếp cho mục tiêu định vị thương hiệu và tăng trưởng lâu dài.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🏥</div>
        <h3 class="bento-title">Thế mạnh Healthcare &amp; FMCG</h3>
        <p class="bento-desc">
          Am hiểu sâu sắc các quy chuẩn khắt khe trong truyền thông Y Dược và Dược mỹ phẩm. Từng triển khai thành công chiến dịch B2B kết nối các nhãn hàng quốc tế với các bệnh viện đầu ngành tại TP.HCM.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">📊</div>
        <h3 class="bento-title">Data-Driven Marketing</h3>
        <p class="bento-desc">
          Lập kế hoạch, triển khai Paid-Ads (Facebook Ads, TikTok Ads) và đo lường liên tục các chỉ số Reach, Engagement, CPC và Conversion Rate để tối ưu hóa ngân sách.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🎬</div>
        <h3 class="bento-title">Short-form Video Creator</h3>
        <p class="bento-desc">
          Làm chủ toàn bộ quy trình sản xuất video ngắn (Reels, TikTok, Shorts) từ lên ý tưởng, viết kịch bản phân cảnh đến quay chụp và dựng hậu kỳ chuyên nghiệp trên CapCut Pro.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🤝</div>
        <h3 class="bento-title">Trải nghiệm &amp; Chăm sóc Khách hàng</h3>
        <p class="bento-desc">
          Từng quản lý thông tin khách hàng và điều phối trải nghiệm dịch vụ chuyên sâu tại Nha Khoa Kim, giúp mình thấu hiểu tường tận hành trình khách hàng từ lúc tiếp cận đến khi hài lòng sử dụng dịch vụ.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- PROJECTS / CASE STUDIES -->
<section id="projects" class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Case Studies Thực Chiến</span>
      <h2 class="section-title">Dự Án Nổi Bật</h2>
      <p class="section-subtitle">Những dấu ấn kết quả thực tế qua các chiến dịch truyền thông đa kênh đã triển khai.</p>
    </div>

    <!-- FILTER TABS -->
    <div class="portfolio-filter">
      <button class="filter-btn active" onclick="filterProjects('all')">Tất cả dự án (4)</button>
      <button class="filter-btn" onclick="filterProjects('healthcare')">Healthcare Marketing</button>
      <button class="filter-btn" onclick="filterProjects('beauty')">Beauty &amp; FMCG</button>
      <button class="filter-btn" onclick="filterProjects('digital')">Digital Ads &amp; SEO</button>
    </div>

    <!-- CASE CARDS GRID -->
    <div class="case-grid">

      <!-- PROJECT 1 -->
      <div class="case-card" data-category="beauty">
        <div class="case-card-top">
          <span class="case-category-tag">Beauty &amp; Influencer KOC</span>
          <span class="case-timeline">09/2024 – Hiện tại</span>
        </div>
        <div class="case-card-body">
          <h3 class="case-title">Chiến dịch Sáng tạo Nội dung Đa nền tảng &amp; Reviewer</h3>
          <div class="case-brands">✨ L’Oréal • Vichy • Eucerin • SVR</div>
          <ul class="case-bullets">
            <li>Lên ý tưởng, viết kịch bản chi tiết, tự chủ quay chụp và dựng video ngắn chuẩn visual mỹ phẩm cao cấp.</li>
            <li>Hợp tác sản xuất video trải nghiệm/cảm nhận sản phẩm theo brief từ các nhãn hàng hàng đầu thế giới, bắt nhịp xu hướng thị hiếu giới trẻ.</li>
            <li>Được các thương hiệu lớn gửi lời mời tham dự sự kiện ra mắt độc quyền và sản xuất video review tại sự kiện.</li>
          </ul>
        </div>
        <div style="padding: 0 28px 24px 28px;">
          <div class="case-metrics-banner">
            <span class="metric-item">👀 Views trung bình: <strong class="metric-badge">15.000 / tháng (+30%)</strong></span>
            <span class="metric-item">👤 Profile Visits: <strong class="metric-badge">800 lượt (+20%)</strong></span>
          </div>
        </div>
      </div>

      <!-- PROJECT 2 -->
      <div class="case-card" data-category="healthcare">
        <div class="case-card-top">
          <span class="case-category-tag">B2B Healthcare &amp; Media</span>
          <span class="case-timeline">03/2026 – 09/2026</span>
        </div>
        <div class="case-card-body">
          <h3 class="case-title">Dự án Kênh Truyền Thông MEDTV &amp; Giáo Dục Sức Khỏe</h3>
          <div class="case-brands">🏥 Comfort • ColosBaby • Gaviscon x BV Nhi Đồng 1, BV 175</div>
          <ul class="case-bullets">
            <li>Quản trị trực tiếp 2 Fanpage trọng điểm: <strong>MEDDC</strong> và <strong>Thân Tâm - CSKH Tại Nhà</strong>.</li>
            <li>Triển khai dự án B2B Healthcare Marketing kết nối nhãn hàng lớn với các bệnh viện đầu ngành qua kênh MEDTV.</li>
            <li>Xây dựng chiến lược chuỗi Reels giáo dục sức khỏe đánh trúng insight phụ huynh và người bệnh.</li>
          </ul>
        </div>
        <div style="padding: 0 28px 24px 28px;">
          <div class="case-metrics-banner">
            <span class="metric-item">🔥 Video Views: <strong class="metric-badge">98.474 lượt</strong></span>
            <span class="metric-item">📈 Tương tác: <strong class="metric-badge">+880.5%</strong></span>
            <span class="metric-item">👥 Followers: <strong class="metric-badge">+547% trong 28 ngày</strong></span>
          </div>
        </div>
      </div>

      <!-- PROJECT 3 -->
      <div class="case-card" data-category="digital">
        <div class="case-card-top">
          <span class="case-category-tag">Pharmaceutical Brand &amp; Ads</span>
          <span class="case-timeline">12/2024 – 02/2026</span>
        </div>
        <div class="case-card-body">
          <h3 class="case-title">Chiến Dịch Content Chuẩn SEO &amp; Vận Hành Paid-Ads</h3>
          <div class="case-brands">💊 Công ty Cổ phần Dược phẩm OPV</div>
          <ul class="case-bullets">
            <li>Lập kế hoạch &amp; sản xuất chuỗi bài viết chuyên sâu chuẩn SEO Y Dược đa kênh (Facebook, TikTok, Website).</li>
            <li>Thiết lập và tối ưu chiến dịch Paid-Ads (Facebook Ads, TikTok Ads, Instagram Ads) gia tăng nhận diện các dòng sản phẩm mới.</li>
            <li>Phối hợp cùng Designer và IT sản xuất tư liệu media và tối ưu giao diện website công ty.</li>
          </ul>
        </div>
        <div style="padding: 0 28px 24px 28px;">
          <div class="case-metrics-banner">
            <span class="metric-item">🚀 Reach tự nhiên: <strong class="metric-badge">+25 – 30%</strong></span>
            <span class="metric-item">📊 Tăng trưởng Follower: <strong class="metric-badge">Từ 2-3% lên 7-8%</strong></span>
          </div>
        </div>
      </div>

      <!-- PROJECT 4 -->
      <div class="case-card" data-category="healthcare">
        <div class="case-card-top">
          <span class="case-category-tag">Customer Experience &amp; Care</span>
          <span class="case-timeline">06/2024 – 12/2024</span>
        </div>
        <div class="case-card-body">
          <h3 class="case-title">Tối Ưu Trải Nghiệm &amp; Quản Trị Thông Tin Dịch Vụ Y Tế</h3>
          <div class="case-brands">🦷 Hệ thống Nha Khoa Kim</div>
          <ul class="case-bullets">
            <li>Hướng dẫn, giải đáp chu đáo các quy trình và liệu trình nha khoa chuyên sâu cho khách hàng.</li>
            <li>Quản lý hệ thống thông tin khách hàng, phân loại tệp và điều phối quy trình đón tiếp cùng đội ngũ bác sĩ.</li>
            <li>Giảm thiểu tối đa thời gian chờ đợi khám và nâng cao chỉ số hài lòng dịch vụ y tế.</li>
          </ul>
        </div>
        <div style="padding: 0 28px 24px 28px;">
          <div class="case-metrics-banner">
            <span class="metric-item">⭐ Tiếp đón &amp; Hỗ trợ: <strong class="metric-badge">10 – 15 khách/ngày</strong></span>
            <span class="metric-item">🎯 KPI chất lượng: <strong class="metric-badge">90 – 110%</strong></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- SKILLS & TOOLS ECOSYSTEM -->
<section id="skills" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Năng Lực Cốt Lõi</span>
      <h2 class="section-title">Kỹ Năng &amp; Hệ Sinh Thái Công Cụ</h2>
      <p class="section-subtitle">Bộ công cụ và năng lực thực chiến giúp tối ưu hiệu suất công việc Marketing hàng ngày.</p>
    </div>

    <div class="skills-grid">
      <!-- LEFT: SKILLS LIST -->
      <div class="skill-box">
        <h3 class="skill-box-title">
          <span>🎯</span> Kỹ Năng Chuyên Môn Thực Chiến
        </h3>
        <ul class="skill-list-items">
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Short-form Video Creation:</strong> Lên ý tưởng, viết kịch bản, quay dựng video ngắn Reels/TikTok bắt nhịp xu hướng và chạm cảm xúc.
            </div>
          </li>
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Content Strategy &amp; Copywriting:</strong> Sáng tạo nội dung đa kênh, kịch bản phân cảnh video, bài PR truyền thông và thông điệp thương hiệu.
            </div>
          </li>
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Digital Marketing &amp; Social Ads:</strong> Thiết lập, theo dõi và tối ưu chiến dịch quảng cáo Facebook Ads, TikTok Ads.
            </div>
          </li>
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Nội dung chuẩn SEO:</strong> Tối ưu bài viết Y Dược/Sản phẩm chuẩn SEO On-page và quản trị giao diện website.
            </div>
          </li>
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Quản trị Social Media &amp; Đo lường:</strong> Vận hành Fanpage/kênh đa nền tảng, đọc báo cáo dữ liệu và tối ưu tỷ lệ chuyển đổi.
            </div>
          </li>
          <li class="skill-list-item">
            <span class="skill-check-icon">✓</span>
            <div>
              <strong style="color: var(--text-primary);">Thấu hiểu khách hàng:</strong> Khéo léo, am hiểu sâu tâm lý và hành vi người tiêu dùng đa độ tuổi.
            </div>
          </li>
        </ul>
      </div>

      <!-- RIGHT: TOOLS & CERTIFICATES -->
      <div style="display: flex; flex-direction: column; gap: 24px;">
        <div class="skill-box">
          <h3 class="skill-box-title">
            <span>⚙️</span> Công Cụ &amp; Ứng Dụng AI
          </h3>
          <div class="tools-pill-grid">
            <div class="tool-chip">
              <div class="tool-icon-square">Cp</div>
              <div>
                <div class="tool-name">CapCut Pro</div>
                <div class="tool-role">Dựng video ngắn đa nền tảng</div>
              </div>
            </div>
            <div class="tool-chip">
              <div class="tool-icon-square">Cv</div>
              <div>
                <div class="tool-name">Canva Pro</div>
                <div class="tool-role">Thiết kế ấn phẩm &amp; Pitching</div>
              </div>
            </div>
            <div class="tool-chip">
              <div class="tool-icon-square">AI</div>
              <div>
                <div class="tool-name">GenAI (Gemini/ChatGPT)</div>
                <div class="tool-role">Nghiên cứu insight &amp; Brainstorm</div>
              </div>
            </div>
            <div class="tool-chip">
              <div class="tool-icon-square">Ad</div>
              <div>
                <div class="tool-name">Meta &amp; TikTok Ads</div>
                <div class="tool-role">Target đối tượng &amp; Đo lường</div>
              </div>
            </div>
            <div class="tool-chip" style="grid-column: span 2;">
              <div class="tool-icon-square">Ps</div>
              <div>
                <div class="tool-name">Photoshop / Premiere Pro</div>
                <div class="tool-role">Xử lý đồ họa, chỉnh sửa ảnh &amp; cắt ghép tư liệu media</div>
              </div>
            </div>
          </div>
        </div>

        <div class="skill-box" style="padding: 24px 32px;">
          <h3 class="skill-box-title" style="margin-bottom: 14px;">
            <span>🎓</span> Học Vấn &amp; Chứng Chỉ
          </h3>
          <div style="display: flex; flex-direction: column; gap: 12px; font-size: 0.93rem;">
            <div>
              <strong style="color: var(--text-primary);">Đại học Sài Gòn (2019 – 2023)</strong><br>
              <span style="color: var(--text-secondary);">Cử nhân Thông Tin – Thư Viện (Thế mạnh: Khai thác, cấu trúc dữ liệu chuẩn xác)</span>
            </div>
            <div style="border-top: 1px solid var(--border-color); padding-top: 10px; display: flex; gap: 16px; flex-wrap: wrap;">
              <span>📜 <strong>TOEIC Speaking &amp; Writing (06/2024)</strong></span>
              <span>💻 <strong>Tin Học Văn Phòng MOS (06/2023)</strong></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- EXPERIENCE TIMELINE -->
<section id="experience" class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Hành Trình Sự Nghiệp</span>
      <h2 class="section-title">Kinh Nghiệm Thực Chiến</h2>
      <p class="section-subtitle">Chặng đường tích lũy kinh nghiệm và khẳng định năng lực qua các môi trường chuyên nghiệp.</p>
    </div>

    <div class="timeline-wrap">
      <!-- ITEM 1 -->
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Freelance Marketing Executive &amp; Content Creator</span>
            <span class="timeline-date">09/2024 – HIỆN TẠI</span>
          </div>
          <div class="timeline-company">Hợp tác thương hiệu mỹ phẩm: L’Oréal • Vichy • Eucerin • SVR</div>
          <p style="font-size: 0.93rem; color: var(--text-secondary); line-height: 1.55;">
            Chủ động toàn bộ quy trình từ ý tưởng, kịch bản, quay chụp đến dựng video ngắn trên đa nền tảng (Facebook, TikTok, Threads, Instagram). Kênh cá nhân đạt mốc 15.000+ views/tháng và thu hút 800 lượt truy cập profile/tháng.
          </p>
        </div>
      </div>

      <!-- ITEM 2 -->
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Digital Marketing</span>
            <span class="timeline-date">03/2026 – 09/2026</span>
          </div>
          <div class="timeline-company">Công ty TNHH Đào tạo &amp; Chăm sóc Sức khỏe Thân Tâm</div>
          <p style="font-size: 0.93rem; color: var(--text-secondary); line-height: 1.55;">
            Trực tiếp quản trị 2 Fanpage MEDDC &amp; Thân Tâm. Phối hợp kết nối các thương hiệu lớn (Comfort, ColosBaby, Gaviscon...) với bệnh viện đầu ngành qua kênh MEDTV. Đạt 98.474 views và tăng trưởng +880.5% tương tác trong 28 ngày.
          </p>
        </div>
      </div>

      <!-- ITEM 3 -->
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Content &amp; Digital Marketing</span>
            <span class="timeline-date">12/2024 – 02/2026</span>
          </div>
          <div class="timeline-company">Công ty Cổ phần Dược phẩm OPV</div>
          <p style="font-size: 0.93rem; color: var(--text-secondary); line-height: 1.55;">
            Phụ trách sản xuất content chuẩn SEO Y Dược và vận hành chiến dịch Paid-Ads đa kênh (Facebook, TikTok, Instagram Ads), thúc đẩy tiếp cận tự nhiên tăng 25–30% sau 2 tháng.
          </p>
        </div>
      </div>

      <!-- ITEM 4 -->
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Chăm sóc &amp; Trải nghiệm Khách hàng</span>
            <span class="timeline-date">06/2024 – 12/2024</span>
          </div>
          <div class="timeline-company">Hệ thống Nha Khoa Kim</div>
          <p style="font-size: 0.93rem; color: var(--text-secondary); line-height: 1.55;">
            Hướng dẫn quy trình điều trị y tế chuyên sâu, quản lý thông tin khách hàng và phối hợp bác sĩ tối ưu quy trình tiếp đón, đạt 90–110% KPI chất lượng dịch vụ.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT SECTION -->
<section id="contact" class="section section-alt">
  <div class="container">
    <div class="contact-card">
      <div>
        <span class="section-tag">Sẵn Sàng Hợp Tác</span>
        <h2 class="contact-title">Bạn đang tìm kiếm một Marketing Executive tận tâm &amp; hiệu quả?</h2>
        <p class="contact-desc">
          Hãy kết nối với mình để cùng nhau xây dựng những chiến dịch truyền thông sáng tạo, chạm đúng insight và mang lại tăng trưởng bền vững cho doanh nghiệp!
        </p>
        <ul class="contact-info-list">
          <li class="contact-info-item">
            <div class="contact-info-icon">📞</div>
            <div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Số điện thoại:</div>
              <a href="tel:0363123121" style="color: var(--accent-dark); font-weight: 700;">0363 123 121</a>
            </div>
          </li>
          <li class="contact-info-item">
            <div class="contact-info-icon">✉️</div>
            <div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Email công việc:</div>
              <a href="mailto:lethihoangcam5@gmail.com" style="color: var(--accent-dark); font-weight: 700;">lethihoangcam5@gmail.com</a>
            </div>
          </li>
          <li class="contact-info-item">
            <div class="contact-info-icon">📍</div>
            <div>
              <div style="font-size: 0.8rem; color: var(--text-muted);">Địa điểm làm việc:</div>
              <span>Bình Tân, TP. Hồ Chí Minh (Sẵn sàng onsite hoặc hybrid)</span>
            </div>
          </li>
        </ul>
      </div>

      <div class="contact-actions-box">
        <h3 style="font-size: 1.3rem; font-weight: 800; color: var(--text-primary);">Tải Hồ Sơ Ứng Tuyển</h3>
        <p style="font-size: 0.92rem; color: var(--text-secondary); line-height: 1.5;">
          Bạn có thể tải ngay bản CV hoàn chỉnh định dạng PDF chuẩn in ấn A4 2 trang đã được tối ưu cho nhà tuyển dụng:
        </p>
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
          <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary" style="padding: 14px; font-size: 1rem;">
            <span>📄 Tải CV Đầy Đủ (Có Ảnh &amp; SĐT)</span>
          </a>
          <a href="CV_Le_Thi_Hoang_Cam_AnDanh.pdf" target="_blank" class="btn btn-secondary" style="padding: 14px; font-size: 1rem;">
            <span>🔒 Tải Bản Ẩn Danh (Blind CV)</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="container">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
      <div>
        <strong>Lê Thị Hoàng Cẩm</strong> — Marketing Executive • Content &amp; Digital Marketing
      </div>
      <div>
        Thiết kế theo chuẩn hiện đại &amp; tối ưu trải nghiệm tuyển dụng.
      </div>
      <div>
        <a href="#" style="color: var(--accent); font-weight: 700;">↑ Về đầu trang</a>
      </div>
    </div>
  </div>
</footer>

<script>
  function filterProjects(category) {{
    const buttons = document.querySelectorAll('.filter-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    const cards = document.querySelectorAll('.case-card');
    cards.forEach(card => {{
      if (category === 'all' || card.getAttribute('data-category') === category) {{
        card.style.display = 'flex';
      }} else {{
        card.style.display = 'none';
      }}
    }});
  }}
</script>

</body>
</html>
'''

# Paths
dir_path = '/Users/Admin/Documents/HRM/portfolio'
os.makedirs(dir_path, exist_ok=True)

html_path = os.path.join(dir_path, 'index.html')
desktop_html = '/Users/Admin/Desktop/Portfolio_Le_Thi_Hoang_Cam.html'
desktop_preview = '/Users/Admin/Desktop/portfolio_preview.png'

# Write to HRM/portfolio/index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(portfolio_html)

# Also copy CV PDFs into the portfolio directory for easy relative links
shutil.copyfile('/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf', os.path.join(dir_path, 'CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf'))
shutil.copyfile('/Users/Admin/Documents/HRM/CV_Le_Thi_Hoang_Cam_AnDanh.pdf', os.path.join(dir_path, 'CV_Le_Thi_Hoang_Cam_AnDanh.pdf'))

# Copy HTML to Desktop
shutil.copyfile(html_path, desktop_html)
print(f"Generated {html_path} and copied to {desktop_html}")

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Take high-res preview screenshot
subprocess.run([
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    f"--screenshot={desktop_preview}",
    "--window-size=1280,3200",
    f"file://{html_path}"
], check=True)

print(f"Exported preview screenshot to {desktop_preview}")
