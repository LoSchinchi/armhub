# armhub

to install the server and our project:

# install nodejs and npm
- sudo apt install nodejs
- sudo apt install npm

# create the server:
- `mkdir server`
- `cd server`
- `npx express-generator --view=pug`
- `npm i`
- `npm i nodemon jquery fs child_prcess`
- in `package.json` modify `"start": "node ./bin/www"` in `"start": "nodemon ./bin/www"`

# install python modules:
- `sudo apt-get -y install python-rpi.gpio`

to run the server, execute `npm start` in terminal in server directory, you will see your site at [localhost:3000](http://localhost:3000)
