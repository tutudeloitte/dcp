# Common errors

yum + unpacking of archive failed: https://unix.stackexchange.com/questions/407740/yum-unpacking-of-archive-failed
Package route is a directory on your machine, delete that directory

“Public key for jenkins-2.232-1.1.noarch.rpm is not installed” while installing AWS on Jenkins: https://stackoverflow.com/questions/61344317/im-getting-error-public-key-for-jenkins-2-232-1-1-noarch-rpm-is-not-installed
Download official Jenkins key from source: 
~~~
sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
~~~
