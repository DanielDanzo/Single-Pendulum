# Single-Pendulum Project

This is a project inspired by the Computer Science second year module, Mechanics. One of the concepts done in this module is that of the single Pendulum. Single Pendulum is the most taught concept in this Mechanics course. Being able to visualise the concepts learnt is the main idea of this project. The thought of bringing what is in your mind to life. A stepping stone to truly understanding the concepts taught.

## Program

The program simulates a single pendulum suspendend from a point in space with a massless and tensionless rod. The pendulum system does not comply with newtonian physics as it swings infinitely, but it can still follow newtonian physics(Can be done by done by uncommenting line65 of the program). The program takes as input the desired length of your rod(ideally less than 800 as this is the total height of the screen) and the mass of the bob. The program uses the given radius to draw the rod and unfortunately the program does not use the mass for any calculations but would be ideal to use the mass in the future.

## Running the program

As stated before, the program takes as input the length of the rod. An example of how to run the program is shown below

```bash
python pendulum.py {radius} {mass}
```

### Example

```bash
python pendulum.py 300 30
```

The above example simulates a pendulum having a rod with length 300 and a bob with mass 30.

