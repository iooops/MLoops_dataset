
# Dataset

The dataset is created mainly from the loopazon website: https://www.loopazon.com/.

The processed data can be accessed at https://drive.google.com/drive/folders/12WZU5IEElXMtQl8aHQwCtmMri0WnDRSJ?usp=sharing.


# Running the Code

Once you download the data, you can run the code in this repository.

Before running the code in `data_analysis_benchmarking.ipynb` and `tempo_cnn.ipynb`, remember to set the environment variable `MLOOPS_DIR` in the notebook.

`data_analysis_benchmarking.ipynb`, `tempo_cnn.ipynb`, `qwen_eval.ipynb` are mainly about data analysis and benchmarking. Since Qwen-Audio requires a different conda environment setting and takes more time to run, we created a `instr.py` file and put the evaluation code in `qwen_eval.ipynb` with the output `qwen_cats.json`.
