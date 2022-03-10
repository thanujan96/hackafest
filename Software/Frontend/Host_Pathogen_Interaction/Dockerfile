# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.9-buster


#install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

COPY nginx.default /etc/nginx/sites-available/default

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


#copy source and install dependencies
RUN mkdir -p /usr/src/Host_Pathogen_Interaction
RUN mkdir -p /usr/src/Host_Pathogen_Interaction/pip_cache

WORKDIR /usr/src/Host_Pathogen_Interaction

COPY requirements.txt start-server.sh /usr/src/Host_Pathogen_Interaction/
COPY .pip_cache /usr/src/Host_Pathogen_Interaction/pip_cache
COPY Host_Pathogen_Interaction /usr/src/Host_Pathogen_Interaction/Host_Pathogen_Interaction/
RUN pip3 install -r requirements.txt --cache-dir /usr/src/Host_Pathogen_Interaction/pip_cache
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/Host_Pathogen_Interaction/entrypoint.sh
# RUN chown -R www-data:www-data /usr/src/Host_Pathogen_Interaction/
RUN chmod +x /usr/src/Host_Pathogen_Interaction/entrypoint.sh

#start server
EXPOSE 8020
STOPSIGNAL SIGTERM
# run entrypoint.sh
ENTRYPOINT ["/usr/src/Host_Pathogen_Interaction/entrypoint.sh"]