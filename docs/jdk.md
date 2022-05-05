
sudo chmod +w /etc/profile
sudo vi /etc/profile

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-12.0.1.jdk/Contents/Home 
export CLASSPATH=.:$JAVA_HOME/lib/tools.jar
