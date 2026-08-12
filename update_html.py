import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_injection = """
    /* --- MOBILE APP STYLES --- */
    .mobile-bottom-nav {
      display: flex;
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      background: color-mix(in srgb, var(--bg2) 94%, transparent);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-top: 1px solid var(--line);
      z-index: 90;
      justify-content: space-around;
      align-items: center;
      padding-bottom: env(safe-area-inset-bottom, 16px);
      height: calc(64px + env(safe-area-inset-bottom, 0px));
      box-shadow: 0 -4px 24px rgba(0,0,0,.08);
    }
    .mobile-bottom-nav a {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--muted);
      gap: 5px;
      flex: 1;
      height: 100%;
      transition: color 0.2s, transform 0.2s;
    }
    .mobile-bottom-nav a:active {
      transform: scale(0.95);
    }
    .mobile-bottom-nav a.active, .mobile-bottom-nav a:hover {
      color: var(--cyan);
    }
    .mobile-bottom-nav svg {
      width: 24px;
      height: 24px;
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }
    @media(min-width: 768px) {
      .mobile-bottom-nav {
        display: none;
      }
    }
    @media(max-width: 767px) {
      body {
        padding-bottom: calc(64px + env(safe-area-inset-bottom, 16px));
      }
      .menu-button, .mobile-menu {
        display: none !important;
      }
      /* Improve touch targets and card sizes on mobile */
      .card, .service-card, .tool-card {
        border-radius: 20px;
        padding: 24px;
      }
      .btn {
        min-height: 56px;
        font-size: 1.05rem;
      }
      .hero {
        padding-top: 40px;
        padding-bottom: 20px;
      }
      .hero h1 {
        font-size: clamp(2.8rem, 12vw, 4rem);
      }
    }
    /* ------------------------- */
"""

    html_injection = """
  <nav class="mobile-bottom-nav" aria-label="Bottom Navigation">
    <a href="#services">
      <svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
      <span>Services</span>
    </a>
    <a href="#studio">
      <svg viewBox="0 0 24 24"><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c4.1 0 7.62-2.46 9.17-6.04.42-1.01-.22-2.14-1.32-2.43l-1.92-.51c-1.12-.3-1.85-1.42-1.63-2.56l.46-2.48c.2-.1-.08-2.22-1.02-3.32C14.77 3.52 13.43 2 12 2z"/></svg>
      <span>Studio</span>
    </a>
    <a href="#tools">
      <svg viewBox="0 0 24 24"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>
      <span>Tools</span>
    </a>
    <a href="#quote" style="color: var(--cyan);">
      <svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
      <span>Estimate</span>
    </a>
  </nav>
"""

    if "/* --- MOBILE APP STYLES --- */" not in content:
        # Inject CSS
        content = content.replace('</style>', css_injection + '\n</style>', 1)
        
        # Inject HTML
        content = content.replace('</body>', html_injection + '\n</body>')

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully injected mobile-first styles and bottom nav.")
    else:
        print("Already injected.")

if __name__ == '__main__':
    main()
