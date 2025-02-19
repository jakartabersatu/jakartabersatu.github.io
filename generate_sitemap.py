import os
from datetime import datetime
import pytz  # Tambahkan pustaka pytz untuk mengatur zona waktu

# URL dasar situs GitHub Pages Anda
BASE_URL = "https://jakartabersatu.github.io"

# Folder tempat artikel disimpan (ubah jika berbeda)
CONTENT_DIR = "."

# Template dasar sitemap
SITEMAP_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
{}
</urlset>
"""

# Fungsi untuk membuat entri sitemap berdasarkan file yang ada
def generate_sitemap():
    url_entries = []

    # Atur zona waktu ke Jakarta (GMT+7)
    jakarta_tz = pytz.timezone("Asia/Jakarta")

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            # Abaikan file GSC (google-verification.html, google*.html)
            if file.startswith("google") and file.endswith(".html"):
                continue  

            # Buat URL untuk homepage tanpa index.html
            if file == "index.html":
                file_url = BASE_URL  # Homepage tanpa index.html
            elif file.endswith(".html"):
                file_path = os.path.relpath(os.path.join(root, file), CONTENT_DIR)
                file_url = f"{BASE_URL}/{file_path.replace(os.sep, '/')}"

            else:
                continue  # Lewati jika bukan file HTML

            # Waktu terakhir diperbarui dalam zona waktu Jakarta
            lastmod = datetime.now(jakarta_tz).strftime("%Y-%m-%dT%H:%M:%S+07:00")

            url_entry = f"""  <url>
    <loc>{file_url}</loc>
    <lastmod>{lastmod}</lastmod>
  </url>"""

            url_entries.append(url_entry)

    sitemap_content = SITEMAP_TEMPLATE.format("\n".join(url_entries))

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print("✅ Sitemap berhasil diperbarui dengan waktu GMT+7!")

if __name__ == "__main__":
    generate_sitemap()
