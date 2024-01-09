#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
* print_python_list_info - function that prints some basic info about Python lists
* @p: python lists
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
int i;
PyListObject *listobj = (PyListObject *)p;
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", listobj->allocated);
for (i = 0; i < size; i++)
printf("Element %i: %s\n", i, Py_TYPE(listobj->ob_item[i])->tp_name);
}
