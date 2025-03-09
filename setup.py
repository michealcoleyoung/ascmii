from setuptools import setup 

setup(
        name='ascmii'
        version ='0.1.0'
        py_modules['ascmii']
        entry_points={
            'console_scripts': [
                'ascmii = ascmii:main',
                ],
            },
        install_requires=[
            'ascii_magic',
            'rich',
            ],
        )
