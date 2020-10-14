# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
    name="londonfields",  # Required
    version="0.0.1",  # Required
    description="Django App for London Fields Website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muffizone/london_fields",
    author="Mufaddal Presswala",
    author_email="muffizone@gmail.com",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="cricket, londonfields, vpccl",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.6s",
    install_requires=[
        "Django>=3.1",
        "django-bootstrap4>=2.2.0",
        "django-filter>=2.4.0",
        "django-forms-bootstrap>=3.1.0",
        "django-tables2>=2.3.2",
    ],
    extras_require={"dev": ["ipython>=7.16.1",], "test": ["coverage"],},
    # package_data={"sample": ["package_data.dat"],},
    # data_files=[("my_data", ["data/data_file"])],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={"console_scripts": ["sample=sample:main",],},
    project_urls={
        "Bug Reports": "https://github.com/muffizone/london_fields/issues",
        "Source": "https://github.com/muffizone/london_fields",
    },
)
