"""Parse HTML files from lovdata.no and extract readable text."""
import re
import sys

def parse_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove script and style tags
    html_clean = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html_clean = re.sub(r'<style[^>]*>.*?</style>', '', html_clean, flags=re.DOTALL)
    html_clean = re.sub(r'<noscript[^>]*>.*?</noscript>', '', html_clean, flags=re.DOTALL)

    html_clean = re.sub(r'<br\s*/?>', '\n', html_clean)
    html_clean = re.sub(r'<p[^>]*>', '\n', html_clean)
    html_clean = re.sub(r'</p>', '\n', html_clean)
    html_clean = re.sub(r'<div[^>]*>', '\n', html_clean)
    html_clean = re.sub(r'</div>', '\n', html_clean)
    html_clean = re.sub(r'<h[1-6][^>]*>', '\n## ', html_clean)
    html_clean = re.sub(r'</h[1-6]>', '\n', html_clean)
    html_clean = re.sub(r'<li[^>]*>', '\n- ', html_clean)
    html_clean = re.sub(r'<[^>]+>', '', html_clean)

    replacements = {
        '&amp;': '&', '&lt;': '<', '&gt;': '>', '&nbsp;': ' ',
        '&#167;': '§', '&mdash;': '—', '&ndash;': '–', '&quot;': '"',
        '&#39;': "'", '&oslash;': 'ø', '&aring;': 'å', '&aelig;': 'æ',
        '&Oslash;': 'Ø', '&Aring;': 'Å', '&Aelig;': 'Æ',
        '&#230;': 'æ', '&#248;': 'ø', '&#229;': 'å',
        '&#198;': 'Æ', '&#216;': 'Ø', '&#197;': 'Å',
    }
    for k, v in replacements.items():
        html_clean = html_clean.replace(k, v)

    lines = [l.strip() for l in html_clean.split('\n')]
    lines = [l for l in lines if l]
    text = '\n'.join(lines)
    return text

if __name__ == "__main__":
    filepath = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 15000
    text = parse_html(filepath)
    sys.stdout.buffer.write(text[:limit].encode('utf-8', errors='replace'))
    sys.stdout.buffer.write(b'\n')
