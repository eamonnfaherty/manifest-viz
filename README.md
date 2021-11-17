## What is this?
This reads a manifest.yaml file from the same dir and outputs a graph in graphviz format to std out

Note that this manifest file is AFTER the merge has been completed with all of the add-ons. You can find this file in the "artifacts" bucket under the "BuiltApp" directories.

## How to use it

### Install

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
deactivate
```

### Use it

Drop a manifest.yaml into the directory

```shell
source .venv/bin/activate
python3 viz.py > output.gv
deactivate
```
