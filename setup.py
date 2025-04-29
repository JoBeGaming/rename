from setuptools import setup, find_packages

setup(
    name="rename",
    version="1.0",
    author="JoBe",
    description="Python `@rename` decorator.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JoBeGaming/rename",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
