# Overall Instructions

## Setup KaliVM on Mac OSX

Install KaliVM on Mac OSX, see [details here](https://github.com/jhu-information-security-institute/NwSec/wiki/JHUISI-VM).

## Setup Docker on KaliVM and Ubuntu

1. Install Docker and Docker machine on KaliVM and Ubuntu
2. Test Docker was installed correctly: `$ docker run hello-world`

## Setup KaliVM on Raspberry Pi (later changed to Ubuntu) and Network Setup for RPi

See instructions [here](https://github.com/jhu-information-security-institute/NwSec/wiki/Kali-RPI4B).

## Setup cross compile environment (VM running Kali OS)

1. Download [gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu](https://releases.linaro.org/components/toolchain/binaries/7.4-2019.02/aarch64-linux-gnu) and install in `/opt/gnu/gcc-linaro-7.4.1-2019.02-x86_64_aarch64-linux-gnu` (note: this version is closest to the gcc binary installed on the RPI4B, Ubuntu/Linaro 7.4.0-1ubuntu1~18.04.1, see detailed [link](https://releases.linaro.org/components/toolchain/binaries/7.4-2019.02/aarch64-linux-gnu/))
2. Build the container `$ sudo docker build -t tubuntubuildenv:2 .`
3. run the container `$ sudo docker run --name ubuntubuildenv2 -v /opt/gnu:/opt/gnu -it -d tubuntubuildenv:2`
4. From the host, copy the cross-compile.sh file into it using:`$ sudo docker cp cross-compile.sh ubuntubuildenv2:/qbittorrent-4.2.2`
5. Run the container:  `$ sudo docker start ubuntubuildenv2` `$ sudo docker exec -it ubuntubuildenv2 bash`
6. Go to the qbittorrent folder: `$ cd /qbittorrent-4.2.2`
7. then, build it by running `$ sh cross-compile.sh`

## Setup build environment (RPI running Ubuntu OS)

1. Enter the corresponding folder: `$ cd ubuntubuildenv`
2. Build the Docker image: `$ sudo docker build -t tubuntubuildenv:latest .`
3. Build the Docker container: `$ sudo docker run --name ubuntubuildenv -it tubuntubuildenv:latest bash`
4. After entering the container, enter the qbittorent folder to install the qbittorrent application: `$ cd qbittorrent-4.2.2`
5. `$ make install`
6. `$ exit`

    To run the application in the runtime environment, we need to copy the generated binary file and dependency library to the local folder, then copy into the runtime container later.

7. Then copy the binary files and dependencies to the runtime folder: 

    `$ sudo docker cp ubuntubuildenv:/usr/local/bin/qbittorrent-nox ../ubunturunenv`

    `$ sudo docker cp ubuntubuildenv:/usr/local/lib/libtorrent-rasterbar.so.10 ../ubunturunenv`

    `$ sudo docker cp ubuntubuildenv:/usr/local/lib/libtorrent-rasterbar.so.10.0.0 ../ubunturunenv`

## Setup build environment (VM running Kali OS)

1. Enter the corresponding folder: `$ cd kalibuildenv`
2. Build the Kali Docker image:`$ sudo docker build -t tkalibuildenv:latest .`
3. Build the Kali Docker container then enter it: `$ sudo docker run --name kalibuildenv -it tkalibuildenv:latest bash`
4. After entering the container, enter the qbittorent folder to install the qbittorrent application: `$ cd qbittorrent-4.2.2`
5. `$ make install`
6. `$ exit`

    To run the application in the runtime environment, we need to copy the generated binary file and dependency library to the local folder, then copy into the runtime container later.

7. Copy the binary files and dependencies to the runtime folder: 
`$ sudo docker cp kalibuildenv:/usr/local/bin/qbittorrent-nox ../kalirunenv`
`$ sudo docker cp kalibuildenv:/usr/local/lib/libtorrent-rasterbar.so.10 ../kalirunenv`
`$ sudo docker cp kalibuildenv:/usr/local/lib/libtorrent-rasterbar.so.10.0.0 ../kalirunenv`

## Setup runtime environment (RPI running Ubuntu OS)

After running the building environment, we need to copy the compiled executable binary file and dependencies from the local folder to the runtime container to run our application.

1. Enter the corresponding folder: `$ cd ubunturunenv`
2. Build the runtime Ubuntu image: `$ sudo docker build -t tubunturunenv:latest .`
3. Build the runtime Ubuntu container: `$ sudo docker run --name ubunturunenv -it -d tubunturunenv:latest`
4. Copy the binary file and dependencies from current folder into runtime Ubuntu container: 

    `$ sudo docker cp qbittorrent-nox ubunturunenv:/usr/local/bin/`

    `$ sudo docker cp libtorrent-rasterbar.so.10 ubunturunenv:/usr/local/lib/`
    
    `$ sudo docker cp libtorrent-rasterbar.so.10.0.0 ubunturunenv:/usr/local/lib/`   
    
5. Then enter the container to run the application: `$ docker exec -it ubunturunenv bash`
6. Add path to run in the terminal: `$ echo /opt/usr/lib > /etc/ld.so.conf.d/qbittorrent.conf && ldconfig`
7. Then start the application: `$ qbittorrent-nox`

## Setup runtime environment (VM running Kali OS)

After running the building environment, we need to copy the compiled executable binary file and dependencies from the local folder to the runtime container to run our application.

1. Enter the corresponding folder: `$ cd kalirunenv`
2. Build the runtime Kali image: `$ sudo docker build -t tkalirunenv:latest .`
3. Build the runtime Kali container: `$ sudo docker run --name kalirunenv -it -d tkalirunenv:latest`
4. Copy the binary file and dependencies from current folder into runtime Kali container: 

    `$ sudo docker cp qbittorrent-nox kalirunenv:/usr/local/bin/`

    `$ sudo docker cp libtorrent-rasterbar.so.10 kalirunenv:/usr/local/lib/`

    `$ sudo docker cp libtorrent-rasterbar.so.10.0.0 kalirunenv:/usr/local/lib/` 
5. Then enter the container to run the application: `$ sudo docker exec -it kalirunenv bash`
6. Add path to run in the terminal: `$ echo /opt/usr/lib > /etc/ld.so.conf.d/qbittorrent.conf && ldconfig`
7. Then start the application: `$ qbittorrent-nox`

## qBittorrent controls and queries status



