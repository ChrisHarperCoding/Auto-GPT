## USER
I have some text in column H in Excel, for example:

"/* RFC5103 - FP 288267 - File Transfer Utility - Anthony Malone 08-03-2023*/
this is an example bit of text"

Could we write a formula to check for text in Column H that is in between /* and */ and then display it in Column I? For example in this scenario I would like to show the following in Column I:

/* RFC5103 - FP 288267 - File Transfer Utility - Anthony Malone 08-03-2023*/

## ASSISTANT
Yes, you can use a combination of Excel functions to achieve this. Here's a formula you can use:

`=IFERROR(MID(H1, SEARCH("/\*", H1), SEARCH("\*/", H1) - SEARCH("/\*", H1) + 2), "")`

In this formula, we use the SEARCH function to find the positions of "/*" and "*/" in the text, then extract the text in between with the MID function. The IFERROR function is used to return an empty string if the formula doesn't find the desired pattern.

Place this formula in cell I1 and copy it down to the other cells in column I as needed. This will display the text between "/*" and "*/" for each cell in column H. If the pattern is not found, the formula will display an empty string.

## USER
Ideally I would like to search specifically for /* and */ rather than just / and / as these symbols might be present elsewhere 

## ASSISTANT
Apologies for the confusion. You can modify the formula to search specifically for "/*" and "*/" as follows:

`=IFERROR(MID(H1, SEARCH("/\*", H1), SEARCH("\*/", H1) - SEARCH("/\*", H1) + 2), "")`

In this formula, we use the SEARCH function to find the positions of "/*" and "*/" in the text by escaping the asterisk (*) with a backslash (\). Then, we extract the text between "/*" and "*/" with the MID function. The IFERROR function is used to return an empty string if the formula doesn't find the desired pattern.

Place this formula in cell I1 and copy it down to the other cells in column I as needed. This will display the text between "/*" and "*/" for each cell in column H. If the pattern is not found, the formula will display an empty string.