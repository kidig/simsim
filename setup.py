import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simsim",
    version="0.0.1",
    author="Dmitry Gerasimenko",
    author_email="kiddima@gmail.com",
    description="Simple python code similarity checker",
    keywords='plagiarism, plage, plagiary, similarity, ast',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kidig/simsim",
    packages=setuptools.find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['simsim = simsim.cmd:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)