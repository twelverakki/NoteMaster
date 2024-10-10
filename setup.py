from setuptools import setup, find_packages

setup(
    name='NoteMaster',
    version='0.1.3',
    description='Paket untuk mengelola catatan dengan metode CRUD',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Kelompok 6 AP B',
    author_email='twelve.rakki@gmail.com',
    url='https://github.com/twelverakki/NoteMaster',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)