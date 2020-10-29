import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name = "v2ray-termianl-eqporyan",
        version = "3.1.post2020",
        author = "FINTF C",
        author_email = "eqpoqpe@gmail.com",
        description = "N/A",
        long_description = long_description,
        long_description_content_type = "N/A",
        url = "https://github.com/Eqpoqpe/v2rayT",
        packages = setuptools.find_packages(),
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: GNU/Linux",
        ],
        python_requires = '>=3.6',
)
