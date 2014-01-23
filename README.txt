pyMySQL-wrapper
===============

A simple wrapper for 3rd-party python package - MySQLdb 

Prerequisites:

1) Install python 2.7.x to specified path of the target box

2) Install mysql server instance on the same box (mysql instance is needed because mysql_config will be used when setup MySQL-python)

3) Download MySQL-python from here: https://pypi.python.org/pypi/MySQL-python

4) unzip MySQL-python-1.2.5.zip (for example), enter the unpacked directory and run the following commands:
   shell> python setup.py build
   shell> python setup.py install

When steps above finished successfully, we can found MySQL_python-1.2.5-py2.7-linux-x86_64.egg (or .egg file with similar name) in python_install_path/lib/python2.7/site-packages/, we can also found './MySQL_python-1.2.5-py2.7-linux-x86_64.egg' has been included in file named 'easy-install.pth'

Just enjoy it now ~

^_^

