import os
import sys
import markdown2


output = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <style type="text/css">
"""

css_path = sys.argv[2]
with open(css_path) as css:
	output += css.read()

	output += """
	    </style>
	    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	</head>

	<body>
	<a href="../blog_home.html"><h1><i class="fa fa-chevron-left back-arrow"></i> Back to blogs...</a></h1>
	"""

infile_path = sys.argv[1]
with open(infile_path, 'r') as infile:
	output += markdown2.markdown(infile.read())

	output += """</body>

	</html>
	"""

# Write outfile html
outfile_name = infile_path.lower()
outfile_name = outfile_name.replace("md", "html")
with open(outfile_name, 'w') as outfile:
	outfile.write(output)