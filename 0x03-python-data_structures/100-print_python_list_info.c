#include <Python.h>
#include <stdio.h>
/**
* print_python_list_info - function name
* @p: argument
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t numof_elem, allo_sz;
	Py_ssize_t i;
	PyObject *kbm;

	numof_elem = PyList_Size(p);
	allo_sz = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", numof_elem);
	printf("[*] Allocated = %zd\n", allo_sz);

	for (i = 0; i < numof_elem; i++)
	{
		kbm = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(kbm)->tp_name);
	}
}
