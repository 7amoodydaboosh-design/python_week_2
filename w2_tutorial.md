# WEEK 2 - TUTORIAL 2

## Movie Theater Admission System

### Scenario

A movie theater has the following admission policy:

* Users are **13 years old or older**, OR
* Users are **accompanied by an adult**
* Users **must have a valid ticket**

The admission rule can be represented as:

```text
(Age >= 13 OR Accompanied by Adult) AND Valid Ticket
```

---

## 1. Identify the Components

### 1.1 Inputs

* Age
* Accompanied by Adult (True/False)
* Valid Ticket (True/False)

### 1.2 Process

Check whether:

```text
(Age >= 13 OR Accompanied by Adult) AND Valid Ticket
```

### 1.3 Output

* Allowed to Enter
* Not Allowed to Enter

---

## 2. Design the Algorithm

### 2.1 Logic Diagram

```text
             +----------------+
             |     Start      |
             +----------------+
                     |
                     v
          Enter Age, Adult,
           and Ticket Info
                     |
                     v
      +-----------------------------+
      | (Age >= 13 OR Adult = Yes) |
      | AND Ticket = Yes ?         |
      +-----------------------------+
             /              \
           Yes              No
            |                |
            v                v
 +----------------+   +-------------------+
 | Allowed Enter  |   | Not Allowed Enter |
 +----------------+   +-------------------+
            |                |
            +-------+--------+
                    |
                    v
               +---------+
               |   End   |
               +---------+
```

---

### 2.2 Truth Table

| Age >= 13 | Adult | Ticket | Result |
| --------- | ----- | ------ | ------ |
| F         | F     | F      | F      |
| F         | F     | T      | F      |
| F         | T     | F      | F      |
| F         | T     | T      | T      |
| T         | F     | F      | F      |
| T         | F     | T      | T      |
| T         | T     | F      | F      |
| T         | T     | T      | T      |

---

### 2.3 Algorithm (Step-by-Step)

1. Start
2. Input age
3. Input adult status
4. Input ticket status
5. Check if:

   * Age is 13 or above OR accompanied by an adult
   * AND has a valid ticket
6. If true, display **"Allowed to Enter"**
7. Otherwise, display **"Not Allowed to Enter"**
8. End

---

### 2.4 Pseudocode

```text
START

INPUT age
INPUT adult
INPUT ticket

IF ((age >= 13 OR adult = TRUE) AND ticket = TRUE)
    PRINT "Allowed to Enter"
ELSE
    PRINT "Not Allowed to Enter"
END IF

END
```

---

## 3. Python Program

```python
# Movie Theater Admission System

def yes_no_prompt(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please answer Yes or No.")

while True:
    age_input = input("Enter age: ").strip()
    if age_input.isdigit():
        age = int(age_input)
        break
    print("Please enter a valid whole number for age.")

adult = yes_no_prompt("Accompanied by an adult? (Yes/No): ")
ticket = yes_no_prompt("Has a valid ticket? (Yes/No): ")

if (age >= 13 or adult) and ticket:
    print("Allowed to Enter")
else:
    print("Not Allowed to Enter")
```

---

## 4. Test Cases

| Age | Adult | Ticket | Result               |
| --- | ----- | ------ | -------------------- |
| 15  | No    | Yes    | Allowed to Enter     |
| 10  | Yes   | Yes    | Allowed to Enter     |
| 10  | No    | Yes    | Not Allowed to Enter |
| 15  | No    | No     | Not Allowed to Enter |

---

## 5. Output Examples

### Example 1

**Input**

```text
Age = 15
Adult = No
Ticket = Yes
```

**Output**

```text
Allowed to Enter
```

### Example 2

**Input**

```text
Age = 10
Adult = No
Ticket = Yes
```

**Output**

```text
Not Allowed to Enter



