# CoughAgainstCovid Official Dataset Repository 

#### Data 
Due to privacy constraints, we are not allowed to release the original raw audiowaveforms. Instead we release spectrograms, which are 2D time-frequency representations of the audio. To create the spectrograms from the raw audio waveform, we used the following transforms, 
1. ToTensor
2. Resample (44.1khz to 16khz)
3. Background Noise (From ESC-50 Dataset)
4. Spectrogram (n_fft=512, win_length=512, hop_length=160)
5. MelScale (n_mels=64, f_min=125, f_max=7500)
6. AmplitudeToDB
6. ToNumpy

We share the 2D numpy arrays (npy files) for all the audio sounds collected.

#### Accessing/Downloading the Data
To download/access the spectrograms, 
1. Sign the data sharing agreement [doc]()
2. Fill the [form](https://docs.google.com/forms/d/e/1FAIpQLSdi-0HL6LLLCSMXK6rnBTs_MuD8E6lsOJbSD6EwH4bQQUBZ8A/viewform) and attach the signed doc file. 
3. Wait for approval, we generally respond in 2-3 days and longer if it's the weekend. Post Approval you would receive links to the zip files. 
4. Create a text file with the one link per line and save it at a location of your choice.
5. Run prepare.py to download and unzip the data.

```bash
# To run prepare.py and download, unzip the data at ~/data
python prepare.py -lp path_to_links_file -od ~/data

Args:
    links_path (lp): Path to the text file with the links to the zip files.
    output_dir (od): Path to the output directory. If it does not exist, it will be created
```

Running this script will download the data and unzip it to the output directory. The spectrograms should be present at `output_dir/spectrograms/`

#### Using the Data
To use the spectrograms, use the `viz.ipynb` notebook. You would need torch, jupyter, pandas, matplotlib and torchvision to use this notebook. 

To set up a conda environment, run the following command in the terminal.
```bash
conda create -n cac-covid-env
conda activate cac-covid-env
conda install -c conda-forge matplotlib pytorch torchvision pandas jupyter

# to start a jupyter notebook
jupyter notebook
```