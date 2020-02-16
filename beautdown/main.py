import beautdown
from beautdown.converter import converter

import argparse
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

template = pkg_resources.open_text(beautdown, 'default_css.css')
custom_link_css = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">'
custom_top_body = '<a href="../blog_home.html"><h1><i class="fa fa-chevron-left back-arrow"></i> Back to blogs...</a></h1>'


def main(args=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("-c",
                    "--css",
                    required=False,
                    help="CSS file to include",
                    type=str,
                    default=template)
    ap.add_argument("-m",
                    "--md",
                    required=True,
                    help="Markdown file to convert",
                    type=str)
    ap.add_argument("--custom-link-css",
                    required=False,
                    help="Add custom css for hyperlinks",
                    default=custom_link_css,
                    type=str)
    ap.add_argument("--custom-top-body",
                    required=False,
                    help="Add a custom header",
                    default=custom_top_body,
                    type=str)
    args = ap.parse_args()

    convert = converter(args.md,
                        args.css,
                        custom_link_css=args.custom_link_css,
                        custom_top_body=args.custom_top_body)
    convert.convert()


if __name__ == '__main__':
    main()
