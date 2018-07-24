# Logfile colorizer
Define Pygments lexer and color schema for eazyBI child and application log files.

Prerequisites
-------------

 - Python
 - pip (Python package manager)

       $pip -V   # check if you have it

       $sudo easy_install pip # install it if you don't have it

Set-up
-------------
 - Install Pygments package

       sudo pip install Pygments

 - Copy .lessfilter file to you home directory
 - Add the following to your .bashrc file

       ############### for less syntax highlight ###############
       # specify options that will be passed to less
       export LESS='-R'
       # specify input preprocessor for less
       export LESSOPEN='|~/.lessfilter %s'
 - Install the python package contained in this repository.

       cd ../    # move up one directory from the setup.py file
       sudo pip install -e log_colorizer
       # -e option installs "in place" therefore allowing you to apply newest version by git pull

Additional information
-------------
You can change tokenizer and/or colors on the fly by editing \_\_init__.py file