/**
* print_python_list_info - function name
* @p: argument
* Return: nothing
*/
void print_python_list_info(PyObject *p )
{
	int numof_elem = Py_SIZE(p);
	int allo_sz = ((PyListObject*)p)->allocated;
	int i;
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", numof_elem);
	printf("[*] allocated = %d\n", allo_sz);

	for (i = 0, i < numof_elem, i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
