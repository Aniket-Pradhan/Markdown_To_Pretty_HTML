# beautdown

A Python package to convert simple markdown to **pretty** HTML files.

## How to install?

1. Firstly, clone the repository.
2. Then move inside the directory, and simply run `pip install .`

Another way to install?

1. Simply run `pip install https://github.com/Aniket-Pradhan/beautdown`

## How to use?

1. Simply run `beautdown` to access the tool.
2. To specify the markdown file, use the `-m` or `--md` args
3. To specify a custom css file to style the webpage, use the `-c` or `-css` args (optional).
4. To add a custom header, use the `-custom-top-body` args and pass the corresponding string.
5. To add additional CSS using a string, use the `--custom-link-css` arg.

```
usage: beautdown [-h] [-c CSS] -m MD [--custom-link-css CUSTOM_LINK_CSS]
                 [--custom-top-body CUSTOM_TOP_BODY]

optional arguments:
  -h, --help            show this help message and exit
  -c CSS, --css CSS     CSS file to include
  -m MD, --md MD        Markdown file to convert
  --custom-link-css CUSTOM_LINK_CSS
                        Add custom css for hyperlinks
  --custom-top-body CUSTOM_TOP_BODY
                        Add a custom header
```
