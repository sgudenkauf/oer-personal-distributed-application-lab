
#!/usr/bin/env python3

"""
mdBook YAML front matter preprocessor.

Reads YAML frontmatter from Markdown sections and replaces it with an
HTML table. The preprocessor is fault-tolerant and handles
empty values as well as YAML parsing errors without interrupting the build. Uses
the external PyYAML library.
"""

import yaml                 # PyYAML (Nicht Teil der Standardbibliothek!)
import re                   # Reguläre Ausdrücke
import sys                  # Systemfunktionen
import json                 # JSON-Verarbeitung
from html import escape     # HTML-Escaping
import pprint               # Formatierte Debug-Auasgabe


FRONTMATTER_PATTERN = re.compile(
    r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n?",
    re.DOTALL,
)


def format_value(value):
    """
    Wandelt Python-Werte in lesbaren HTML-Text um.
    """
    if value is None:
        return ""

    if isinstance(value, list):
        return ", ".join(str(v) for v in value)

    return str(value)


def frontmatter_to_html(data):
    """
    Generates an HTML table from the front matter data.
    """

    rows = []

    for key, value in data.items():
        rows.append(
            f"""
<tr>
    <th>{escape(str(key))}</th>
    <td>{escape(format_value(value))}</td>
</tr>
"""
        )

    return f"""
<style>
.frontmatter-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1.5rem;
}}

.frontmatter-table th,
.frontmatter-table td {{
    border: 1px solid var(--table-border-color, #444);
    padding: 0.5rem;
}}

.frontmatter-table th {{
    text-align: left;
    width: 25%;
}}
</style>

<table class="frontmatter-table">
{''.join(rows)}
</table>
"""


def process_content(content):
    """
    Replaces YAML front matter with an HTML table.
    """
    match = FRONTMATTER_PATTERN.match(content)

    if not match:
        return content

    yaml_text = match.group(1)

    try:
        data = yaml.safe_load(yaml_text)

        if not isinstance(data, dict):
            return content

    except Exception as exc:
        print(
            f"[frontmatter] YAML-Fehler: {exc}",
            file=sys.stderr,
        )
        return content

    html = frontmatter_to_html(data)

    return html + "\n\n" + content[match.end():].lstrip()


def process_chapter(chapter):
    """
    Processes chapters and subchapters recursively.
    """
    if "content" in chapter:
        chapter["content"] = process_content(chapter["content"])

    for sub_item in chapter.get("sub_items", []):
        if "Chapter" in sub_item:
            process_chapter(sub_item["Chapter"])
    
    #for sub_item in chapter.get("sub_items", []):
    #    chapter_obj = sub_item.get("Chapter")
    #
    #if chapter_obj:
    #    process_chapter(chapter_obj)


def main():
    """
    Main entry point for the mdBook preprocessor.
    """
    if len(sys.argv) > 1 and sys.argv[1] == "supports":
        sys.exit(0)

    data = json.load(sys.stdin)
    
    if not isinstance(data, list) or len(data) != 2:
        raise RuntimeError(
            "Unexpected mdBook preprocessor input format."
        )
    
    context, book = data

    #context, book = json.load(sys.stdin)
    
    # Show the structure of the internal book representation:
    # print(book, file=sys.stderr)
    # sys.exit(1)

    for item in book.get("items", []):
        chapter = item.get("Chapter")

        if chapter:
            process_chapter(chapter)

    json.dump(book, sys.stdout)


if __name__ == "__main__":
    main()
