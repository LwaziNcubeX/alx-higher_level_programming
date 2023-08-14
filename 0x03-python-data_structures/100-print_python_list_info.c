#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints info
 * @p: pointet to the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);
		if (PyUnicode_Check(item))
			printf("str\n");
		else if (PyLong_Check(item))
			printf("int\n");
		else if (PyFloat_Check(item))
			printf("float\n");
		else if (PyBytes_Check(item))
			printf("bytes\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PySet_Check(item))
			printf("set\n");
		else if (PyAnySet_Check(item))
			printf("%s\n", item->ob_type->tp_name);
	}
}
