# Installation

First, install [anaconda](https://www.anaconda.com/products/distribution) or [mini-conda](https://docs.conda.io/en/latest/miniconda.html) on your computer as explained in [this blog post](https://biapol.github.io/blog/johannes_mueller/anaconda_getting_started/).

Afterwards, install [devbio-napari](https://www.napari-hub.org/plugins/devbio-napari) by setting up an environment for it. Start by installing mamba in your base environment:

```
conda install mamba -c conda-forge
```

Afterwards, create the environment using mamba.

```
mamba create --name devbio-napari-env python=3.9 devbio-napari -c conda-forge
```
alternatively:
```
conda create --name devbio-napari-env python=3.9 devbio-napari -c conda-forge
```

Afterwards, activate the environment like this:
    
    conda activate devbio-napari-env

Mac-users please also install this:

    mamba install -c conda-forge ocl_icd_wrapper_apple
    
Linux users please also install this:
    
    mamba install -c conda-forge ocl-icd-system

Afterwards, run this command from the command line

```
naparia
```

This window should open. It shows the [Assistant](https://www.napari-hub.org/plugins/napari-assistant) graphical user interface. 

![img.png](https://github.com/haesleinhuepf/devbio-napari/raw/master/docs/screenshot.png)

## Troubleshooting: Graphics cards drivers

In case error messages contains "ImportError: DLL load failed while importing cl: The specified procedure could not be found" [see also](https://github.com/clEsperanto/pyclesperanto_prototype/issues/55) or ""clGetPlatformIDs failed: PLATFORM_NOT_FOUND_KHR", please install recent drivers for your graphics card and/or OpenCL device. Select the right driver source depending on your hardware from this list:

* [AMD drivers](https://www.amd.com/en/support)
* [NVidia drivers](https://www.nvidia.com/download/index.aspx)
* [Intel CPU OpenCL drivers](https://www.intel.com/content/www/us/en/developer/articles/tool/opencl-drivers.html#latest_CPU_runtime)
* [Microsoft Windows OpenCL support](https://www.microsoft.com/en-us/p/opencl-and-opengl-compatibility-pack/9nqpsl29bfff)

In case installation didn't work in the first attempt, you may have to call this command line to reset the napari configuration:

```
napari --reset
```



