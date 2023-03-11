from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='AsperaSRAgetter',
    version='1.0',
    description="The AsperaSRAgetter provides a easy way to download sequencing data from ENA by using Aspera.",
    url="https://github.com/RunJiaJi/AsperaSRAgetter",
    author='Runjia Ji',
    author_email='jirunjia@gmail.com',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pandas',
        'requests'
    ],
    entry_points={
        'console_scripts':[
            'sragetter = AsperaSRAgetter:main',
        ]
    },
)