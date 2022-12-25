import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecrypto",
    version="0.0.1",
    author="Esteban Vilca",
    author_email="evilcazu@gmail.com",
    description="A small crypto tools package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/estebanvz/ecrypto",
    project_urls={
        "Bug Tracker": "https://github.com/estebanvz/ecrypto/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7.9",
    install_requires=[
       "python-binance>=1.0.15",
       "numpy>=1.21.5",
   ],
)
