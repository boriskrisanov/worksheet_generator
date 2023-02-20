#!/bin/sh
# Update packages
echo "Updating packages"
sudo apt update
sudo apt upgrade -y

# Set up UFW
echo "Setting up UFW to allow SSH"

sudo ufw allow ssh
sudo ufw allow 3000
sudo ufw --force enable

# Secure SSH
echo "Securing SSH"

echo $(cat ./ssh_key.pub) > ~/.ssh/authorized_keys
sudo cp ./sshd_config /etc/ssh/sshd_config

# Set up Prometheus

mkdir prometheus
cd prometheus
wget https://github.com/prometheus/prometheus/releases/download/v2.37.5/prometheus-2.37.5.linux-amd64.tar.gz -O prometheus.tar.gz
tar -xf prometheus.tar.gz
rm prometheus.tar.gz
cp -r prometheus-2.37.5.linux-amd64/* .
rm -rf prometheus-2.37.5.linux-amd64/
cd ..
cp prometheus.yml prometheus/prometheus.yml
sudo cp prometheus.service /etc/systemd/system/prometheus.service
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus

# Set up Node Exporter

wget https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz -O node_exporter.tar.gz
tar -xf node_exporter.tar.gz
rm node_exporter.tar.gz
mv node_exporter-1.5.0.linux-amd64 node_exporter
sudo cp node_exporter.service /etc/systemd/system/node_exporter.service
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl enable node_exporter

# Set up Grafana

sudo adduser --disabled-password --gecos "" grafana
sudo passwd -d grafana
sudo cd /home/grafana
sudo wget https://dl.grafana.com/oss/release/grafana-9.3.2.linux-amd64.tar.gz -O grafana.tar.gz
sudo tar -xf grafana.tar.gz
sudo rm grafana.tar.gz
sudo cp -r grafana-9.3.2/* .
sudo rm -rf grafana-9.3.2/
cd ~
sudo cp grafana.service /etc/systemd/system/grafana.service
sudo systemctl daemon-reload
sudo systemctl start grafana
sudo systemctl enable grafana

# Set up Nginx

# Set up Certbot

echo "Done"
