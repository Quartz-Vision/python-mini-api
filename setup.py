import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fr:
    reqs = fr.read().strip().split("\n")


setuptools.setup(
    name="mini-api",
    version="0.0.1",
    author="liava",
    author_email="liava@tuta.io",
    description="Minimal Web API for lambdas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quartz-Vision/python-mini-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=reqs,
    package_data={
        "mini_api": [],
    },
    entry_points={
        #"console_scripts": ["sometool=.cli:cli"],
    },
)