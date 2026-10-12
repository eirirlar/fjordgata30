#!/usr/bin/env python
"""
Extract verbatim law texts from lovdata.no for Fjordgata 30 project.
Fetches and verifies: fvl §§ 28, 35, 36; tvl §§ 34-1, 34-2; EMK P1-1.
Run from project root: uv run python scripts/extract_lovdata_laws.py
"""

import re
import subprocess
import os
import sys
import tempfile

sys.stdout.reconfigure(encoding='utf-8')

TMPDIR = tempfile.gettempdir()

def fetch_url(url, filename):
    outfile = os.path.join(TMPDIR, filename)
    result = subprocess.run(
        ['curl', '-s', '--max-time', '30', '-L', url,
         '-H', 'Accept: text/html',
         '-H', 'User-Agent: Mozilla/5.0',
         '-o', outfile],
        capture_output=True
    )
    if result.returncode == 0 and os.path.exists(outfile):
        return outfile
    return None

def fetch_pdf(url, filename):
    outfile = os.path.join(TMPDIR, filename)
    result = subprocess.run(
        ['curl', '-s', '--max-time', '60', '-L', url,
         '-H', 'User-Agent: Mozilla/5.0',
         '-o', outfile],
        capture_output=True
    )
    if result.returncode == 0 and os.path.exists(outfile):
        return outfile
    return None

def pdf_to_text(pdf_file):
    result = subprocess.run(
        ['pdftotext', '-layout', pdf_file, '-'],
        capture_output=True
    )
    if result.returncode == 0:
        raw = result.stdout
        # Try latin1 first (common for Norwegian PDFs)
        try:
            return raw.decode('latin1')
        except:
            return raw.decode('utf-8', errors='replace')
    return None

def clean_html(text):
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&lt;', '<', text)
    text = re.sub(r'&gt;', '>', text)
    text = re.sub(r'&#[x0-9a-fA-F]+;', '', text)
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r'\n +', '\n', text)
    return text.strip()

def extract_from_html(filepath, marker, max_len=5000):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    idx = content.find(marker)
    if idx < 0:
        return None
    snippet = content[max(0, idx-500):idx+max_len]
    return clean_html(snippet)

def extract_from_text(text, marker, max_len=2000):
    idx = text.find(marker)
    if idx < 0:
        return None
    return text[max(0, idx-200):idx+max_len]


