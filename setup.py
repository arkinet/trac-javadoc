from setuptools import setup

PACKAGE = 'TracJavaDoc'
VERSION = '0.1'

setup(name=PACKAGE,
	version=VERSION,
	description="Load JavaDoc comments from code into trac",
	author="Christofer Karlsson",
	author_email="buxxi@omfilm.net",
	packages=['javadoc'],
	entry_points={'trac.plugins': '%s = javadoc' % PACKAGE},
)
