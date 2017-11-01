# speedtest-py

Command line tool to test the download/upload speed and ping of a network during a determined time

## Requirements
* Python > 3
* [speedtest-cli](https://github.com/sivel/speedtest-cli)
    
    sudo pip install matplotlib
* [matplotlib](https://matplotlib.org/users/installing.html)
    
    sudo pip install matplotlib

## Installation
    git clone 

## Usage
    $ speedtest-py -h
    Speedtest-py

    Usage : speedtest.py -i interval -d duration
    Test the download/upload speed and ping of a network during a determined time.

    Arguments: 
      -i minutes         time interval in minutes
      -d minutes         duration of the test in minutes (0 for no timeout)
      --kill         	kill the process

    Examples: 
      speedtest.py -i 30 -d 3600
      speedtest.py -i 60 -d 0

## Knows bugs
   * Microseconds are displayed on png graph
   * Duration time is not 100% correct (use -d 0)!
