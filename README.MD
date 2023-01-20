# DoppelTest

## Introduction

DoppelTest is a Doppelganer Testing approach for automatically finding bug-revealing
violations of autonomous driving systems. We recommend obtaining the artifact from
GitHub at https://github.com/YuqiHuai/DoppelTest, we also make a version available
via an archival repository at **URL TO BE ADDED**.


## Requirements

### HARDWARE:

1. CPU: Intel Core i9 12900K (24 Core)
2. Memory: 32 GB DDR5 and above
3. Graphics Card: NVIDIA RTX 3090 and above

### SOFTWARE:

1. Ubuntu 18.04 and above
2. Docker-CE version 19.03 and above
3. NVIDIA driver version 455.32.00 and above
4. NVIDIA Container Toolkit (https://github.com/NVIDIA/nvidia-docker)
5. Python 3.8.10 and above

## Installing

### INSTALLING Baidu Apollo

1. Clone the forked version of Apollo 7.0 from https://github.com/YuqiHuai/apollo

> In this forked version, we made slight adjustments that are not related to the AD stack

2. Start up Apollo container via `./docker/scripts/dev_start.sh -l`

3. Find the name of the container via `docker ps -a`

4. Enter the container in root mode via `docker exec -it apollo_dev_your_name /bin/bash`

> Remember to replace `apollo_dev_your_name` with the container's actual name

5. In the container, build Apollo via `./apollo.sh build`

6. Exit the container and create directories `data`, `data/log`, `data/bag`, `data/log`, 
`data/core` under Apollo's root directory.

> This step is necessary for DoppelTest running on the host machine to delete Apollo's log files.
> Our framework restarts modules being tested after every scenario, which creates a large number
> of unnecessary log files.


### INSTALLING DoppelTest

1. Install the required Python libraries: `numpy`, `Shapely`, `DEAP`, `pandas`, `networkx`,
`docker`, and `cyber_record`

2. Replace location of directories in `config.py`

3. Verify the framework is runnable via `python test_main.py`

> You might be prompted to downgrade Python protobuf via `pip install protobuf==3.20.1`

4. Start the magic via `python main_ga.py` or `python main_random.py`

> You should start seeing 2 Apollo instances being started and the scenario is visualizable via
> a browser. DoppelTest will provide the URL to visualize each instance.

## Citing

If you use the project in your work, please consider citing the following work:

```
@inproceedings{doppeltest,
	address = {Melbourne, Australia},
	title = {Doppelganger {Test} {Generation} for {Revealing} {Bugs} in {Autonomous} {Driving} {Software}},
	author = {Huai, Yuqi and Chen, Yuntianyi and Almanee, Sumaya and Ngo, Tuan and Liao, Xiang and Wan, Ziwen and Chen, Qi Alfred and Garcia, Joshua},
    booktitle = {{ACM}/{IEEE} 45th {International} {Conference} on {Software} {Engineering}},
	year = {2023},
}
```