import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='scribble',
    version='1.0.0',
    author='Mike Malinowski',
    author_email='mike@twisted.space',
    description='Allows for persistent storage of dictionary data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/scribble',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
    ],
    keywords="scribble dictionary appdata persistent",
)
