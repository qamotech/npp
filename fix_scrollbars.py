import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to change all overflow-x: hidden !important; to overflow: visible !important; EXCEPT for html and body
    
    css_fix = """
    /* Fix for touch scroll blocking */
    @media(max-width: 767px) {
      .wrap, .hero-stack, .hero-intro, .hero-container, .reactor, .proof-row {
        overflow: visible !important;
        overflow-x: visible !important;
        overflow-y: visible !important;
      }
      .proof-row {
        flex-wrap: wrap !important;
      }
    }
"""

    if "/* Fix for touch scroll blocking */" not in content:
        content = content.replace('</style>', css_fix + '\\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied scrollblock fix.")

if __name__ == '__main__':
    main()
