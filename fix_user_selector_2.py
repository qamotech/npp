import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Focus Mode targeted element (services section wrap) */
    main#main:nth-of-type(1) > div:nth-of-type(2) > section#services:nth-of-type(1) > div:nth-of-type(1) {
        overflow-x: clip !important;
        overflow-y: visible !important;
        /* Disable touch actions that might cause scroll interference on this container */
        touch-action: pan-y !important;
        overscroll-behavior: none !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        padding-left: 16px !important;
        padding-right: 16px !important;
    }
"""

    if "/* Focus Mode targeted element (services section wrap) */" not in content:
        content = content.replace('</style>', css_fix + '\\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied user selector fix 2.")

if __name__ == '__main__':
    main()
