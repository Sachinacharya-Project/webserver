# webserver
This is simple webserver from PHP development Environments.
This helps you to use local-webserver for your developement environment.
This feature came along with the PHP you have on you computer.
This program just help to access it with single command.
This is Command-Line Tool

----------------------------------------------------
## Installation
You can find .whl(wheel) file in dist folder.
Navigate to dist folder and hit the following command
````powershell
    python -m pip install wheel_file_name # For Unix it would be pip3 instead of just pip
````
## Usages
1. Basic Command
````powershell
    server --help
````
This displayes all the options

2. Starting Server
````powershell
    server
````
This start server on port 8000
URL: http://localhost:8000

3. Passing Options
host: your hostname. Default localhost or 127.0.0.1
port your port. Default 8000
````powershell
    server --host hostname --port port_number # These are optional parameter. These are not manditory
````
If --update is passed along with the above flags, Host and Port will be added to settings.json

4. Opening PHPMYADMIN
````powershell
    server --admin
````
This open phpmyadmin.
cannot use this with --admin
It open PhpMyAdmin under the port and host found in settings.json in installed folder or The PORT and HOST passed with flag --port and --host previously. To Access and edit this file, --set can be use as a flag
````powershell
    server --set
````
