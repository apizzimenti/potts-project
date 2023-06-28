
import pandas as pd
import numpy as np
import json
from potts import Lattice, SwendsonWang, Chain
from potts.stats import randomizedToConstant
from potts.utils import Metadata

# Set the order of our coefficient field and the size of the lattice.
q = 27
corners = [20, 20, 20]
steps = 1000

# Create an integer lattice to experiment on.
lattice = Lattice(corners=corners, field=q)
schedule = randomizedToConstant(steps=steps, field=q, distribution=np.random.normal)
model = SwendsonWang(temperature=schedule)
initial = model.initial(lattice)

# Create a chain and iterate, stashing information as we go.
chain = Chain(lattice, model, initial=initial, sampleInterval=50, steps=steps)

# Step through the chain.
with Metadata(chain) as metadata:
    for step in chain.progress(): pass

# Write statistics to file.
# Write statistics to file.
pd.DataFrame.from_dict(chain.statistics).to_csv("./output/statistics/energy.csv")
with open("./output/statistics/assignments.json", "w") as w: json.dump(chain.assignments, w)