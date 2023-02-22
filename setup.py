#!/usr/bin/env python3

"""
The setup and build script for the bloget library.
"""

import setuptools  # type: ignore

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="columbo",
    version="1.0.0",
    description="???",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vkostyanetsky/Columbo",
    license="MIT",
    python_requires=">=3.10",
    packages=["columbo"],
    install_requires=[],
    entry_points={"console_scripts": ["columbo=columbo.app:main"]},
    author="Vlad Kostyanetsky",
    author_email="vlad@kostyanetsky.me",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    keywords="static blog generator",
)
