import os

BASE = '/home/hamiddi/projects/coway-product-pages'
WA_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
NAV_SVG = WA_SVG.replace('width="20"','width="18"').replace('height="20"','height="18"')

COMMON_CSS = '''
:root {
  --navy: #002856; --blue: #0066b3; --blue-light: #e8f4fd; --blue-accent: #0099e6;
  --green: #00a859; --red: #e31837; --white: #ffffff;
  --gray-50: #f8fafb; --gray-100: #f0f4f6; --gray-200: #e2e8f0;
  --gray-300: #cbd5e1; --gray-400: #94a3b8; --gray-500: #64748b;
  --gray-600: #475569; --gray-700: #334155; --gray-800: #1e293b;
  --wa: #25D366; --radius: 12px; --radius-lg: 20px; --max: 1140px;
  --shadow: 0 2px 16px rgba(0,0,0,0.06); --shadow-lg: 0 8px 40px rgba(0,0,0,0.08);
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: 'Noto Sans', system-ui, -apple-system, sans-serif; color: var(--gray-800); background: var(--white); line-height: 1.6; -webkit-font-smoothing: antialiased; }
img { max-width: 100%; height: auto; display: block; }
a { color: inherit; text-decoration: none; }
.container { max-width: var(--max); margin: 0 auto; padding: 0 24px; }
.section { padding: 80px 0; }
.section-narrow { padding: 60px 0; }
.section-label { font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--blue); margin-bottom: 8px; }
.section-title { font-size: clamp(28px, 4vw, 40px); font-weight: 800; line-height: 1.2; color: var(--navy); margin-bottom: 16px; }
.section-desc { font-size: 16px; color: var(--gray-500); max-width: 640px; line-height: 1.7; }
.nav { position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--gray-200); padding: 14px 0; }
.nav-inner { max-width: var(--max); margin: 0 auto; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; }
.nav-logo { font-size: 22px; font-weight: 800; color: var(--navy); letter-spacing: -0.02em; }
.nav-cta { background: var(--wa); color: #fff; padding: 10px 20px; border-radius: 50px; font-size: 14px; font-weight: 600; transition: all 0.25s; display: flex; align-items: center; gap: 6px; }
.nav-cta:hover { transform: translateY(-1px); box-shadow: 0 4px 16px rgba(37,211,102,0.3); }
.hero { background: linear-gradient(135deg, var(--navy) 0%, #001a3d 100%); color: var(--white); position: relative; overflow: hidden; min-height: 560px; display: flex; align-items: center; }
.hero-bg { position: absolute; inset: 0; background: var(--hero-bg-img) center/cover no-repeat; opacity: 0.25; }
.hero .container { position: relative; z-index: 2; display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; }
.hero-badge { display: inline-block; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2); padding: 6px 16px; border-radius: 50px; font-size: 13px; font-weight: 600; letter-spacing: 0.04em; margin-bottom: 20px; }
.hero-promo-badge { display: inline-block; background: var(--red); color: #fff; padding: 8px 20px; border-radius: 50px; font-size: 14px; font-weight: 700; letter-spacing: 0.04em; margin-bottom: 16px; animation: pulse 2s infinite; }
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
.hero h1 { font-size: clamp(36px, 5vw, 56px); font-weight: 800; line-height: 1.05; letter-spacing: -0.02em; margin-bottom: 8px; }
.hero-model { font-size: 16px; color: rgba(255,255,255,0.6); font-weight: 500; letter-spacing: 0.04em; margin-bottom: 4px; }
.hero-tagline { font-size: 18px; color: rgba(255,255,255,0.8); margin-bottom: 32px; max-width: 400px; }
.hero-pricing { display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
.hero-price { font-size: 48px; font-weight: 800; letter-spacing: -0.02em; }
.hero-price-unit { font-size: 16px; color: rgba(255,255,255,0.6); }
.hero-original { font-size: 16px; color: rgba(255,255,255,0.5); text-decoration: line-through; }
.hero-cta { display: inline-flex; align-items: center; gap: 10px; background: var(--wa); color: #fff; padding: 16px 36px; border-radius: 50px; font-size: 17px; font-weight: 700; transition: all 0.3s; box-shadow: 0 4px 20px rgba(37,211,102,0.35); }
.hero-cta:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(37,211,102,0.45); }
.hero-image { display: flex; align-items: center; justify-content: center; }
.hero-image img { max-height: 420px; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.3)); }
.img-text { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
.img-text.reverse { direction: rtl; }
.img-text.reverse > * { direction: ltr; }
.img-text-image { border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); }
.img-text-image img { width: 100%; }
.full-img { position: relative; width: 100%; min-height: 400px; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.full-img img { width: 100%; max-height: 560px; object-fit: cover; }
.colors-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-top: 32px; }
.color-card { text-align: center; background: var(--gray-50); border-radius: var(--radius-lg); padding: 32px 24px; border: 2px solid transparent; transition: border-color 0.3s; }
.color-card:hover { border-color: var(--blue); }
.color-swatch { width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 16px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); }
.color-name { font-size: 16px; font-weight: 600; color: var(--navy); }
.features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 40px; }
.feature-card { background: var(--white); border: 1px solid var(--gray-200); border-radius: var(--radius-lg); padding: 32px 24px; text-align: center; transition: all 0.3s; }
.feature-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--blue-light); }
.feature-card img { width: 120px; margin: 0 auto 20px; }
.feature-icon { font-size: 48px; margin: 0 auto 20px; }
.feature-name { font-size: 18px; font-weight: 700; color: var(--navy); margin-bottom: 8px; }
.feature-desc { font-size: 14px; color: var(--gray-500); line-height: 1.6; }
.filter-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 40px; }
.filter-step { text-align: center; padding: 32px 20px; background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--gray-200); }
.filter-step img { width: 64px; margin: 0 auto 20px; }
.filter-step-num { font-size: 12px; font-weight: 700; color: var(--blue); letter-spacing: 0.06em; margin-bottom: 8px; }
.filter-step h4 { font-size: 15px; font-weight: 700; color: var(--navy); margin-bottom: 8px; line-height: 1.3; }
.filter-step p { font-size: 13px; color: var(--gray-500); line-height: 1.5; }
.filter-code { font-size: 11px; color: var(--gray-400); margin-top: 6px; }
.specs-table { width: 100%; border-collapse: collapse; margin-top: 32px; }
.specs-table th, .specs-table td { padding: 16px 20px; text-align: left; border-bottom: 1px solid var(--gray-200); }
.specs-table th { width: 220px; font-size: 14px; font-weight: 600; color: var(--gray-500); background: var(--gray-50); white-space: nowrap; }
.specs-table td { font-size: 15px; color: var(--gray-800); line-height: 1.6; }
.pricing-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 32px; }
.pricing-card { background: var(--white); border: 2px solid var(--gray-200); border-radius: var(--radius-lg); padding: 36px 28px; transition: all 0.3s; }
.pricing-card.featured { border-color: var(--blue); box-shadow: 0 0 0 1px var(--blue), var(--shadow-lg); position: relative; }
.pricing-card.featured::before { content: 'POPULAR'; position: absolute; top: -13px; left: 50%; transform: translateX(-50%); background: var(--blue); color: #fff; padding: 4px 20px; border-radius: 50px; font-size: 12px; font-weight: 700; letter-spacing: 0.04em; }
.pricing-type { font-size: 14px; font-weight: 600; color: var(--blue); letter-spacing: 0.04em; margin-bottom: 8px; text-transform: uppercase; }
.pricing-amount { font-size: 42px; font-weight: 800; color: var(--navy); }
.pricing-unit { font-size: 14px; color: var(--gray-400); font-weight: 500; }
.pricing-bonus { display: inline-block; background: var(--blue-light); color: var(--blue); padding: 6px 14px; border-radius: 50px; font-size: 13px; font-weight: 600; margin: 12px 0; }
.pricing-list { list-style: none; margin-top: 16px; }
.pricing-list li { padding: 8px 0; font-size: 14px; color: var(--gray-600); border-bottom: 1px solid var(--gray-100); display: flex; justify-content: space-between; }
.pricing-list li:last-child { border-bottom: none; }
.pricing-list .price-val { font-weight: 600; color: var(--navy); }
.heart-service { background: linear-gradient(135deg, #f0f7ff 0%, #e8f4fd 100%); text-align: center; }
.heart-service img { max-width: 500px; margin: 0 auto 24px; }
.heart-service .section-desc { margin: 0 auto; }
.heart-service .btn-outline { display: inline-block; margin-top: 24px; padding: 12px 32px; border: 2px solid var(--blue); color: var(--blue); border-radius: 50px; font-weight: 600; transition: all 0.3s; }
.heart-service .btn-outline:hover { background: var(--blue); color: #fff; }
.ar-section { background: var(--navy); color: #fff; text-align: center; }
.ar-section .section-title { color: #fff; }
.ar-section .section-desc { color: rgba(255,255,255,0.7); margin: 0 auto; }
.ar-stores { display: flex; gap: 16px; justify-content: center; margin-top: 24px; }
.ar-stores img { height: 44px; }
.ar-phone { max-width: 300px; margin: 24px auto 0; }
.disclaimer { font-size: 12px; color: var(--gray-400); line-height: 1.7; margin-top: 16px; }
.gallery-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 32px; }
.gallery-strip img { border-radius: var(--radius); box-shadow: var(--shadow); transition: transform 0.3s; }
.gallery-strip img:hover { transform: scale(1.02); }
.footer { background: var(--gray-50); border-top: 1px solid var(--gray-200); padding: 40px 0; text-align: center; }
.footer-links { display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; margin-bottom: 16px; }
.footer-links a { font-size: 13px; color: var(--gray-500); transition: color 0.2s; }
.footer-links a:hover { color: var(--blue); }
.footer-copy { font-size: 12px; color: var(--gray-400); }
.float-wa { position: fixed; bottom: 24px; right: 24px; z-index: 200; background: var(--wa); color: #fff; width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 20px rgba(37,211,102,0.4); transition: all 0.3s; font-size: 24px; }
.float-wa:hover { transform: scale(1.1); }
.uv-stats { display: flex; gap: 24px; justify-content: center; margin-top: 24px; flex-wrap: wrap; }
.uv-stat { text-align: center; padding: 24px; background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--gray-200); min-width: 200px; }
.uv-stat-num { font-size: 32px; font-weight: 800; color: var(--blue); }
.uv-stat-label { font-size: 14px; color: var(--gray-500); margin-top: 4px; }
.temp-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-top: 32px; }
.temp-card { text-align: center; padding: 24px 16px; background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--gray-200); transition: all 0.3s; }
.temp-card:hover { border-color: var(--blue); transform: translateY(-3px); box-shadow: var(--shadow); }
.temp-deg { font-size: 28px; font-weight: 800; color: var(--navy); }
.temp-use { font-size: 13px; color: var(--gray-500); margin-top: 8px; }
.video-thumb { position: relative; border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-lg); cursor: pointer; }
.video-thumb img { width: 100%; }
.video-play-btn { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); width: 72px; height: 72px; background: rgba(0,0,0,0.6); border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.video-play-btn::after { content: ''; display: block; width: 0; height: 0; border-left: 24px solid #fff; border-top: 14px solid transparent; border-bottom: 14px solid transparent; margin-left: 6px; }
.ombak-temp-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 32px; }
.ombak-temp-card { text-align: center; padding: 32px 16px; background: var(--white); border-radius: var(--radius-lg); border: 1px solid var(--gray-200); transition: all 0.3s; }
.ombak-temp-card:hover { border-color: var(--blue); transform: translateY(-3px); box-shadow: var(--shadow); }
.ombak-temp-deg { font-size: 36px; font-weight: 800; color: var(--navy); margin-bottom: 8px; }
.ombak-temp-use { font-size: 15px; color: var(--gray-500); }
@media (max-width: 768px) {
  .section { padding: 48px 0; }
  .hero { min-height: auto; padding: 60px 0 40px; }
  .hero .container { grid-template-columns: 1fr; gap: 32px; text-align: center; }
  .hero-tagline { margin: 0 auto 32px; }
  .hero-pricing { justify-content: center; }
  .hero-cta { margin: 0 auto; }
  .hero-image img { max-height: 300px; }
  .img-text { grid-template-columns: 1fr; gap: 32px; }
  .img-text.reverse { direction: ltr; }
  .features-grid { grid-template-columns: 1fr; }
  .filter-steps { grid-template-columns: repeat(2, 1fr); }
  .pricing-grid { grid-template-columns: 1fr; }
  .colors-grid { grid-template-columns: 1fr; }
  .temp-grid { grid-template-columns: repeat(2, 1fr); }
  .ombak-temp-grid { grid-template-columns: 1fr; }
  .specs-table th { width: 140px; font-size: 13px; }
  .specs-table td { font-size: 13px; }
  .gallery-strip { grid-template-columns: repeat(2, 1fr); }
  .nav-logo { font-size: 18px; }
  .nav-cta { padding: 8px 16px; font-size: 13px; }
  .hero h1 { font-size: 32px; }
  .hero-price { font-size: 36px; }
}
@media (max-width: 480px) {
  .container { padding: 0 16px; }
  .filter-steps { grid-template-columns: 1fr; }
  .temp-grid { grid-template-columns: 1fr; }
  .gallery-strip { grid-template-columns: 1fr; }
}
'''

