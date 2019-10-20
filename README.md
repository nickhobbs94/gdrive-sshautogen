# gdrive-sshautogen
Autogenerate ssh authorized_keys file and .ssh/config files based on a network schema stored in a google sheet.

Needs a file called homenetwork_secret.json that contains secret key to connect to GDrive.

There are two pages in the sheets doc called "IP schema" and "SSH Keys", they are organised as follows:

<pre>
-------------------------------------------------------------------------------
Page:IP Schema

Device  IP Address     MAC          SSH Port      SSH Alias       SSH User
dev1    192.168.0.1    (optional)   22            alias1          username
dev2    192.168.0.2    (optional)   2222          alias2          username2

-------------------------------------------------------------------------------
Page: SSH-Keys

Description       Key                             dev1      dev2
dev1 git repo     ssh-rsa aksdjfhklah...          FALSE     TRUE
dev2 login        ssh-rsa aksdjfhklab...          TRUE      FALSE
</pre>
