import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Fix for hero intro */
    @media(max-width: 767px) {
      main#main > section.hero > div > div.hero-intro {
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 16px;
      }
      main#main > section.hero > div > div.hero-intro h1 {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
      }
      main#main > section.hero > div > div.hero-intro .hero-copy {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
      }
      main#main > section.hero > div > div.hero-intro .actions {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }
      main#main > section.hero > div > div.hero-intro .actions .btn {
        width: 100%;
        max-width: 320px;
      }
    }
"""

    if "/* Fix for hero intro */" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed hero intro styles.")

if __name__ == '__main__':
    main()
