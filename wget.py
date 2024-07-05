import os.path
import requests


def url_download_save(url):
    if url.endswith("/"):
        basename = "index.html"
    else:
        basename = os.path.basename(url)

    response = requests.get(url)

    if response.status_code == 200:
        with open(basename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded and saved as {basename}")
    else:
        print(f"Failed to download URL: {url}. Status code: {response.status_code}")


# Example usage:
url = "https://chatgpt.com/c/7244724a-0df6-4510-83fd-3d4bee2b9c3c"
url_download_save(url)
