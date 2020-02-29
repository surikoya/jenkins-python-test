# import codecs
# try:
#     codecs.lookup('mbcs')
# except LookupError:
#     ascii = codecs.lookup('ascii')
#     func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
#     codecs.register(func)

from setuptools import setup, find_packages


setup(
	name='basicvmpy',
	version='0.0.1',
	description='Basic python build',
	author='Suresh Koya',
	author_email="sk@gm.com',
	license='MIT',
	packages=find_packages(),
	install_requires=requirements,
	entry_points={
    	'console_scripts': [
        		'hello = basicvmpy.iris:cli',
        	],
        },
	zip_safe=False
)