---
title: "How to Build the mdBook"
author: "Prof. Dr.- Ing. Gudenkauf, Stefan"
email: "pdal@jade-hs.de"
organization: "PDAL-Projekt, Jade HS"
date: "2026-06-16"
version: "0.0.1"
level: ""
duration: ""
prerequisites: ""
tags: ["PDAL", "Build", "mdBook"]
license: "CC BY-SA 4.0"
---

# How to Build the mdBook

## Install Rust

Always use `rustup`:  
https://rust-lang.org/tools/install/

Download and execute `rustup`:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

`rustup` will install the complete Rust toolchain, including [Cargo](https://doc.rust-lang.org/cargo/index.html), the Rust package manager. We need Cargo to install [mdBook](https://rust-lang.github.io/mdBook/) and [preprocessors](https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/) for mdBook.

`rustup` will also add the Rust toolchain directory to the operating system's PATH environment variable. Close and restart the terminal session, so that the modifications to PATH may take effect. 

Test successful installation by checking the version of the Rust compiler:

```bash
rustc --version
```

## Install and run mdBook

> **Note:** We currently use mdBook v0.5.2

Install mdBook with Cargo:

```bash
cargo install mdbook
```


Make familiar with CLI interface:

```bash
mdbook --help
```

- `mdbook build` builds a book from markdown files located in the directory `/src`. The output directory is `/book`.
- `mdbook serve` serves a book at http://localhost:3000, and rebuilds it on changes.
- `mdbook clean` deletes a built book. Recommended to be used before every rebuild and/or if changes are not reflected into a served book.



## On Preprocessors

The output of the [build process](https://eli.thegreenplace.net/2025/plugins-case-study-mdbook-preprocessors/) can be modified by preprocessors, if included in the `book.toml` build configuration file. There are several preprocessors crates available, but most are not well documented, or only work well with older versions of mdBook that use a different internal structure for book content.

In our case, we use a [custom](https://www.thenegation.com/posts/mdbook-preprocessing/) Python preprocessor `preproc-frontmatter.py` that replaces yaml formatters in all Markdown files with html tables. See the current `book.toml`:

```toml
[preprocessor.my-frontmatter]
command = "python3 ./preproc-frontmatter.py"
```

Our Python preprocessor requries the PyYAML package, as documented in the file `requirements.txt`. We recommend to [create and use a local virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for the mdBook project, and install the required package in the virtual environment. We use and recommend `.venv` as the name of the virtual environment:

```bash
(.venv) python3 -m pip install -r requirements.txt
```

If you modify or add additional packages to the project, document the depdendencies in the requirements file:

```bash
(.venv) pip freeze --local > requirements.txt 
```

### Alternative preprocessors:

Available preprocessors (Rust binaries):

```bash
cargo install mdbook-frontmatter-strip
cargo install mdbook-frontmatter
```

- `mdbook-frontmatter-strip` strips the yaml formatters from all Markdown files. Add to `book.toml` as follows:

    ```toml
    [preprocessor.frontmatter-strip]
    renderers = ["html"]
    ```

- `mdbook-frontmatter` replaces yaml formatters in all Markdown files with pretty html code. Add to `book.toml` as follows:

    ```toml
    [preprocessor.frontmatter]
    ```




The project directory also includes a minimal Python preprocessor `preproc-min.py` as a template:

```python
#!/usr/bin/env python

import json
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'supports':
        # sys.argv[2] is the renderer name
        sys.exit(0)

# load book content
context, book = json.load(sys.stdin) 
# write back unmodified
json.dump(book, sys.stdout) 
```

## Troubleshooting

### Oops, I installed Cargo via homebrew!

**Note:** On macOS you *can* use [homebrew](https://brew.sh) to install Rust and Cargo, but this *can* generate a lot of problems (e. g., Cargo binaries not added to PATH).

Add Cargo binary to PATH, if missing:

1. Open configuration file:
    
    ```bash
    nano ~/.zshrc
    ```

2. Add export line at the end of the file:
    
    ```bash
    export PATH="$HOME/.cargo/bin:$PATH"
    ```

3. Restart terminal session 

### What the heck is a *crate*?

The documentation of [The Rust Programming Language](https://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/crates-and-modules.html) puts it well:

*"A crate is synonymous with a ‘library’ or ‘package’ in other languages. Hence “Cargo” as the name of Rust’s package management tool: you ship your crates to others with Cargo. Crates can produce an executable or a library, depending on the project."* 

$\rightarrow$ a binary file generated from Rust code

*"Each crate has an implicit root module that contains the code for that crate. You can then define a tree of sub-modules under that root module. Modules allow you to partition your code within the crate itself."* 

$\rightarrow$ a structural feature to groupe code elements into subsets

### Oops, I don't remember which crates I have installed!

List all crates (rust programs) installed via Cargo including version numbers:

```bash
cargo install --list
```

