from setuptools import setup, find_packages

setup(
    name="NumberPlateGen",
    version="0.1.0",
    author="'İnanç Yiğit",
    author_email="incyi@users.noreply.github.com",
    description="A Python tool to generate random car license/number plates for various regions.",
    long_description=open('README.md').read(),  # Read the content of README.md
    long_description_content_type='text/markdown',
    url="https://github.com/incyi/NumberPlateGen",  # Update with your GitHub URL
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
    install_requires=[
        "pytest",  # For testing
        "flask",   # For future web API (if needed)
    ],
    entry_points={
        'console_scripts': [
            'numberplategen=cli:main',  # Command line interface entry point
        ],
    },
)
