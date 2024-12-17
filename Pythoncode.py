import requests

targets = [
    "www.google.com","www.youtube.com""https://brightspace.uakron.edu/d2l/home"
]

for target in targets:
    if target.startswith("http://") or target.startswith("https://"):
        headers = requests.get(target).headers
        if 'X-Frame-Options' in headers:
            print(target + "NOT VULNERABLE")
        else:
            print(target + "VULNERABLE")
    else:
        with open(target, 'r') as file:
            html_content = file.read()
        if 'X-Frame-Options' in html_content:
            print(target + "NOT VULNERABLE")
        else:
            print(target + "VULNERABLE")
            
