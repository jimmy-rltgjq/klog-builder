from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read().splitlines()


setup(
    name='Klog',
    version='0.1',
    author='Kim Ji Min',
    author_email='jimmy.work.kr@gmail.com',
    packages=find_packages(exclude=['docs']),
    python_requires='>=3',
    install_requires=install_requires
)