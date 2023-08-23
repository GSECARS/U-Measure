# U-Measure

[![License](https://img.shields.io/badge/license-GPL--3.0-orange.svg)](LICENSE) 
![Python](https://img.shields.io/badge/python-v3.10,_v3.11-blue.svg?logo=python)
[![GSEWidgets](https://img.shields.io/badge/GSEWidgets-v0.0.2-forestgreen.svg)](https://github.com/GSECARS/GSEWidgets/)
[![GSELogger](https://img.shields.io/badge/GSELogger-v1.0.1-forestgreen.svg)](https://github.com/GSECARS/GSELogger/)

U-Measure is an ultrasonic measurement data collection software.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Requirements
The following VISA packages are required regradless of the installation method you choose.

- [NI-VISA](https://www.ni.com/en-us/shop/product/ni-visa.html)
- [Tek-VISA](https://www.tek.com/en)

### Source code requirements
The following packages are only required if you choose to install the software from source.
- Python >= 3.11
- GSEWidgets >= 0.0.2
- GSELogger >= 1.0.1
- qtpy >= 2.3.1
- PyQt6 >= 6.5.2
- PyVisa >= 1.13.0

To install the requiremets run the following command:
```python
pip install -r requirements.txt  # (replace requirements.txt with /path/to/requirements.txt if not in root directory)
```

## Installation
------------
U-Measure can be installed as an executable or from the source files. **In both cases NI Visa and Tek VISA packages
are required, [see requirements](#requirements).**

### Executables
You can find the executables under the project [releases](https://github.com/GSECARS/U-Measure/releases).

### Source files
To install from source follow the steps bellow:

- Clone the repository and navigate to the project folder:
  ```bash
  git clone -b main https://github.com/GSECARS/U-Measure.git && cd U-Measure
  ```
- Install the project localy:
  ```bash
  pip install .
  ```
- Run it using the following command:
  ```bash
  python Measure.py
  ```

## Contributing

All contributions to U-Measure are welcome! Here are some ways you can help:
- Report a bug by opening an [issue](https://github.com/GSECARS/U-Measure/issues).
- Add new features, fix bugs or improve documentation by submitting a [pull request](https://github.com/GSECARS/U-Measure/pulls).

Please adhere to the [Github flow](https://docs.github.com/en/get-started/quickstart/github-flow) model when making your contributions!
This means creating a new branch for each feature or bug fix, and submitting your changes as a pull request against the main branch.
If you're not sure how to contribute, please open an issue and we'll be happy to help you out.

By contributing to U-Measure, you agree that your contributions will be licensed under the GNU General Public License version 3.0.

## License

U-Measure is distributed under the GNU General Public License version 3. You should have received a [copy](LICENSE) of the GNU General Public License along with this program. 
If not, see https://www.gnu.org/licenses/ for additional details.

##
[Christofanis Skordas](mailto:skordasc@uchicago.edu) - Last updated: 23-Aug-2023