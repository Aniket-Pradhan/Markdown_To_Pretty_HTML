import markdown2


class converter:

    def read_file(self, path):
        try:
            with open(path, 'r') as file:
                read_out = file.read()
        except TypeError:
            read_out = path.read()
        return read_out

    def write_file(self, path, what_to_write):
        with open(path, 'w') as file:
            file.write(what_to_write)

    def convert(self):
        output = '<!DOCTYPE html>\n<html lang="en">\n\
            <head>\n<meta charset="utf-8">\n\
            <style type="text/css">\n'

        css_file = self.read_file(self.css_path)
        output += css_file

        output += """
            </style>
            """

        if self.custom_link_css is not None:
            output += """
            {}
            """.format(self.custom_link_css)

        output += """
        </head>
        <body>
        """

        if self.custom_top_body is not None:
            output += """
            {}
            """.format(self.custom_top_body)

        mark_file = self.read_file(self.infile_path)
        output += markdown2.markdown(mark_file)

        output += """
        </body>
        </html>
        """

        # Write outfile html
        outfile_name = self.infile_path.lower()
        outfile_name = outfile_name.replace("md", "html")
        self.write_file(outfile_name, output)

    def __init__(self,
                 infile_path,
                 css_path,
                 custom_link_css=None,
                 custom_top_body=None):
        self.infile_path = infile_path
        self.css_path = css_path
        self.custom_link_css = custom_link_css
        self.custom_top_body = custom_top_body
