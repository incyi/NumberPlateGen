"""Setup script for the NumberPlateGen project.

This script defines the installation configuration for the project.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="NumberPlateGen",
    version="0.1.0",
    author="İnanç Yiğit",
    author_email="incyi@users.noreply.github.com",
    description="A Python tool to generate random car license/number plates for various regions.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/incyi/NumberPlateGen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'numberplategen=cli:main',  # Command line interface entry point
        ],
    },
)
