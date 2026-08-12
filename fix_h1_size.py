import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Specific fix for hero h1 mobile font size */
    @media(max-width: 767px) {
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro > h1 {
        font-size: clamp(2.2rem, 8vw, 3.2rem) !important;
        white-space: normal !important;
        line-height: 1.1 !important;
        margin-bottom: 12px !important;
        width: 100% !important;
        padding: 0 16px !important;
        box-sizing: border-box !important;
      }
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro {
        padding-left: 0 !important;
        padding-right: 0 !important;
      }
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro > p.hero-copy {
        padding: 0 16px !important;
        font-size: 1rem !important;
      }
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro > p.kicker {
        padding: 0 16px !important;
      }
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro > .actions {
        padding: 0 16px !important;
      }
      main#main > section.hero > div.wrap.hero-stack > div.hero-intro > .proof-row {
        margin-left: 16px !important;
        margin-right: 16px !important;
        width: calc(100% - 32px) !important;
      }
    }
"""

    if "/* Specific fix for hero h1" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed h1 size.")

if __name__ == '__main__':
    main()
