import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = [
    r.strip() for r in open("requirements.txt") if r.strip() and not r.strip().startswith("#")
]


setuptools.setup(
    name="iterfast",
    version="0.0.3",
    author="Pradip Bankar",
    author_email="pradipbankar0097@gmail.com",
    description="A library for fast iterative operations.",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pradipbankar0097/iterfast",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
