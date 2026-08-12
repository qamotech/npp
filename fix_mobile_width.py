import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Fix for mobile width overflow */
    @media(max-width: 767px) {
      main#main > section.hero {
        width: 100%;
        max-width: 100vw;
        overflow-x: hidden;
        box-sizing: border-box;
      }
      main#main > section.hero > div > div.hero-intro {
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
      }
      main#main > section.hero > div > div.hero-intro .proof-row {
        width: 100%;
        max-width: 100%;
        /* Enable smooth horizontal scrolling within the bounded container */
        -webkit-overflow-scrolling: touch; 
      }
      main#main > section.hero > div > div.hero-intro h1,
      main#main > section.hero > div > div.hero-intro p {
        width: 100%;
        max-width: 100%;
        word-wrap: break-word;
        overflow-wrap: break-word;
      }
    }
"""

    if "/* Fix for mobile width overflow */" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed mobile width overflow.")

if __name__ == '__main__':
    main()