FOOTER = '''<footer class="footer">
  <div class="container">
    <div class="footer-links">
      <a href="#">FAQ</a><a href="#">Terms of Use</a><a href="#">Privacy Notice</a>
      <a href="#">Governance</a><a href="#">Warranty Policy</a><a href="#">Support</a>
    </div>
    <p class="footer-copy">COWAY (MALAYSIA) \u00a9 2026. ALL RIGHTS RESERVED. (735420-H) (AJL931694)</p>
  </div>
</footer>'''

FLOAT_WA = '''<a href="{wa_text}" class="float-wa" target="_blank" aria-label="WhatsApp">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>'''

HEART_SERVICE = '''<section class="section heart-service">
  <div class="container">
    <img src="https://www.coway.com.my/files/Products/water-purifier/villaem3/coway-heart-service.jpg" alt="Coway Heart Service" loading="lazy">
    <p class="section-label">Service</p>
    <h2 class="section-title">Protected by Complimentary Care Service</h2>
    <p class="section-desc">Every Coway product comes with complimentary Heart Service \u2014 regular maintenance by certified technicians. *Terms and conditions apply.</p>
    <a href="https://wa.me/60137227961?text=Saya%20nak%20tanya%20pasal%20Coway%20Heart%20Service" class="btn-outline" target="_blank">LEARN MORE</a>
  </div>
</section>'''

