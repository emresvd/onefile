# Merge Imported Modules into One File

This is a Python script that merges all imported modules into a single file. The script takes one argument which is the file path of the main module to be processed.

## Usage
```bash
python onefile.py [file_path]
```
Where `[file_path]` is the file path of the main module to be processed.

## How it works

The script performs the following steps:
1. Reads the contents of the main module file and saves it to the "code" variable.
2. Replaces commas in import statements with line breaks.
3. Imports modules and appends their code to the main module.
4. Iteratively repeats steps 2 and 3 until there are no more modules to import.
5. Uses autopep8 to format the final code.
6. Prints the final code.

## Dependencies

The script requires the autopep8 library. To install, run the following command:
```bash
pip install autopep8
```

This README.md file was written by ChatGPT.