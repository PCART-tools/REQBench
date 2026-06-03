## What is REQBench?
REQBench is a large-scale benchmark with `2,095` test cases, each labeled with compatibility information. This large-scale dataset serves as a benchmark for evaluating compatible requirements inference approaches of TPL upgrades in Python projects.

## Label Folder Explanation
Each `.json` file in the label directory represents a different scenario used to determine compatibility in TPL upgrades:

| File Name           | Meaning When `false`                            |
| ------------------- | ----------------------------------------------- |
| `pip.json`          | Pip failed to resolve dependencies              |
| `module.json`       | Pip unresolved; issue due to module             |
| `apiname.json`      | Pip unresolved; issue due to API name           |
| `apiparameter.json` | Pip unresolved; issue due to API parameter      |
| `apibody.json`      | Pip unresolved; issue due to API body           |
| `project_tpl.json`  | Pip unresolved; issue at the project-TPL level  |
| `tpl_tpl.json`      | Pip unresolved; issue at the TPL-TPL level      |


## Projects
The source code of each Python project can be accessed at [Zenodo](https://doi.org/10.5281/zenodo.16100741).

### **Example Directory Layout**

```bash
./
├── 3d-ken-burns.tar.gz                            # Project source code
...
```

### :hammer_and_wrench: **Extracting**

To extract the project, run:
```bash
cd /home/usr/
mkdir projects
tar -xzvf projectName.tar.gz -C projects
```

## How Does PCREQ Use It?
Each test case in REQBench can be regarded as an independent test project. To use [PCREQ](https://github.com/PCREQ/PCREQ) to infer compatible requirements in REQBench, you need a configuration file for each test case.

### Batch-Generate Config Files (Recommended)

All test cases are defined in `configure/test.json`. Use `configure/run.py` to batch-generate every `config.json` at once.

**Step 1:** Edit the three paths at the top of `configure/run.py` to match your local environment:
```python
knowledge_path = "/dataset/lei/"              # Change to your knowledge directory
proj_path = "/dataset/lei/projects/"           # Change to your projects directory
requirements_path = "/dataset/lei/requirements/"  # Change to your requirements directory
```

**Step 2:** Run the generator from the `configure/` directory:
```shell
cd configure
python run.py
```
This creates the directory tree `configure/<project>/<library>/<version>/config.json` for all 2,095 test cases.

**Step 3:** Copy the generated config to `PCREQ/configure` and run PCREQ:
```shell
cp configure/PyTorch-ENet/torch/1.2.0/config.json /path/to/PCREQ/configure/
cd /path/to/PCREQ
python main.py --config config.json
```

### Write a Single Config File Manually
Alternatively, create a config.json by hand:
```json
{
    "projPath": "/home/usr/projects/project",
    "requirementsPath": "/home/usr/requirements/project/requirements.txt",
    "targetLibrary": "pillow",
    "startVersion": "6.2.0",
    "targetVersion": "7.0.0",
    "pythonVersion": "3.7",
    "knowledgePath": "/home/usr/knowledge/"
}
```
Then, copy the configuration file to `PCREQ/configure` and run the command as follows:
```shell
python main.py --config config.json
```

## License

REQBench is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [LICENSE.txt](./LICENSE.txt) for details.
