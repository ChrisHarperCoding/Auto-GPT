## USER
Please help me to write an excel formula to pull out text located between the following

/* */

## ASSISTANT
You can use the following formula to extract text located between "/*" and "*/" in cell A1:

= MID(A1, FIND("/*", A1) + 2, FIND("*/", A1) - FIND("/*", A1) - 2)

This formula uses the MID function to extract a specific number of characters from a text string, based on the starting position and length specified. The starting position is determined by the FIND function, which locates the first occurrence of "/*" and adds 2 to move the starting position to the first character after "/*". The length is determined by subtracting the position of "/*" from the position of "*/" and then subtracting 2 to exclude the "/*" and "*/" characters themselves.

You can drag this formula down to apply it to multiple cells if needed. Just be sure to update the cell reference "A1" to the appropriate cell for each row.

## USER
It doesn't work why is this so complicated 😢

## ASSISTANT
I'm sorry to hear that the formula didn't work for you. It's possible that the formula may not work if the text you are trying to extract is located in a different position within the cell, or if the cell contains multiple occurrences of "/*" and "*/". 

Here's another formula that you can try which should be simpler and more flexible:

=SUBSTITUTE(SUBSTITUTE(MID(A1,FIND("/*",A1)+2,999),"*/",""),CHAR(10),"")

This formula uses the FIND function to locate the position of "/*" within the cell. It then uses the MID function to extract all the characters in the cell starting from the position of "/*" plus 2, up to a maximum of 999 characters.

Next, it uses the SUBSTITUTE function to remove any instances of "*/" that may be present in the extracted text, since we don't want to include those characters in the final result.

Finally, it uses another SUBSTITUTE function to remove any line breaks or carriage returns that may be present in the extracted text.

Remember to replace "A1" in the formula with the appropriate cell reference that contains the text you want to extract.

## USER
We're looking for /* and */ that has the text between,there may be other slash symbols elsewhere, can you account for this please? 

## ASSISTANT
Sure, here's a modified formula that should work even if there are other slash symbols present in the text, and only extracts the text between the first occurrence of "/*" and the first occurrence of "*/":

=TRIM(MID(SUBSTITUTE(SUBSTITUTE(A1,"/*",REPT(" ",99)),"*/",REPT(" ",99)),FIND(REPT(" ",99),SUBSTITUTE(SUBSTITUTE(A1,"/*",REPT(" ",99)),"*/",REPT(" ",99)))+99,99))

This formula uses the SUBSTITUTE function to replace "/*" and "*/" with 99 spaces each. It then uses the FIND function to locate the position of the first occurrence of 99 spaces within the modified text string, which should correspond to the start of the text you want to extract. The TRIM function is used to remove any extra spaces that may appear at the beginning or end of the extracted text.

Note that this formula assumes that the text you want to extract is no more than 99 characters long. If the text is longer than 99 characters, you can increase the number 99 to a larger value in both places in the formula.

Remember to replace "A1" in the formula with the appropriate cell reference that contains the text you want to extract.