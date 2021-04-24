import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='specx_simulator',
    version='1.0',
    url='https://github.com/danialeresbar/specx_simulator',
    license='Open',
    author='Unillanos',
    author_email='daniel.restrepo@unillanos.edu.co',
    description='White Spaces Simulator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
