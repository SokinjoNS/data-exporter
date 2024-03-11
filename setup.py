from setuptools import setup, find_packages

setup(
    name="data-exporter",
    version="0.1.2",
    author="SokinjoNS",
    author_email="sokinjo.155@gmail.com",
    description="A module for exporting email data to CSV format.",
    long_description=open('README.md').read(),
    url="https://github.com/SokinjoNS/data-exporter",
    project_urls":{"Source":"https://github.com/SokinjoNS/data-exporter"},
    packages=find_packages(),
    install_requires=[
        'gmail-message-processor>=0.1.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
