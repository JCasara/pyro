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
$ crontab -l
0 0 * * * /usr/local/bin/pyro
```
## Modify Config

```
$ cat /etc/pyrorc 
# file - file name to rollover
# backupCount - at most backupCount files will be kept (0 means no limit)

[bash]
file = $HOME/.bash_history
backupCount = 0

```


