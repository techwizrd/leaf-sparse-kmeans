Top-k Sparsification
===

This experiment tests top-k sparsification to reduce the size of model updates between rounds of federated averaging by 10%, i.e., the compressed model update should be 90% the size of the uncompressed model update.

Top-k Sparsification
---

Top-k sparsification retains only the k items of an array with the largest magnitude. All other values are sparsified, i.e., replaced with zero. To see this illustrated, please look at the example below.


The top-k compressor retains the five entries with the largest magnitude.
```py
>>> import numpy as np
>>> from compressors import TopKCompressor
>>> x = np.random.randint(-100, 100, 10)
>>> x
array([-65, -99,  53,  95, -43, -55, -41, -71, -55, -61])
>>> Cx = TopKCompressor.compress(x, 5)
>>> Cx
array([-65, -99,   0,  95,   0,   0,   0, -71,   0, -61])
>>> TopKCompressor.getsizeof(x)
160
>>> TopKCompressor.getsizeof(Cx)
80
```

Before compression, `x` is 160 bytes. After applying the top-k compressor with `k=5`, the compressed vector `Cx` is 80 bytes.

Running this Experiment
---

In order to run this experiment,

1. Copy the `baseline_constants.py`, `compressors.py`, and `client.py` into the `models/` directory.
2. Change into the `models/` directory using `cd`.
3. Run the following command:

```sh
unbuffer time python main.py -dataset femnist -model cnn -lr 0.002 | tee metrics/accuracy.out
```

4. Copy the results (`metrics/{*.out,*.csv}`) here for further analysis.

NOTE: You may need to modify the `layers_to_compress` and `space_savings` to correspond with different datasets, networks, and sparsification factors.

