import urllib.request

# Liest Inhalt von URL in eine Datei
urllib.request.urlretrieve \
   ("http://localhost/Python34/url_lesen.htm",
    "url_kopieren.htm")

