import setuptools

with open('README.md', 'rt', encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fibonacci-calculator',
    version='0.0.1',
    author='Leon Feng',
    author_email='leonlibinfeng@gmail.com',
    description='A package to calculate fibonacci number',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leon0707/fibonacci-calculator',
    packages=['fibonacci_calculator'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>= 2.7, >=3.6',
)