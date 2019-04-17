import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygul",
    version="0.0.1",
    author="Raghul Asokan",
    author_email="mailcorahul@gmail.com",
    description="A python utility for computer vision and deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mailcorahul/pygul",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
