"""
// Variables

let someVar = "some value.";
const someConstant = "This value can not change after it has been assigned!";
"""
some_var: str = "some value."
some_const = "some other value, but Python doesn't *really* have consts."

"""
// Numbers

let someNumber = 10;
let someInt = 10; // Integers are whole numbers, e.g. 1,2,3,4...
let someFloat = 10.0; // Floats are floating point numbers, e.g. 0.12345

// Sometimes floats are weird: https://0.30000000000000004.com
// console.log(0.1 + 0.2);
"""

some_float: float = 3.1415
some_int: int = 100
# You will probably never use imaginary numbers.
some_img_num = 1 + 1j

"""
// Strings

let someString = "This is a string.";
let someOtherString = "They can use either type of quotes.";
let someStrLiteral = `These strings are fancy!
They can break returns in them, and you can have both
types of normal quotes in them ("",'')
They also support interpolation: ${Math.PI * 2}`;

// Interpolation:
// console.log(someStrLiteral);

// Concatenation:
// console.log("Hello" + " world!");
"""
some_str: str = "Strings are text."
some_str = 'Either type of quotes are okay.'
some_str_literal: str = """
This can have multiple lines without escaping characters!

See?!
"""
some_fmt_str: str = f"The stuff between the curly braces gets interpolated: {
    some_img_num}"


"""
// Booleans

let someBool = true;
let someOtherBool = false;

// Most of the time, you'll make bools with expressions:
// console.log((0.1 + 0.2) !== 0.3);

// A nearly comprehensive list of falsy values:
// console.log("null:", !!null);
// console.log("undefined:", !!undefined);
// console.log("false:", !!false);
// console.log("NaN:", !!NaN);
// console.log("0:", !!0);
// console.log("-0:", !!-0);
// console.log("0n:", !!0n);
// console.log('"":', !!null);
// https://developer.mozilla.org/en-US/docs/Glossary/Falsy
"""
some_bool: bool = True
some_bool = False

some_exp: bool = 0.1 + 0.2 == 0.3

# print(0.1 + 0.2, some_exp)

"""
// Nullish values:
let someNull = null;
let someUndefined;

// console.log(someNull);
// console.log(someUndefined);
"""
some_null: None = None

"""
// Arrays:
let someArr = [2, 3, 5, 7, 13, 17, 23];

// Accessing individual values in an array:
// console.log(someArr[0]);
// console.log(someArr[1]);
"""
some_list: list[int] = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20
]
# print(some_list[10])

some_tuple: tuple[str] = (
    "Tuples are like lists",
    "Except that they are immutable."
)
# tuples must have at least 1 comma, or else they are
# just sparling code grouping.

"""
// Objects:

let someObj = {
key: "value",
attribute: "some other value",
property: "some random value",
};

let someBook = {
title: "Guards! Guards!",
author: "Terry Pratchett",
isbn_13: "978-0-06-222-575-7",
published: 1989,
};

let someChessMove = {
turn: 0,
move: "e7-e6",
};
"""
some_dict: dict[str, str] = {
    # Your keys can be any *hashable* data type.
    # But you'll mostly be using strings.
    "key": "value",
    "something": "some other thing."
}

some_dict["cats"] = "are cool, even when they try to walk on your keyboard."

# print(some_dict["cats"])

"""
// Arrays of objects:

let bookshelf = [
{
    title: "Guards! Guards!",
    author: "Terry Pratchett",
    isbn_13: "978-006222575-7",
    published: 1989,
},
{
    title: "Snow Crash",
    author: "Neal Stephenson",
    isbn_13: "978-061336162-0",
    published: 1992,
},
];
"""
bookshelf = [
    {
        "title": "Guards! Guards!",
        "author": "Terry Pratchett",
        "isbn_13": "978-006222575-7",
        "published": 1989,
    },
    {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "isbn_13": "978-061336162-0",
        "published": 1992,
    },
]

"""
// Iteration!

for (let book of bookshelf) {
    console.log(
        `${book.title} -- ${book.author}, published: ${book.published}`
    );
}
"""
# for book in bookshelf:
#     print(book)
# print("Iteration done!")

total = 0
for i in range(101):
    total += i
