#!/bin/bash
nginx -t &&
service nginx start &&
streamlit run app.py --theme.base "dark" & #--server.port 80 
sleep 300 &&
certbot --nginx -d ailytics.francecentral.azurecontainer.io --non-interactive --agree-tos --register-unsafely-without-email --redirect &&
tar -cpzf /mnt/letsencrypt/etc.tar.gz -C / etc/letsencrypt/ &&
while true; do sleep 600; done