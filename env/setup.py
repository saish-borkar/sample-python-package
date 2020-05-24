import setuptools

setuptools.setup(
    name="junk", # Replace with your own username
    version="1",
    author="Saish Borkar",
    author_email="borkarsg@gmail.com",
    description="Nothing much here just for demo....",
    long_description="test in prog",
    long_description_content_type="text/markdown",
    url="",
    packages=['junk'],
    install_requires=[],#setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license = "MIT",
    python_requires='>=3.6',
)