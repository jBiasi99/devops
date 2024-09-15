# Use a imagem oficial do Nginx
FROM nginx:alpine

# Copie o conteúdo da pasta "public" para a pasta padrão de arquivos do Nginx
COPY ./public /usr/share/nginx/html

# Exponha a porta 80 para acessar o site
EXPOSE 80

# Inicie o Nginx
CMD ["nginx", "-g", "daemon off;"]
