# openpy
Openpy is a simple command line tool using which you don't have to type every charactors for some very long commands everyday repeatedly. You can add a shortcut for a long command, next time you can call the command through this shortcut. It's much easier to remember a shorter substitude command. And there's another usage for Openpy: you could run a file directly by typing file name with wildcards and you don't have to remember its absolute path.

# Examples
add a shortcut for a command:


* ```opy -as c -d "curl -get http://127.0.0.1:5000" ```


call the command through shortcut "c":


* ``` opy @c```

open qq.app:

* opy q*

# Requirements
Openpy is written in python 2.7

# Systems
Openpy now only supports Mac system.

# Installing Openpy
Download files in dist folder and put them in your Mac folder /usr/bin

# TODO
1. Support Windows system
2. Automatically generate json files and initiallize path
3. Install package using pip 
4. Rebuild code
5. Documentation

# Contributing
Your contributions are always welcome!
