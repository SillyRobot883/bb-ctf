FROM nginx:stable

# Copy your website files into the default Nginx HTML directory
COPY . /usr/share/nginx/html

# Expose port 80 to Docker
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]