import setuptools

setuptools.setup(
    name="testpyhon",
    version="1.0.0",
    author="Alexandre Mai",
    author_email="alexandre.mai@gmail.com",
    description="test",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requires,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*model.xlsx", "../requirements.txt", "../README.md"],
    },
)
