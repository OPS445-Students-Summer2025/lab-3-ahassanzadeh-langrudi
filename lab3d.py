#!/usr/bin/env python3
#Author ID: ahassanzadeh-langrud

import subprocess

def free_space():

    command = "df -h | grep '/$' | awk '{print $4}'"
    
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    return result.stdout.strip()

if __name__ == "__main__":
   
    print(free_space())
