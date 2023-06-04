# Installation

## Installing the conda environment
Based on: 
- https://github.com/ageron/handson-ml3
- https://developer.apple.com/metal/tensorflow-plugin/

and a lot of struggles.

In the end, I removed prior installation of Anaconda and Sage and started from scratch.

```bash
xcode-select --install
brew install miniconda
conda update -n base -c defaults conda
conda init
conda install python=3.10
conda create -n homl3
conda activate homl3
conda install python=3.10
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos
python -m pip install tensorflow-metal

conda env export --no-builds
```

I then updated the environment.yml, merging the results of the export and the book's environment.yml.
Then run:
```bash
conda env update -f environment.yml
python -m ipykernel install --user --name=python3
```

Initially, I attempted:
```bash
conda env create -f environment.yml
conda activate homl3
python -m ipykernel install --user --name=python3
```

### Alternative without Conda:
https://medium.com/@sorenlind/tensorflow-with-gpu-support-on-apple-silicon-mac-with-homebrew-and-without-conda-miniforge-915b2f15425b

```
brew install hdf5
pip install tensorflow-macos
pip install tensorflow-metal
```

Ensure that this is the output:
```
import tensorflow as tf
tf.config.list_physical_devices("GPU")
# => [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```
