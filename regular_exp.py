import re

def slug(name):
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip("-")
    slug = re.sub(r'-', "-", slug,2 )

    print(slug)

name = "!nizam --mudhe--e--"
slug(name)