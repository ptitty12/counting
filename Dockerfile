FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git openssh-client && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY run.sh update_counter.py ./
# The container just idles; Dokploy's schedule execs "bash run.sh" on a cron.
CMD ["sleep", "infinity"]
