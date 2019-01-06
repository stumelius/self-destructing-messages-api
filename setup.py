from setuptools import setup, find_packages
from seppuku import __version__

setup(
    name='seppuku',
    version=__version__,
    description='REST API for writing and reading self-destructing messages with '
                'optional auto-expiry timers using a redis backend.',
    author='Simo Tumelius',
    author_email='simo.tumelius@gmail.com',
    url='https://github.com/smomni/self-destructing-messages-api',
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages(),
    install_requires=['redis', 'flask', 'flask-restful'],
    extras_require={
        'dev': [],
        'test': ['pytest', 'pytest-cov', 'pytest-flask', 'pytest-env'],
        'docs': []
    },
    scripts=['serve_seppuku_api.py'],
    entry_points={
        'console_scripts': [],
    },
)
