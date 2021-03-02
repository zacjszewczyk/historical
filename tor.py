#!/usr/bin/python3

# Imports
from libs.web import Web # Web requests library.
from re import search # Resource extraction.
from sys import exit # Error handling.
from os import system, mkdir, listdir, walk # Compressed files. Directory ops.
from os.path import exists # File checking.

# If run as a standalone program, retrieve all available Tor exit node lists.
if (__name__ == "__main__"):
    # Create the "tor" directory if it doesn't already exist.
    if (not exists("./tor")):
        mkdir("./tor")

    w = Web()

    # Retrieve webpage containing historical list of Tor exit nodes.
    w.get("https://metrics.torproject.org/collector/archive/exit-lists/")
    tor_lists = w.get_data().split('\n')
    
    # Extract all Tor exit node lists from the stored webpage.
    for i,line in enumerate(tor_lists):
        line = line.strip() # Strip whitespace from each line.

        # Only consider lines with links to historical Tor exit node lists.
        if ("https://collector.torproject.org/archive/exit-lists/exit-list" in line):
            
            # Specify dates to include
            if (any([x in line for x in ["2021-02", "20201-03"]])):
                print("FOUND!")
            else:
                continue

            # Extract the exit node list URL
            m = search("(?=http)http[^\"]+", line)
            
            if (m): # Retrieve the exit node list if it does not exist locally.
                filename = m.group(0).split('/')[-1]
                if (exists(f"./tor/{filename}")):
                    print(f"./tor/{filename} exists. Skipping.")
                else:
                    print(f"Retrieving {m.group(0)} ...", end="", flush=True)
                    system(f"wget --quiet {m.group(0)} -O tor/{filename}")
                    print("done.")

            else: # Handle errors by notifying and exiting.
                print("Error extracting Tor node list.")
                print(line)
                exit(1)

    # Extract contents of all .tar.xz archives in ./tor
    for each in listdir("./tor"):
        if (".tar.xz" in each):
            if (not exists(f"./tor/{each[:-7]}")):
                print(f"Extracting {each} ... ", end="", flush=True)
                system(f"tar -xf ./tor/{each} -C ./tor 1> /dev/null")
                print("done")
            else:
                print(f"./tor/{each[:-7]} exists. Skipping.")


    # Keep track of the number of files processed
    file_count = 0
    # And the number of Tor nodes processed
    tor_count = 0

    # Clear the output CSV file, then insert its header.
    open("./tor.csv", "w").close()
    o_fd = open("./tor.csv", "a")
    o_fd.write("exit_node,published,last_status,ip,ip_ts\n")

    # Iterate over extracted Tor exit list archives to build historical Tor
    # exit node CSV.
    for folder in listdir("./tor"):
        # Only consider folders, not .tar.xz archives.
        if (".tar.xz" not in folder):
            # Recursively move through the extracted archives to find the
            # files with the actual exit node listings.
            for root, dirs, files in walk(f"./tor/{folder}", topdown=True):
                # Open the exit node listings.
                for file in files:
                    # Output a status message to the user.
                    print(f"Processing {root}/{file} ... ", end="", flush=True)
                    
                    # Open the file.
                    i_fd = open(f"{root}/{file}", "r")

                    # Iterate over the file. Ignore the first two lines
                    # (metadata), then parse each line according to its label.
                    for i,line in enumerate(i_fd):
                        if (i < 2): continue
                        if (line.startswith("ExitNode")):
                            exit_node = ""
                            published = ""
                            last_status = ""
                            exit_address = ""
                            exit_ts = ""
                            exit_node = line.split(' ',1)[1].strip()
                        if (line.startswith("Published")):
                            published = line.split(' ',1)[1].strip()
                        if (line.startswith("LastStatus")):
                            last_status = line.split(' ',1)[1].strip()
                        if (line.startswith("ExitAddress")):
                            line = line.split(' ',2)
                            exit_address = line[1].strip()
                            exit_ts = line[2].strip()                            
                            o_fd.write(f"{exit_node},{published},{last_status},{exit_address},{exit_ts}\n")
                            tor_count += 1

                    print("done.")
                    file_count += 1

                    # Close the input file
                    i_fd.close()

    # Cleanup
    o_fd.close()

    print(f"Done. {file_count:,} files processed with {tor_count:,} exit node entries.")