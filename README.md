# Matrix

Project to learn Linear Algebra with Matrix and Vectors.

## History

The complex_list folder contains the 1st version of the project, which was quickly abandoned because it wasn't generic.

Instead, there are 2 folders after a misunderstanding about the second bonus:
 - The complex_builtin folder, which contains the Vector and Matrix classes using the complex type available in vanilla Python3.10.
 - The complex_created folder, which contains the same classes, but using a Complex class.

For each exercise, the 4 classes are imported with the following names B_[Class] for the built-in complex type and C_[Class] for the complex type created by my Complex class.

## Structure

File `creation.py` shows how to create Vectors and Matrix and all exceptions at creation of objects.
Furthermore, there is one file per exercise, from `ex00.py` to `ex<n>.py`.

Only complex_created classes will be used for exercises, complex_builtin will be used for checking.
In final version, complex_builtin is removed for import issues.

Time and space complexity are calculated with [Big(O) Calculator](https://big-o-calculator.vercel.app/).