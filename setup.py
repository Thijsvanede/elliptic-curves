import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ec',
    version='1.0',
    author="Thijs van Ede",
    author_email='t.s.vanede@utwente.nl',
    description='Toy Elliptic Curves implementation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Thijsvanede/elliptic-curves",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
