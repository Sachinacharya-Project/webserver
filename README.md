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
````python
    python -m pip install wheel_file_name # For Unit it would be pip3 instead of pip
````
## Usages
1. Basic Command
````python
    server --help
````
This displayes all the options
2. Starting Server
````python
    server
````
This start server on port 8000
URL: http://localhost:8000
3. Passing Options
host: your hostname. Default localhost or 127.0.0.1
port your port. Default 8000
````python
    server --host hostname --port port_number # These are optional parameter. These are not manditory
````
4. Opening PHPMYADMIN
````python
    server --admin
````
This open phpmyadmin.
This is irrespective of the --host and --port (cannot use this with --admin)
It open PhpMyAdmin under the port and host found in settings.json in installed folder. To Access and edit this file, --set can be use as a flag
````python
    server --set
````