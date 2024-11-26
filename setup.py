from setuptools import setup, find_packages

setup(
    name="My_python_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Anmol",
    author_email="xxxxxxxxxxxxxxx",
    description="A simple package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/anmoldotkr/My_python_package.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)