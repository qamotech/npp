import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Use clip to prevent touch block */
    @media(max-width: 767px) {
      .wrap, .hero-stack, .hero-intro, .hero-container, .reactor, .proof-row, .service-grid, .service-card, .section {
        overflow-x: clip !important;
      }
      .proof-row {
        flex-wrap: wrap !important;
      }
    }
"""
    if "/* Use clip to prevent touch block */" not in content:
        content = content.replace('</style>', css_fix + '\\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied clip fix.")

if __name__ == '__main__':
    main()
