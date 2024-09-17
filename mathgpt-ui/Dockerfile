# Use an official Node.js image as the base
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY package.json yarn.lock ./

# Install the dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN yarn build

# Serve the app with a static server
RUN yarn global add serve

# Expose the port on which the app will be served
EXPOSE 3000

# Start the app
CMD ["serve", "-s", "build"]
