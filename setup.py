from setuptools import setup, find_packages

setup(
    name="cli",
    version="0.1.0",
    packages=find_packages(),
    author="Juho Jokisalo",
    author_email="xboxj2012@gmail.com",
    description="A simple Python package for CLI tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Specifies markdown format
    url="https://github.com/TheDoubleMix/cli", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.9",
)
