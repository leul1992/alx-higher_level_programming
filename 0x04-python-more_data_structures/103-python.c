#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes-Prints bytes info
 * @p: Object of python
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int si, i, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	si = ((PyVarObject *)(p))->ob_si;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  si: %ld\n", si);
	printf("  trying string: %s\n", str);

	if (si >= 10)
		lim = 10;
	else
		lim = si + 1;

	printf("  first %ld bytes:", lim);

	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p:Object of python
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int si, i;
	PyListObject *li;
	PyObject *obj;

	si = ((PyVarObject *)(p))->ob_si;
	li = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] si of the Python List = %ld\n", si);
	printf("[*] Allocated = %ld\n", li->allocated);

	for (i = 0; i < si; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
