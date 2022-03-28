U-Measure
=========
A GUI software application for ultrasonic data collection.

Installation
------------
This software is developed with python 3.10. No other versions of python are tested.

### Executables
The executables do not require any additional packages to be installed, other than the VISA requirements.
Additional platforms can be supported.

https://github.com/skordaschristofanis/U-Measure/releases

### Source files
In order to use the source files, please install requirements and VISA requirements.

#### Running from source
```bash
python Measure.py
```


VISA Requirements
-----------------
- NIVisa
- tekVisa

Requirements
------------

- qtpy (a wrapper for PyQt/PySide)
- PyQt6 / PySide6 
- PyVisa

```python
pip install -r requirements.txt  # (replace requirements.txt with /path/to/requirements.txt if not in root directory)
```
