from setuptools import setup
from setuptools import find_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()
    setup(
        name="u-measure",
        author="Christofanis Skordas",
        author_email="skordasc@uchicago.edu",
        version="0.1.0",
        description="A GUI software for ultrasonic data collection.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/skordaschristofanis/U-Measure",
        install_requires=[
            "qtpy",
            "pyqt6",
            "pyvisa",
        ],
        keywords="Measure, U-Measure",
        packages=find_packages(where="\\"),
        include_package_data=False,
        python_requires=">=3.10",
        classifiers=[
            "Development Status :: 3 - Development",
            "Intended Audience :: GSECARS Users",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Geoscience Departments and Institutes",
            "License :: OSI Approved :: GPL-3.0 License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.10",
            "Topic :: GUI Software",
            "Topic :: Education",
            "Topic :: Science/Research",
        ],
    )
