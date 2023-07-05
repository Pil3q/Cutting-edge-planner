# Cutting-edge planner
## Problem 
A passion for sewing inevitably leads to a stash of offcuts that could be repurposed for new projects. Measuring, drawing and placing the pattern pieces it's often a tedious and time-consuming task that requires precision and good planning. It's definitely not as much fun as sewing! This app will help you check if the required pattern pieces for your project fit in the fabric leftovers and will suggest how to optimize the placement for minimal waste sewing. All you need to know is the measurements of the fabric and of each piece.

## Assumptions
1. Only rectangular and squared pieces are currently supported. All measurements are in centimetres.
2. Patter pieces won't be overlapped
3. Include the seam allowances in the measurements of each pattern piece (We might add an offset option later to automatically calculate seam allowances)
4. Unfortunately, as for now the selvedge is not included in the parameters
5. Pattern matching might be limited
   
## What it does
The program will return the coordinates of each pattern piece as text as shown below. All measurements are in centimetres.

<p align="center">
  <img src="./images/coordinates.png" />
</p>

And it will display a graphic placement suggestion.

<p align="center">
  <img src="./images/result.png" />
</p>

## How do I use it
Prereqs - Python (tested on 3.9)
Install requirements with
```bash
pip install -r requirements.txt
```

Define the project in `input.json` file:
```json
{
  "project_name": "my_project",
  "material_dimensions": [105, 68],
  "cut_dimensions": {
    "A": [52.5, 41],
    "B": [41, 17],
    "C": [53, 7],
    "D": [52.5, 41],
    "E": [41, 17]
  }
}

```

Run the program from the repo directory with 
```bash
python how_to_cut.py
```
