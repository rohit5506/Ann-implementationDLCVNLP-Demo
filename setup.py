import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Project_name="Ann-implementationDLCVNLP-Demo"
User_name="rohit5506"
setuptools.setup(
    name="f{Project_name}-{User_name}",
    version="0.0.1",
    author="Rohit Bisht",
    author_email="bishtrohit097@gmail.com",
    description="a small package for ann implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{User_name}/{Project_name}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn"
    ]
)