Wrap-it Challenge


||||| 5 TESTS |||||

1 >> Test purpose:

See whether the example in the program description produces the output it says it should

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

21

Expected output:

how now brown cow,
gannin doon the pub
for a bottle of broon
--END OF FILE--

>> Overall result was as intended although was there was an extra empty line added between the end 
of my example and the line indicating it was END OF FILE. 
The other notable difference from the result was the END OF FILE line, this is because I was expecting --END OF FILE--, as oper the specifications. 


2 >> Test purpose:

See whether the example in the program description produces an error by not giving a wrap number

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

Expected output:

I am expecting this to fail as not integer has been given, if it doesnt fail then I would expect it to return the string in its original form 

>> Returned an error due to no wrap integer being given, this aligns with my first thought in which I expected the program to fail to run and return an error. 
Program returned the following Python error - IndexError: list index out of range



3 >>Test purpose:

See whether the example in the program description produces the output it says it should with a wrap of 0 

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

0

Expected output:

how now brown cow, gannin doon the pub for a bottle of broon

>> This test returned an unexpected result. This test failed and returned a Traceback error. I can only assume that the program is designed to run with numbers larger than 0.
Program returned following error message - ValueError: substring not found


4 >>Test purpose:

See whether the example in the program description produces the output it says it should

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

6

Expected output:

how
now
brown
cow,
gannin
 doon
the
pub
for a
bottle
 of
broon
--END OF FILE--

>> Test produced the desired and expected result. Program performed as per the given program description.

5 >> Test purpose:

See whether the test fails due to giving a String letter in place of an integer number 

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

A

Expected output:

I am expecting this to fail as no integer has been given, if it doesnt fail then I would expect it to return the string in its original form 

>> Test performed as expected and gave an error stating that it was expecting an int and in its place it was given 'A' which did not meet the ptrogram criteria for a wrap number. 
Returned the following Python error - ValueError: invalid literal for int() with base 10: 'A'



6 >>Test purpose:

See whether the example in the program description produces the output it says it should with a wrap of 1

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

1

Expected output:

Expecting each string character to be on its own line with a empty line in plkace of the spaces between words.

>> Program failed with a Python error, this was not expected as believed it was a number above 0 and would allow the program to run.
Program returned following Python error - ValueError: substring not found



7 >>Test purpose:

See whether the example in the program description produces the output it says it should with a wrap of 3

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

3

Expected output:
how
now
bro
wn 
cow
, g
ann
in 
doo
n t
he 
pub
for
a b
ott
le 
of 
broo
n
END OF FILE
>> Progrm failed with the same error as above.
program returned Python error = ValueError: substring not found


8 >>Test purpose:

See whether the example in the program description produces the output it says it should with a wrap of 60

Text input:

how now brown cow, gannin doon the pub for a bottle of broon

Wrap limit:

60

Expected output:
how now brown cow, gannin doon the pub for a bottle of broon

END OF FILE

>> Test returned the expected result, including the empty line before the END OF FILE marker due to hitting the wrap_it character limit that we set at 60.

