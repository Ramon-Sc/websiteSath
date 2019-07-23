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


## SSL

Wurde mit Certbot + Let's encrypt installiert nach Anleitung:
https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx

Manuelle Anpassungen:
/etc/nginx/sites-enabled/default:

include options-ssl-nginx.conf ausgeschaltet

hinzugefügt:

    ssl_session_cache shared:SSL:20m;
    ssl_session_timeout 60m;

    ssl_prefer_server_ciphers on;

    ssl_ciphers ECDH+AESGCM:ECDH+AES256:ECDH+AES128:DHE+AES128:!ADH:!AECDH:!MD5;

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;

    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8 8.8.4.4;

    add_header Strict-Transport-Security "max-age=31536000" always;

-- Ende

## Renew SSL Certificate 

 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/schwerathletik-giessen.de/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/schwerathletik-giessen.de/privkey.pem
   Your cert will expire on 2019-10-17. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
