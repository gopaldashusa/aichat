from setuptools import setup, find_packages

setup(
    name="chatapp",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai>=0.1.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "graphviz>=0.20.1",
        "pyyaml>=6.0.1",
    ],
    python_requires=">=3.7",
) 