# Week 2 - Tutorial 2: Admission Policy

## 1. Identify the Components
### 1.1. What are the inputs?
- age (Integer)
- is_accompanied (Boolean)
- has_ticket (Boolean)

### 1.2. What is the process?
- Logical Expression: (age >= 13 OR is_accompanied) AND has_ticket

### 1.3. What is the output?
- Access Status ("Allowed to enter" / "Not allowed to enter")

## 2. Truth Table
| Age >= 13? | Accompanied by Adult? | Has Valid Ticket? | Allowed to Enter? |
| :--- | :--- | :--- | :--- |
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | True |
| True | False | False | False |
| True | False | True | True |
| True | True | False | False |
| True | True | True | True |

## 3. Pseudocode
```text
BEGIN
    INPUT age
    INPUT is_accompanied
    INPUT has_ticket

    IF (age >= 13 OR is_accompanied == True) AND has_ticket == True THEN
        OUTPUT "Allowed to enter"
    ELSE
        OUTPUT "Not allowed to enter"
    ENDIF
END