# PDS-Tarea-1


## Dependencies 
For a reproducible enviroment Conda Miniforge was used. For Linux Ubuntu, the following command was used:
```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

## Running scripts
1.  Run the enviroment script to setup dependencies
```
conda env create -f environment.yml
conda activate pds-tarea1
```
2. Run script
```
python3 vis-senal-alias.py
```
3. Exit enviroment
```
conda deactivate
```

### Script Options
On launching the script the user will be presented with options for creating
the sine waves
```
    1) Set analog signal frequency (Hz)
    2) Set sample frequency
    3) Set number of cycles to graph for the signal
    4) Create graph of the signal
    5) Exit
```
Options 1 and 2 will allow to set values for the frequencies and sampling frequencies.
These allow for fractions and float numbers to be set. Negative values are not permitted.

```
3) Set number of cycles to graph for the signal
```
Option 3 will set how many complete cycles of the sine wave are plotted on the 
displayed graph.

```
4) Create graph of the signal
```
Once the parameters are set, option 4 will create the desired plots. **If no values are
input, default value are used**. 

```
5) Exit
```
Use option 5 to exit

## Troubleshooting
When installing the conda enviroment. The base enviroment might not activate. This can
result in the `conda` commands not being recognized. This can be fixed by running the
conda binary as follows:
```
<PATH TO MINIFORGE INSTALL>/miniforge3/bin/conda init
```
The terminal should show `(base)` at the start of the line if the conda base
enviroment was succesfully enabled.
