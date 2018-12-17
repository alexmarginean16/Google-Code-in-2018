# localhost-task
This task is made of two scripts. A flask server that should run on a laptop to display the battery percentage for a GET request at `/` and a python script running on a Raspberry Pi that makes a get request and changes the state of a LED based on the battery percentage from the laptop.

## Connecting to the localhost - Fedora Project
### Task description

In this task, you have to connect your board with your Fedora terminal.

To accomplish this task, your system should be connected to a WiFi network; and your board should also be connected to the same network through WiFi.

Send the battery percentage of your laptop to the board and if it is less than 20% switch ON a Relay (or or change the state of any output mode, like: LED, DC motor, etc.); and if it reaches 100% switch OFF; print this on the Serial Monitor/Terminal.

For example, if the battery is less than 20%, switch ON you relay (or LED) and if it reaches 100%, switch OFF the relay (or LED)

### Deliverables: 

Both the server side code and the device Sketch; Circuit constructed; sh file if you have used;

NOTE: Please write the necessary comments.