def main():
    results = {}

    # ========== FVL § 28 ==========
    print("Fetching fvl § 28...")
    f = fetch_url('https://lovdata.no/lov/1967-02-10/%C2%A728', 'fvl28_ld.html')
    if f:
        text = extract_from_html(f, 'Enkeltvedtak kan påklages av en part eller annen')
        if text:
            idx = text.find('§ 28.')
            if idx < 0:
                idx = text.find('Enkeltvedtak kan påklages')
            text = text[max(0, idx-10):]
            end = text.find('§ 29.', 50)
            if end > 0:
                text = text[:end]
            results['fvl_28'] = {
                'text': text.strip(),
                'url': 'https://lovdata.no/lov/1967-02-10/%C2%A728',
                'method': 'curl direct HTML, lovdata.no'
            }
            print(f"  OK ({len(results['fvl_28']['text'])} chars)")
        else:
            print("  FAILED to extract text")
            results['fvl_28'] = None
    else:
        print("  FAILED to fetch")
        results['fvl_28'] = None

    # ========== FVL § 35 ==========
    print("Fetching fvl § 35...")
    f = fetch_url('https://lovdata.no/lov/1967-02-10/%C2%A735', 'fvl35_ld.html')
    if f:
        text = extract_from_html(f, 'Et forvaltningsorgan kan omgjøre sitt eget vedtak uten at det er påklaget')
        if text:
            idx = text.find('§ 35.')
            if idx < 0:
                idx = text.find('omgjøring av vedtak uten klage')
            text = text[max(0, idx-10):]
            end = text.find('§ 36.', 50)
            if end > 0:
                text = text[:end]
            results['fvl_35'] = {
                'text': text.strip(),
                'url': 'https://lovdata.no/lov/1967-02-10/%C2%A735',
                'method': 'curl direct HTML, lovdata.no'
            }
            print(f"  OK ({len(results['fvl_35']['text'])} chars)")
        else:
            print("  FAILED")
            results['fvl_35'] = None
    else:
        results['fvl_35'] = None

    # ========== FVL § 36 ==========
    print("Fetching fvl § 36...")
    f = fetch_url('https://lovdata.no/lov/1967-02-10/%C2%A736', 'fvl36_ld.html')
    if f:
        text = extract_from_html(f, 'Når et vedtak blir endret til gunst for en part')
        if text:
            idx = text.find('§ 36.')
            if idx < 0:
                idx = text.find('sakskostnader')
            text = text[max(0, idx-10):]
            end = text.find('§ 37.', 50)
            if end > 0:
                text = text[:end]
            results['fvl_36'] = {
                'text': text.strip(),
                'url': 'https://lovdata.no/lov/1967-02-10/%C2%A736',
                'method': 'curl direct HTML, lovdata.no'
            }
            print(f"  OK ({len(results['fvl_36']['text'])} chars)")
        else:
            print("  FAILED")
            results['fvl_36'] = None
    else:
        results['fvl_36'] = None

    # ========== TVL §§ 34-1 and 34-2 ==========
    print("Fetching tvl §§ 34-1 and 34-2...")
    f = fetch_url('https://lovdata.no/lov/2005-06-17-90/%C2%A734-1', 'tvl341_ld.html')
    if f:
        text = extract_from_html(f, 'Midlertidig forføyning kan besluttes:', max_len=4000)
        if text:
            idx = text.find('§ 34-1')
            if idx < 0:
                idx = text.find('Sikringsgrunn')
            text = text[max(0, idx-20):]
            end = text.find('§ 34-3', 100)
            if end > 0:
                text = text[:end]
            results['tvl_34-1'] = {
                'text': text.strip(),
                'url': 'https://lovdata.no/lov/2005-06-17-90/%C2%A734-1',
                'method': 'curl direct HTML, lovdata.no'
            }
            print(f"  OK tvl 34-1+34-2 ({len(results['tvl_34-1']['text'])} chars)")
            # Extract 34-2 from same text
            idx2 = text.find('§ 34-2')
            if idx2 > 0:
                text2 = text[idx2:]
                end2 = text2.find('§ 34-3', 50)
                if end2 > 0:
                    text2 = text2[:end2]
                results['tvl_34-2'] = {
                    'text': text2.strip(),
                    'url': 'https://lovdata.no/lov/2005-06-17-90/%C2%A734-2',
                    'method': 'curl direct HTML, lovdata.no (same page as 34-1)'
                }
                print(f"  OK tvl 34-2 ({len(results['tvl_34-2']['text'])} chars)")
            else:
                results['tvl_34-2'] = None
        else:
            print("  FAILED - extracting with alternative marker")
            text = extract_from_html(f, '§ 34-1. Sikringsgrunn')
            if text:
                results['tvl_34-1'] = {'text': text[:3000], 'url': 'https://lovdata.no/lov/2005-06-17-90/%C2%A734-1', 'method': 'curl direct HTML'}
            else:
                results['tvl_34-1'] = None
            results['tvl_34-2'] = None
    else:
        results['tvl_34-1'] = None
        results['tvl_34-2'] = None

    # ========== EMK P1-1 ==========
    print("Fetching EMK P1-1...")
    emk_pdf = fetch_pdf(
        'https://www.echr.coe.int/documents/d/echr/Convention_NOR',
        'emk_coe_nor.pdf'
    )
    if emk_pdf:
        text = pdf_to_text(emk_pdf)
        if text:
            idx = text.find('Vern om eiendom')
            if idx >= 0:
                snippet = text[max(0, idx-600):idx+600]
                # Fix encoding issues
                results['emk_p1-1'] = {
                    'text': snippet.strip(),
                    'url': 'https://www.echr.coe.int/documents/d/echr/Convention_NOR',
                    'method': 'Council of Europe official PDF + pdftotext (Norwegian official text)'
                }
                print(f"  OK EMK P1-1 ({len(results['emk_p1-1']['text'])} chars)")
            else:
                print("  FAILED - article text not found in PDF")
                results['emk_p1-1'] = None
        else:
            print("  FAILED - pdftotext failed")
            results['emk_p1-1'] = None
    else:
        print("  FAILED - could not fetch PDF")
        results['emk_p1-1'] = None

    # ========== OUTPUT ==========
    print("\n\n=== VERBATIM TEXTS ===\n")
    for name, r in results.items():
        print(f"\n{'='*60}")
        print(f"LAW: {name}")
        if r:
            print(f"SOURCE: {r['url']}")
            print(f"METHOD: {r['method']}")
            print(f"TEXT:\n{r['text']}")
        else:
            print("STATUS: FAILED")

    return results


if __name__ == '__main__':
    main()
