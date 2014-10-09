from setuptools import setup, find_packages


setup(
    name='python-acoustid-api',
    version='0.0.1',
    description="Lightweight wrapper around AcoustID's API",
    author='Matt Dennewitz',
    author_email='mattdennewitz@gmail.com',
    url='http://github.com/mattdennewitz/python-acoustid-api',
    packages=find_packages(),
    install_requires=['requests == 2.4.3'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
    ],
)
