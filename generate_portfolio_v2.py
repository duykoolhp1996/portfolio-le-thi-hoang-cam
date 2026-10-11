import base64
import os
import subprocess
import shutil

assets_dir = '/Users/Admin/Documents/HRM/portfolio/assets'

def get_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Read avatar and optimized proof images
avatar_b64 = get_b64('/Users/Admin/Documents/HRM/avatar.jpg')
koc_b64 = get_b64(os.path.join(assets_dir, 'opt_koc.jpg'))
medtv_b64 = get_b64(os.path.join(assets_dir, 'opt_medtv.jpg'))
meddc_cover_b64 = get_b64(os.path.join(assets_dir, 'opt_meddc_cover.jpg'))
opv_b64 = get_b64(os.path.join(assets_dir, 'opt_opv.jpg'))
dental_b64 = get_b64(os.path.join(assets_dir, 'opt_dental.jpg'))
credentials_b64 = get_b64(os.path.join(assets_dir, 'opt_credentials.jpg'))
workflow_b64 = get_b64(os.path.join(assets_dir, 'opt_workflow.jpg'))
affiliate_b64 = get_b64(os.path.join(assets_dir, 'opt_affiliate.jpg'))

portfolio_html = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lê Thị Hoàng Cẩm — Marketing Executive Portfolio & Minh Chứng</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-main: #FAF8F5;
    --bg-card: #FFFFFF;
    --bg-card-sub: #F4F0EA;
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
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--bg-main);
    color: var(--text-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-rendering: optimizeLegibility;
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

  /* NAVBAR */
  .navbar {{
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    background: rgba(250, 248, 245, 0.92);
    border-bottom: 1px solid var(--border-color);
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
  }}
  .brand-badge {{
    width: 38px;
    height: 38px;
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
    gap: 24px;
    list-style: none;
  }}
  .nav-link {{
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--text-secondary);
    transition: color 0.2s ease;
    padding: 6px 0;
  }}
  .nav-link:hover {{
    color: var(--accent-dark);
  }}
  .nav-badge-pill {{
    background: #e0ece3;
    color: var(--accent-dark);
    font-size: 0.72rem;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: var(--radius-full);
    margin-left: 4px;
  }}

  .btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: var(--radius-full);
    font-size: 0.9rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s ease;
    border: none;
    font-family: inherit;
  }}
  .btn-primary {{
    background: var(--accent);
    color: #FFFFFF;
    box-shadow: 0 4px 14px rgba(91, 130, 102, 0.3);
  }}
  .btn-primary:hover {{
    background: var(--accent-dark);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(91, 130, 102, 0.4);
  }}
  .btn-secondary {{
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
  }}
  .btn-secondary:hover {{
    background: #d8e5da;
    transform: translateY(-2px);
  }}
  .btn-outline {{
    background: transparent;
    color: var(--text-primary);
    border: 1px solid var(--border-color);
  }}
  .btn-outline:hover {{
    background: #FFFFFF;
    border-color: var(--accent);
  }}

  /* HERO SECTION */
  .hero-section {{
    padding: 64px 0 50px 0;
  }}
  .hero-grid {{
    display: grid;
    grid-template-columns: 1.25fr 0.75fr;
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
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.6px;
    margin-bottom: 20px;
  }}
  .hero-badge-dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent);
  }}
  .hero-title {{
    font-size: 2.85rem;
    font-weight: 900;
    line-height: 1.18;
    letter-spacing: -0.8px;
    color: var(--text-primary);
    margin-bottom: 18px;
  }}
  .hero-title .highlight {{
    color: var(--accent);
    position: relative;
    display: inline-block;
  }}
  .hero-desc {{
    font-size: 1.08rem;
    color: var(--text-secondary);
    line-height: 1.6;
    margin-bottom: 26px;
    max-width: 620px;
  }}
  .hero-cta-group {{
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 36px;
  }}
  .hero-stats-row {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    border-top: 1px solid var(--border-color);
    padding-top: 24px;
  }}
  .stat-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 14px 16px;
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
  }}
  .stat-num {{
    font-size: 1.55rem;
    font-weight: 900;
    color: var(--accent-dark);
    font-family: 'Space Grotesk', sans-serif;
    line-height: 1.1;
  }}
  .stat-label {{
    font-size: 0.78rem;
    color: var(--text-secondary);
    font-weight: 600;
    margin-top: 2px;
  }}
  .stat-verified {{
    font-size: 0.7rem;
    color: var(--accent);
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 4px;
    margin-top: 4px;
  }}

  /* AVATAR WRAP */
  .hero-avatar-wrap {{
    position: relative;
    display: flex;
    justify-content: center;
  }}
  .hero-avatar-card {{
    position: relative;
    width: 320px;
    border-radius: var(--radius-lg);
    background: #fff;
    padding: 10px;
    border: 1px solid var(--border-color);
    box-shadow: var(--shadow-md);
  }}
  .hero-avatar-img {{
    width: 100%;
    height: 380px;
    object-fit: cover;
    object-position: center top;
    border-radius: calc(var(--radius-lg) - 6px);
    display: block;
  }}
  .status-floating-pill {{
    position: absolute;
    bottom: -14px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(12px);
    border: 1px solid var(--accent-border);
    padding: 7px 18px;
    border-radius: var(--radius-full);
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: var(--shadow-md);
    white-space: nowrap;
    font-size: 0.84rem;
    font-weight: 700;
    color: var(--text-primary);
  }}
  .status-pulse {{
    width: 8px;
    height: 8px;
    background: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.2);
  }}

  /* SECTION BASICS */
  .section {{
    padding: 70px 0;
  }}
  .section-alt {{
    background: var(--bg-card-sub);
    border-top: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
  }}
  .section-header {{
    text-align: center;
    max-width: 720px;
    margin: 0 auto 40px auto;
  }}
  .section-tag {{
    display: inline-block;
    background: var(--accent-soft);
    color: var(--accent-text);
    border: 1px solid var(--accent-border);
    padding: 3px 12px;
    border-radius: var(--radius-full);
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 10px;
  }}
  .section-title {{
    font-size: 2.15rem;
    font-weight: 900;
    letter-spacing: -0.5px;
    color: var(--text-primary);
    margin-bottom: 8px;
  }}
  .section-subtitle {{
    font-size: 1rem;
    color: var(--text-secondary);
  }}

  /* PROOF SHOWCASE TABS */
  .proof-filter-bar {{
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 30px;
    flex-wrap: wrap;
  }}
  .proof-tab-btn {{
    padding: 8px 18px;
    border-radius: var(--radius-full);
    font-size: 0.88rem;
    font-weight: 700;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: inherit;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .proof-tab-btn.active, .proof-tab-btn:hover {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
    box-shadow: 0 4px 12px rgba(91, 130, 102, 0.25);
  }}

  /* VISUAL PROOF GRID */
  .evidence-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-bottom: 40px;
  }}
  .evidence-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    cursor: pointer;
    position: relative;
  }}
  .evidence-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-border);
  }}
  .evidence-thumb-wrap {{
    position: relative;
    width: 100%;
    height: 220px;
    background: #EFECE6;
    overflow: hidden;
  }}
  .evidence-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }}
  .evidence-card:hover .evidence-img {{
    transform: scale(1.05);
  }}
  .evidence-zoom-overlay {{
    position: absolute;
    inset: 0;
    background: rgba(38, 74, 49, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.25s ease;
    color: #fff;
    font-size: 0.9rem;
    font-weight: 700;
    gap: 8px;
  }}
  .evidence-card:hover .evidence-zoom-overlay {{
    opacity: 1;
  }}
  .evidence-pill-tag {{
    position: absolute;
    top: 12px;
    left: 12px;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(8px);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    font-size: 0.72rem;
    font-weight: 800;
    color: var(--accent-text);
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  }}
  .evidence-content {{
    padding: 16px 18px 18px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
  }}
  .evidence-title {{
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.35;
    margin-bottom: 6px;
  }}
  .evidence-caption {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 12px;
  }}
  .evidence-stat-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--accent-soft);
    color: var(--accent-dark);
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 0.8rem;
    font-weight: 700;
    font-family: 'Space Grotesk', sans-serif;
  }}

  /* FEATURED VIDEOS SECTION */
  .video-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
  }}
  .video-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    transition: all 0.25s ease;
  }}
  .video-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-border);
  }}
  .video-thumb {{
    position: relative;
    width: 100%;
    height: 220px;
    background: #18221b;
    overflow: hidden;
    display: block;
  }}
  .video-thumb-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }}
  .video-card:hover .video-thumb-img {{
    transform: scale(1.06);
  }}
  .video-play-overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.65) 0%, rgba(0,0,0,0.2) 60%, rgba(0,0,0,0.1) 100%);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 14px;
  }}
  .video-play-btn {{
    align-self: center;
    margin-top: auto;
    margin-bottom: auto;
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.95);
    color: var(--accent-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.3);
    transition: all 0.25s ease;
  }}
  .video-card:hover .video-play-btn {{
    transform: scale(1.15);
    background: var(--accent);
    color: #fff;
  }}
  .video-badge-views {{
    align-self: flex-start;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(8px);
    color: #fff;
    font-size: 0.76rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: var(--radius-full);
  }}
  .video-card-body {{
    padding: 20px 22px 22px 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
  }}
  .video-meta-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    gap: 8px;
    flex-wrap: wrap;
  }}
  .video-source-pill {{
    font-size: 0.72rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--accent-text);
    background: var(--accent-soft);
    padding: 3px 10px;
    border-radius: var(--radius-full);
    border: 1px solid var(--accent-border);
  }}
  .video-hospital-tag {{
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--accent);
    font-family: 'Space Grotesk', sans-serif;
  }}
  .video-card-title {{
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.35;
    margin-bottom: 8px;
  }}
  .video-card-desc {{
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.55;
    margin-bottom: 18px;
    flex: 1;
  }}
  .video-analysis-box {{
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 12px 14px;
    margin-bottom: 16px;
    font-size: 0.82rem;
    line-height: 1.5;
  }}
  .analysis-item {{
    margin-bottom: 6px;
    display: flex;
    align-items: flex-start;
    gap: 6px;
    color: var(--text-secondary);
  }}
  .analysis-item:last-child {{
    margin-bottom: 0;
  }}
  .analysis-label {{
    font-weight: 700;
    color: var(--accent-text);
    white-space: nowrap;
    font-size: 0.8rem;
  }}
  .btn-group-card {{
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }}

  /* CASE STUDIES GRID */
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
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--accent-border);
  }}
  .case-media-header {{
    position: relative;
    width: 100%;
    height: 260px;
    background: #EAE6DF;
    overflow: hidden;
    cursor: pointer;
  }}
  .case-media-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }}
  .case-card:hover .case-media-img {{
    transform: scale(1.04);
  }}
  .case-media-overlay {{
    position: absolute;
    bottom: 12px;
    right: 12px;
    background: rgba(255, 255, 255, 0.94);
    padding: 5px 12px;
    border-radius: var(--radius-full);
    font-size: 0.76rem;
    font-weight: 700;
    color: var(--accent-dark);
    display: flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }}
  .case-body {{
    padding: 24px 26px 20px 26px;
    flex: 1;
    display: flex;
    flex-direction: column;
  }}
  .case-meta-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }}
  .case-category-tag {{
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    color: var(--accent-text);
    background: var(--accent-soft);
    padding: 2px 10px;
    border-radius: var(--radius-full);
    border: 1px solid var(--accent-border);
  }}
  .case-timeline {{
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-muted);
    font-family: 'Space Grotesk', sans-serif;
  }}
  .case-title {{
    font-size: 1.25rem;
    font-weight: 800;
    line-height: 1.3;
    color: var(--text-primary);
    margin-bottom: 6px;
  }}
  .case-title[onclick] {{
    cursor: pointer;
    transition: color 0.2s ease;
  }}
  .case-title[onclick]:hover {{
    color: var(--accent);
  }}
  .case-brands {{
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .case-bullets {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-size: 0.88rem;
    color: var(--text-secondary);
    margin-bottom: 16px;
    flex: 1;
  }}
  .case-bullets li {{
    position: relative;
    padding-left: 18px;
    line-height: 1.5;
  }}
  .case-bullets li::before {{
    content: "✓";
    position: absolute;
    left: 2px;
    color: var(--accent);
    font-weight: 800;
    font-size: 0.8rem;
  }}
  .case-metrics-banner {{
    background: var(--accent-soft);
    border-left: 3px solid var(--accent);
    padding: 10px 14px;
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
  }}
  .metric-item {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--accent-text);
  }}
  .metric-badge {{
    background: #fff;
    padding: 2px 7px;
    border-radius: 4px;
    font-family: 'Space Grotesk', sans-serif;
    color: var(--accent-dark);
    font-weight: 800;
  }}

  /* SKILLS DUAL SYSTEM: KINH NGHIỆM & NĂNG LỰC */
  .skills-dual-grid {{
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    gap: 32px;
    align-items: start;
  }}
  @media (max-width: 992px) {{
    .skills-dual-grid {{
      grid-template-columns: 1fr;
      gap: 28px;
    }}
  }}
  .skills-dual-col {{
    background: #fff;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 32px 28px;
    box-shadow: var(--shadow-sm);
  }}
  .skills-dual-col-header {{
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 24px;
    padding-bottom: 18px;
    border-bottom: 2px solid var(--accent-soft);
  }}
  .skills-dual-icon {{
    width: 48px;
    height: 48px;
    border-radius: var(--radius-sm);
    background: var(--accent-soft);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    flex-shrink: 0;
  }}
  .skills-dual-badge {{
    display: inline-block;
    font-size: 0.74rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--accent-dark);
    margin-bottom: 2px;
  }}
  .skills-dual-title {{
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--text-primary);
  }}

  /* TIMELINE TRONG CỘT KINH NGHIỆM */
  .dual-timeline-wrap {{
    position: relative;
    padding-left: 28px;
  }}
  .dual-timeline-wrap::before {{
    content: '';
    position: absolute;
    top: 10px;
    bottom: 10px;
    left: 8px;
    width: 2px;
    background: var(--accent-border);
  }}
  .dual-timeline-item {{
    position: relative;
    margin-bottom: 20px;
  }}
  .dual-timeline-item:last-child {{
    margin-bottom: 0;
  }}
  .dual-timeline-dot {{
    position: absolute;
    left: -28px;
    top: 8px;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: #fff;
    border: 3.5px solid var(--accent);
    box-shadow: 0 0 0 2px rgba(91, 130, 102, 0.18);
  }}
  .dual-timeline-card {{
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 16px 18px;
    transition: all 0.2s ease;
  }}
  .dual-timeline-card:hover {{
    border-color: var(--accent-border);
    background: #fff;
    box-shadow: var(--shadow-sm);
  }}
  .dual-timeline-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 4px;
    flex-wrap: wrap;
  }}
  .dual-timeline-role {{
    font-size: 1rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.35;
  }}
  .dual-timeline-date {{
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--accent);
    background: var(--accent-soft);
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Space Grotesk', sans-serif;
    white-space: nowrap;
  }}
  .dual-timeline-company {{
    font-size: 0.82rem;
    font-weight: 700;
    color: var(--accent-dark);
    margin-bottom: 6px;
  }}
  .dual-timeline-desc {{
    font-size: 0.86rem;
    color: var(--text-secondary);
    line-height: 1.5;
  }}

  /* NĂNG LỰC TRONG CỘT NĂNG LỰC */
  .competency-item {{
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 14px 16px;
    margin-bottom: 12px;
    transition: all 0.2s ease;
  }}
  .competency-item:hover {{
    border-color: var(--accent-border);
    background: #fff;
    box-shadow: var(--shadow-sm);
  }}
  .competency-item-top {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 6px;
  }}
  .competency-item-icon {{
    font-size: 1.15rem;
  }}
  .competency-item-title {{
    font-size: 0.96rem;
    font-weight: 800;
    color: var(--text-primary);
  }}
  .competency-item-desc {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.48;
  }}

  /* SKILL PILLS BOXES */
  .dual-skill-box {{
    margin-top: 18px;
    padding-top: 16px;
    border-top: 1px dashed var(--border-color);
  }}
  .dual-skill-box-title {{
    font-size: 0.95rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .skill-pill-list {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }}
  .skill-pill {{
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    padding: 6px 12px;
    border-radius: var(--radius-full);
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
  }}
  .skill-pill:hover {{
    border-color: var(--accent);
    background: var(--accent-soft);
    color: var(--accent-dark);
  }}
  .skill-pill strong {{
    color: var(--accent-dark);
  }}

  /* CONTACT CARD */
  .contact-card {{
    background: #fff;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    padding: 44px;
    box-shadow: var(--shadow-md);
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 40px;
    align-items: center;
  }}
  .contact-title {{
    font-size: 2rem;
    font-weight: 900;
    letter-spacing: -0.5px;
    margin-bottom: 12px;
  }}
  .contact-desc {{
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-bottom: 22px;
  }}
  .contact-info-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .contact-info-item {{
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 0.95rem;
  }}
  .contact-info-icon {{
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--accent-soft);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .contact-actions-box {{
    background: var(--bg-card-sub);
    padding: 28px;
    border-radius: var(--radius-md);
    border: 1px solid var(--border-color);
    text-align: center;
  }}

  /* FOOTER */
  .footer {{
    background: #202723;
    color: #C8D1CB;
    padding: 30px 0;
    font-size: 0.86rem;
    border-top: 1px solid #333D37;
  }}

  /* LIGHTBOX MODAL */
  .lightbox-modal {{
    position: fixed;
    inset: 0;
    background: rgba(18, 24, 21, 0.88);
    backdrop-filter: blur(10px);
    z-index: 2000;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .lightbox-modal.active {{
    display: flex;
  }}
  .lightbox-container {{
    max-width: 860px;
    width: 100%;
    max-height: 90vh;
    background: #fff;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: 0 25px 60px rgba(0,0,0,0.5);
    position: relative;
    display: flex;
    flex-direction: column;
    animation: modalScale 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  @keyframes modalScale {{
    from {{ transform: scale(0.94); opacity: 0; }}
    to {{ transform: scale(1); opacity: 1; }}
  }}
  .lightbox-img-wrap {{
    width: 100%;
    max-height: 52vh;
    background: #0d120f;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    flex-shrink: 0;
  }}
  .lightbox-img {{
    max-width: 100%;
    max-height: 52vh;
    object-fit: contain;
    display: block;
  }}
  .lightbox-info {{
    padding: 20px 24px;
    background: #fff;
    border-top: 1px solid var(--border-color);
    overflow-y: auto;
    flex: 1;
  }}
  .lightbox-title {{
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .lightbox-caption {{
    font-size: 0.9rem;
    color: var(--text-secondary);
    line-height: 1.55;
  }}
  .lightbox-close {{
    position: absolute;
    top: 14px;
    right: 14px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(0,0,0,0.65);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.3rem;
    border: none;
    transition: background 0.2s;
    z-index: 10;
  }}
  .lightbox-close:hover {{
    background: rgba(0,0,0,0.9);
  }}

  /* VIDEO SYSTEM MODAL */
  .video-modal {{
    position: fixed;
    inset: 0;
    background: rgba(18, 24, 21, 0.88);
    backdrop-filter: blur(12px);
    z-index: 2100;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }}
  .video-modal.active {{
    display: flex;
  }}
  .video-modal-dialog {{
    max-width: 780px;
    width: 100%;
    max-height: 92vh;
    background: #fff;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: 0 25px 65px rgba(0,0,0,0.5);
    position: relative;
    display: flex;
    flex-direction: column;
    animation: modalScale 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  .video-modal-close {{
    position: absolute;
    top: 14px;
    right: 14px;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(0,0,0,0.6);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.4rem;
    border: none;
    transition: background 0.2s;
    z-index: 20;
  }}
  .video-modal-close:hover {{
    background: rgba(0,0,0,0.9);
  }}
  .video-modal-header {{
    padding: 22px 24px 14px 24px;
    border-bottom: 1px solid var(--border-color);
    background: #fff;
  }}
  .video-modal-tags {{
    display: flex;
    gap: 8px;
    align-items: center;
    margin-bottom: 8px;
    flex-wrap: wrap;
  }}
  .video-modal-title {{
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.35;
    margin: 0;
  }}
  .video-modal-body {{
    padding: 20px 24px;
    overflow-y: auto;
    flex: 1;
  }}
  .video-preview-banner {{
    position: relative;
    width: 100%;
    height: 280px;
    border-radius: var(--radius-sm);
    overflow: hidden;
    background: #0d120f;
    margin-bottom: 20px;
  }}
  .video-preview-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease;
  }}
  .video-preview-banner:hover .video-preview-img {{
    transform: scale(1.04);
  }}
  .video-preview-overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.25) 50%, rgba(0,0,0,0.4) 100%);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 16px;
  }}
  .video-preview-play-btn {{
    align-self: center;
    margin-top: auto;
    margin-bottom: auto;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.95);
    color: var(--accent-dark);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    text-decoration: none;
    transition: all 0.25s ease;
  }}
  .video-preview-play-btn:hover {{
    transform: scale(1.15);
    background: var(--accent);
    color: #fff;
  }}
  .video-preview-cta-wrap {{
    text-align: center;
  }}
  .video-preview-fb-btn {{
    box-shadow: 0 4px 14px rgba(0,0,0,0.4);
    font-weight: 700;
  }}
  .vm-metrics-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 22px;
  }}
  .vm-metric-card {{
    background: var(--bg-card-sub);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 12px 14px;
    text-align: center;
  }}
  .vm-metric-value {{
    font-size: 1.2rem;
    font-weight: 800;
    color: var(--accent-dark);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 2px;
  }}
  .vm-metric-label {{
    font-size: 0.74rem;
    font-weight: 700;
    color: var(--text-primary);
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-bottom: 2px;
  }}
  .vm-metric-desc {{
    font-size: 0.72rem;
    color: var(--text-muted);
  }}
  .vm-analysis-section {{
    background: #faf9f6;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    padding: 18px 20px;
  }}
  .vm-section-heading {{
    font-size: 0.92rem;
    font-weight: 800;
    color: var(--accent-text);
    margin-top: 14px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }}
  .vm-section-heading:first-child {{
    margin-top: 0;
  }}
  .vm-text {{
    font-size: 0.88rem;
    color: var(--text-secondary);
    line-height: 1.6;
    margin: 0;
  }}
  .video-modal-footer {{
    padding: 16px 24px;
    background: #fff;
    border-top: 1px solid var(--border-color);
    display: flex;
    justify-content: flex-end;
  }}
  @media (max-width: 640px) {{
    .vm-metrics-grid {{
      grid-template-columns: repeat(2, 1fr);
    }}
    .video-preview-banner {{
      height: 200px;
    }}
  }}

  /* MOBILE TOGGLE & DRAWER */
  .nav-actions {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .nav-cv-btn {{
    padding: 8px 16px;
    font-size: 0.85rem;
  }}
  .brand-name {{
    font-size: 1.05rem;
    font-weight: 800;
    line-height: 1.2;
    color: var(--text-primary);
  }}
  .brand-sub {{
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.5px;
  }}
  .mobile-toggle-btn {{
    display: none;
    width: 40px;
    height: 40px;
    background: #FFFFFF;
    border: 1px solid var(--border-color);
    border-radius: var(--radius-sm);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5px;
    cursor: pointer;
    padding: 0;
    transition: all 0.2s ease;
  }}
  .mobile-toggle-btn span {{
    display: block;
    width: 20px;
    height: 2px;
    background: var(--text-primary);
    border-radius: 2px;
    transition: all 0.25s ease;
  }}
  .mobile-toggle-btn:hover {{
    background: var(--accent-soft);
    border-color: var(--accent-border);
  }}
  .mobile-toggle-btn.active span:nth-child(1) {{
    transform: translateY(7px) rotate(45deg);
  }}
  .mobile-toggle-btn.active span:nth-child(2) {{
    opacity: 0;
  }}
  .mobile-toggle-btn.active span:nth-child(3) {{
    transform: translateY(-7px) rotate(-45deg);
  }}

  .mobile-drawer {{
    position: fixed;
    inset: 0;
    z-index: 3000;
    visibility: hidden;
    pointer-events: none;
    transition: visibility 0.3s ease;
  }}
  .mobile-drawer.active {{
    visibility: visible;
    pointer-events: auto;
  }}
  .mobile-drawer-backdrop {{
    position: absolute;
    inset: 0;
    background: rgba(18, 24, 21, 0.65);
    backdrop-filter: blur(4px);
    opacity: 0;
    transition: opacity 0.3s ease;
  }}
  .mobile-drawer.active .mobile-drawer-backdrop {{
    opacity: 1;
  }}
  .mobile-drawer-content {{
    position: absolute;
    top: 0;
    right: 0;
    width: 320px;
    max-width: 86vw;
    height: 100%;
    background: #FFFFFF;
    box-shadow: -10px 0 35px rgba(0,0,0,0.18);
    display: flex;
    flex-direction: column;
    transform: translateX(100%);
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 1;
    overflow-y: auto;
  }}
  .mobile-drawer.active .mobile-drawer-content {{
    transform: translateX(0);
  }}
  .mobile-drawer-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 20px;
    border-bottom: 1px solid var(--border-color);
  }}
  .mobile-drawer-close {{
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: var(--accent-soft);
    border: none;
    font-size: 1.3rem;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }}
  .mobile-nav-list {{
    list-style: none;
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
  }}
  .mobile-nav-link {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 14px;
    border-radius: var(--radius-sm);
    color: var(--text-primary);
    font-weight: 700;
    font-size: 0.95rem;
    transition: background 0.2s ease;
    text-decoration: none;
  }}
  .mobile-nav-link:hover, .mobile-nav-link:active {{
    background: var(--accent-soft);
    color: var(--accent-dark);
  }}
  .mobile-drawer-footer {{
    padding: 18px 20px;
    border-top: 1px solid var(--border-color);
    background: var(--bg-card-sub);
  }}

  /* RESPONSIVE */
  @media (max-width: 992px) {{
    .nav-menu {{
      display: none;
    }}
    .mobile-toggle-btn {{
      display: flex;
    }}
    .hero-grid {{
      grid-template-columns: 1fr;
      text-align: center;
      gap: 32px;
    }}
    .hero-avatar-wrap {{
      order: -1;
      margin: 0 auto;
    }}
    .hero-avatar-card {{
      width: 240px;
    }}
    .hero-avatar-img {{
      height: 280px;
    }}
    .hero-desc {{
      margin: 0 auto 24px auto;
    }}
    .hero-cta-group {{
      justify-content: center;
    }}
    .hero-stats-row {{
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }}
    .evidence-grid {{
      grid-template-columns: repeat(2, 1fr);
      gap: 18px;
    }}
    .video-grid {{
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    .case-grid {{
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    .about-grid {{
      grid-template-columns: 1fr;
      gap: 16px;
    }}
    .bento-card-span2 {{
      grid-column: span 1;
    }}
    .skills-grid {{
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    .contact-card {{
      grid-template-columns: 1fr;
      padding: 30px 20px;
      gap: 28px;
    }}
  }}

  @media (max-width: 768px) {{
    .container {{
      padding: 0 16px;
    }}
    .section {{
      padding: 50px 0;
    }}
    .section-title {{
      font-size: 1.85rem;
    }}
    .section-subtitle {{
      font-size: 0.95rem;
    }}
    .section-header {{
      margin-bottom: 28px;
    }}
    .hero-title {{
      font-size: 2.1rem;
      line-height: 1.22;
    }}
    .proof-filter-bar {{
      flex-wrap: nowrap;
      overflow-x: auto;
      justify-content: flex-start;
      padding: 4px 16px 14px 16px;
      margin-left: -16px;
      margin-right: -16px;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }}
    .proof-filter-bar::-webkit-scrollbar {{
      display: none;
    }}
    .proof-tab-btn {{
      flex-shrink: 0;
      white-space: nowrap;
      font-size: 0.82rem;
      padding: 8px 14px;
    }}
  }}

  @media (max-width: 640px) {{
    .evidence-grid {{
      grid-template-columns: 1fr;
      gap: 16px;
    }}
    .hero-avatar-card {{
      width: 210px;
    }}
    .hero-avatar-img {{
      height: 250px;
    }}
    .case-card {{
      padding: 20px 16px;
    }}
    .case-title {{
      font-size: 1.15rem;
    }}
    .case-metrics-banner {{
      flex-direction: column;
      align-items: flex-start;
      gap: 6px;
    }}
    .bento-card {{
      padding: 20px 16px;
    }}
    .skill-box {{
      padding: 20px 16px;
    }}
    .video-card-body {{
      padding: 16px;
    }}
    .video-title {{
      font-size: 1.05rem;
    }}
    .footer .container > div {{
      flex-direction: column;
      text-align: center;
      gap: 12px;
    }}
    .lightbox-modal {{
      padding: 12px;
    }}
    .lightbox-container {{
      max-height: 92vh;
      border-radius: var(--radius-sm);
    }}
    .lightbox-img-wrap {{
      max-height: 38vh;
    }}
    .lightbox-img {{
      max-height: 38vh;
    }}
    .lightbox-info {{
      padding: 16px 14px;
    }}
    .lightbox-title {{
      font-size: 1rem;
    }}
    .lightbox-caption {{
      font-size: 0.82rem;
    }}
    .lightbox-close {{
      top: 10px;
      right: 10px;
      width: 32px;
      height: 32px;
      font-size: 1.1rem;
    }}
  }}

  @media (max-width: 480px) {{
    .hero-title {{
      font-size: 1.68rem;
      line-height: 1.25;
    }}
    .hero-desc {{
      font-size: 0.92rem;
    }}
    .hero-badge {{
      font-size: 0.68rem;
      padding: 5px 12px;
      letter-spacing: 0.2px;
      white-space: normal;
      line-height: 1.4;
    }}
    .hero-cta-group {{
      flex-direction: column;
      width: 100%;
      gap: 10px;
    }}
    .hero-cta-group .btn {{
      width: 100%;
      justify-content: center;
    }}
    .hero-stats-row {{
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }}
    .stat-card {{
      padding: 10px 10px;
    }}
    .stat-num {{
      font-size: 1.28rem;
    }}
    .stat-label {{
      font-size: 0.7rem;
    }}
    .stat-verified {{
      font-size: 0.64rem;
    }}
    .brand-sub {{
      display: none;
    }}
    .brand-name {{
      font-size: 0.92rem;
    }}
    .nav-cv-btn {{
      display: none;
    }}
    .contact-card {{
      padding: 22px 14px;
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
        <div class="brand-name">LÊ THỊ HOÀNG CẨM</div>
        <div class="brand-sub">MARKETING EXECUTIVE</div>
      </div>
    </a>
    <ul class="nav-menu">
      <li><a href="#evidence" class="nav-link">Minh chứng thực tế <span class="nav-badge-pill">7 Proofs</span></a></li>
      <li><a href="#videos" class="nav-link">🎬 Video đã làm <span class="nav-badge-pill" style="background:#e0f2fe; color:#0369a1;">3 Kênh</span></a></li>
      <li><a href="#projects" class="nav-link">Dự án &amp; Case Studies</a></li>
      <li><a href="#skills" class="nav-link">Kỹ năng (Kinh nghiệm &amp; Năng lực)</a></li>
      <li><a href="#contact" class="nav-link">Liên hệ</a></li>
    </ul>
    <div class="nav-actions">
      <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary nav-cv-btn">
        <span>📄 Tải CV PDF</span>
      </a>
      <button class="mobile-toggle-btn" id="mobileToggleBtn" onclick="toggleMobileMenu()" aria-label="Mở menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </div>
</nav>

<!-- MOBILE DRAWER -->
<div id="mobileDrawer" class="mobile-drawer">
  <div class="mobile-drawer-backdrop" onclick="closeMobileMenu()"></div>
  <div class="mobile-drawer-content">
    <div class="mobile-drawer-header">
      <div class="brand-logo">
        <div class="brand-badge">HC</div>
        <div>
          <div style="font-weight: 800; font-size: 0.95rem; color: var(--text-primary);">LÊ THỊ HOÀNG CẨM</div>
          <div style="font-size: 0.7rem; font-weight: 700; color: var(--accent);">MARKETING EXECUTIVE</div>
        </div>
      </div>
      <button class="mobile-drawer-close" onclick="closeMobileMenu()">&times;</button>
    </div>
    <ul class="mobile-nav-list">
      <li><a href="#evidence" onclick="closeMobileMenu()" class="mobile-nav-link">🔍 Minh chứng thực tế <span class="nav-badge-pill">7 Proofs</span></a></li>
      <li><a href="#videos" onclick="closeMobileMenu()" class="mobile-nav-link">🎬 Video đã làm <span class="nav-badge-pill" style="background:#e0f2fe; color:#0369a1;">3 Kênh</span></a></li>
      <li><a href="#projects" onclick="closeMobileMenu()" class="mobile-nav-link">💼 Dự án &amp; Case Studies</a></li>
      <li><a href="#skills" onclick="closeMobileMenu()" class="mobile-nav-link">⚡ Kỹ năng (Kinh nghiệm &amp; Năng lực)</a></li>
      <li><a href="#contact" onclick="closeMobileMenu()" class="mobile-nav-link">📞 Liên hệ ứng tuyển</a></li>
    </ul>
    <div class="mobile-drawer-footer">
      <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary" style="width: 100%; justify-content: center; font-size: 0.9rem; padding: 12px;">
        <span>📄 Tải CV Đầy Đủ (Có Ảnh &amp; SĐT)</span>
      </a>
      <a href="CV_Le_Thi_Hoang_Cam_AnDanh.pdf" target="_blank" class="btn btn-secondary" style="width: 100%; justify-content: center; font-size: 0.9rem; padding: 12px; margin-top: 10px;">
        <span>🔒 Tải Bản Ẩn Danh (Blind CV)</span>
      </a>
    </div>
  </div>
</div>

<!-- HERO SECTION -->
<section class="hero-section">
  <div class="container hero-grid">
    <div>
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        MARKETING EXECUTIVE
      </div>
      <h1 class="hero-title">
        Sáng tạo nội dung chạm <span class="highlight">insight</span>, dữ liệu chứng minh <span class="highlight">hiệu quả</span>.
      </h1>
      <p class="hero-desc">
        Hơn <strong>3 năm kinh nghiệm thực chiến</strong> bao quát từ xây dựng chiến lược Content &amp; Short-form Video (Reels, TikTok) đến tối ưu chiến dịch Paid Ads, truyền thông Healthcare &amp; FMCG. Mọi kết quả đều được kiểm chứng bằng số liệu và sản phẩm truyền thông thực tế.
      </p>
      <div class="hero-cta-group">
        <a href="#evidence" class="btn btn-primary" style="padding: 12px 24px; font-size: 0.95rem;">
          <span>🔍 Xem Minh Chứng</span>
        </a>
        <a href="#videos" class="btn btn-secondary" style="padding: 12px 22px; font-size: 0.95rem;">
          <span>🎬 Xem Video Đã Làm</span>
        </a>
        <a href="#projects" class="btn btn-outline" style="padding: 12px 20px;">
          <span>Dự án Case Studies</span>
        </a>
        <a href="tel:0363123121" class="btn btn-outline" style="padding: 12px 18px;">
          <span>📞 0363 123 121</span>
        </a>
      </div>

      <div class="hero-stats-row">
        <div class="stat-card">
          <span class="stat-num">3+ Năm</span>
          <span class="stat-label">Kinh nghiệm thực chiến</span>
          <span class="stat-verified">✓ 4 Chặng đường</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">98.4K+</span>
          <span class="stat-label">Views chiến dịch Healthcare</span>
          <span class="stat-verified">✓ Báo cáo Meta Suite</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">+880%</span>
          <span class="stat-label">Tăng trưởng tương tác Reels</span>
          <span class="stat-verified">✓ Insight 28 ngày</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">+30%</span>
          <span class="stat-label">Reach tự nhiên đa kênh</span>
          <span class="stat-verified">✓ Chiến dịch OPV Pharma</span>
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

<!-- EVIDENCE GALLERY SECTION (HÌNH ẢNH CHỨNG MINH) -->
<section id="evidence" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Hình Ảnh Chứng Minh</span>
      <h2 class="section-title">Kho Minh Chứng Năng Lực &amp; Dữ Liệu</h2>
      <p class="section-subtitle">Mỗi năng lực và kết quả đều có hình ảnh minh chứng sản phẩm sáng tạo, dashboard báo cáo và chứng chỉ xác thực.</p>
    </div>

    <!-- TAB FILTER -->
    <div class="proof-filter-bar">
      <button class="proof-tab-btn active" onclick="filterEvidence('all')">Tất cả minh chứng (7)</button>
      <button class="proof-tab-btn" onclick="filterEvidence('content')">🎬 Video &amp; KOC Review</button>
      <button class="proof-tab-btn" onclick="filterEvidence('data')">📈 Báo Cáo Dữ Liệu Ads &amp; GMV</button>
      <button class="proof-tab-btn" onclick="filterEvidence('credentials')">📜 Bằng Cấp &amp; Dịch Vụ</button>
    </div>

    <!-- 7 EVIDENCE CARDS -->
    <div class="evidence-grid">

      <!-- PROOF 1: TIKTOK SHOP AFFILIATE GMV -->
      <div class="evidence-card" data-evidence="data" onclick="openLightbox('affiliate')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">TikTok Shop Affiliate</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{affiliate_b64}" alt="Minh chứng GMV TikTok Shop Affiliate">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Dashboard Tiếp Thị Liên Kết (Affiliate)</h3>
            <p class="evidence-caption">Báo cáo thực tế ghi nhận GMV đạt 239,9M đ (+4,000%), 3.3K sản phẩm bán ra, 1.3M lượt hiển thị và 34.7K lượt click vào sản phẩm.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">💰 GMV 239,9M đ • 3,3K Đơn • 1,3M Views</span>
          </div>
        </div>
      </div>

      <!-- PROOF 2: KOC BEAUTY REVIEW -->
      <div class="evidence-card" data-evidence="content" onclick="openLightbox('koc')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">KOC Beauty Reviewer</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{koc_b64}" alt="Minh chứng video KOC Review mỹ phẩm">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Sản Phẩm Video KOC Review Đa Nền Tảng</h3>
            <p class="evidence-caption">Hợp tác cùng các nhãn hàng quốc tế L’Oréal, Vichy, Eucerin, SVR. Video đạt tỷ lệ tương tác cao với hơn 15.000 views/tháng.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">👀 15.000+ Views/tháng • 800 Profile Visits</span>
          </div>
        </div>
      </div>

      <!-- PROOF 3: MEDTV HEALTHCARE VIRAL METRICS -->
      <div class="evidence-card" data-evidence="data" onclick="openLightbox('medtv')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Báo Cáo Tăng Trưởng Meta</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{medtv_b64}" alt="Minh chứng báo cáo kênh MEDTV">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Báo Cáo Kênh MEDTV &amp; Giáo Dục Sức Khỏe</h3>
            <p class="evidence-caption">Dashboard thống kê chiến dịch B2B kết nối Comfort, ColosBaby với BV Nhi Đồng 1, BV 175. Tăng trưởng vượt bậc trong 28 ngày.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">🔥 98.474 Views • +880.5% Tương tác</span>
          </div>
        </div>
      </div>

      <!-- PROOF 3: VIDEO PRODUCTION WORKFLOW -->
      <div class="evidence-card" data-evidence="content" onclick="openLightbox('workflow')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Quy Trình Sáng Tạo Video</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{workflow_b64}" alt="Quy trình dựng video và kịch bản phân cảnh">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Kịch Bản Phân Cảnh &amp; Dựng Video CapCut Pro</h3>
            <p class="evidence-caption">Tự chủ toàn bộ quy trình: Lên ý tưởng storyboard, chuẩn bị đạo cụ quay chụp, dựng timeline video ngắn và tối ưu âm thanh.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">🎬 Quy Trình Tự Chủ 100% Media</span>
          </div>
        </div>
      </div>

      <!-- PROOF 4: OPV PHARMA FANPAGE MANAGEMENT -->
      <div class="evidence-card" data-evidence="data" onclick="openLightbox('opv')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Quản Trị Fanpage &amp; Content</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{opv_b64}" alt="Báo cáo hiệu quả Fanpage Dược phẩm OPV">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Quản Trị Fanpage &amp; Nội Dung Dược Phẩm OPV</h3>
            <p class="evidence-caption">Lập kế hoạch nội dung chuẩn Y Dược, trực tiếp quản lý và chăm sóc Fanpage OPV, thúc đẩy lượng tiếp cận tự nhiên của trang tăng 25–30%.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">🌿 Reach tự nhiên Page +30% • Follower +8%</span>
          </div>
        </div>
      </div>

      <!-- PROOF 5: DENTAL CARE CUSTOMER EXPERIENCE -->
      <div class="evidence-card" data-evidence="credentials" onclick="openLightbox('dental')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Trải Nghiệm Khách Hàng</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{dental_b64}" alt="Quy trình quản trị trải nghiệm khách hàng Nha Khoa Kim">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Quản Trị Trải Nghiệm &amp; CSKH Y Tế Nha Khoa Kim</h3>
            <p class="evidence-caption">Hệ thống đón tiếp, điều phối lịch tư vấn bác sĩ chuyên sâu và khảo sát mức độ hài lòng khách hàng đạt điểm số tối ưu.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">⭐ CSAT 4.9/5 • 90–110% KPI Chất lượng</span>
          </div>
        </div>
      </div>

      <!-- PROOF 6: CREDENTIALS & CERTIFICATES -->
      <div class="evidence-card" data-evidence="credentials" onclick="openLightbox('credentials')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Bằng Cấp &amp; Chứng Chỉ</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{credentials_b64}" alt="Chứng chỉ TOEIC và Tin học MOS">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Chứng Chỉ Chuyên Môn &amp; Học Vấn Đại Học</h3>
            <p class="evidence-caption">TOEIC Speaking &amp; Writing (06/2024), Tin học văn phòng MOS (06/2023) và Cử nhân Thông Tin – Thư Viện Trường ĐH Sài Gòn.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">📜 TOEIC Quốc Tế • MOS Master • ĐH Sài Gòn</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- FEATURED VIDEOS & CHANNELS (VIDEO THỰC TẾ) -->
<section id="videos" class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-tag" style="background: #e0f2fe; color: #0369a1; border-color: #bae6fd;">Sản Phẩm Video Thực Tế</span>
      <h2 class="section-title">Video &amp; Kênh Truyền Thông Đã Thực Hiện</h2>
      <p class="section-subtitle">Trực tiếp xem các sản phẩm video ngắn, phóng sự y tế và chiến dịch truyền thông đa kênh do Hoàng Cẩm lên kịch bản, quay dựng và trực tiếp quản trị.</p>
    </div>

    <div class="video-grid">
      <!-- VIDEO 1: THÂN TÂM HOME HEALTHCARE (KÊNH QUẢN TRỊ CHÍNH) -->
      <div class="video-card">
        <div onclick="openVideoModal('than_tam')" class="video-thumb" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">
          <img src="data:image/jpeg;base64,{workflow_b64}" alt="Kênh Thân Tâm Chăm sóc sức khỏe tại nhà" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">🩺 Kênh Quản Trị Chính • Y Tế Tại Nhà</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem chi tiết &amp; video ↗</div>
          </div>
        </div>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill" style="background:#e0f2fe; color:#0369a1;">Facebook Video • Kênh Quản Trị Chính</span>
              <span class="video-hospital-tag">📍 TP. Hồ Chí Minh</span>
            </div>
            <h3 onclick="openVideoModal('than_tam')" class="video-card-title" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">Thân Tâm — Chăm Sóc Sức Khỏe &amp; Người Cao Tuổi</h3>
            <p class="video-card-desc">
              Kênh truyền thông y tế gia đình trực tiếp quản lý và tự chủ 100% quy trình sản xuất media: Lên kịch bản storyboard, thu âm mic Rode, dựng CapCut Pro hướng dẫn điều dưỡng chuyên sâu tại nhà.
            </p>
          </div>
          <div>
            <button type="button" onclick="openVideoModal('than_tam')" class="btn btn-primary" style="width: 100%; justify-content: center; padding: 12px 16px; font-size: 0.88rem; font-weight: 700; border-radius: 9999px; cursor: pointer;">
              <span>▶ Xem Video Kênh Thân Tâm trên Facebook ↗</span>
            </button>
          </div>
        </div>
      </div>

      <!-- VIDEO 2: MEDDC TRUYỀN THÔNG SỐ BỆNH VIỆN (KÊNH MỚI KHỞI TẠO) -->
      <div class="video-card">
        <div onclick="openVideoModal('medtv')" class="video-thumb" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">
          <img src="data:image/jpeg;base64,{meddc_cover_b64}" alt="Kênh MEDDC Truyền thông số Bệnh viện" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">🏥 Kênh Mới Khởi Tạo • 98.4K+ Views</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem chi tiết &amp; video ↗</div>
          </div>
        </div>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill">Facebook Video • Dự Án Mới Khởi Tạo</span>
              <span class="video-hospital-tag">🏥 BV Nhi Đồng 1 &amp; BV 175</span>
            </div>
            <h3 onclick="openVideoModal('medtv')" class="video-card-title" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">Kênh MEDDC — Truyền Thông Số Bệnh Viện (Mới Khởi Tạo)</h3>
            <p class="video-card-desc">
              Kênh mới được thành lập khi tham gia dự án, kết nối các nhãn hàng quốc tế (Comfort, ColosBaby, Gaviscon...) với bệnh viện đầu ngành qua chuỗi Reels giáo dục sức khỏe đạt 98.4K+ views.
            </p>
          </div>
          <div>
            <button type="button" onclick="openVideoModal('medtv')" class="btn btn-primary" style="width: 100%; justify-content: center; padding: 12px 16px; font-size: 0.88rem; font-weight: 700; border-radius: 9999px; cursor: pointer;">
              <span>▶ Xem Video Kênh MEDDC trên Facebook ↗</span>
            </button>
          </div>
        </div>
      </div>

      <!-- VIDEO 3: OPV PHARMACEUTICAL -->
      <div class="video-card">
        <div onclick="openVideoModal('opv')" class="video-thumb" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">
          <img src="data:image/jpeg;base64,{opv_b64}" alt="Kênh Dược phẩm OPV Pharmaceutical" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">🌿 21.6K+ Followers • Reach Page +30%</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem chi tiết &amp; video ↗</div>
          </div>
        </div>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill">Facebook Media • Quản Trị Fanpage</span>
              <span class="video-hospital-tag">🌿 OPV Pharmaceutical</span>
            </div>
            <h3 onclick="openVideoModal('opv')" class="video-card-title" style="cursor: pointer;" title="Bấm mở popup chi tiết video &amp; hệ thống">OPV Pharmaceutical — Video &amp; Quản Trị Kênh Fanpage</h3>
            <p class="video-card-desc">
              Quản trị Fanpage OPV, biên tập nội dung bài viết và video ngắn chuẩn SEO y dược, chăm sóc tương tác cộng đồng và duy trì lượng tiếp cận tự nhiên ổn định cho trang.
            </p>
          </div>
          <div>
            <button type="button" onclick="openVideoModal('opv')" class="btn btn-primary" style="width: 100%; justify-content: center; padding: 12px 16px; font-size: 0.88rem; font-weight: 700; border-radius: 9999px; cursor: pointer;">
              <span>▶ Xem Chi Tiết Kênh Fanpage OPV ↗</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PROJECTS & CASE STUDIES -->
<section id="projects" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Case Studies Trọng Điểm</span>
      <h2 class="section-title">Dự Án Đã Triển Khai</h2>
      <p class="section-subtitle">Tóm tắt ngắn gọn mục tiêu, hành động thực thi và số liệu kết quả của từng chiến dịch.</p>
    </div>

    <div class="case-grid">

      <!-- PROJECT 1 -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('koc')">
          <img class="case-media-img" src="data:image/jpeg;base64,{koc_b64}" alt="Case study KOC Beauty Reviewer">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">Beauty &amp; Influencer KOC</span>
            <span class="case-timeline">09/2024 – Hiện tại</span>
          </div>
          <h3 class="case-title" onclick="openVideoModal('koc')" title="Bấm xem chi tiết dự án KOC">Sáng Tạo Nội Dung Đa Nền Tảng &amp; KOC Reviewer</h3>
          <div class="case-brands">✨ L’Oréal • Vichy • Eucerin • SVR</div>
          <ul class="case-bullets">
            <li>Tự chủ 100% quy trình từ ý tưởng, kịch bản, quay chụp đến dựng video ngắn review mỹ phẩm chuẩn visual cao cấp.</li>
            <li>Hợp tác nhận PR kit, sản xuất video trải nghiệm sản phẩm theo brief nhãn hàng và tham gia sự kiện ra mắt độc quyền.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">👀 Views trung bình: <strong class="metric-badge">15.000 / tháng (+30%)</strong></span>
            <span class="metric-item">👤 Profile Visits: <strong class="metric-badge">800 lượt (+20%)</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <button type="button" onclick="openVideoModal('koc')" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>▶ Xem Chi Tiết Dự Án KOC</span>
            </button>
            <button type="button" onclick="openLightbox('koc')" class="btn btn-outline" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>🔍 Phóng To Minh Chứng</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PROJECT 2: THÂN TÂM HOME HEALTHCARE (KÊNH QUẢN TRỊ CHÍNH) -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('workflow')">
          <img class="case-media-img" src="data:image/jpeg;base64,{workflow_b64}" alt="Case study Kênh Thân Tâm Y Tế Gia Đình">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag" style="background:#e0f2fe; color:#0369a1;">Home Healthcare • Kênh Quản Trị Chính</span>
            <span class="case-timeline">06/2025 – Hiện tại</span>
          </div>
          <h3 class="case-title" onclick="openVideoModal('than_tam')" title="Bấm xem chi tiết video Thân Tâm">Kênh Thân Tâm — Chăm Sóc Sức Khỏe &amp; Người Cao Tuổi</h3>
          <div class="case-brands">🩺 Dịch Vụ Điều Dưỡng &amp; Y Tế Gia Đình (TP. Hồ Chí Minh)</div>
          <ul class="case-bullets">
            <li><strong>Kênh quản trị chính:</strong> Trực tiếp vận hành kênh và tự chủ 100% quy trình sản xuất media: Lên kịch bản storyboard, thu âm mic Rode, dựng CapCut Pro tái hiện quy trình chăm sóc y tế tại gia.</li>
            <li><strong>Tác động:</strong> Minh bạch hóa thao tác điều dưỡng giúp xóa bỏ rào cản tâm lý của thân nhân, nâng cao uy tín thương hiệu dịch vụ chăm sóc tại gia và tăng trưởng tỷ lệ inbox tư vấn đặt lịch.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">🩺 Kênh: <strong class="metric-badge">Quản Trị Chính</strong></span>
            <span class="metric-item">🎬 Quy trình: <strong class="metric-badge">Tự chủ 100% Media</strong></span>
            <span class="metric-item">📍 Địa bàn: <strong class="metric-badge">TP. Hồ Chí Minh</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <button type="button" onclick="openVideoModal('than_tam')" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>▶ Xem Chi Tiết Video Thân Tâm</span>
            </button>
            <button type="button" onclick="openLightbox('workflow')" class="btn btn-outline" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>🎬 Xem Minh Chứng Quy Trình</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PROJECT 3: MEDDC TRUYỀN THÔNG SỐ BỆNH VIỆN (KÊNH MỚI KHỞI TẠO) -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('meddc_cover')">
          <img class="case-media-img" src="data:image/jpeg;base64,{meddc_cover_b64}" alt="Cover Kênh MEDDC Giáo Dục Sức Khỏe">
          <div class="case-media-overlay">🔍 Bấm xem ảnh Cover MEDDC</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">B2B Healthcare • Kênh Mới Khởi Tạo</span>
            <span class="case-timeline">03/2026 – 09/2026</span>
          </div>
          <h3 class="case-title" onclick="openVideoModal('medtv')" title="Bấm xem chi tiết video MEDDC">Kênh MEDDC — Truyền Thông Số Bệnh Viện (Mới Khởi Tạo)</h3>
          <div class="case-brands">🏥 Comfort • ColosBaby • Gaviscon x BV Nhi Đồng 1, BV 175</div>
          <ul class="case-bullets">
            <li><strong>Dự án mới:</strong> Kênh mới thành lập khi tham gia dự án, kết nối nhãn hàng quốc tế với các bệnh viện đầu ngành qua chuỗi Reels giáo dục sức khỏe.</li>
            <li><strong>Thực thi &amp; Kết quả:</strong> Xây dựng chuỗi Reels giáo dục sức khỏe đạt tốc độ viral tự nhiên cao, tiếp cận 98.4K+ lượt xem và tương tác tăng trưởng +880.5%.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">🔥 Video Views: <strong class="metric-badge">98.474 lượt</strong></span>
            <span class="metric-item">📈 Tương tác: <strong class="metric-badge">+880.5%</strong></span>
            <span class="metric-item">👥 Followers: <strong class="metric-badge">+547% trong 28 ngày</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <button type="button" onclick="openVideoModal('medtv')" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>▶ Xem Chi Tiết Video Kênh MEDDC</span>
            </button>
            <button type="button" onclick="openLightbox('medtv')" class="btn btn-outline" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>📈 Xem Báo Cáo Tăng Trưởng</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PROJECT 4: OPV PHARMACEUTICAL -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('opv')">
          <img class="case-media-img" src="data:image/jpeg;base64,{opv_b64}" alt="Case study Dược phẩm OPV">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">Pharma Marketing &amp; Fanpage Management</span>
            <span class="case-timeline">12/2024 – 02/2026</span>
          </div>
          <h3 class="case-title" onclick="openVideoModal('opv')" title="Bấm xem chi tiết dự án OPV">Quản Trị Fanpage &amp; Kế Hoạch Content Dược Phẩm</h3>
          <div class="case-brands">💊 Công ty Cổ phần Dược phẩm OPV</div>
          <ul class="case-bullets">
            <li>Lập kế hoạch nội dung định kỳ và biên soạn bài viết, kịch bản video chuẩn SEO Y Dược theo đúng quy định truyền thông Dược phẩm.</li>
            <li>Trực tiếp quản lý và chăm sóc Fanpage OPV, tương tác cộng đồng người theo dõi, phối hợp cùng Designer sản xuất tư liệu và theo dõi báo cáo trang.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">🚀 Tiếp cận tự nhiên: <strong class="metric-badge">+25 – 30%</strong></span>
            <span class="metric-item">👥 Tăng trưởng người theo dõi: <strong class="metric-badge">Từ 2-3% lên 7-8%</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <button type="button" onclick="openVideoModal('opv')" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>▶ Xem Chi Tiết Kênh Fanpage OPV</span>
            </button>
            <button type="button" onclick="openLightbox('opv')" class="btn btn-outline" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>📈 Phóng To Báo Cáo Page</span>
            </button>
          </div>
        </div>
      </div>

      <!-- PROJECT 5: NHA KHOA KIM -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('dental')">
          <img class="case-media-img" src="data:image/jpeg;base64,{dental_b64}" alt="Case study Nha Khoa Kim">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">Customer Experience &amp; Care</span>
            <span class="case-timeline">06/2024 – 12/2024</span>
          </div>
          <h3 class="case-title" onclick="openLightbox('dental')" title="Bấm xem báo cáo CSAT Nha Khoa Kim">Tối Ưu Trải Nghiệm &amp; Quản Trị Thông Tin Dịch Vụ</h3>
          <div class="case-brands">🦷 Hệ thống Nha Khoa Kim</div>
          <ul class="case-bullets">
            <li>Tư vấn chu đáo quy trình và liệu trình nha khoa chuyên sâu, quản lý tệp thông tin và điều phối đón tiếp cùng bác sĩ.</li>
            <li>Rút ngắn thời gian chờ khám, tạo trải nghiệm ân cần, nâng cao tỷ lệ khách hàng an tâm tiếp tục liệu trình.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">⭐ Tiếp đón &amp; Chăm sóc: <strong class="metric-badge">10 – 15 khách/ngày</strong></span>
            <span class="metric-item">🎯 KPI chất lượng dịch vụ: <strong class="metric-badge">90 – 110%</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <button type="button" onclick="openLightbox('dental')" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem; cursor: pointer;">
              <span>⭐ Xem Báo Cáo Trải Nghiệm CSAT 4.9/5</span>
            </button>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- SKILLS SYSTEM: KINH NGHIỆM & NĂNG LỰC THỰC CHIẾN -->
<section id="skills" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Hồ Sơ Chuyên Môn</span>
      <h2 class="section-title">Kỹ Năng: Kinh Nghiệm &amp; Năng Lực</h2>
      <p class="section-subtitle">Kỹ năng vững vàng được minh chứng qua Hành trình Kinh nghiệm thực tế kết hợp Hệ thống Năng lực chuyên môn toàn diện.</p>
    </div>

    <!-- BỐ CỤC CHIA LÀM: KINH NGHIỆM VÀ NĂNG LỰC -->
    <div class="skills-dual-grid">

      <!-- CỘT 1: KINH NGHIỆM THỰC CHIẾN -->
      <div class="skills-dual-col">
        <div class="skills-dual-col-header">
          <div class="skills-dual-icon">💼</div>
          <div>
            <div class="skills-dual-badge">Hành Trình Thực Tế</div>
            <h3 class="skills-dual-title">Kinh Nghiệm Làm Việc</h3>
          </div>
        </div>

        <div class="dual-timeline-wrap">
          <!-- EXP 1 -->
          <div class="dual-timeline-item">
            <div class="dual-timeline-dot"></div>
            <div class="dual-timeline-card">
              <div class="dual-timeline-top">
                <span class="dual-timeline-role">Content Creator &amp; KOC Reviewer</span>
                <span class="dual-timeline-date">09/2024 – HIỆN TẠI</span>
              </div>
              <div class="dual-timeline-company">Độc Lập • Hợp tác: L’Oréal • Vichy • Eucerin • SVR</div>
              <p class="dual-timeline-desc">
                Creator &amp; KOC là một: Tự chủ kịch bản, quay dựng video ngắn review mỹ phẩm trên iPhone; hợp tác nhận PR kit cùng các nhãn hàng da liễu; duy trì 15.000+ views/tháng và vận hành Affiliate TikTok Shop đạt GMV 239M đ.
              </p>
            </div>
          </div>

          <!-- EXP 2 -->
          <div class="dual-timeline-item">
            <div class="dual-timeline-dot"></div>
            <div class="dual-timeline-card">
              <div class="dual-timeline-top">
                <span class="dual-timeline-role">Chuyên viên Content &amp; Quản Trị Kênh</span>
                <span class="dual-timeline-date">03/2026 – 09/2026</span>
              </div>
              <div class="dual-timeline-company">Công ty TNHH Đào tạo &amp; Chăm sóc Sức khỏe Thân Tâm</div>
              <p class="dual-timeline-desc">
                Trực tiếp quản lý và tự chủ 100% media cho kênh chính Thân Tâm (Y tế tại nhà); đồng thời tham gia khởi tạo và phát triển kênh mới MEDDC (dự án truyền thông số kết nối BV Nhi Đồng 1, BV 175); đạt 98.4K lượt xem và tương tác tăng +880.5%.
              </p>
            </div>
          </div>

          <!-- EXP 3 -->
          <div class="dual-timeline-item">
            <div class="dual-timeline-dot"></div>
            <div class="dual-timeline-card">
              <div class="dual-timeline-top">
                <span class="dual-timeline-role">Chuyên viên Content &amp; Quản Trị Fanpage</span>
                <span class="dual-timeline-date">12/2024 – 02/2026</span>
              </div>
              <div class="dual-timeline-company">Công ty Cổ phần Dược phẩm OPV</div>
              <p class="dual-timeline-desc">
                Lập kế hoạch nội dung chuẩn SEO y dược, trực tiếp quản lý và chăm sóc Fanpage OPV; tối ưu tương tác cộng đồng giúp độ tiếp cận tự nhiên (Reach) của trang tăng 25–30%. (Không phụ trách Brand Mkt).
              </p>
            </div>
          </div>

          <!-- EXP 4 -->
          <div class="dual-timeline-item">
            <div class="dual-timeline-dot"></div>
            <div class="dual-timeline-card">
              <div class="dual-timeline-top">
                <span class="dual-timeline-role">Chuyên viên Chăm sóc &amp; Trải nghiệm Khách hàng</span>
                <span class="dual-timeline-date">06/2024 – 12/2024</span>
              </div>
              <div class="dual-timeline-company">Hệ thống Nha Khoa Kim</div>
              <p class="dual-timeline-desc">
                Tư vấn liệu trình chuyên sâu, điều phối đón tiếp 10–15 khách/ngày cùng bác sĩ, duy trì 90–110% KPI chất lượng dịch vụ và CSAT 4.9/5 sao.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- CỘT 2: NĂNG LỰC CỐT LÕI & CÔNG CỤ -->
      <div class="skills-dual-col">
        <div class="skills-dual-col-header">
          <div class="skills-dual-icon">⭐</div>
          <div>
            <div class="skills-dual-badge">Thế Mạnh &amp; Kỹ Thuật</div>
            <h3 class="skills-dual-title">Năng Lực &amp; Bộ Kỹ Năng</h3>
          </div>
        </div>

        <!-- 5 THẾ MẠNH CỐT LÕI -->
        <div class="competency-item">
          <div class="competency-item-top">
            <span class="competency-item-icon">💡</span>
            <h4 class="competency-item-title">Chiến Lược Content Dựa Trên Dữ Liệu &amp; Insight</h4>
          </div>
          <p class="competency-item-desc">
            Cử nhân ĐH Sài Gòn với tư duy cấu trúc thông tin khoa học, phân tích sâu hành vi độc giả để sáng tạo nội dung có tính chuyển đổi cao.
          </p>
        </div>

        <div class="competency-item">
          <div class="competency-item-top">
            <span class="competency-item-icon">🏥</span>
            <h4 class="competency-item-title">Am Hiểu Y Dược &amp; Dược Mỹ Phẩm (Healthcare &amp; FMCG)</h4>
          </div>
          <p class="competency-item-desc">
            Nắm vững quy chuẩn truyền thông y tế, thấu hiểu tâm lý phụ huynh, bệnh nhân và kết nối thông điệp tài trợ nhãn hàng B2B.
          </p>
        </div>

        <div class="competency-item">
          <div class="competency-item-top">
            <span class="competency-item-icon">🎬</span>
            <h4 class="competency-item-title">Tự Chủ Sản Xuất Short-form Video Độc Lập</h4>
          </div>
          <p class="competency-item-desc">
            Trọn gói từ ý tưởng Hook 3 giây, storyboard, quay trên iPhone, mic thu âm Rode đến dựng hậu kỳ CapCut Pro.
          </p>
        </div>

        <div class="competency-item">
          <div class="competency-item-top">
            <span class="competency-item-icon">📊</span>
            <h4 class="competency-item-title">Vận Hành &amp; Đo Lường Paid-Ads Đa Kênh</h4>
          </div>
          <p class="competency-item-desc">
            Thành thạo Meta Ads, TikTok Ads, Meta Suite; đọc hiểu dữ liệu CPC, CPM, CTR và A/B testing tối ưu chi phí.
          </p>
        </div>

        <div class="competency-item">
          <div class="competency-item-top">
            <span class="competency-item-icon">🤝</span>
            <h4 class="competency-item-title">Quản Trị Trải Nghiệm Khách Hàng Đa Điểm Chạm</h4>
          </div>
          <p class="competency-item-desc">
            Kinh nghiệm CSKH Nha Khoa Kim giúp đặt sự ân cần và thấu hiểu khách hàng làm trọng tâm cho mọi chiến dịch truyền thông.
          </p>
        </div>

        <!-- MARKETING SKILLS PILLS -->
        <div class="dual-skill-box">
          <h4 class="dual-skill-box-title">🎯 Kỹ Năng Marketing Chuyên Môn</h4>
          <div class="skill-pill-list">
            <span class="skill-pill">✍️ <strong>Content Strategy</strong></span>
            <span class="skill-pill">🎬 <strong>Short-form Video</strong></span>
            <span class="skill-pill">📈 <strong>Paid-Ads Meta &amp; TikTok</strong></span>
            <span class="skill-pill">🔍 <strong>SEO Y Dược</strong></span>
            <span class="skill-pill">🤝 <strong>B2B Healthcare Media</strong></span>
            <span class="skill-pill">👥 <strong>KOC / Influencer Collab</strong></span>
            <span class="skill-pill">💖 <strong>Customer Experience CSAT</strong></span>
          </div>
        </div>

        <!-- TOOLS & AI PILLS -->
        <div class="dual-skill-box" style="margin-top: 14px; padding-top: 14px;">
          <h4 class="dual-skill-box-title">💻 Hệ Sinh Thái Công Cụ &amp; GenAI</h4>
          <div class="skill-pill-list">
            <span class="skill-pill">✨ <strong>CapCut Pro</strong></span>
            <span class="skill-pill">🎨 <strong>Canva Pro</strong></span>
            <span class="skill-pill">🤖 <strong>Gemini &amp; ChatGPT</strong></span>
            <span class="skill-pill">📊 <strong>Meta Business Suite</strong></span>
            <span class="skill-pill">📱 <strong>TikTok Creator Hub</strong></span>
            <span class="skill-pill">🖌️ <strong>Photoshop &amp; Premiere</strong></span>
            <span class="skill-pill">📑 <strong>Google Docs &amp; Sheets</strong></span>
          </div>
        </div>

      </div>

    </div>
  </div>
</section>

<!-- CONTACT SECTION -->
<section id="contact" class="section">
  <div class="container">
    <div class="contact-card">
      <div>
        <span class="section-tag">Kết Nối Ứng Tuyển</span>
        <h2 class="contact-title">Sẵn Sàng Đồng Hành Cùng Đội Ngũ Của Bạn</h2>
        <p class="contact-desc">
          Nếu doanh nghiệp của bạn đang cần một Marketing Executive sáng tạo, vững dữ liệu và sẵn sàng lăn xả triển khai, hãy liên hệ ngay với mình nhé!
        </p>
        <ul class="contact-info-list">
          <li class="contact-info-item">
            <div class="contact-info-icon">📞</div>
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">Điện thoại liên hệ:</div>
              <a href="tel:0363123121" style="color: var(--accent-dark); font-weight: 700; font-size: 1.05rem;">0363 123 121</a>
            </div>
          </li>
          <li class="contact-info-item">
            <div class="contact-info-icon">✉️</div>
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">Email công việc:</div>
              <a href="mailto:lethihoangcam5@gmail.com" style="color: var(--accent-dark); font-weight: 700; font-size: 1.05rem;">lethihoangcam5@gmail.com</a>
            </div>
          </li>
          <li class="contact-info-item">
            <div class="contact-info-icon">📍</div>
            <div>
              <div style="font-size: 0.78rem; color: var(--text-muted);">Khu vực làm việc:</div>
              <span style="font-weight: 600;">Bình Tân, TP. Hồ Chí Minh (Sẵn sàng Onsite hoặc Hybrid)</span>
            </div>
          </li>
        </ul>
      </div>

      <div class="contact-actions-box">
        <h3 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-bottom: 6px;">Tải Hồ Sơ Tuyển Dụng PDF</h3>
        <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 16px;">
          Bản in ấn A4 chuẩn chỉnh, rõ ràng, tiện lợi cho việc lưu trữ và xem xét nội bộ:
        </p>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary" style="padding: 12px; font-size: 0.95rem;">
            <span>📄 Tải CV Đầy Đủ (Có Ảnh &amp; SĐT)</span>
          </a>
          <a href="CV_Le_Thi_Hoang_Cam_AnDanh.pdf" target="_blank" class="btn btn-secondary" style="padding: 12px; font-size: 0.95rem;">
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
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
      <div>
        <strong>Lê Thị Hoàng Cẩm</strong> — Marketing Executive • Content &amp; Digital Marketing
      </div>
      <div>
        Hồ sơ trực tuyến kết hợp minh chứng thực tế &amp; số liệu xác thực.
      </div>
      <div>
        <a href="#" style="color: #9EC0A7; font-weight: 700;">↑ Về đầu trang</a>
      </div>
    </div>
  </div>
</footer>

<!-- VIDEO DETAIL MODAL (POPUP HỆ THỐNG) -->
<div id="videoModal" class="video-modal" onclick="closeVideoModal(event)">
  <div class="video-modal-dialog" onclick="event.stopPropagation()">
    <button class="video-modal-close" onclick="closeVideoModalDirect()">&times;</button>
    
    <!-- MODAL HEADER -->
    <div class="video-modal-header">
      <div class="video-modal-tags">
        <span id="vmCategory" class="video-source-pill"></span>
        <span id="vmPartner" class="video-hospital-tag"></span>
      </div>
      <h3 id="vmTitle" class="video-modal-title"></h3>
    </div>

    <!-- MODAL BODY -->
    <div class="video-modal-body">
      <!-- VIDEO PREVIEW BANNER -->
      <div class="video-preview-banner">
        <img id="vmThumb" src="" alt="Video Preview" class="video-preview-img">
        <div class="video-preview-overlay">
          <span id="vmBadge" class="video-badge-views"></span>
          <a id="vmPlayBtn" href="#" target="_blank" rel="noopener noreferrer" class="video-preview-play-btn" title="Phát Video trên Facebook">
            ▶
          </a>
          <div class="video-preview-cta-wrap">
            <a id="vmFbBannerLink" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-primary video-preview-fb-btn">
              <span>▶ Bấm Mở Xem Video Trực Tiếp Trên Facebook ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- METRICS GRID -->
      <div class="vm-metrics-grid" id="vmMetricsGrid"></div>

      <!-- STRATEGIC ANALYSIS DETAILS -->
      <div class="vm-analysis-section">
        <h4 class="vm-section-heading">🎯 Bối Cảnh &amp; Insight Chiến Dịch</h4>
        <p id="vmInsight" class="vm-text"></p>

        <h4 class="vm-section-heading" style="margin-top: 14px;">🎬 Quy Trình Sản Xuất &amp; Thực Thi Media</h4>
        <p id="vmExecution" class="vm-text"></p>

        <h4 class="vm-section-heading" style="margin-top: 14px;">📈 Tác Động Định Lượng &amp; Giá Trị Chuyển Đổi</h4>
        <p id="vmImpact" class="vm-text"></p>
      </div>
    </div>

    <!-- MODAL FOOTER -->
    <div class="video-modal-footer">
      <div style="display: flex; gap: 10px; width: 100%; flex-wrap: wrap;">
        <a id="vmFooterFbBtn" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="flex: 2; min-width: 200px; padding: 12px; font-size: 0.92rem; text-align: center;">
          <span>▶ Mở Xem Video Trên Facebook ↗</span>
        </a>
        <button id="vmProofBtn" onclick="" class="btn btn-outline" style="flex: 1; min-width: 160px; padding: 12px; font-size: 0.92rem;">
          <span>🔍 Phóng To Báo Cáo</span>
        </button>
        <button onclick="closeVideoModalDirect()" class="btn btn-secondary" style="padding: 12px 20px; font-size: 0.92rem;">
          <span>Đóng</span>
        </button>
      </div>
    </div>
  </div>
</div>

<!-- LIGHTBOX MODAL -->
<div id="lightboxModal" class="lightbox-modal" onclick="closeLightbox(event)">
  <div class="lightbox-container" onclick="event.stopPropagation()">
    <button class="lightbox-close" onclick="closeLightboxDirect()">&times;</button>
    <div class="lightbox-img-wrap">
      <img id="lightboxImg" class="lightbox-img" src="" alt="Minh chứng phóng to">
    </div>
    <div class="lightbox-info">
      <div id="lightboxTitle" class="lightbox-title"></div>
      <div id="lightboxCaption" class="lightbox-caption"></div>
    </div>
  </div>
</div>

<script>
  // Video Modal System Data
  const videoModalData = {{
    koc: {{
      title: "Sáng Tạo Nội Dung Đa Nền Tảng &amp; KOC Reviewer",
      category: "Short-form Video • Beauty &amp; Skincare KOC",
      partner: "✨ L’Oréal • Vichy • Eucerin • SVR",
      badge: "✨ 15.000+ Views/tháng • 800+ Profile Visits",
      thumb: "data:image/jpeg;base64,{koc_b64}",
      fbUrl: "https://www.tiktok.com",
      proofKey: "koc",
      proofBtnText: "🔍 Phóng To Minh Chứng KOC &amp; Đơn Hàng",
      metrics: [
        {{ value: "15.000+", label: "Views trung bình/tháng", desc: "Tăng trưởng +30%" }},
        {{ value: "800+", label: "Profile Visits", desc: "Tăng trưởng +20%" }},
        {{ value: "4 Brand", label: "Hợp tác nhãn hàng", desc: "L'Oréal, Vichy, Eucerin..." }},
        {{ value: "100%", label: "Tự chủ media", desc: "Ý tưởng, quay dựng iPhone" }}
      ],
      insight: "Người xem mỹ phẩm hiện đại rất nhạy cảm với quảng cáo; họ tìm kiếm những video chân thật, quay cận chất kem, đánh giá thẳng thắn hiệu quả và bảng thành phần lành tính.",
      execution: "Tự chủ 100% quy trình sản xuất video trên iPhone: Lên kịch bản Hook 3 giây, quay cận cảnh kết cấu mỹ phẩm với ánh sáng tự nhiên, thu âm giọng đọc truyền cảm và dựng CapCut Pro bắt nhịp trending.",
      impact: "Được các nhãn hàng dược mỹ phẩm uy tín gửi PR kit trải nghiệm sản phẩm, đạt mức độ tương tác cao và chuyển đổi đơn hàng vượt trội qua TikTok Shop Affiliate."
    }},
    medtv: {{
      title: "Kênh MEDDC — Truyền Thông Số Bệnh Viện (MEDTV)",
      category: "Facebook Video • B2B Healthcare",
      partner: "🏥 BV Nhi Đồng 1 &amp; BV 175",
      badge: "🔥 98.4K+ Views • +880% Tương tác",
      thumb: "data:image/jpeg;base64,{meddc_cover_b64}",
      fbUrl: "https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr",
      proofKey: "medtv",
      proofBtnText: "📈 Xem Báo Cáo Tăng Trưởng Meta",
      metrics: [
        {{ value: "98.474", label: "Lượt xem video", desc: "Reels giáo dục y tế" }},
        {{ value: "+880.5%", label: "Tăng tương tác", desc: "Bình luận &amp; Chia sẻ" }},
        {{ value: "+547%", label: "Followers mới", desc: "Trong 28 ngày" }},
        {{ value: "3+ Brand", label: "Nhãn hàng B2B", desc: "Comfort, ColosBaby..." }}
      ],
      insight: "Thông tin y tế thường khô khan; phụ huynh và người bệnh rất cần kiến thức nhi khoa chuẩn xác, dễ hiểu từ bác sĩ đầu ngành. Nhãn hàng quốc tế cần một kênh truyền thông uy tín, có bảo chứng chuyên môn y tế để tài trợ nội dung B2B.",
      execution: "Biên soạn kịch bản Reels ngắn 45–60 giây, tối ưu Hook 3 giây đầu giữ chân khán giả; lồng ghép tự nhiên thông điệp nhãn hàng với lời khuyên bác sĩ BV Nhi Đồng 1 &amp; BV 175; trực tiếp quản trị và tracking hiệu suất trên Meta Suite.",
      impact: "Xây dựng định vị kênh truyền thông y tế hàng đầu; tạo dựng niềm tin bền vững giữa bệnh viện, chuyên gia y tế, nhãn hàng tài trợ và cộng đồng phụ huynh."
    }},
    than_tam: {{
      title: "Thân Tâm — Chăm Sóc Sức Khỏe &amp; Người Cao Tuổi",
      category: "Facebook Video • Y Tế Gia Đình &amp; Home Care",
      partner: "📍 TP. Hồ Chí Minh (Dịch Vụ Điều Dưỡng)",
      badge: "🩺 Chăm Sóc Sức Khỏe Tại Nhà",
      thumb: "data:image/jpeg;base64,{workflow_b64}",
      fbUrl: "https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr",
      proofKey: "workflow",
      proofBtnText: "🎬 Xem Minh Chứng Quy Trình",
      metrics: [
        {{ value: "100%", label: "Tự chủ quy trình", desc: "Sản xuất Media" }},
        {{ value: "Storyboard", label: "Kịch bản phân cảnh", desc: "Chuẩn chỉ từng shot" }},
        {{ value: "Rode Mic", label: "Thu âm chuyên dụng", desc: "Âm thanh trong trẻo" }},
        {{ value: "TP.HCM", label: "Địa bàn phục vụ", desc: "Toàn khu vực thành phố" }}
      ],
      insight: "Dịch vụ điều dưỡng và y tế gia đình tại nhà đòi hỏi niềm tin tuyệt đối. Rào cản lớn nhất của con cái khi thuê người chăm sóc cha mẹ già là lo ngại về sự an toàn và tay nghề chuyên môn của điều dưỡng viên.",
      execution: "Tự chủ 100% quy trình sản xuất media: Phác thảo storyboard kịch bản phân cảnh chi tiết, thiết lập mic thu âm Rode Wireless, biên tập dựng timeline CapCut Pro; sản xuất chuỗi video ngắn hướng dẫn chăm sóc y tế tại gia và giải đáp quy trình điều dưỡng chuyên sâu.",
      impact: "Minh bạch hóa thao tác điều dưỡng giúp xóa tan hoài nghi của thân nhân, nâng cao uy tín thương hiệu dịch vụ chăm sóc tại gia chuẩn mực và tăng trưởng tỷ lệ inbox tư vấn đặt lịch dịch vụ tại TP.HCM."
    }},
    opv: {{
      title: "OPV Pharmaceutical — Video &amp; Quản Trị Kênh Fanpage",
      category: "Facebook Media • Quản Trị Fanpage Dược Phẩm",
      partner: "🌿 OPV Pharmaceutical",
      badge: "🌿 21.6K+ Followers • Reach Page +30%",
      thumb: "data:image/jpeg;base64,{opv_b64}",
      fbUrl: "https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr",
      proofKey: "opv",
      proofBtnText: "📈 Phóng To Báo Cáo Tăng Trưởng Page",
      metrics: [
        {{ value: "21.6K+", label: "Cộng đồng Fanpage", desc: "Người theo dõi trang" }},
        {{ value: "+25 – 30%", label: "Tiếp cận tự nhiên", desc: "Organic Reach trang" }},
        {{ value: "7 – 8%", label: "Tăng trưởng Follower", desc: "Tăng từ mức 2-3%" }},
        {{ value: "100%", label: "Chăm sóc Fanpage", desc: "Nội dung &amp; Tương tác" }}
      ],
      insight: "Fanpage Dược phẩm đòi hỏi thông tin chuẩn xác, đáng tin cậy và tuân thủ nghiêm ngặt quy định y tế; người dùng cần nội dung dễ hiểu giải đáp đúng thắc mắc sức khỏe thường gặp.",
      execution: "Lập lịch nội dung định kỳ, trực tiếp quản trị Fanpage OPV, chăm sóc tương tác và xây dựng chuỗi bài viết/video ngắn chia sẻ kiến thức dược phẩm; theo dõi chỉ số hiệu suất trên Meta Suite để liên tục tối ưu nội dung.",
      impact: "Duy trì lượng tiếp cận tự nhiên của Fanpage tăng trưởng 25–30%, giữ vững sự gắn kết của cộng đồng 21.6K+ followers và gia tăng mức độ nhận diện thương hiệu bền vững."
    }}
  }};

  function openVideoModal(key) {{
    const data = videoModalData[key];
    if (!data) return;
    document.getElementById('vmTitle').innerHTML = data.title;
    document.getElementById('vmCategory').innerHTML = data.category;
    document.getElementById('vmPartner').innerHTML = data.partner;
    document.getElementById('vmBadge').innerHTML = data.badge;
    document.getElementById('vmThumb').src = data.thumb;
    document.getElementById('vmPlayBtn').href = data.fbUrl;
    document.getElementById('vmFbBannerLink').href = data.fbUrl;
    document.getElementById('vmFooterFbBtn').href = data.fbUrl;

    const isVideo = (key !== 'koc');
    document.getElementById('vmPlayBtn').style.display = isVideo ? 'flex' : 'none';
    document.getElementById('vmFbBannerLink').style.display = isVideo ? 'inline-flex' : 'none';
    document.getElementById('vmFooterFbBtn').style.display = isVideo ? 'inline-flex' : 'none';

    document.getElementById('vmInsight').innerHTML = data.insight;
    document.getElementById('vmExecution').innerHTML = data.execution;
    document.getElementById('vmImpact').innerHTML = data.impact;

    const proofBtn = document.getElementById('vmProofBtn');
    if (data.proofBtnText) {{
      proofBtn.innerHTML = `<span>${{data.proofBtnText}}</span>`;
    }} else {{
      proofBtn.innerHTML = `<span>🔍 Phóng To Báo Cáo</span>`;
    }}
    proofBtn.onclick = function() {{
      closeVideoModalDirect();
      openLightbox(data.proofKey);
    }};

    // Metrics grid
    const mg = document.getElementById('vmMetricsGrid');
    mg.innerHTML = data.metrics.map(m => `
      <div class="vm-metric-card">
        <div class="vm-metric-value">${{m.value}}</div>
        <div class="vm-metric-label">${{m.label}}</div>
        <div class="vm-metric-desc">${{m.desc}}</div>
      </div>
    `).join('');

    document.getElementById('videoModal').classList.add('active');
    document.body.style.overflow = 'hidden';
  }}

  function closeVideoModal(e) {{
    if (e.target.id === 'videoModal') {{
      closeVideoModalDirect();
    }}
  }}

  function closeVideoModalDirect() {{
    const vm = document.getElementById('videoModal');
    if (vm) vm.classList.remove('active');
    document.body.style.overflow = 'auto';
  }}

  // Proof Data for Lightbox
  const proofData = {{
    affiliate: {{
      src: "data:image/jpeg;base64,{affiliate_b64}",
      title: "💰 Minh Chứng: Báo Cáo Doanh Thu TikTok Shop Affiliate",
      caption: "Dashboard TikTok Shop Creator ghi nhận GMV đạt 239.9M VNĐ (+4,000%), 3.300+ đơn hàng xuất bán thành công, 1.3 Triệu lượt hiển thị sản phẩm và 34.7K lượt click trong chưa đầy 1 tháng."
    }},
    koc: {{
      src: "data:image/jpeg;base64,{koc_b64}",
      title: "✨ Minh Chứng: Video KOC Skincare Reviewer Đa Nền Tảng",
      caption: "Sản phẩm video review thực tế trên iPhone kết hợp cùng các thương hiệu da liễu hàng đầu L’Oréal, Vichy và Eucerin. Đạt tỷ lệ người xem trung bình 15.000 lượt/tháng và hơn 800 lượt truy cập trang hồ sơ."
    }},
    meddc_cover: {{
      src: "data:image/jpeg;base64,{meddc_cover_b64}",
      title: "🏥 Cover Kênh MEDDC: Truyền Thông Giáo Dục Sức Khỏe Tại Bệnh Viện",
      caption: "Hệ thống truyền thông số y tế (TV, LED, Digital Standee) kết nối thông tin y tế, nâng cao sức khỏe cộng đồng tại hệ thống bệnh viện hàng đầu (BV Nhi Đồng 1, BV 175).<div style='margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap;'><a href='https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Video Kênh MEDDC (Facebook) ↗</a><button data-key='medtv' onclick='closeLightboxDirect(); openLightbox(this.dataset.key);' class='btn btn-outline' style='padding: 8px 16px; font-size: 0.85rem;'>📈 Xem Báo Cáo Tăng Trưởng Meta</button></div>"
    }},
    medtv: {{
      src: "data:image/jpeg;base64,{medtv_b64}",
      title: "📈 Minh Chứng: Báo Cáo Tăng Trưởng Meta Suite Kênh MEDTV",
      caption: "Dashboard trực tiếp từ Meta Suite ghi nhận chiến dịch Reels giáo dục sức khỏe đạt 98.474 lượt xem, tương tác tăng trưởng đột biến +880.5% và follower tăng +547% trong vòng 28 ngày triển khai dự án B2B Healthcare.<div style='margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap;'><a href='https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Video Kênh MEDDC (Facebook) ↗</a><a href='https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-outline' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Xem Kênh Thân Tâm ↗</a></div>"
    }},
    workflow: {{
      src: "data:image/jpeg;base64,{workflow_b64}",
      title: "🎬 Minh Chứng: Quy Trình Lên Kịch Bản &amp; Dựng Video Kênh Thân Tâm",
      caption: "Hậu trường tự chủ 100% quy trình sản xuất video y tế gia đình Thân Tâm: Soạn thảo storyboard kịch bản phân cảnh chi tiết, thiết bị thu âm chuyên nghiệp Rode Wireless và timeline biên tập CapCut Pro trực quan.<div style='margin-top: 14px;'><a href='https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Kênh Thân Tâm trên Facebook ↗</a></div>"
    }},
    opv: {{
      src: "data:image/jpeg;base64,{opv_b64}",
      title: "🌿 Minh Chứng: Báo Cáo Tăng Trưởng Fanpage Dược Phẩm OPV",
      caption: "Dashboard ghi nhận hiệu quả quản trị Fanpage Dược phẩm OPV: Lượng tiếp cận tự nhiên (Organic Reach) tăng 25–30%, tỷ lệ người theo dõi mới tăng từ 2% lên 8% sau 2 tháng tối ưu nội dung và chăm sóc kênh định kỳ.<div style='margin-top: 14px;'><a href='https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Video &amp; Kênh Fanpage OPV (Facebook) ↗</a></div>"
    }},
    dental: {{
      src: "data:image/jpeg;base64,{dental_b64}",
      title: "⭐ Minh Chứng: Trải Nghiệm Khách Hàng &amp; Điều Phối Khám Nha Khoa Kim",
      caption: "Giao diện quản lý quy trình điều phối tiếp đón bệnh nhân và kết quả khảo sát mức độ hài lòng khách hàng CSAT 4.9/5 sao tại Hệ thống Nha Khoa Kim, hoàn thành 90–110% KPI chất lượng dịch vụ."
    }},
    credentials: {{
      src: "data:image/jpeg;base64,{credentials_b64}",
      title: "📜 Minh Chứng: Bằng Cấp Cử Nhân &amp; Chứng Chỉ Quốc Tế",
      caption: "Chứng chỉ TOEIC Speaking &amp; Writing (06/2024), Chứng chỉ Tin học Văn phòng MOS (06/2023) và Bằng Cử nhân Thông Tin – Thư Viện Trường Đại học Sài Gòn."
    }}
  }};

  function openLightbox(key) {{
    const data = proofData[key];
    if (!data) return;
    document.getElementById('lightboxImg').src = data.src;
    document.getElementById('lightboxTitle').innerHTML = data.title;
    document.getElementById('lightboxCaption').innerHTML = data.caption;
    document.getElementById('lightboxModal').classList.add('active');
    document.body.style.overflow = 'hidden';
  }}

  function closeLightbox(e) {{
    if (e.target.id === 'lightboxModal') {{
      closeLightboxDirect();
    }}
  }}

  function closeLightboxDirect() {{
    document.getElementById('lightboxModal').classList.remove('active');
    document.body.style.overflow = 'auto';
  }}

  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      closeLightboxDirect();
      closeVideoModalDirect();
    }}
  }});

  function filterEvidence(category) {{
    const buttons = document.querySelectorAll('.proof-tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    const cards = document.querySelectorAll('.evidence-card');
    cards.forEach(card => {{
      if (category === 'all' || card.getAttribute('data-evidence') === category) {{
        card.style.display = 'flex';
      }} else {{
        card.style.display = 'none';
      }}
    }});
  }}

  function toggleMobileMenu() {{
    const drawer = document.getElementById('mobileDrawer');
    const btn = document.getElementById('mobileToggleBtn');
    drawer.classList.toggle('active');
    btn.classList.toggle('active');
    if (drawer.classList.contains('active')) {{
      document.body.style.overflow = 'hidden';
    }} else {{
      document.body.style.overflow = 'auto';
    }}
  }}

  function closeMobileMenu() {{
    const drawer = document.getElementById('mobileDrawer');
    const btn = document.getElementById('mobileToggleBtn');
    if (drawer) drawer.classList.remove('active');
    if (btn) btn.classList.remove('active');
    document.body.style.overflow = 'auto';
  }}
</script>

</body>
</html>
'''

# Paths
dir_path = '/Users/Admin/Documents/HRM/portfolio'
os.makedirs(dir_path, exist_ok=True)

html_path = os.path.join(dir_path, 'index.html')

# Write to HRM/portfolio/index.html and HRM/index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(portfolio_html)

root_html = '/Users/Admin/Documents/HRM/index.html'
shutil.copyfile(html_path, root_html)
print(f"Generated {html_path} and {root_html}")

