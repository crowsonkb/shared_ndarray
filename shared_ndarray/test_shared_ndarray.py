import multiprocessing as mp
import unittest

import numpy as np

from . import SharedNDArray, SharedNDArrayError


class TestSharedNDArray(unittest.TestCase):
    def test_create(self):
        try:
            shm = SharedNDArray(4)
            shm.array[0] = 1

            def write_to_shm(q):
                shm = q.get()
                shm.array += 1

            q = mp.Queue()
            p = mp.Process(target=write_to_shm, args=(q,))
            p.start()
            q.put(shm)
            p.join()

            self.assertEqual(shm.array[0], 2)
        finally:
            shm.unlink()

    def test_unlink_twice(self):
        shm = SharedNDArray(4)
        shm.unlink()
        with self.assertRaises(SharedNDArrayError):
            shm.unlink()

    def test_unlink_two_processes(self):
        shm = SharedNDArray(4)
        q = mp.Queue()
        p = mp.Process(target=lambda q: q.get().unlink(), args=(q,))
        p.start()
        q.put(shm)
        p.join()
        with self.assertRaises(SharedNDArrayError):
            shm.unlink()

    def test_copy(self):
        try:
            arr = np.array(range(4))
            shm = SharedNDArray.copy(arr)
            self.assertEqual(arr.shape, shm.array.shape)
            self.assertEqual(arr.dtype, shm.array.dtype)
            self.assertTrue((arr == shm.array).all())
        finally:
            shm.unlink()

    def test_zeros_like(self):
        try:
            arr = np.array(range(4))
            shm = SharedNDArray.zeros_like(arr)
            self.assertEqual(arr.shape, shm.array.shape)
            self.assertEqual(arr.dtype, shm.array.dtype)
            self.assertTrue((shm.array == 0).all())
        finally:
            shm.unlink()


if __name__ == '__main__':
    unittest.main()
