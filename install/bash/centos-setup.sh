sudo yum update -y
sudo yum upgrade -y
sudo yum install epel-release -y
sudo yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm -y
sudo yum update -y
sudo yum install wget nano git curl screen ncdu unzip inotify-tools ffmpeg -y
sudo yum update -y
sudo yum upgrade -y

sudo ClientAliveInterval=$(cat /etc/ssh/sshd_config | grep -m 1 ClientAliveInterval | head -1)
sudo ClientAliveCountMax=$(cat /etc/ssh/sshd_config | grep -m 1 ClientAliveCountMax | head -1)
sudo sed -i "s/^$ClientAliveInterval/ClientAliveInterval 30/" /etc/ssh/sshd_config
sudo sed -i "s/^$ClientAliveCountMax/ClientAliveCountMax 720/" /etc/ssh/sshd_config 
sudo systemctl restart sshd

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
rm -rf awscliv2.zip

mkdir ~/.aws/
touch ~/.aws/credentials
touch ~/.aws/config
echo '[default]' >> ~/.aws/credentials
echo 'aws_access_key_id=AKIA42IJAAWUDMXBG7PZ' >> ~/.aws/credentials
echo 'aws_secret_access_key=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' >> ~/.aws/credentials
echo '[default]' >> ~/.aws/config
echo 'region=us-east-1' >> ~/.aws/config
echo 'output=json' >> ~/.aws/config

echo 'alias e="exit"' >> /home/centos/.bashrc
echo 'alias c="clear"' >> /home/centos/.bashrc
echo 'alias r="source ~/.bashrc"' >> /home/centos/.bashrc
echo 'alias f2bs="sudo systemctl status fail2ban.service"' >> /home/centos/.bashrc
echo 'alias f2bu="sudo systemctl start fail2ban.service"' >> /home/centos/.bashrc
echo 'alias f2bd="sudo systemctl stop fail2ban.service"' >> /home/centos/.bashrc
echo 'alias fws="sudo systemctl stop firewalld"' >> /home/centos/.bashrc

screen screen -S innova
