- [Final Goal:](#final-goal)
- [First step](#first-step)
    - [Python.h](#pythonh)
    - [PyObject *](#pyobject)
- [Errors and Exception](#errors-and-exception)
    - [Exception Object Type](#exception-object-type)
        - [Custom exception `PyErr_NewException()`](#custom-exception-pyerrnewexception)
    - [The most common one `PyErr_SetString()`](#the-most-common-one-pyerrsetstring)
    - [Another useful function is `PyErr_SetFromErrno()`](#another-useful-function-is-pyerrsetfromerrno)
    - [test whether an exception has been set with `PyErr_Occurred()`](#test-whether-an-exception-has-been-set-with-pyerroccurred)
    - [No need to declare error for nested function](#no-need-to-declare-error-for-nested-function)
    - [To ignore an exception `PyErr_Clear()`](#to-ignore-an-exception-pyerrclear)
    - [falling `malloc()` must be turned into an exception `PyErr_NoMemory()`](#falling-malloc-must-be-turned-into-an-exception-pyerrnomemory)
    - [Always clean up garbage when you return an error indicator ` Py_XDECREF()` or `Py_DECREF()`](#always-clean-up-garbage-when-you-return-an-error-indicator-pyxdecref-or-pydecref)

# Final Goal: 
```python
import spam
status = spam.system("ls -l")
```

define a module `spam` and create a `Python` interface to the `C` library function `system() `.

```C
int system(char[] s);
```

# First step
creating a file `spam.c`

## Python.h
**!** you must include `Python.h` before any standard headers are included.

```C
// spam.c
#include<Python.h>
```

`Python.h` includes a few standard header files: `<stdio.h>`, `<string.h>`, `<errno.h>`, and `<stdlib.h>`

## PyObject *
```C
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}
``` 

* The `self` argument points to the module object for module-level functions; for a method it would point to the object instance.
* The `args` argument will be a pointer to a Python tuple object containing the arguments.
* `PyArg_ParseTuple()` in the Python API checks the argument types and converts them to C values.
    * returns true (nonzero) if all arguments have the right type and its components have been stored in the variables whose addresses are passed
    
# Errors and Exception
## Exception Object Type
```C
PyExc_ZeroDivisionError
PyExc_TypeError
PyExc_IOError
PyExc_ValueError
```
### Custom exception `PyErr_NewException(),PyModule_AddObject()`
```C
PyObject* PyErr_NewException(const char *name, PyObject *base, PyObject *dict)
```
* It creates and returns a new exception class.

Creation demo:
```C
static PyObject *SpamError;

PyMODINIT_FUNC
PyInit_spam(void)
{
    PyObject *m;

    m = PyModule_Create(&spammodule);
    if (m == NULL)
        return NULL;

    SpamError = PyErr_NewException("spam.error", NULL, NULL);
    Py_INCREF(SpamError);
    PyModule_AddObject(m, "error", SpamError);
    return m;
}
``` 
Raise demo:
```C
static PyObject *
spam_system(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(SpamError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}
```
## The most common one `PyErr_SetString()`
```C
void PyErr_SetString(PyObject *type, const char *message)
```
    
* The `type` is usually a predefined object like `PyExc_ZeroDivisionError`.
* The `message` is a `C string`. It indicates the cause of the error and is converted to a Python string object and stored as the “associated value” of the exception
## Another useful function is `PyErr_SetFromErrno()`
```C
PyObject* PyErr_SetFromErrno(PyObject *type)
```
* Always return `NULL`
* Only takes an exception argument and constructs the associated value by inspection of the global variable `errno`. 

## test whether an exception has been set with `PyErr_Occurred()`
Normally no need to call this to see whether an error occurred in a function call, since you should be able to tell from the return value.


```C
PyObject* PyErr_Occurred()
```
* If set, return the exception type 
* If not set, return NULL.
* You do not own a reference to the return value, so you do not need to `Py_DECREF()` it.
* Do not compare the return value to a specific exception; use `PyErr_ExceptionMatches() `

## No need to declare error for nested function
When a function `f` that calls another function `g `detects that the latter (`g`) fails, `f` should itself return an error value (usually `NULL` or `-1`). It should not call one of the `PyErr_*() ` functions — one has already been called by `g`. 

**!** RETURN `NULL` INSTEAD
## To ignore an exception `PyErr_Clear()`
```C
void PyErr_Clear()
```
* Clear the error indicator. If the error indicator is not set, there is no effect.
* Only apply in situation where `C` wishes to handle it completely by itself (possibly by trying something else, or pretending nothing went wrong).

## falling `malloc()` must be turned into an exception `PyErr_NoMemory()`
```C
PyObject* PyErr_NoMemory()
```
* Always return `NULL`
* All the object-creating functions (for example, `PyLong_FromLong()`) already do this, so this note is only relevant to those who call `malloc() `directly.

## Always clean up garbage when you return an error indicator ` Py_XDECREF()` or `Py_DECREF()`
```C
void Py_XDECREF(PyObject *o)
void Py_DECREF(PyObject *o)
```
* Decrement the reference count for `object o`.
* The one with `X` allows  `object o` to be `NULL`, while the other does not allow.

# Return
## Return `Py_None`
If you have a `C` function that returns no useful argument (a function returning `void`), the corresponding Python function must return `None`.
```C
Py_INCREF(Py_None);
return Py_None;
```