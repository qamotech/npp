import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Global touch-action fix for all sections to prevent horizontal scroll lock */
    @media(max-width: 767px) {
        .wrap, section, .section, main, body, html {
            touch-action: pan-y !important;
            overscroll-behavior-x: none !important;
            overflow-x: clip !important;
        }
    }
"""

    if "/* Global touch-action fix for all sections" not in content:
        content = content.replace('</style>', css_fix + '\\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied global touch fix.")

if __name__ == '__main__':
    main()
