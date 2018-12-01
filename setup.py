import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_utils",
    version="0.0.1",
    author="Dennis Barger",
    author_email="dennis.barger@outlook.com",
    description="Python AWS utilities",
    long_description=Python utility functions to interact with AWS resources,
    long_description_content_type="text/markdown",
    url="https://github.com/dlbarger/utils/aws_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
