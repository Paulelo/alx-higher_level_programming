#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p) {
    // Make sure the input is a list object
    if (!PyList_Check(p)) {
        printf("Input is not a list object\n");
        return;
    }

    // Get the length of the list
    int len = PyList_Size(p);
    printf("Length of list: %d\n", len);

    // Print the elements of the list
    printf("Elements of the list:\n");
    for (int i = 0; i < len; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("%d: %s\n", i, PyUnicode_AsUTF8(item));
    }
}
