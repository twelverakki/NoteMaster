from setuptools import setup, find_packages  

setup(  
    name="NoteMaster",  
    version="0.1.0",  
    author="Kelompok 6",  
    author_email="twelve.rakki@gmail.com",  
    description="Package untuk mengelola catatan dengan metode CRUD",  
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/twelverakki/NoteMaster",  
    packages=find_packages(),  
    install_requires=open('requirements.txt').read().splitlines(),  
    classifiers=[  
        "Programming Language :: Python :: 3",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],  
    python_requires='>=3.6',
)