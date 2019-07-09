import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='dstr-services-common',
    version='0.1.9',
    author="Henrique Bolzan Batista",
    author_email="henrique@bolzan.com.br",
    description="Common functions for Django SQL To Rest Microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hbolzan/sql-to-rest-services-common",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2-Clause License",
        "Operating System :: OS Independent",
    ],
)
