import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_injection = """
    @media(max-width: 767px) {
      .nav {
        justify-content: center;
        position: relative;
      }
      .head-actions {
        position: absolute;
        right: 16px;
      }
      .brand-name {
        display: none;
      }
      .site-header {
        border-bottom: none;
        box-shadow: none;
        background: transparent;
      }
      .hero {
        padding-top: 0;
      }
    }
"""

    if "/* Mobile header tweak */" not in content:
        content = content.replace('</style>', css_injection + '\n/* Mobile header tweak */\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated header for mobile.")

if __name__ == '__main__':
    main()
