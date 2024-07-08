# Usa una imagen base de Node.js
FROM node:14

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de package.json y package-lock.json e instala las dependencias
COPY package*.json ./
RUN npm install

# Copia el resto de los archivos del proyecto
COPY . .

# Compila la aplicación
RUN npm run build

# Expone el puerto de la aplicación
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
