# Home-Control
A home control centre from the a smartphone.

# History
I recently wanted to see how I can connect to a localhost server on my laptop
through my smartphone. Turns out this is [very easy](https://stackoverflow.com/questions/4779963/how-can-i-access-my-localhost-from-my-android-device)
if you know the `IP` address of your laptop. So I went on and created a small
controller for my laptop, i.e. a web page with buttons to turn on/off programs.

# Installation
This is a python Flask project, and the installation is the usual

```
$ git clone https://github.com/DanielAndreasen/Home-Control
$ cd Home-Control
$ pip install -r requirements.txt # Alternatively make a virtualenv first
$ python app.py
```
Simply open up the localhost at the port indicated after the last command and
you will be able to see a simple control panel.

# Connect your phone
You will need to know the `IP` of your hosting server. On Linux just run
`ifconfig` to find it. I only tested this when the smartphone and laptop are on
the same network! If they are, simply visit `<your IP adress>:<PORT>` and you
are done!

# Add/remove new entry
At the moment of writing, simple edit line 11 in `app.py` and add/delete the
`templates/main.html` file according to your changes.

# Add custom command
Sometimes you don't have the command available that you would like to issue.
Maybe you want to run a script that fetch data and analyse it. Simply write this
in a small script and add the script to your `PATH`.
