choldate
========

Somewhat fast updating and downdating of Cholesky factors in Python

## Installation

### From GitHub
```sh
pip install git+https://github.com/jcrudy/choldate.git
```

### From source
```sh
git clone https://github.com/jcrudy/choldate.git
cd choldate
pip install .
```

For an editable (development) install:
```sh
pip install -e .
```

To install with Cython (required only if you need to rebuild the C extension from the `.pyx` source):
```sh
pip install -e .[build]
```

**Requirements:** Python >= 3.8, NumPy. Cython is optional (used automatically when available and when `_choldate.pyx` is present).

## usage

```python
from choldate import cholupdate, choldowndate
import numpy

#Create a random positive definite matrix, V
numpy.random.seed(1)
X = numpy.random.normal(size=(100,10))
V = numpy.dot(X.transpose(),X)

#Calculate the upper Cholesky factor, R
R = numpy.linalg.cholesky(V).transpose()

#Create a random update vector, u
u = numpy.random.normal(size=R.shape[0])

#Calculate the updated positive definite matrix, V1, and its Cholesky factor, R1
V1 = V + numpy.outer(u,u)
R1 = numpy.linalg.cholesky(V1).transpose()

#The following is equivalent to the above
R1_ = R.copy()
cholupdate(R1_,u.copy())
assert(numpy.all((R1 - R1_)**2 < 1e-16))

#And downdating is the inverse of updating
R_ = R1.copy()
choldowndate(R_,u.copy())
assert(numpy.all((R - R_)**2 < 1e-16))  
``` 
