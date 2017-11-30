#Install
First install git and docker on your server.
```
sudo yum install -y git
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo curl -L https://github.com/docker/compose/releases/download/1.17.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
/usr/local/bin/docker-compose --version
```

grab the respo.
```
git clone https://github.com/jsett/Bookmarker.git
```
build and run it just the docker.
```
docker build -t bookmarker:latest .
docker run -d -p 5000:5000 bookmarker
```
build and run the compose.
```
docker-compose build
docker-compose up
```


#phantomjs
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xvfj phantomjs-2.1.1-linux-x86_64.tar.bz2
