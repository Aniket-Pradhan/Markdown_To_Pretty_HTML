import setuptools
from pathlib import Path

from beautdown.version import __version__ as version

REQUIREMENTS = Path("./requirements.txt").read_text()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beautdown",
    version=version,
    include_package_data=True,
    package_data={
        "": ["default_css.css"]
    },
    author="Aniket Pradhan",
    author_email="aniketpradhan1999@gmail.com",
    description="Markdown to pretty html",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://home.iiitd.edu.in/~aniket17133",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=REQUIREMENTS
)