print(total)

"""
// // Operators:
// console.log("Equality:", 1 == "1");
// console.log("Strict equality:", 1 === "1"); // Use this most of the time!
// console.log("Inequality:", 1 != "1");
// console.log("Strict inequality:", 1 !== "1");
// console.log("Less than:", 1 < 5);
// console.log("Less than or equal:", 5 <= 5);
// console.log("Greater than:", 1 > 5);
// console.log("Greater than or equal:", 5 >= 5);

// console.log("Plus:", 1 + 2);
// console.log("Minus:", 1 - 2);
// console.log("Mul:", 1 * 2);
// console.log("Div:", 1 / 2);

// // Logical operations:
// console.log("Not:", !true);
// console.log("And:", true && !false);
// console.log("Or:", false || true);
"""
# print("Equality:", 1 == "1")
# print("Inequality:", 1 != "1")
# print("Less than:", 1 < 5)
# print("Less than or equal:", 5 <= 5)
# print("Greater than:", 1 > 5)
# print("Greater than or equal:", 5 >= 5)

# a = {"a": "b"}
# b = {"a": "b"}
# print("Identity:", a is b)
# print("Identity:", a is not b)
# print("Equality:", a == b)
# print(a is not None)

# print("Plus:", 1 + 2)
# print("Minus:", 1 - 2)
# print("Mul:", 1 * 2)
# print("Exp:", 2 ** 2)
# print("Div:", 1 / 2)
# print("Floor Div:", 1 // 2)
# print("Modulo:", 1 % 2)

"""
// // If statements:
let tempF = -40;

// if (tempF === -40) {
//   console.log("It's -40 in both C and F.");
// } else if (tempF <= 0) {
//   console.log("Yeah, it's getting cold.");
// } else if (tempF <= 32) {
//   console.log("Water freezes now, and it's 0C.");
// } else {
//   console.log("It's kinda warm.");
// }
"""
# temp_f = -40

# if temp_f == -40:
#     print("It's -40 in both C and F.")
# elif temp_f <= 0:
#     print("Yeah, it's getting cold.")
# elif temp_f <= 32:
#     print("Water freezes now, and it's 0C.")
# else:
#     print("It's kinda warm.")

"""
// console.log("Now this code executes!");

// // Switch statements:
// switch (tempF) {
//   case -40:
//     console.log("It is -40 in both C and F");
//   case 32:
//     console.log("Water is solid now, which is kinda a bummer.");
//     break;
//   case 65:
//     console.log("It's a nice temperature.");
//     break;
//   default:
//     console.log("This is the default case.");
//     break;
// }

// Looping:
let fib = [1, 1, 2, 3, 5, 8, 13];

// for (let val of fib) {
//   console.log(val);
// }

let someBook = {
    title: "Guards! Guards!",
    author: "Terry Pratchett",
    isbn_13: "978-0-06-222-575-7",
    published: 1989,
};

// for (let key in someBook) {
//   console.log(key, someBook[key]);
// }

let sum = 0;

// for (let i = 0; i < 100; i++) {
//   sum += i;
// }

// console.log(sum);

// sum = 1;

// while (sum > 1024) {
//   sum += sum;
// }

// console.log(sum);

// Functions:

// const someFunc = (a, b) => {
//   console.log(a, b);
//   return a + b;
// };

// sum = someFunc(5, 10);
// console.log(sum);

// function fibonacci(n) {
//   if (n <= 1) {
//     return 1;
//   }

//   let numbers = [1n, 1n];
//   for (let i = n; i > 1; i--) {
//     numbers.unshift(numbers[0] + numbers[1]);
//   }
//   return numbers[0];
// }

// for (let i = 0; i < 100; i++) {
//   console.log(i, fibonacci(i));
// }
"""
def summation(n: int) -> int:
    """
    Returns the sum of all integers from 0
    to n, inclusive.
    """
    return (n * (n+1)) // 2

print(summation(100))

"""
// Try/catch:

/**
* Try/catch blocks hide useful info about errors from you!
*/

try {
    1n / 0n;
} catch {
    console.log("oops!");
}
"""

if __name__ == "__main__":
    pass
