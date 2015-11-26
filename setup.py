from setuptools import setup


setup(
    name='roomservice',
    version='0.0.1',
    author='Statscrafters',
    packages=['roomservice'],
    entry_points={
        'console_scripts': [
            'rms = roomservice.rms:main',
        ]
    },
    install_requires=[
        'click==6.0',
        'Flask==0.10.1',
        'Flask-RESTful==0.3.4',
        'flask-restful-swagger==0.19',
        'psutil==3.3.0',
        'PyMySQL==0.6.7'
    ]
)
