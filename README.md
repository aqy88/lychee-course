# Lychee's Class

## Overview
This project uses JupyterLab, a web-based interactive development environment (IDE) that uses "notebooks" to better organize code and data. You will only need to install Git, Docker Engine, then two scripts to get started!

Using Python and a handful of open source packages, you will learn to apply open source machine learning tools in the context of gender bias in supervised learning. Topics covered include:
- Studying the structure of "features" in training data sets.
- Explore a data set and perform basic "preprocessing" techniques.
- Create visualizations.
- Train a naive Bayes classifier while examining the potential and limitations of machine learning.

### Setup
The setup for this project focuses on Linux-based operating systems, and is not readily compatible with Windows without some tinkering. In particular, this guide is focused on setting up the requisite software and tools on MacOS.

Follow the installation steps below in order.

#### 1. Download this repository.

If you are comfortable with `git` and package management, go ahead and clone this repository.

Otherwise, open the green button labeled "Code" at the top of this page on the [Github page](https://github.com/aqy88/lychee-course/tree/main) for this repository and click "Download Zip." You should extract the `.zip`'s contents to its own directory! Take note of where this is.

#### 2. Docker Engine
Follow the steps [here](https://docs.docker.com/desktop/install/mac-install/) to install Docker Engine on your machine.

NOTE: There are two download links, only one of which you will need to use. Click on the Apple logo on the top left of your screen, then "About." The "Processor" field should indicate if your chip is Intel or Apple; use the appropriate download link.

After installation and restarting your machine, make sure Docker Engine is running.

### Getting Started

Inside this repository, you will find 3 scripts:
- `setup.sh`
- `startup.sh`
- `stop.sh`

All of these scripts must be run from root level directory of this repository. Simply put, these scripts can only be run from the folder where this README is located. 

The deployed JupyterLab container mounts the `data-volume` directory in this repository to the default working path to the container itself. Simply put, any changes to available resources in JupyterLab should be reflected in the `data-volume` folder itself on your machine.

1. In the terminal, you will need to `cd` (change directory) to where this repository is located. For example, if you have downloaded these resources to `/Users/YourUserName/someFolder`, when entering the terminal, you must run:
	```
	cd /Users/YourUserName/someFolder
	```
	Again, the `.sh` scripts can ONLY be run from this folder.

2. Verify that you have `cd`'d to the right folder. Running `pwd` will output the current working directory. It should output a path that matches where this repository was downloaded. Alternatively, after step 1, running `ls` should output a list of all of the files present in this repository.
	```
	pwd
	ls
	```

3. With Docker Engine running, build the image that the environment will use to deploy JupyterLab. This may take some time to run. This step only needs to be run once (unless you manage to delete the created image).
	```
	./setup.sh
	```

4. With the image built, you are ready to start!
	```
	./start.sh
	```

5. You have successfully launched JupyterLab on your Mac machine! In the browser of your choice, navigate to http://127.0.0.1:8888.

6. Open the `work` folder on the navbar to the left of the screen. Open `hello-world.ipynb`, then click on the "Play" arrow. It should print "Hello, world!", meaning that you have successfully completed setup!

To stop running JupyterLab, run the stop script. You may start and stop JupyterLab at any point.
```
./stop.sh
```

