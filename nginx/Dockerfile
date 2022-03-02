# Pull official base image
FROM nginx

# Delete nginx default.conf
RUN rm /etc/nginx/conf.d/default.conf

# Add custom nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf