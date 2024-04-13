#!/bin/bash
tar -xzf /mnt/letsencrypt/etc.tar.gz -C / &&
nginx -t &&
service nginx start &&
cron &&
streamlit run app.py --theme.base "dark" #--server.port 80