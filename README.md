# CoughAgainstCovid Official Dataset Repository 
This is the official repository for accessing the data used by the project [CoughAgainstCovid](https://www.wadhwaniai.org/programs/cough-against-covid/).

### Data Description 
Due to privacy constraints, we are not allowed to release the original raw audiowaveforms. Instead we release spectrograms, which are 2D time-frequency representations of the audio. To create the spectrograms from the raw audio waveform, we used the following transforms, 
1. ToTensor
2. Resample (44.1khz to 16khz)
3. Background Noise (From ESC-50 Dataset)
4. Spectrogram (n_fft=512, win_length=512, hop_length=160)
5. MelScale (n_mels=64, f_min=125, f_max=7500)
6. AmplitudeToDB
6. ToNumpy

We share the 2D numpy arrays (npy files) for all the audio sounds collected.

### Accessing/Downloading the Data
To download/access the spectrograms, 
1. Fill the [form](https://docs.google.com/forms/d/e/1FAIpQLSdi-0HL6LLLCSMXK6rnBTs_MuD8E6lsOJbSD6EwH4bQQUBZ8A/viewform) and attach the signed doc file. You will receive a text file with the links in 10-15 mins.
2. Download the text file, rename it (to say links.txt) and save it at a location where you can access it.
4. Run prepare.py to download and unzip the data. (This script should take 1-2hrs depending upon the download speed)

```bash
# To run prepare.py and download, unzip the data at ~/data, (wget would be used to download)
python prepare.py -lp path_to_links_file -od ~/data

Args:
    links_path (lp): Path to the text file with the links to the zip files.
    output_dir (od): Path to the output directory. If it does not exist, it will be created
```

Running this script will download the data and unzip it to the output directory. The spectrograms should be present at `output_dir/spectrograms/`

<!-- ### Using the Data
To use the spectrograms, use the `viz.ipynb` notebook. You would need torch, jupyter, pandas, matplotlib and torchvision to use this notebook. 

To set up a conda environment, run the following command in the terminal.
```bash
conda create -n cac-covid-env
conda activate cac-covid-env
conda install -c conda-forge matplotlib pytorch torchvision pandas jupyter

# to start a jupyter notebook
jupyter notebook
``` -->

### Metadata Details
We provide a metadata file (`attributes.csv`) that contains supplementary information about the patients. The table contains the supplementary information present in the csv file.

| Attribute                           |              Column Name in CSV               | Description       |
| ----------------------------------- | :-------------------------------------------: | ----------------- |
| Patient Id                          |                  patient\_id                  | Unique Identifier |
| Patient Age                         |             enroll\_patient\_age              | Continuous        |
| Health Worker                       |            enroll\_health\_worker             | Discrete          |
| Temperature                         |         enroll\_patient\_temperature          | Continuous        |
| Travel History                      |            enroll\_travel\_history            | Discrete          |
| Presence of Cough                   |                 enroll\_cough                 | Discrete          |
| Presence of Shortness of Breath     |         enroll\_shortness\_of\_breath         | Discrete          |
| Presence of Fever                   |                 enroll\_fever                 | Discrete          |
| Days with Cough                     |           enroll\_days\_with\_cough           | Continuous        |
| Days with Shortness of Breath (SOB) |   enroll\_days\_with\_shortness\_of\_breath   | Continuous        |
| Days with Fever                     |           enroll\_days\_with\_fever           | Continuous        |
| Contact with Covid Confirmed Case   | enroll\_contact\_with\_confirmed\_covid\_case | Discrete          |
| Comorbidities                       |             enroll\_comorbidities             | Discrete          |
| Patient Respiratory Rate            |      enroll\_patient\_respiratory\_rate       | Continuous        |
| Smoking Habits                      |                enroll\_habits                 | Discrete          |
| Cough Relief Measures               |        enroll\_cough\_relief\_measures        | Discrete          |
| State                               |               testresult\_state               | Discrete          |
| Test Facility                       |             testresult\_facility              | Discrete          |
| Test Time                           |             testresult\_end\_time             | DateTime          |
| Covid Result                        |        testresult\_covid\_test\_result        | Discrete          |
| Covid Test Type                     |      testresult\_diagnostics\_test\_type      | Discrete          |
| Audio Recording (aaaaaa sound)      |                aaaaa_recording                | File Name         |
| Audio Recording (oooooo sound)      |                ooooo_recording                | File Name         |
| Audio Recording (eeeeee sound)      |                eeeee_recording                | File Name         |
| Audio Recording (a sound)           |                    a_sound                    | File Name         |
| Audio Recording (e sound)           |                    e_sound                    | File Name         |
| Audio Recording (o sound)           |                    o_sound                    | File Name         |
| Audio Recording (Cough Sound 1)     |                    cough_1                    | File Name         |
| Audio Recording (Cough Sound 2)     |                    cough_2                    | File Name         |
| Audio Recording (Cough Sound 3)     |                    cough_3                    | File Name         |
| Audio Recording (Breathing)         |                   breathing                   | File Name         |
| Audio Recording (1 to 10 Counting)  |                 audio_1_to_10                 | File Name         |
| Audio Recording (Room)              |                  room_sound                   | File Name         |
| Audio Recording (Room Recording)    |                room_recording                 | File Name         |

While we collect cough sounds for all the 7169 patients, we collect some outher sounds as well. The audio recording for them would exist only if their filename exists in this metadata file.

## Dataset Paper will be Released Soon.
