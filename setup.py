#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
]

setup_requirements = []

test_requirements = []

setup(
    author="Srijith Balakrishnan",
    author_email="srijith.balakrishnan@sec.ethz.ch",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="An integrated power-water-transportation model for urban simulations.",
    entry_points={
        "console_scripts": [
            "infrarisk=infrarisk.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="infrarisk",
    name="infrarisk",
    packages=find_packages(include=["infrarisk", "infrarisk.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/srijithabalakrishnan/dreaminsg_integrated_model",
    version="0.1.0",
    zip_safe=False,
)
