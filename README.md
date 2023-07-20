# Cutting-edge planner

## Introduction
A passion for sewing _inevitably_ leads to a stash of offcuts that could be repurposed for a new little project. Drawing and planning the pattern pieces is certainly less fun than sewing new items. This app will help you check if the pieces required for your project fit the fabric leftovers and suggest how to optimize the placement for minimal waste sewing. All you need to know is the size of the fabric leftover and the measurements of each piece needed.

## Use case
The aim of this application is to help the user quickly evaluate if a piece of (scrap) fabric is suitable to be upcycled for a new project. The app will also generate a graphic representation of the optimized pattern layout. Refer to the section [What it does](#what-it-does) for more details.

## Assumptions and Limitations
1. Only rectangular and squared pieces are currently supported. All measurements are in centimetres.
2. Pattern pieces won't be overlapped
3. Include the seam allowances in the measurements of each pattern piece. We might add an offset option later to automatically calculate seam allowances.
4. Unfortunately, the selvedge direction (grainline) is not an available parameter for now.
5. Pattern matching might be limited

We're working on improving this little mighty planner so that new features will be added. Any feedback will help us grow! 

## What it does
The program will return the coordinates of each pattern piece as text as shown below. All measurements are in centimetres.

<p align="center">
  <img src="./images/coordinates.png" />
</p>

And it will display a graphic layout suggestion.

<p align="center">
  <img src="./images/result.png" />
</p>

## How do I use it
As a first step, check you have all the necessary prerequisites.

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
As a final step, run the program from the repo directory with 
```bash
python how_to_cut.py
```

## Practical Example
"Can you help me to figure out if I have enough of this fabric?" - This is the question that started it all!
We have created this planner for a very hands-on problem: the wish of sewing the lining to a recently sewn beach bag. We initially started planning how to cut out the pieces on a simple piece of paper, but the need for something more efficient was clear.
In this case, the lining pieces were reinforced with iron-on interfacing, so we weren't too concerned about following the grainline.
After a couple of tries with the coding and an hour or so at the sewing machine, here it is - a refined, fully-lined beach bag!
We even managed to repurpose the tiny scraps left for some internal pockets.

<center>
<b>Pictures coming soon - we need to go on holidays first! ⛱️</b>
</center>
<br>
We hope you enjoy this little planner we've put together and please share with us your results!
