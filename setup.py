from setuptools import setup

setup(
    name='webserver',
    version='2.0.1',
    description='This is a small web server to server PHP files',
    keywords='php webserver localhost',
    author='Sachin Acharya',
    author_email='acharyaraj71+webserver@gmail.com',
    packages=['webserver'],
    install_requires = ['py_setenv'], # pathlib2
    url='https://github.com/sachin-acharya-projects/webserver',
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
