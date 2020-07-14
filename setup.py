from setuptools import setup

with open("README.md", "r") as doc:
    long_description = doc.read()

setup(
    name="pyise",
    version="0.0.1",
    url="https://github.com/tlofreso/python-ise",
    author="Tony Lofreso Jr",
    author_email="tlofreso@outlook.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=[""],
    package_dir={"": ""},
    install_requires=["netaddr"]
    extras_require={
        "dev": [
            "pytest"
        ],
    },
)
