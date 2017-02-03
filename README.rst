shared\_ndarray
===============

A pickleable wrapper for sharing NumPy ndarrays between processes using POSIX
shared memory.

SharedNDArrays are designed to be sent over multiprocessing.Pipe and Queue
without serializing or transmitting the underlying ndarray or buffer. While the
associated file descriptor is closed when the SharedNDArray is garbage
collected, the underlying buffer is not released when the process ends: you
must manually call the ``unlink()`` method from the last process to use it.

Usage
-----

.. code:: python

    from __future__ import print_function

    import multiprocessing as mp

    import numpy as np
    from shared_ndarray import SharedNDArray

    try:
        shm = SharedNDArray((4, 4))
        shm.array[0, 0] = 1
        p = mp.Process(target=lambda shm: print(shm.array), args=(shm,))
        p.start()
        p.join()
    finally:
        shm.unlink()

This should print::

    [[ 1.  0.  0.  0.]
     [ 0.  0.  0.  0.]
     [ 0.  0.  0.  0.]
     [ 0.  0.  0.  0.]]

There are also convenience methods to create a new SharedNDArray from an
existing NumPy array:

.. code:: python

    arr = np.array([0, 0])
    shm1 = SharedNDArray.copy(arr)
    shm2 = SharedNDArray.zeros_like(arr)
    shm1.unlink()
    shm2.unlink()

Dependencies
------------

- `numpy <http://www.numpy.org>`_
- `posix_ipc <http://semanchuk.com/philip/posix_ipc/>`_
