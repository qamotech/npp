import sys

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_injection = """
  <!-- Mobile Nav Script -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const navLinks = document.querySelectorAll('.mobile-bottom-nav a');
      const sections = Array.from(navLinks).map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);
      
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            navLinks.forEach(a => {
              if (a.getAttribute('href') === '#' + entry.target.id) {
                a.style.color = 'var(--cyan)';
              } else {
                a.style.color = '';
              }
            });
          }
        });
      }, { threshold: 0.3 });
      
      sections.forEach(sec => observer.observe(sec));
    });
  </script>
"""

    if "<!-- Mobile Nav Script -->" not in content:
        content = content.replace('</body>', js_injection + '\n</body>')
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Injected JS.")

if __name__ == '__main__':
    main()
