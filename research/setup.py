
from setuptools import find_packages
from setuptools import setup

setup(
    name="object_detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Cython>=0.29.21",
        "contextlib2>=0.5.5",
        "Pillow>=7.2.0",
        "lxml>=4.6.1",
        "jupyter>=1.0.0",
        "matplotlib>=3.3.3",
        "numpy>=1.19.1",
        "opencv-python>=4.4.0.46",
        "pandas>=1.1.4",
        "scikit-image>=0.17.2",
        "scipy>=1.4.1",
        "six>=1.15.0",
        "tensorflow>=2.4.0",
        "tfds-nightly>=3.2.1.dev202007140105",
        "tqdm>=4.50.0",
        "wrapt>=1.12.1",
    ],
)