# Wine.Quality-MLOps
MLOps

## Step: 1
1. Create environment
```bash
conda create -n <environment-name> python=3.10 -y
```
2. Activate environment
```bash
conda activate <environment-name>
```
3. Create a requirements.txt file
   * Install the requirements
```bash
pip install -r requirements.txt
```
4. Download the dataset - [winequality.csv](https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec)
5. ``git init``
6. ``dvc init``
7. ``dvc add data data_given/<dataset-name>``
8. ``git add.``
9. ``git commit -m "<commit-message>"``