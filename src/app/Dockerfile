FROM mambaorg/micromamba:0.15.3
USER root
RUN apt-get update && DEBIAN_FRONTEND=“noninteractive” apt-get install -y --no-install-recommends \
       nginx \
       ca-certificates \
       apache2-utils \
       certbot \
       python3-certbot-nginx \
       sudo \
       cifs-utils \
       && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install cron
RUN mkdir /opt/gen_ai_hackaton
RUN chmod -R 777 /opt/gen_ai_hackaton
WORKDIR /opt/gen_ai_hackaton
USER micromamba
COPY . .
RUN micromamba install -y -n base -f environment.yml && \
   micromamba clean --all --yes
USER root
RUN chmod a+x run.sh run_without_ssl.sh generate_ssl.sh
RUN touch /var/log/cron.log
# Setup cron job
RUN (crontab -l ; echo "0 12 12 * * /usr/bin/certbot renew --quiet && tar -cpzf /mnt/letsencrypt/etc.tar.gz -C / etc/letsencrypt/ ") | crontab
# CMD ["./run_without_ssl.sh"]
# CMD ["./generate_ssl.sh"]
CMD ["./run.sh"] 