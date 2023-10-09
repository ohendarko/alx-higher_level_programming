#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
* print_python_list_info - function name
* @p: argument
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t numof_elem = PyList_Size(p);
	Py_ssize_t allo_sz = ((PyListObject *)p)->allocated;
	Py_ssize_t i;
	PyObject *kbm;

	printf("[*] Size of the Python List = %ld\n", numof_elem);
	printf("[*] Allocated = %ld\n", allo_sz);

	for (i = 0; i < numof_elem; i++)
	{
		printf("Element %ld: ", i);

		kbm = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(kbm)->tp_name);
	}
}
