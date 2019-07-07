# Linux / bash commands

## Check which versions of python I have
```ls usr/bin/python*
```

Should see something like this:
/usr/bin/python              /usr/bin/python3.6m
/usr/bin/python2             /usr/bin/python3.7
/usr/bin/python2.7           /usr/bin/python3.7m
/usr/bin/python2.7-config    /usr/bin/python3-jsonschema
/usr/bin/python2-config      /usr/bin/python3m
/usr/bin/python2-futurize    /usr/bin/python3-wsdump
/usr/bin/python2-pasteurize  /usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/python2-qr          /usr/bin/python-argcomplete-tcsh
/usr/bin/python3             /usr/bin/python-config
/usr/bin/python3.6           /usr/bin/python-faraday


## Use a different version of python
alias python=/usr/bin/python3
**alias** - 



## downloading software
* wget
	* downloads files served with http, https, ftp over a network
	* example
		* ``` wget [url or package or SW]
	
	* downloads file into working directory
	* wget vs apt get
		

## Move files
**mv** - move files from one directory to another
	syntax: 
```
[mv][filename][new location]
```

## remove directory
-to remove a directory tht contains files or directorys,
```
rm -r directoryname
```

-if the directory is empty:
```
rmdir directory_name
```

## Navigating through driectorys
**cd** - changes directory
syntax:
```
cd [directory]
```

### Shortcuts
#### Go to home directory
```
cd ~
```
-make sure to include space

#### Go up one directory
```
cd ..
```
-Make sure to include space










