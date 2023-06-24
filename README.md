# Cutting-edge planner
## Problem 
A passion for sewing inevitably leads to a stash of offcuts that could be repurposed for a new little project. Drawing and planning the pattern pieces is not as much fun as sewing new items. This app will help you check if the pieces required for your project fit in the fabric leftovers and will suggest how to optimize the placement for minimal waste sewing. All you need to know is the size of the fabric and of each piece.

## Assumptions
1. Only rectangular and squared pieces are currently supported 
2. Remember to include the seam allowances in the measurements of each pattern piece (We might add an offset option later)
3. Patter pieces won't be overlapped

## What it does
The program will return the coordinates of each pattern piece as text as shown below

<p align="center">
  <img src="./images/coordinates.png" />
</p>

and will save a graphic with a cut placement suggestion.

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
