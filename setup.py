from setuptools import setup, find_packages


setup(
	name='basicvmpy',
	version='0.0.1',
	description='Basic python build',
	author='Suresh Koya',
	author_email="sk@gm.com',
	packages=find_packages(),
	install_requires=requirements,
	entry_points={
    	'console_scripts': [
        		'hello = basicvmpy.basic:cli',
        	],
        },
	zip_safe=False
)