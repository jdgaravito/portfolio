FROM node:lts-slim

# Set the Node environment to development to ensure all packages are installed
ENV NODE_ENV development

# Define build arguments
ARG USER_ID
ARG GROUP_ID

# Define environment variables
ENV USER_ID=$USER_ID
ENV GROUP_ID=$GROUP_ID
ENV USER_ID=${USER_ID:-1001}
ENV GROUP_ID=${GROUP_ID:-1001}

# Add group and user based on build arguments
RUN addgroup --gid ${GROUP_ID} devt
RUN adduser --disabled-password --gecos '' --uid ${USER_ID} --gid ${GROUP_ID} devt
WORKDIR /usr/src/app

# Copy over `package.json` and lock files to optimize the build process
COPY package*.json ./

# Install Node modules
RUN npm install -g npm@latest
RUN npm install  

# Copy over rest of the project files
COPY . .

# Expose port 3000 for the SvelteKit app

EXPOSE 3000

# Run `npm run dev` and set the host to 0.0.0.0 so we can access the web app from outside

CMD [ "npm" , "run" ,  "dev"]
