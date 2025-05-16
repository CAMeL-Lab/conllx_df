from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="conllx-df",
    version="0.1.0",
    author="Muhammed AbuOdeh",
    author_email="mra9407@nyu.edu",
    description="A lightweight tool handle CoNLL-X files using pandas DataFrames.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CAMeL-Lab/conllx_df",
    project_urls={
        "Bug Tracker": "https://github.com/CAMeL-Lab/conllx_df/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    install_requires=[
        "pandas>=2.2.0",
    ],
)
