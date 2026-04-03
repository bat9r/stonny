import sys
import urllib.request

def fetch_content(target_url):
    jina_url = f"https://r.jina.ai/{target_url}"
    try:
        req = urllib.request.Request(jina_url, headers={'User-Agent': 'StonnyAgent/1.0'})
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {target_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_content(sys.argv[1])
    else:
        print("Error: Provide a target URL as an argument.")
