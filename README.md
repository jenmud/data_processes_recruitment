# Assumptions

* You are running on Linux
* Python3.5 installed
* python3-virtualenv installed
* You have internet access 

# Setup
To run the following, you need to create a virtual environment and install
all the requirements.

## Create a virtual environment to install dependencies

```bash
$ virtualenv-3.5 /tmp/demo
Using base prefix '/usr'
New python executable in /tmp/demo/bin/python3
Also creating executable in /tmp/demo/bin/python
Installing setuptools, pip, wheel...done. 
```

## Install dependencies

_Note that the output of pip install may be different_

```bash
$ /tmp/demo/bin/pip install -r requirement.txt 
Collecting coverage==4.4 (from -r requirement.txt (line 1))
  Using cached coverage-4.4-cp35-cp35m-manylinux1_x86_64.whl
Collecting lxml==3.7.3 (from -r requirement.txt (line 2))
  Using cached lxml-3.7.3-cp35-cp35m-manylinux1_x86_64.whl
Collecting nose==1.3.7 (from -r requirement.txt (line 3))
  Using cached nose-1.3.7-py3-none-any.whl
Collecting nose2==0.6.5 (from -r requirement.txt (line 4))
Collecting pylint==1.7.1 (from -r requirement.txt (line 5))
  Using cached pylint-1.7.1-py2.py3-none-any.whl
Requirement already satisfied: six>=1.1 in /tmp/demo/lib/python3.5/site-packages (from nose2==0.6.5->-r requirement.txt (line 4))
Collecting mccabe (from pylint==1.7.1->-r requirement.txt (line 5))
  Using cached mccabe-0.6.1-py2.py3-none-any.whl
Collecting isort>=4.2.5 (from pylint==1.7.1->-r requirement.txt (line 5))
  Using cached isort-4.2.5-py2.py3-none-any.whl
Collecting astroid>=1.5.1 (from pylint==1.7.1->-r requirement.txt (line 5))
  Using cached astroid-1.5.2-py2.py3-none-any.whl
Collecting wrapt (from astroid>=1.5.1->pylint==1.7.1->-r requirement.txt (line 5))
Collecting lazy-object-proxy (from astroid>=1.5.1->pylint==1.7.1->-r requirement.txt (line 5))
  Using cached lazy_object_proxy-1.3.1-cp35-cp35m-manylinux1_x86_64.whl
Installing collected packages: coverage, lxml, nose, nose2, mccabe, isort, wrapt, lazy-object-proxy, astroid, pylint
Successfully installed astroid-1.5.2 coverage-4.4 isort-4.2.5 lazy-object-proxy-1.3.1 lxml-3.7.3 mccabe-0.6.1 nose-1.3.7 nose2-0.6.5 pylint-1.7.1 wrapt-1.10.10
```

## Running the script

You will need a job reference number which should have been provided to you.

```bash
$ /tmp/demo/bin/python solve_puzzle.py --ref ##### http://apply.dataprocessors.com.au/
INFO:__main__:Response code: 200
INFO:__main__:Response: <html>
...
...
...
</html> 
```
