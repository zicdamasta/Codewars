# ------------------------------------------------------
# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.
#
# For example:
#
# solve("our code") = "edo cruo"
# -- Normal reversal without spaces is "edocruo".
# -- However, there is a space after the first three characters, hence "edo cruo"
#
#   solve("your code rocks") = "skco redo cruoy"
#   solve("codewars") = "srawedoc"
#
# ------------------------------------------------------


def solve(string):
    list_string_reversed = list(string[::-1].replace(" ", ""))
    for i in range(len(string)):
        if string[i] == " ":
            list_string_reversed.insert(i, " ")
    return "".join(list_string_reversed)
