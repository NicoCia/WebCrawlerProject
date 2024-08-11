def adapt_url_to_be_valid(url: str) -> str:
    if not url.endswith('/'):
        url = f"{url}/"

    if not (url.startswith("http://") or url.startswith("https://")):
        url = f"https://{url}"

    return url
