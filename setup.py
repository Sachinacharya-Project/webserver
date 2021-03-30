from setuptools import setup

setup(
    name='webserver',
    version='1.0.1',
    description='This is a small web server to server PHP files',
    keyword='php webserver localhost',
    author='Sachin Acharya',
    author_email='acharyaraj71@gmail.com',
    packages=['webserver'],
    install_requires = ['pathlib', ''],
    entry_points = {
        'console_scripts': [
            'server = webserver.__main__:main'
        ]
    }
)
# python .\setup.py sdist bdist_wheel
