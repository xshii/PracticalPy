# PracticalPy
Some practical python technique

## include
* add command line ```argument_.py``` support. 
    ```bash
    $ python argument.py 1 2 3 --sum
    ```
* log message and write to file ```logger_.py```
    ```bash
    $ python logger_.py
    # alternatively
    $ python logger_.py --info
    ```
    
 * C extension support via ```CPython```
    ```bash
    (cExtension)$ python setup.py build_ext --inplace
    ```
    ```python
    from cExtension.demo import add
    add(1,2)   // 3
    ```

* Intel mkl support for python ```mkl```