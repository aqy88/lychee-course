# An Introductory Exploration of Gender Bias Analysis with an NB Classifier vs Distilled LLM

## Overview
This project uses JupyterLab, a web-based interactive development environment (IDE) that uses "notebooks" to better organize code and data. You will only need to install Docker Engine, then run two scripts to get started!

Using Python and a handful of open source packages, you will learn to apply open source machine learning tools in the context of gender bias in supervised learning. Topics covered include:
- Studying the structure of "features" in training data sets.
- Explore a data set and perform basic "preprocessing" techniques.
- Create visualizations.
- Train a naive Bayes classifier and distilled pre-trained LLM while examining the potential and limitations of machine learning.

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

NOTE: If a dialog box says the "kernel" has "died" while running the notebooks, you may need to increase the memory allocated to Docker (Open Docker => Click gearbox (settings) => Resources).

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

### Converting TSV Data into Hugging Face-compatible Dataset

The `.tsv` files that the NB classifier uses are not directly compatible for use with `distilled-llm_exercise.ipynb`. The data in `aggregate_data.tsv` has already been converted for use with Hugging Faces into the `dataset` directory, but the `data_manip.py` script provided allows for an enabled user to do this conversion as well.

```bash
# Ideally, `cd` into ./data-volume dir to run this script.
# python ./data_manip.py <input TSV file here> <desired output directory here>
python ./data_manip.py aggregate_data.tsv output-data-dir/
```

The output directory for the converted dataset should be swapped into the top dataset loading command in `distilled-llm_exercise.ipynb`.

## Sources

### Paper Citations

Kalra, A., & Zubiaga, A. (2021). Sexism identification in tweets and gabs using deep neural networks. *arXiv preprint arXiv:2111.03612*.

Doughman, J., & Khreich, W. (2022). Gender bias in text: Labeled datasets and lexicons. *arXiv preprint arXiv:2201.08675*.

### Datasets

[https://www.kaggle.com/datasets/dgrosz/sexist-workplace-statements](https://www.kaggle.com/datasets/dgrosz/sexist-workplace-statements)

[https://github.com/khahnmad/DSP/blob/main/sexism_data.csv](https://github.com/khahnmad/DSP/blob/main/sexism_data.csv)

Additional datasets constructed by Andy Yang, using `llama.cpp` [(LINK)](https://github.com/ggerganov/llama.cpp) and a pre-quantized Llama 3 model [(LINK)](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF).

### Online Guides

NB classifier developed from [this Coursera course](https://www.coursera.org/learn/twitter-sentiment-analysis/).

Distilled LLM sentiment analysis exercise derived from [DistilBERT base model (uncased)](https://huggingface.co/distilbert/distilbert-base-uncased). More documentation [here](https://huggingface.co/docs/transformers/en/model_doc/distilbert) and a good blog post [here](https://medium.com/huggingface/distilbert-8cf3380435b5).
