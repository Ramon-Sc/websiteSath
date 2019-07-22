# config log

## security configurations:

fail2ban enabled
   
  /etc/fail2ban/jail.local configured as follows:
   
  * [sshd]
  * enabled = true
  * port = 30022
  * filter = sshd
  * logpath = /var/log/auth.log
  * maxretry = 3
  * findtime = 10m
  * bantime = 1440m
