import markdown, sys
src = r"C:\Users\31514\Desktop\3024\REPORT.md"
dst = r"C:\Users\31514\Desktop\3024\REPORT.html"
md = open(src, encoding="utf-8").read()
body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])
css = """
body { font-family: 'Segoe UI', Arial, sans-serif; max-width: 820px; margin: 40px auto; line-height: 1.55; color: #1a1a1a; }
h1 { border-bottom: 2px solid #333; padding-bottom: 8px; }
h2 { margin-top: 28px; border-bottom: 1px solid #ccc; padding-bottom: 4px; }
h3 { margin-top: 20px; }
table { border-collapse: collapse; margin: 14px 0; width: 100%; font-size: 14px; }
th, td { border: 1px solid #bbb; padding: 6px 10px; text-align: left; }
th { background: #f0f0f0; }
code { background: #f4f4f4; padding: 1px 4px; border-radius: 3px; font-family: Consolas, monospace; font-size: 13px; }
pre { background: #f4f4f4; padding: 10px; overflow-x: auto; }
blockquote { border-left: 4px solid #ccc; margin-left: 0; padding-left: 12px; color: #555; }
a { color: #0366d6; }
"""
html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>AI Assignment #2 Report</title>
<style>{css}</style></head><body>{body}</body></html>"""
open(dst, "w", encoding="utf-8").write(html)
print("wrote", dst, len(html), "bytes")
