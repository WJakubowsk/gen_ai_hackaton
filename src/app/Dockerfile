FROM mambaorg/micromamba:0.15.3
USER root
RUN mkdir /opt/gen_ai_hackaton
RUN chmod -R 777 /opt/gen_ai_hackaton
WORKDIR /opt/gen_ai_hackaton
USER micromamba
COPY . .
RUN micromamba install -y -n base -f environment.yml && \
   micromamba clean --all --yes
USER root
RUN chmod a+x run.sh
CMD ["./run.sh"]