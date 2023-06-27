Exploratory Testing

Email Sign Up Challenge
-VALID CASES
---sean@hotmail.co.uk  ** Test failed unexpectedly even though valid address // test was of a good format and had no reason to fail, - Investigation needed.

---sean@outlook.com    ** Test passed as expected

---123456@hotmail.com  ** Test passed as expected

---123+sean@hotmail.com   ** Test failed unexpectedly even though valid address // Again this test was of a good format and should not have failed, - Investigation needed.

---sean@outlook.org    ** Test passed as expected

---sean@outlook.net    ** Test passed as expected

-INVALID CASES
---sean.hotmail.co.uk     ** Test failed as expeted // this test failed as it did not have @ seperating the recipient and the domain name.

---sean@wright@hotmaill.com    ** Test failed as expeted // this test failed due to having more than one @ in the address, only one is allowed.

---1234567890123456789012345678901234567890123456789012345678901234+x@hotmail.com   ** Test broke the sign up page, had only expected a generic fail like other tests. // this test caused the browser to stop responding, could possibly be due to the number of characters it wa trying to verify in one go, - Investigation needed. 



||||||| REPORT |||||
>>Upon testing the email sign up page it is clear to see that this does not meet the standard email protocols that dictate valid and invalid email addresses. 
>>The following email addresses all passed as expected - (sean@outlook.com) + (123456@hotmail.com) + (sean@outlook.org). This is the expected outcome and no further testing or work is needed in regards to these email addresses.
>>The following email address should be valid - (sean@hotmail.co.uk), but was giving an error stating that the email address was invalid and to try again. This differs to the 2 email addresses above in that it has a .co.uk top-level domain. This will need further investigation as to why this domain is failing.
>>The following email also failed testing - (123+sean@hotmail.com), even this should also be a valid email address. This could possibly be due to the special character within the email address. 
>> All the invalid tests failed as expected, the last test case which included a recipient of more than 64 characters managed to cause the page to stop responding, this may be intentional but will cause a user to think the page is broken. 

In conclusion, the email sign up page in its current format is not fit for purpose and requires extra work within the programs code to ensure it successfully tests each email address given and follows the correct protocols for assessing if an email address is correct or not. 