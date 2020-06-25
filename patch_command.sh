# Red Hat commands
# To update all packages
yum update
# To view info of a package
yum info <package-name>
# To install package to specific version
yum install <version-name>
# Remove a package
yum remove <package-name>

# Common errors
# yum + unpacking of archive failed: https://unix.stackexchange.com/questions/407740/yum-unpacking-of-archive-failed
# Package route is a directory on your machine, delete that directory
