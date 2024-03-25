# Step 1: Use an official Node image as the base
FROM node:14-alpine as build-stage

# Step 2: Set the working directory inside the container
WORKDIR /frontend

# Step 3: Copy the package.json and package-lock.json (if available)
COPY package*.json ./

# Step 4: Install all dependencies
RUN npm install

# Step 5: Copy the rest of your application's source code
COPY . .

# Step 6: Build your application
RUN npm run build

# Step 7: Use an Nginx image to serve your application
FROM nginx:stable-alpine as production-stage

# Step 8: Copy the build from the previous stage to Nginx's serve directory
COPY --from=build-stage /frontend/build /usr/share/nginx/html

# Step 9: Expose port 80 to access the container
EXPOSE 80

# Step 10: Start Nginx
CMD ["nginx", "-g", "daemon off;"]
