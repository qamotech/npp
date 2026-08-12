import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Fix for the user's specific selected element to fit in mobile view */
    @media(max-width: 767px) {
      main#main:nth-of-type(1) > section:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) {
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        padding-left: 16px !important;
        padding-right: 16px !important;
        overflow-x: hidden !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
      }
      
      main#main:nth-of-type(1) > section:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > * {
        max-width: 100% !important;
        box-sizing: border-box !important;
      }

      /* Fix the text from overflowing */
      main#main:nth-of-type(1) > section:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > h1 {
        font-size: clamp(2.2rem, 9vw, 3rem) !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        hyphens: auto !important;
        white-space: normal !important;
      }
      
      main#main:nth-of-type(1) > section:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > .proof-row {
        flex-wrap: wrap !important;
        justify-content: center !important;
        overflow-x: hidden !important;
      }
    }
"""

    if "/* Fix for the user's specific selected element" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied user selector fix.")

if __name__ == '__main__':
    main()
