# Quiz 1

Quizzes are optional, but encouraged. They are a good way to test your conceptual understanding, before diving into the programming projects. Consider each question below, then reveal the answer. If you didn't get it right, consider why you may have had that misunderstanding!

## Question 1

Consider these logical sentences:

1. If Hermione is in the library, then Harry is in the library.
2. Hermione is in the library.
3. Ron is in the library and Ron is not in the library.
4. Harry is in the library.
5. Harry is not in the library or Hermione is in the library.
6. Ron is in the library or Hermione is in the library.

**Which of the following logical entailments is true?**

- Sentence 6 entails Sentence 2
- Sentence 1 entails Sentence 4
- Sentence 6 entails Sentence 3
- Sentence 2 entails Sentence 5 -> true
- Sentence 1 entails Sentence 2
- Sentence 5 entails Sentence 6

---

### **Resolution**

**Symbols:**
- `Harry` = "Harry is in the library"
- `Hermione` = "Hermione is in the library"  
- `Ron` = "Ron is in the library"

**Analysis:**
1. **Ron or Hermione entails Hermione** → `false`
2. **Hermione then Harry entails Harry** → `false`
3. **Ron or Hermione entails Ron and not Ron** → `false`
4. **Hermione entails not Harry or Hermione** → `true`
5. **Hermione then Harry entails Hermione** → `false`
6. **Not Harry or Hermione entails Ron or Hermione** → `false`

**Answer:** Sentence 2 entails Sentence 5


## Question 2

There are other logical connectives that exist, other than the ones discussed in lecture. One of the most common is "Exclusive Or" (represented using the symbol ⊕). The expression A ⊕ B represents the sentence "A or B, but not both." 

**Which of the following is logically equivalent to A ⊕ B?**

1. (A ∨ B) ∧ ¬ (A ∧ B)
2. (A ∧ B) ∨ ¬ (A ∨ B)
3. (A ∨ B) ∧ (A ∧ B)
4. (A ∨ B) ∧ ¬ (A ∨ B)

### **Resolution**

- ∨ -> OR
- ∧ -> AND
- ¬ -> NOT

1. (A ∨ B) ∧ ¬ (A ∧ B) = (A OR B) AND NOT (A AND B) == A OR B, but not both.




## Question 3

Let propositional variable R be that "It is raining," the variable C be that "It is cloudy," and the variable S be that "It is sunny." 

**Which of the following a propositional logic representation of the sentence "If it is raining, then it is cloudy and not sunny."?**

1. (R → C) ∧ ¬S
2. R → C → ¬S
3. R ∧ C ∧ ¬S
4. R → (C ∧ ¬S)
5. (C ∨ ¬S) → R

### **Resolution**

- R = "It is raining"
- C = "It is cloudy"
- S = "It is sunny"

4. R → (C ∧ ¬S) = R implies (C AND NOT S)


## Question 4

Consider, in first-order logic, the following predicate symbols. Student(x) represents the predicate that "x is a student." Course(x) represents the predicate that "x is a course." Enrolled(x, y) represents the predicate that "x is enrolled in y." 

**Which of the following is a first-order logic translation of the sentence "There is a course that Harry and Hermione are both enrolled in."?**

1. ∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)
2. ∀x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)
3. ∃x. Enrolled(Harry, x) ∧ ∃y. Enrolled(Hermione, y)
4. ∀x. Enrolled(Harry, x) ∧ ∀y. Enrolled(Hermione, y)
5. ∃x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)
6. ∀x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)

### **Resolution**

- Student(x)      = x is a student.
- Course(x)       = x is a course.
- Enrolled(x,y)   = x is enrolled in y.

1. ∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)

