#!/usr/bin/env python
#  setup.py
#  
#  Dustin Dorroh <dustin.dorroh@decisionsciencescorp.com>
#  

from distutils.core import setup

setup(name='pyro',
	version='0.3',
	description='Python file rotater',
	author='Dustin Dorroh',
	author_email='dustin.dorroh@decisionsciencescorp.com',
	maintainer='Dustin Dorroh',
	maintainer_email='dustin.dorroh@decisionsciencescorp.com',
	scripts=['pyro'],
	data_files=[('/etc',['pyrorc'])]
	)
