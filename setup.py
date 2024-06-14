from setuptools import find_packages, setup


setup(
    name="rito",
    version="0.0.15",
    author="Mathias Gout",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests==2.32.3"],
    python_requires="==3.9.*",
)