AR_SECTION = '''<section class="section ar-section">
  <div class="container">
    <p class="section-label" style="color:rgba(255,255,255,0.6);">AR Experience</p>
    <h2 class="section-title">Use Coway AR to See<br>{product} in Your Home</h2>
    <p class="section-desc">and unlock the unlimited possibilities with Coway products.</p>
    <div class="ar-stores">
      <img src="https://www.coway.com.my/files/Products/mattress/primelite/an-image-of-download-on-the-app-store-for-coway-ar-app.png" alt="Download on App Store" loading="lazy">
      <img src="https://www.coway.com.my/files/Products/mattress/primelite/an-image-of-get-it-on-google-play-for-coway-ar-app.png" alt="Get it on Google Play" loading="lazy">
    </div>
    <div class="ar-phone">
      <img src="https://www.coway.com.my/files/Products/mattress/primelite/a-screenshot-of-the-coway-ar-app-on-a-mobile-phone.png" alt="Coway AR App" loading="lazy">
    </div>
  </div>
</section>'''

DISCLAIMER = '''<p class="disclaimer">\u00b9The recommended filter replacement period is based on standard usage conditions. In cases where the filter lifespan is affected by external factors (e.g. poor water quality, abnormal usage or environmental conditions), additional filters may be provided and replaced as needed, without affecting the standard replacement cycle. We reserve the right to charge for any additional filters provided due to such factors beyond the standard replacement cycle.</p>'''

PRICING_DISC = '''<p class="disclaimer" style="margin-top:16px;">*The 3+2 plan carries a minimum obligation period of 3 years, with an optional 2 year extension during which the product may be returned without penalties. While the 5 year, 7 year, and 9 year plans are full-term obligations, and early terminations will result in penalties.<br><br>Prices displayed include SST and are subject to change without prior notice. Promotions, product availability, specifications, and service schedules may vary by model and may be updated without notice. Coway reserves the right to revise or withdraw prices, offers, and service packages at its discretion. Product images are for illustration only and may differ from actual items.</p>'''

print(f"Common components loaded. CSS: {len(COMMON_CSS)} chars")
