### Check Python and Pip versions
- `python3 --version`
- `pip3 --version`

### Install NumPy for the Correct Python Version
- `which python3` --> `/path/to/your/python3 -m pip install numpy`
#### Use a Virtual Environment
- `python3 -m venv myenv`      # Create a virtual environment named 'myenv'
- `source myenv/bin/activate`  # Activate the virtual environment
- `pip install numpy`          # Install NumPy in the virtual environment
