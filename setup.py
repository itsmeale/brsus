from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

setup(
    name="brsus",
    version="0.0.2-ALPHA",
    description="A tool to download data from datasus.",
    author="Ale Farias",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    test_suite="tests",
    install_requires=[],
    entry_points={},
)