
# SI 506: Problem Set 01

## This week's Problem Set

This week's problem set includes four problems that focus on variable assignments, using built-in functions, and basic string operations.

:bulb: In order to check your work, try using the built-in function `print()` to print out the results.

## Background

This week's problem set is based around restaurants in Ann Arbor. Ann Arbor is home to a diverse range of tantalizing restaurants and eateries, and this problem set features some of Central Campus's popular spots.

## 1.0 Problem 01 (10 Points)

1. You have been provided with ten lines of code that attempt to assign a restaurant's name to a variable. Only three of these lines contain valid variable assignments. Comment out the statements that contain invalid variable assignments.

2. Create a new variable called `cottage_inn` and assign to it a string representation of the restaurant **Cottage Inn Pizza**.

    :warning: Make sure that you treat the restaurant name as a title (i.e., capitalize the first letter of every word).

3. Similarly, create a new variable called `madras_masala` and assign to it a string representation of the restaurant **Madras Masala**.

    :warning: Make sure that you treat the restaurant name as a title (i.e., capitalize the first letter of every word).

## 2.0 Problem 02 (30 Points)

1. Call the appropriate `str` method to return a version of the string assigned to `hopcat` that converts all its characters to _upper_ case. Assign the return value to a new variable named `hopcat_all_upper`.

2. Call the appropriate `str` method to return a version of of the string assigned to `jerk_pit` that converts all its characters to _lower_ case. Assign the return value to a new variable named `jerk_pit_all_lower`.

3. Call the appropriate `str` method that can sum the number of times the letter 'a' appears in the string assigned to `madras_masala`. Assign the return value to a new variable named `madras_masala_count_a`.

4. Call the appropriate `str` method that can be used to check whether the string assigned to `cottage_inn` ends with **"Pizza"**. Assign the return value to a new variable named `has_pizza`.

5. Call the appropriate `str` method to check whether the string assigned to `madras_masala` starts with **"madras"**. Assign the return value to a new variable named `has_madras`.

6. Call the appropriate `str` method that can return a version of the string `comment` that substitutes the substring **"and"** for the character **"&"**. Assign the return value to a new variable named `updated_comment`.

## 3.0 Problem 03 (30 Points)

1. Count the total number of characters in the string assigned to the variable `updated_comment` and assign it to a new variable called `num_chars`.

    :bulb: You should utilize a built-in function to help you determine the length of the string.

2. Mr.Foodie would like to visit each of the popular restaurants in Ann Arbor. He collected the restaurant names and stored them in the `restaurants` list. Please use a built-in function inside the `print()` function to print out the data type of the object assigned to the variable `restaurants`.

3. Please also help Mr.Foodie count how many restaurants are listed in the `restaurants`. Assign the return value to a new variable called `num_restaurants`.

    :bulb: You should utilize a built-in function to help you count.

4. Mr.Foodie would like to invite three of his friends to the restaurant Frita Batidos. Before he visits the restaurant, he checks the menu online. Below is a table that shows the popular dishes it offers:

    | Food & Drinks| Price       |
    | -----------  | ----------- |
    | Beef Frita   | $10         |
    | Chicken Frita| $10         |
    | Fish Frita   | $10         |
    | Passion Fruit Batido | $5.5|
    | Fresh Lime Batido    | $5.5|
    | Tropical Salad| $12  |

    What would be the total price if Mr.Foodie orders a Beef Frita, a Chicken Frita, a Passion Fruit Batido, and a Tropical Salad for his friends and himself? (Do not consider taxes and tips for this problem) Assign the return value to a variable called `total_price`.

5. Given that the state sales tax rate for Michigan is 6%, and the diners are willing to pay 20% tips of the total price, before taxes, for servers, what should be the total amount they need to pay for this meal? Assign the return value to a variable called `total_bill`.

    :exclamation: Please use the variable `total_price` to calculate the total amount they need to pay.

6. Mr.Foodie and his three friends decide to split the entire bill evenly. What would be the amount that each person pays? Assign the return value to a variable called `each_pay`.

    :exclamation: Please use the variable `total_bill` to calculate the amount each person must pay and keep all digits after the decimal.

## 4.0 Problem 04 (5 Points)

1. Utilize an f-string and the variables `updated_comment` and `jerk_pit` to print out the following sentence:

```markdown
Someone said 'Truly authentic Jamaican food and drinks' on Yelp for the restaurant Jamaican Jerk Pit.
```

:exclamation: The comment **Truly authentic Jamaican food and drinks** in the sentence must be surrounded by single quotes.