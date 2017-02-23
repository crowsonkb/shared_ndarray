import setuptools

setuptools.setup(
    name='shared-ndarray',
    version='1.1.1',
    description='A pickleable wrapper for sharing NumPy ndarrays between processes using POSIX shared memory.',
    long_description=open('README.rst').read(),
    url='https://github.com/crowsonkb/shared_ndarray',
    author='Katherine Crowson',
    author_email='crowsonkb@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
    keywords='numpy ndarray array shared memory shm',
    packages=['shared_ndarray'],
    install_requires=['numpy >= 1.11.3', 'posix_ipc >= 1.0.0'],
)
