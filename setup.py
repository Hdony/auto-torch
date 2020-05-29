import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-torch",
    version="0.0.1",
    author="You Wu",
    author_email="13943173135@163.com",
    description="Auto-ML platform based on Pytorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WuYou950731/auto-torch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)