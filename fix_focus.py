import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    css_fix = """
    /* Focus Mode targeted elements */
    main#main:nth-of-type(1) > div:nth-of-type(2) > section#work:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2) > article:nth-of-type(1) > img:nth-of-type(1),
    main#main:nth-of-type(1) > div:nth-of-type(2) > section#work:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2) > article:nth-of-type(2) > img:nth-of-type(1),
    main#main:nth-of-type(1) > div:nth-of-type(2) > section#work:nth-of-type(4) > div:nth-of-type(1) > div:nth-of-type(2) > article:nth-of-type(3) > img:nth-of-type(1) {
        width: 100% !important;
        height: 220px !important;
        object-fit: cover !important;
        display: block !important;
        background-color: var(--panel) !important;
    }
"""

    if "/* Focus Mode targeted elements */" not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied focus mode fix.")

if __name__ == '__main__':
    main()
