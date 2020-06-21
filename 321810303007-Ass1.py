{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid character in identifier (<ipython-input-12-324cc8e4f53c>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-12-324cc8e4f53c>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    return num1 + num2\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid character in identifier\n"
     ]
    }
   ],
   "source": [
    "# Program to design simple calculator\n",
    "def add(num1, num2): \n",
    "    return num1 + num2  \n",
    "def subtract(num1, num2): \n",
    "    return num1 - num2 \n",
    "def multiply(num1, num2): \n",
    "    return num1 * num2  \n",
    "def divide(num1, num2): \n",
    "    return num1 / num2  \n",
    "def modulus(num1, num2):\n",
    "    return num1 % num2\n",
    "def exponent(num1, num2):\n",
    "    return num1 ** num2\n",
    "def floor(num1, num2):\n",
    "    return num1 // num2\n",
    "print(\"1. add\\n2. subtract\\n3. multiply\\n4. divide\\n5. modulus\\n6. exponent\\n7. floor division\")\n",
    "s = int(input(\"Select an operation\")) \n",
    "n1 = float(input(\"Enter first number: \"))\n",
    "n2 = float(input(\"Enter second number: \")) \n",
    "if select == 1:\n",
    "    print(n1, \"+\", n2, \"=\", add(n1, n2))  \n",
    "elif select == 2: \n",
    "    print(n1, \"-\", n2, \"=\", subtract(n1, n2))  \n",
    "elif select == 3: \n",
    "    print(n1, \"*\", n2, \"=\", multiply(n1, n2)) \n",
    "elif select == 4: \n",
    "    print(n1, \"/\", n2, \"=\", divide(n1, n2)) \n",
    "elif select == 5: \n",
    "    print(n1, \"%\", n2, \"=\", modulus(n1, n2)) \n",
    "elif select == 6: \n",
    "    print(n1, \"**\", n2, \"=\", exponent(n1, n2)) \n",
    "elif select == 7: \n",
    "    print(n1, \"//\", n2, \"=\", floor(n1, n2)) \n",
    "else: \n",
    "    print(\"Enter a valid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter principle: 500\n",
      "Enter time in months24\n",
      "Enter rate of interest2\n",
      "Simple interest for above details is 240.0\n"
     ]
    }
   ],
   "source": [
    "# program to calculate simple interest\n",
    "p=int(input('Enter principle: '))\n",
    "t=int(input('Enter time in months'))\n",
    "r=int(input('Enter rate of interest'))\n",
    "si=(p*t*r)/100\n",
    "print(\"Simple interest for above details is\",si)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius of circle5\n",
      "Area of circle is 78.58000000000001\n"
     ]
    }
   ],
   "source": [
    "# program to create area of circle\n",
    "pi=3.1432\n",
    "r=float(input('Enter radius of circle'))\n",
    "a=pi*r*r\n",
    "print(\"Area of circle is\", a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter base of the triangle6\n",
      "Enter height of the triangle12\n",
      "Area of triangle is 36.0\n"
     ]
    }
   ],
   "source": [
    "# program to create area of triangle\n",
    "b=float(input('Enter base of the triangle'))\n",
    "h=float(input('Enter height of the triangle'))\n",
    "a=0.5*b*h\n",
    "print(\"Area of triangle is\", a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter temp in celsius0\n",
      "temp in fahrenheit is 32.0\n"
     ]
    }
   ],
   "source": [
    "# program to convert temp in celsius to fahrenheit\n",
    "c=float(input('Enter temp in celsius'))\n",
    "f=((9*c)/5)+32\n",
    "print(\"temp in fahrenheit is\", f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter length of the triangle4\n",
      "Enter base of the triangle5.5\n",
      "Area of triangle is 22.0\n"
     ]
    }
   ],
   "source": [
    "# program to create area of rectangle\n",
    "l=float(input('Enter length of the triangle'))\n",
    "b=float(input('Enter base of the triangle'))\n",
    "a=l*b\n",
    "print(\"Area of triangle is\", a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter side of square4.5\n",
      "Perimeter of square is 18.0\n"
     ]
    }
   ],
   "source": [
    "# program to create perimeter of square\n",
    "s=float(input('Enter side of square'))\n",
    "p=4*s\n",
    "print(\"Perimeter of square is\", p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius of circle2.5\n",
      "circumference of circle is 15.716000000000001\n"
     ]
    }
   ],
   "source": [
    "# program to create circumference of circle\n",
    "pi=3.1432\n",
    "r=float(input('Enter radius of circle'))\n",
    "c=2*pi*r\n",
    "print(\"circumference of circle is\", c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 1st number: 3.5\n",
      "Enter 2nd number: 54\n",
      "After swapping\n",
      "\n",
      "a= 54.0\n",
      "b= 3.5\n"
     ]
    }
   ],
   "source": [
    "# program to swap two numbers\n",
    "t=0\n",
    "a=float(input('Enter 1st number: '))\n",
    "b=float(input('Enter 2nd number: '))\n",
    "t=a\n",
    "a=b\n",
    "b=t\n",
    "print(\"After swapping\\n\")\n",
    "print(\"a=\", a)\n",
    "print(\"b=\", b)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
