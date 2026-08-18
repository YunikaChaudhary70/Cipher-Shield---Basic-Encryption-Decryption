Project 2: CIPHER-SHIELD - Test Cases

Test Case 1: Basic Encryption
**Input:**
Enter Choice: 1
Enter Plaintext: HELLO
Enter Shift Key 1-25: 3
**Output:**
```[ENCRYPTED]: KHOOR
[VALIDATION]: HELLO```
**Result:** PASS ✅

---

Test Case 2: Decryption Validation
**Input:**
Enter Choice: 2
Enter Ciphertext: KHOOR
Enter Shift Key 1-25: 3
**Output:**
```[DECRYPTED]: HELLO```
**Result:** PASS ✅ - Encryption reversible hai

---

Test Case 3: Alphabet Wrap-around
**Input:**
Enter Choice: 1
Enter Plaintext: XYZ
Enter Shift Key 1-25: 4
**Output:**
```[ENCRYPTED]: BCD
[VALIDATION]: XYZ```
**Result:** PASS ✅ - %26 logic working
