import json
import sys

from .page import Page

def main():
    try:
        page_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        print('File is invalid JSON format')
        return
    if not isinstance(page_data, dict):
        print('JSON object must be a dictionary', file=sys.stderr)
        return
    Page(page_data).print()

if __name__ == '__main__':
    main()
