#! /bin/bash

sudo mkdir /root/.ssh/
sudo chmod 700 /root/.ssh
cat /local/migration_experiment/id_ed25519.pub | sudo tee /root/.ssh/authorized_keys
