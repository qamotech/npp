import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Fix for top banner image */
    main#main > section#top > div > img {
      display: block;
      width: 100%;
      height: auto;
      object-fit: cover;
    }
    
    @media(max-width: 767px) {
      main#main > section#top > div > img {
        border-bottom-left-radius: 24px;
        border-bottom-right-radius: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
      }
    }
"""

    if "/* Fix for top banner image */" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed top banner image styles.")

if __name__ == '__main__':
    main()
