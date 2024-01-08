from setuptools import find_packages, setup


setup(
    name="rito",
    version="0.0.14",
    author="Mathias Gout",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests==2.31.0", "pydantic==1.10.9"],
    python_requires="==3.9.*",
)
