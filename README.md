pyro
====

Small utility to rotate files.Example of a crontab

# Install
```
sudo python setup.py install
```

## Setup crontab to rotate periodically
This will rotate every night at midnight.
```
$ crontab -e
0 0 * * * /usr/local/bin/pyro
```
## Modify Config

```
$ cat /etc/pyrorc 
# file - file name to rollover
# backupCount - at most backupCount files will be kept (0 means no limit)

[bash]
file = $HOME/bash_history/.bash_history
backupCount = 0

```
## Add new .bash_history location to /etc/profile
```bash
echo "# Move .bash_history location" | sudo tee -a /etc/profile
echo "export HISTFILE=/home/$USER/.bash_history" | sudo tee -a /etc/profile
```