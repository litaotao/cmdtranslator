
import os
import io
from setuptools import find_packages, setup


setup(
    name="cmdtranslator",
    # Increase the version in ggplot/__init__.py
    version='0.1.0',
    author="Taotao Li",
    author_email="litaotao@vip.163.com",
    url="http://litaotao.github.io",
    license="BSD",
    packages=find_packages(),
    package_dir={"translator": "translator"},
    description="A console dictionary",
    # run pandoc --from=markdown --to=rst --output=README.rst README.md
    long_description=io.open("README.md", encoding='utf8').read(),
    install_requires=[
        "beautifulsoup4",
        "docopt==0.6.2"
    ],
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'trans = translator.trans:trans',
        ]
    }
)

