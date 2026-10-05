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
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
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
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    border-top: 1px solid var(--border-color);
    padding-top: 24px;
  }}
  .stat-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 12px 18px;
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

  /* ABOUT BENTO SECTION */
  .about-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }}
  .bento-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 24px;
    box-shadow: var(--shadow-sm);
    transition: all 0.25s ease;
  }}
  .bento-card:hover {{
    transform: translateY(-3px);
    border-color: var(--accent-border);
  }}
  .bento-card-span2 {{
    grid-column: span 2;
  }}
  .bento-icon {{
    width: 42px;
    height: 42px;
    border-radius: var(--radius-sm);
    background: var(--accent-soft);
    color: var(--accent);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    margin-bottom: 14px;
  }}
  .bento-title {{
    font-size: 1.15rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 6px;
  }}
  .bento-desc {{
    font-size: 0.9rem;
    color: var(--text-secondary);
    line-height: 1.55;
  }}

  /* SKILLS & ECOSYSTEM */
  .skills-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }}
  .skill-box {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 28px;
    box-shadow: var(--shadow-sm);
  }}
  .skill-box-title {{
    font-size: 1.2rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 16px;
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
    padding: 7px 14px;
    border-radius: var(--radius-full);
    font-size: 0.85rem;
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

  /* TIMELINE */
  .timeline-wrap {{
    position: relative;
    max-width: 860px;
    margin: 0 auto;
  }}
  .timeline-wrap::before {{
    content: '';
    position: absolute;
    top: 10px;
    bottom: 10px;
    left: 20px;
    width: 2px;
    background: var(--accent-border);
  }}
  .timeline-item {{
    position: relative;
    padding-left: 56px;
    margin-bottom: 24px;
  }}
  .timeline-dot {{
    position: absolute;
    left: 12px;
    top: 16px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #fff;
    border: 4px solid var(--accent);
    box-shadow: 0 0 0 3px rgba(91, 130, 102, 0.15);
  }}
  .timeline-card {{
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 18px 22px;
    box-shadow: var(--shadow-sm);
  }}
  .timeline-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
  }}
  .timeline-role {{
    font-size: 1.05rem;
    font-weight: 800;
    color: var(--text-primary);
  }}
  .timeline-date {{
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--accent);
    background: var(--accent-soft);
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Space Grotesk', sans-serif;
  }}
  .timeline-company {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    font-weight: 600;
    margin-bottom: 6px;
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
    padding: 24px;
  }}
  .lightbox-modal.active {{
    display: flex;
  }}
  .lightbox-container {{
    max-width: 900px;
    width: 100%;
    background: #fff;
    border-radius: var(--radius-md);
    overflow: hidden;
    box-shadow: 0 25px 60px rgba(0,0,0,0.5);
    position: relative;
    animation: modalScale 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  @keyframes modalScale {{
    from {{ transform: scale(0.94); opacity: 0; }}
    to {{ transform: scale(1); opacity: 1; }}
  }}
  .lightbox-img-wrap {{
    width: 100%;
    max-height: 540px;
    background: #000;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .lightbox-img {{
    max-width: 100%;
    max-height: 540px;
    object-fit: contain;
    display: block;
  }}
  .lightbox-info {{
    padding: 20px 24px;
    background: #fff;
    border-top: 1px solid var(--border-color);
  }}
  .lightbox-title {{
    font-size: 1.2rem;
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
    line-height: 1.5;
  }}
  .lightbox-close {{
    position: absolute;
    top: 14px;
    right: 14px;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(0,0,0,0.6);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.2rem;
    border: none;
    transition: background 0.2s;
    z-index: 10;
  }}
  .lightbox-close:hover {{
    background: rgba(0,0,0,0.9);
  }}

  /* RESPONSIVE */
  @media (max-width: 992px) {{
    .hero-grid {{
      grid-template-columns: 1fr;
      text-align: center;
    }}
    .hero-desc {{
      margin: 0 auto 24px auto;
    }}
    .hero-cta-group, .hero-stats-row {{
      justify-content: center;
    }}
    .evidence-grid {{
      grid-template-columns: repeat(2, 1fr);
    }}
    .video-grid {{
      grid-template-columns: 1fr;
    }}
    .case-grid {{
      grid-template-columns: 1fr;
    }}
    .about-grid {{
      grid-template-columns: 1fr;
    }}
    .bento-card-span2 {{
      grid-column: span 1;
    }}
    .skills-grid {{
      grid-template-columns: 1fr;
    }}
    .contact-card {{
      grid-template-columns: 1fr;
      padding: 32px 20px;
    }}
  }}

  @media (max-width: 640px) {{
    .hero-title {{
      font-size: 2.2rem;
    }}
    .nav-menu {{
      display: none;
    }}
    .evidence-grid {{
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
      <li><a href="#evidence" class="nav-link">Minh chứng thực tế <span class="nav-badge-pill">7 Proofs</span></a></li>
      <li><a href="#videos" class="nav-link">🎬 Video đã làm <span class="nav-badge-pill" style="background:#e0f2fe; color:#0369a1;">3 Kênh</span></a></li>
      <li><a href="#projects" class="nav-link">Dự án &amp; Case Studies</a></li>
      <li><a href="#about" class="nav-link">Năng lực cốt lõi</a></li>
      <li><a href="#skills" class="nav-link">Công cụ &amp; AI</a></li>
      <li><a href="#contact" class="nav-link">Liên hệ</a></li>
    </ul>
    <div style="display: flex; gap: 8px;">
      <a href="CV_Le_Thi_Hoang_Cam_A4_2Trang.pdf" target="_blank" class="btn btn-primary" style="padding: 8px 16px; font-size: 0.85rem;">
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

      <!-- PROOF 4: OPV PHARMA ADS DASHBOARD -->
      <div class="evidence-card" data-evidence="data" onclick="openLightbox('opv')">
        <div class="evidence-thumb-wrap">
          <span class="evidence-pill-tag">Dashboard Paid Ads &amp; SEO</span>
          <img class="evidence-img" src="data:image/jpeg;base64,{opv_b64}" alt="Báo cáo hiệu quả Ads Dược phẩm OPV">
          <div class="evidence-zoom-overlay">🔍 Bấm xem ảnh phóng to</div>
        </div>
        <div class="evidence-content">
          <div>
            <h3 class="evidence-title">Chiến Dịch Content SEO &amp; Paid-Ads Dược Phẩm</h3>
            <p class="evidence-caption">Vận hành quảng cáo Facebook &amp; TikTok Ads cho Dược phẩm OPV kết hợp tối ưu SEO web, thúc đẩy reach tự nhiên tăng 25–30%.</p>
          </div>
          <div>
            <span class="evidence-stat-badge">🚀 Reach tự nhiên +30% • Follower +8%</span>
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
      <!-- VIDEO 1: MEDDC TRUYỀN THÔNG SỐ BỆNH VIỆN -->
      <div class="video-card">
        <a href="https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="video-thumb">
          <img src="data:image/jpeg;base64,{medtv_b64}" alt="Kênh MEDDC Truyền thông số Bệnh viện" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">🔥 98.4K+ Views • +880% Tương tác</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem trên Facebook ↗</div>
          </div>
        </a>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill">Facebook Video • B2B Healthcare</span>
              <span class="video-hospital-tag">🏥 BV Nhi Đồng 1 &amp; BV 175</span>
            </div>
            <h3 class="video-card-title">Kênh MEDDC — Truyền Thông Số Bệnh Viện (MEDTV)</h3>
            <p class="video-card-desc">
              Dự án kết nối nhãn hàng quốc tế (Comfort, ColosBaby, Gaviscon...) với các bệnh viện đầu ngành qua chuỗi Reels giáo dục sức khỏe và phóng sự y tế tiếp cận 98.4K+ lượt xem.
            </p>
          </div>
          <div>
            <a href="https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="width: 100%; padding: 11px; font-size: 0.88rem;">
              <span>▶ Xem Video Kênh MEDDC trên Facebook ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- VIDEO 2: THÂN TÂM HOME HEALTHCARE -->
      <div class="video-card">
        <a href="https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="video-thumb">
          <img src="data:image/jpeg;base64,{workflow_b64}" alt="Kênh Thân Tâm Chăm sóc sức khỏe tại nhà" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">🩺 Chăm Sóc Sức Khỏe Tại Nhà</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem trên Facebook ↗</div>
          </div>
        </a>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill">Facebook Video • Y Tế Gia Đình</span>
              <span class="video-hospital-tag">📍 TP. Hồ Chí Minh</span>
            </div>
            <h3 class="video-card-title">Thân Tâm — Chăm Sóc Sức Khỏe &amp; Người Cao Tuổi</h3>
            <p class="video-card-desc">
              Chuỗi nội dung video ngắn hướng dẫn chăm sóc y tế tại gia, giải đáp quy trình điều dưỡng chuyên sâu, tạo dựng niềm tin và sự gắn kết bền vững với khách hàng.
            </p>
          </div>
          <div>
            <a href="https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="width: 100%; padding: 11px; font-size: 0.88rem;">
              <span>▶ Xem Video Kênh Thân Tâm trên Facebook ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- VIDEO 3: OPV PHARMACEUTICAL -->
      <div class="video-card">
        <a href="https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="video-thumb">
          <img src="data:image/jpeg;base64,{opv_b64}" alt="Kênh Dược phẩm OPV Pharmaceutical" class="video-thumb-img">
          <div class="video-play-overlay">
            <span class="video-badge-views">💊 21.6K+ Followers • Reach +30%</span>
            <div class="video-play-btn">▶</div>
            <div style="font-size: 0.76rem; color: #fff; text-align: center; text-shadow: 0 1px 4px rgba(0,0,0,0.8);">Bấm mở xem trên Facebook ↗</div>
          </div>
        </a>
        <div class="video-card-body">
          <div>
            <div class="video-meta-top">
              <span class="video-source-pill">Facebook Media • Dược Phẩm</span>
              <span class="video-hospital-tag">🌿 OPV Pharmaceutical</span>
            </div>
            <h3 class="video-card-title">OPV Pharmaceutical — Video &amp; Truyền Thông Thương Hiệu</h3>
            <p class="video-card-desc">
              Sản xuất video sản phẩm và nội dung bài viết chuẩn SEO Y Dược, kết hợp vận hành quảng cáo Paid-Ads đa kênh, thúc đẩy nhận diện dòng sản phẩm mới tăng trưởng 25–30%.
            </p>
          </div>
          <div>
            <a href="https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="width: 100%; padding: 11px; font-size: 0.88rem;">
              <span>▶ Xem Video Kênh OPV trên Facebook ↗</span>
            </a>
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
          <h3 class="case-title">Sáng Tạo Nội Dung Đa Nền Tảng &amp; KOC Reviewer</h3>
          <div class="case-brands">✨ L’Oréal • Vichy • Eucerin • SVR</div>
          <ul class="case-bullets">
            <li>Tự chủ 100% quy trình từ ý tưởng, kịch bản, quay chụp đến dựng video ngắn review mỹ phẩm chuẩn visual cao cấp.</li>
            <li>Hợp tác nhận PR kit, sản xuất video trải nghiệm sản phẩm theo brief nhãn hàng và tham gia sự kiện ra mắt độc quyền.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">👀 Views trung bình: <strong class="metric-badge">15.000 / tháng (+30%)</strong></span>
            <span class="metric-item">👤 Profile Visits: <strong class="metric-badge">800 lượt (+20%)</strong></span>
          </div>
        </div>
      </div>

      <!-- PROJECT 2 -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('medtv')">
          <img class="case-media-img" src="data:image/jpeg;base64,{medtv_b64}" alt="Case study Kênh MEDTV">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">B2B Healthcare &amp; Media</span>
            <span class="case-timeline">03/2026 – 09/2026</span>
          </div>
          <h3 class="case-title">Kênh Truyền Thông Y Tế MEDTV &amp; Giáo Dục Sức Khỏe</h3>
          <div class="case-brands">🏥 Comfort • ColosBaby • Gaviscon x BV Nhi Đồng 1, BV 175</div>
          <ul class="case-bullets">
            <li>Quản trị 2 Fanpage MEDDC &amp; Thân Tâm, kết nối nhãn hàng quốc tế với các bệnh viện đầu ngành qua dự án B2B MEDTV.</li>
            <li>Xây dựng chuỗi Reels giáo dục sức khỏe đạt tốc độ viral tự nhiên cao, đánh trúng tâm lý phụ huynh và bệnh nhân.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">🔥 Video Views: <strong class="metric-badge">98.474 lượt</strong></span>
            <span class="metric-item">📈 Tương tác: <strong class="metric-badge">+880.5%</strong></span>
            <span class="metric-item">👥 Followers: <strong class="metric-badge">+547% trong 28 ngày</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <a href="https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem;">
              <span>▶ Xem Video Kênh MEDDC ↗</span>
            </a>
            <a href="https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-outline" style="padding: 8px 14px; font-size: 0.82rem;">
              <span>▶ Xem Kênh Thân Tâm ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- PROJECT 3 -->
      <div class="case-card">
        <div class="case-media-header" onclick="openLightbox('opv')">
          <img class="case-media-img" src="data:image/jpeg;base64,{opv_b64}" alt="Case study Dược phẩm OPV">
          <div class="case-media-overlay">🔍 Bấm xem ảnh minh chứng</div>
        </div>
        <div class="case-body">
          <div class="case-meta-row">
            <span class="case-category-tag">Pharma Marketing &amp; Paid Ads</span>
            <span class="case-timeline">12/2024 – 02/2026</span>
          </div>
          <h3 class="case-title">Chiến Dịch Content Chuẩn SEO &amp; Paid-Ads Đa Kênh</h3>
          <div class="case-brands">💊 Công ty Cổ phần Dược phẩm OPV</div>
          <ul class="case-bullets">
            <li>Lập kế hoạch &amp; viết bài chuẩn SEO Y Dược trên Website, Facebook, TikTok gia tăng thứ hạng tìm kiếm tự nhiên.</li>
            <li>Cài đặt, theo dõi và tối ưu chiến dịch Paid-Ads (Facebook Ads, TikTok Ads) giúp tăng nhận diện dòng sản phẩm mới.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">🚀 Tiếp cận tự nhiên: <strong class="metric-badge">+25 – 30%</strong></span>
            <span class="metric-item">📊 Tăng trưởng người theo dõi: <strong class="metric-badge">Từ 2-3% lên 7-8%</strong></span>
          </div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px;">
            <a href="https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="padding: 8px 14px; font-size: 0.82rem;">
              <span>▶ Xem Video &amp; Kênh OPV Pharmaceutical ↗</span>
            </a>
          </div>
        </div>
      </div>

      <!-- PROJECT 4 -->
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
          <h3 class="case-title">Tối Ưu Trải Nghiệm &amp; Quản Trị Thông Tin Dịch Vụ</h3>
          <div class="case-brands">🦷 Hệ thống Nha Khoa Kim</div>
          <ul class="case-bullets">
            <li>Tư vấn chu đáo quy trình và liệu trình nha khoa chuyên sâu, quản lý tệp thông tin và điều phối đón tiếp cùng bác sĩ.</li>
            <li>Rút ngắn thời gian chờ khám, tạo trải nghiệm ân cần, nâng cao tỷ lệ khách hàng an tâm tiếp tục liệu trình.</li>
          </ul>
          <div class="case-metrics-banner">
            <span class="metric-item">⭐ Tiếp đón &amp; Chăm sóc: <strong class="metric-badge">10 – 15 khách/ngày</strong></span>
            <span class="metric-item">🎯 KPI chất lượng dịch vụ: <strong class="metric-badge">90 – 110%</strong></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ABOUT / CORE COMPETENCIES -->
<section id="about" class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Thế Mạnh</span>
      <h2 class="section-title">Năng Lực Cốt Lõi</h2>
      <p class="section-subtitle">Tư duy hệ thống từ chuyên ngành thông tin kết hợp khả năng sáng tạo đa phương tiện.</p>
    </div>

    <div class="about-grid">
      <div class="bento-card bento-card-span2">
        <div class="bento-icon">💡</div>
        <h3 class="bento-title">Chiến Lược Content Dựa Trên Dữ Liệu &amp; Insight</h3>
        <p class="bento-desc">
          Tốt nghiệp chuyên ngành <strong>Thông Tin – Thư Viện (ĐH Sài Gòn)</strong>, mình có kỹ năng cấu trúc thông tin khoa học và phân tích sâu hành vi người dùng, biến insight thành nội dung có tính lan tỏa và thúc đẩy chuyển đổi tự nhiên.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🏥</div>
        <h3 class="bento-title">Thế Mạnh Y Tế &amp; Dược Mỹ Phẩm</h3>
        <p class="bento-desc">
          Nắm vững quy chuẩn truyền thông Healthcare &amp; FMCG, am hiểu cách tiếp cận từ phụ huynh, bệnh nhân đến đối tác B2B.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🎬</div>
        <h3 class="bento-title">Sản Xuất Short-form Video Độc Lập</h3>
        <p class="bento-desc">
          Tự đảm nhiệm kịch bản phân cảnh, ghi hình và hậu kỳ CapCut Pro, tạo nhịp điệu cuốn hút giữ chân người xem.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">📊</div>
        <h3 class="bento-title">Vận Hành &amp; Đo Lường Paid-Ads</h3>
        <p class="bento-desc">
          Thành thạo tối ưu Facebook Ads, TikTok Ads, theo dõi CPC, CPM, CTR và phân tích dữ liệu để điều chỉnh chiến dịch tức thì.
        </p>
      </div>

      <div class="bento-card">
        <div class="bento-icon">🤝</div>
        <h3 class="bento-title">Trải Nghiệm Khách Hàng Đa Điểm Chạm</h3>
        <p class="bento-desc">
          Kinh nghiệm từ Nha Khoa Kim giúp mình luôn đặt sự thấu hiểu tâm lý khách hàng làm trọng tâm cho mọi thông điệp truyền thông.
        </p>
      </div>
    </div>
  </div>
</section>

<!-- SKILLS & TOOLS ECOSYSTEM -->
<section id="skills" class="section">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Bộ Công Cụ</span>
      <h2 class="section-title">Kỹ Năng &amp; Công Nghệ Thực Chiến</h2>
      <p class="section-subtitle">Ứng dụng AI và các phần mềm hiện đại nhằm tối đa hóa tốc độ sáng tạo và chất lượng đầu ra.</p>
    </div>

    <div class="skills-grid">
      <!-- SKILLS -->
      <div class="skill-box">
        <h3 class="skill-box-title">🎯 Kỹ Năng Marketing Chuyên Môn</h3>
        <div class="skill-pill-list">
          <span class="skill-pill">✍️ <strong>Content Strategy</strong> (Xây dựng chiến lược)</span>
          <span class="skill-pill">🎬 <strong>Short-form Video</strong> (Reels, TikTok, Shorts)</span>
          <span class="skill-pill">📈 <strong>Paid-Ads</strong> (Meta Ads, TikTok Ads)</span>
          <span class="skill-pill">🔍 <strong>SEO Y Dược</strong> (Onpage, Keyword Research)</span>
          <span class="skill-pill">🤝 <strong>B2B Healthcare Media</strong> (Kết nối viện - nhãn)</span>
          <span class="skill-pill">👥 <strong>KOC / Influencer Collab</strong> (L'Oréal, Vichy, SVR)</span>
          <span class="skill-pill">💖 <strong>Customer Care</strong> (Trải nghiệm khách hàng)</span>
        </div>
      </div>

      <!-- TOOLS & AI -->
      <div class="skill-box">
        <h3 class="skill-box-title">💻 Hệ Sinh Thái Công Cụ &amp; GenAI</h3>
        <div class="skill-pill-list">
          <span class="skill-pill">✨ <strong>CapCut Pro</strong> (Dựng video ngắn tốc độ)</span>
          <span class="skill-pill">🎨 <strong>Canva Pro</strong> (Visual post, infographic)</span>
          <span class="skill-pill">🤖 <strong>Gemini &amp; ChatGPT</strong> (Brainstorm, kịch bản)</span>
          <span class="skill-pill">📊 <strong>Meta Business Suite</strong> (Báo cáo, đo lường)</span>
          <span class="skill-pill">📱 <strong>TikTok Creator Hub</strong> (Bắt trend, tối ưu)</span>
          <span class="skill-pill">🖌️ <strong>Photoshop &amp; Premiere</strong> (Cắt ghép, tinh chỉnh)</span>
          <span class="skill-pill">📑 <strong>Google Docs &amp; Sheets</strong> (Kế hoạch nội dung)</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TIMELINE -->
<section class="section section-alt">
  <div class="container">
    <div class="section-header">
      <span class="section-tag">Hành Trình</span>
      <h2 class="section-title">Kinh Nghiệm Làm Việc</h2>
      <p class="section-subtitle">4 cột mốc khẳng định sự phát triển và tính kỷ luật trong công việc.</p>
    </div>

    <div class="timeline-wrap">
      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Freelance Marketing Executive &amp; Content Creator</span>
            <span class="timeline-date">09/2024 – HIỆN TẠI</span>
          </div>
          <div class="timeline-company">Hợp tác nhãn hàng: L’Oréal • Vichy • Eucerin • SVR</div>
          <p style="font-size: 0.88rem; color: var(--text-secondary);">
            Tự chủ kịch bản, quay dựng video ngắn đa nền tảng, duy trì đều đặn 15.000+ views/tháng và 800 lượt truy cập trang.
          </p>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Digital Marketing</span>
            <span class="timeline-date">03/2026 – 09/2026</span>
          </div>
          <div class="timeline-company">Công ty TNHH Đào tạo &amp; Chăm sóc Sức khỏe Thân Tâm</div>
          <p style="font-size: 0.88rem; color: var(--text-secondary);">
            Quản trị fanpage MEDDC &amp; Thân Tâm, kết nối chiến dịch B2B kênh MEDTV đạt 98.474 views và tăng trưởng +880.5% tương tác.
          </p>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Content &amp; Digital Marketing</span>
            <span class="timeline-date">12/2024 – 02/2026</span>
          </div>
          <div class="timeline-company">Công ty Cổ phần Dược phẩm OPV</div>
          <p style="font-size: 0.88rem; color: var(--text-secondary);">
            Sản xuất nội dung chuẩn SEO Y Dược và điều phối chiến dịch quảng cáo Paid-Ads giúp độ tiếp cận tự nhiên tăng 25–30%.
          </p>
        </div>
      </div>

      <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div class="timeline-header">
            <span class="timeline-role">Chuyên viên Chăm sóc &amp; Trải nghiệm Khách hàng</span>
            <span class="timeline-date">06/2024 – 12/2024</span>
          </div>
          <div class="timeline-company">Hệ thống Nha Khoa Kim</div>
          <p style="font-size: 0.88rem; color: var(--text-secondary);">
            Tư vấn quy trình dịch vụ nha khoa, điều phối lịch hẹn bác sĩ chuyên môn và duy trì 90–110% KPI chất lượng dịch vụ.
          </p>
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
    medtv: {{
      src: "data:image/jpeg;base64,{medtv_b64}",
      title: "📈 Minh Chứng: Báo Cáo Tăng Trưởng Meta Suite Kênh MEDTV",
      caption: "Dashboard trực tiếp từ Meta Suite ghi nhận chiến dịch Reels giáo dục sức khỏe đạt 98.474 lượt xem, tương tác tăng trưởng đột biến +880.5% và follower tăng +547% trong vòng 28 ngày triển khai dự án B2B Healthcare.<div style='margin-top: 14px; display: flex; gap: 8px; flex-wrap: wrap;'><a href='https://www.facebook.com/share/14tuJtmuRGS/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Video Kênh MEDDC (Facebook) ↗</a><a href='https://www.facebook.com/share/1HcnkPgAuy/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-outline' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Xem Kênh Thân Tâm ↗</a></div>"
    }},
    workflow: {{
      src: "data:image/jpeg;base64,{workflow_b64}",
      title: "🎬 Minh Chứng: Quy Trình Lên Kịch Bản &amp; Dựng Video CapCut Pro",
      caption: "Ảnh chụp hậu trường quy trình sản xuất video ngắn: Soạn thảo storyboard kịch bản phân cảnh chi tiết, thiết bị thu âm chuyên nghiệp Rode và timeline biên tập dựng phim hiệu ứng trên máy tính bảng."
    }},
    opv: {{
      src: "data:image/jpeg;base64,{opv_b64}",
      title: "🚀 Minh Chứng: Dashboard Paid Ads &amp; Tăng Trưởng SEO Dược Phẩm OPV",
      caption: "Báo cáo chiến dịch Paid Advertising đa kênh (Facebook, TikTok Ads) và biểu đồ lượng tìm kiếm tự nhiên (Organic Reach) tăng 25–30%, tỷ lệ người theo dõi mới tăng từ 2% lên 8% sau 2 tháng tối ưu.<div style='margin-top: 14px;'><a href='https://www.facebook.com/share/1CR4mtMRDN/?mibextid=wwXIfr' target='_blank' rel='noopener noreferrer' class='btn btn-primary' style='padding: 8px 16px; font-size: 0.85rem;'>▶ Mở Xem Video &amp; Kênh OPV (Facebook) ↗</a></div>"
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
</script>

</body>
</html>
'''

# Paths
dir_path = '/Users/Admin/Documents/HRM/portfolio'
os.makedirs(dir_path, exist_ok=True)

html_path = os.path.join(dir_path, 'index.html')
desktop_html = '/Users/Admin/Desktop/Portfolio_Le_Thi_Hoang_Cam.html'
desktop_preview = '/Users/Admin/Desktop/portfolio_preview_full.png'

# Write to HRM/portfolio/index.html and HRM/index.html
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(portfolio_html)

root_html = '/Users/Admin/Documents/HRM/index.html'
shutil.copyfile(html_path, root_html)

# Copy HTML to Desktop
shutil.copyfile(html_path, desktop_html)
print(f"Generated {html_path}, {root_html} and copied to {desktop_html}")

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Take high-res preview screenshot
subprocess.run([
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    f"--screenshot={desktop_preview}",
    "--window-size=1280,3600",
    f"file://{html_path}"
], check=True)

print(f"Exported preview screenshot to {desktop_preview}")
