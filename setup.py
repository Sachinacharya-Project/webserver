from setuptools import setup

setup(
    name='webserver',
    version='1.0.3',
    description='This is a small web server to server PHP files',
    keyword='php webserver localhost',
    author='Sachin Acharya',
    author_email='acharyaraj71@gmail.com',
    packages=['webserver'],
    install_requires = ['pathlib2'],
    package_data={
        '': ['Liscence.md', 'php-cli-server.ini', 'README.md', 'settings.json']
    },
    include_package_data=True,
    entry_points = {
        'console_scripts': [
            'server = webserver.__main__:main'
        ]
    }
)
# python .\setup.py sdist bdist_wheel
