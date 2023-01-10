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

One line update:
10. ``git add . && git commit -m "<commit-message>"``
11. add stage 1 to the dvc.yaml file and run - ``dvc repro``

``dvc metrics show``
``dvc metrics diff``

## Test
pytest: ``pytest -v``
``tox.ini``

run test: ``tox``
rebuild/after updating requirements.txt: ``tox -r``

### Setup 
setup.py 

run the setup: ``pip install -e .``

show install packages: ``pip freeze``

Create a distribution in 'dist' folder what can be share for other collaborators for environment setup: ``python setup.py sdist bdist_wheel``

build your own package commands: ``python setup.py sdist bdist_wheel``


**PEP 8 - Style Guide for Python Code**: ``flake8``
running flask app: ``python app.py``

``cp .\saved_models\model.joblib .\prediction_service\model\``
