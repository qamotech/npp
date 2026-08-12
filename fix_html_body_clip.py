import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Global body clip */
    html, body {
      overflow-x: clip !important;
    }
"""
    if "/* Global body clip */" not in content:
        content = content.replace('</style>', css_fix + '\\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied html body clip.")

if __name__ == '__main__':
    main()
