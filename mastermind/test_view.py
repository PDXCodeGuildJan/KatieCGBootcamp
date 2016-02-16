import os

title = "Master Mind"
guess1 = "R G B W"
guess2 = "B G R W"
guess3 = "B G R G"
guess4 = "W B Y G"
guess5 = "- - - -"
guess6 = "- - - -"
guess7 = "- - - -"
guess8 = "- - - -"
guess9 = "- - - -"
guess10 = "- - - -"
res1 = "wb"
res2 = "wbb"
res3 = "www"
res4 = "wbwb"
res5 = ""
res6 = ""
res7 = ""
res8 = ""
res9 = ""
res10 = ""
res = "Res."

result_str = """{title:^70}\n\n
{guesses:>38}{res:>7}\n
{divider:>38}{divs:>7}\n\n
{guess1:>38}{res1:>7}\n
{guess2:>38}{res2:>7}\n
{guess3:>38}{res3:>7}\n
{guess4:>38}{res4:>7}\n
{guess5:>38}{res5:>7}\n
{guess6:>38}{res6:>7}\n
{guess7:>38}{res7:>7}\n
{guess8:>38}{res8:>7}\n
{guess9:>38}{res9:>7}\n
{guess10:>38}{res10:>7}\n






""".format(
	title=title, 
	guesses="Guesses", res=res,
	divider="=======", divs="====",
	guess1=guess1, res1=res1,
	guess2=guess2, res2=res2,
	guess3=guess3, res3=res3,
	guess4=guess4, res4=res4,
	guess5=guess5, res5=res5,
	guess6=guess6, res6=res6,
	guess7=guess7, res7=res7,
	guess8=guess8, res8=res8,
	guess9=guess9, res9=res9,
	guess10=guess10, res10=res10)

os.system("clear")
print(result_str)