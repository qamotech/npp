import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Global mobile overflow prevention */
    @media(max-width: 767px) {
      html, body {
        overflow-x: hidden !important;
        width: 100vw !important;
        max-width: 100vw !important;
      }
      .wrap, .hero-stack, .hero-intro {
        min-width: 0 !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
      }
      .reactor, .hero-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
      }
    }
"""

    if "/* Global mobile overflow prevention */" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied global overflow fix.")

if __name__ == '__main__':
    main()
