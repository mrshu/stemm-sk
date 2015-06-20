from setuptools import setup
from os import path

setup(
    name='stemmsk',
    version='0.0.2',

    description='A Pythonic stemmer for Slovak language',

    url='https://github.com/mrshu/stemm-sk',

    author='mr.Shu',
    author_email='mr@shu.io',

    maintainer='mr.Shu',
    maintainer_email='mr@shu.io',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Natural Language :: Slovak',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='stemming slovak',

    packages=['stemmsk'],
    entry_points={
        'console_scripts': [
            'stemmsk=stemmsk:main',
        ],
    },
)
