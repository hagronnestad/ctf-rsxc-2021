# 16 - A scary command

> Sometimes while monitoring networks and machines, or doing incident response, we find some obfuscated commands. We didn't have time to deobfuscate this, and it is not recommended to just run it. Could you help us with it?
> 
> https://rsxc.no/dfb61488866658d31e3e7ccd2287caf233108a7eb917da6aefde3792d0fd79d2/16-challenge.sh

---

For this one I just kept running all variables and concatenation in bash, but being careful to remove all `eval` and `|sh`. I also used some auto formatting and syntax highlighting.


```bash
┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ cat 16-challenge.sh
gH4="Ed";kM0="xSz";c="ch";L="4";rQW="";fE1="lQ";s=" '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
' | r";HxJ="s";Hc2="";f="as";kcE="pas";cEf="ae";d="o";V9z="6";P8c="if";U=" -d";Jc="ef";N0q="";v="b";w="e";b="v |";Tx="Eds";xZp=""
x=$(eval "$Hc2$w$c$rQW$d$s$w$b$Hc2$v$xZp$f$w$V9z$rQW$L$U$xZp")
eval "$N0q$x$Hc2$rQW"

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ gH4="Ed"
kM0="xSz"
c="ch"
L="4"
rQW=""
fE1="lQ"
s=" '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
' | r"
HxJ="s"
f="as"
kcE="pas"
cEf="ae"
d="o"
V9z="6"
P8c="if"
U=" -d"
Jc="ef"
N0q=""
v="b"
w="e"
b="v |"
Tx="Eds"
xZp=""

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo "$w$c$rQW$d$s$w$b$v$xZp$f$w$V9z$rQW$L$U$xZp"
echo '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
' | rev |base64 -d

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo "$N0q$x$rQW"

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo '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
' | rev |base64 -d
gH4="Ed";kM0="xSz";c="ch";L="4";rQW="";fE1="lQ";s=" 'Kg2cgwHIk1CI0YTZzFmYgwHIis0ZyM2Z3hUS3FzQJlXMDl0aohUZndHSJhmQEpleRJTT4VlaOJTSt5kMRRkWysGVOJTWE5kMR1mTiEWY3RWbuF2dmFGJiISY3J3ZhRiIzcmaONTUE5kMN1mT41kaNpXSq5EakR1T6VkeNJSYhdHZt5WY3ZWYkIiaZJza61kMRRkTykVbOBTW65UMFpmTwMGVPpXWE5EMZJSY3J3ZhRiIzsmeNJTVUlVMJ1mT10kaNp3aU5kMZpWTxMGVOhmViE2dydWYkIieZRkT51EVPFTRy4kMVRlWyU0VOVTWU9keJpXT0UlIhdncnFGJioXVH5ENVRkTysmeOlXV61kenRlTx0ERPNzYE5EaWRlTz0UbONTUq1kMrpmT10kaOBTUq5EbaRkT6lkeNJSYhdHZt5WY3ZWYkICVOBTU65keNRVTxsGVOxmU6llMVRlT6lkaZpXUy00aORVTxklaOlmWq5EMR1mT1UlaOJTUq50aapWTyEkeORTW65EMRpmTqpFVNpXS61kIhF2dk1mbhdnZhRiIUl1MrpXT41kaNJTSt5UNNpmTwElaO1mWE5kMjRlT4lFRONza61kMRRkTyEkeOVTTq5UMFdlTppFVPpXS61UNVpmTykEVONTVUlVMBpXTyElaNp3aU5EakpmTxUVbOhmVU9kMrpXT51ERPFTQ61EbSR0TxElaOVzYq1UMNpXT0UFVOp3Z650MRRVWxUleOpmW65EMJpmT1kFVPpXWE5EMZRlWyEleNlXTq1kMVRkTwMmeNpXRU5UNVRlWw0UbOFTV61UeJJTTwMGRPNTU65EbKpnTyUkaOpmWq5kMZ1WTykFVOpXUq5kIhF2dk1mbhdnZhRiIU5kMBpXT10EROJTRq5UMNJSY3J3ZhRiI61keNFTWiE2dydWYkIieVpXT10ERPpXWq5kIhF2dk1mbhdnZhRiIq1keJpmT31keOpXTq5UeNR0T6NmeNFTWiE2dydWYkIiejpXTiEWY3RWbuF2dmFGJiQkTy0kaOdXTU1keNpmTiEWY3RWbuF2dmFGJiomTyUlaOhXTE5keNpXTy0keNJTU61UMZJSY3J3ZhRiI6VleNVTT61keJpmTw0EROJTTq5kMZRVTykkeNBTWE5keNpXTiEWY3RWbuF2dmFGJiISY3J3ZhRiI6lleNJSYhdHZt5WY3ZWYkIiaaJSYhdHZt5WY3ZWYkISbOxmWUpVeNpmT0MmeNNTS65UbKpmW5VkMNd3YE50MRpnT0klIhdncnFGJikXTt5UejRlTz0kaOdXSEV2dBlnYv50VaJCIvh2YltTeZ1TYhdHZt5WY3ZWY7QUT9E2dydWY
' | r";HxJ="s";Hc2="";f="as";kcE="pas";cEf="ae";d="o";V9z="6";P8c="if";U=" -d";Jc="ef";N0q="";v="b";w="e";b="v |";Tx="Eds";xZp=""
x=$(eval "$Hc2$w$c$rQW$d$s$w$b$Hc2$v$xZp$f$w$V9z$rQW$L$U$xZp")
eval "$N0q$x$Hc2$rQW"
base64: invalid input
┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo "$N0q$x$rQW"

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo '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
' | rev |base64 -d
gH4="Ed";kM0="xSz";c="ch";L="4";rQW="";fE1="lQ";s=" 'Kg2cgwHIk1CI0YTZzFmYgwHIis0ZyM2Z3hUS3FzQJlXMDl0aohUZndHSJhmQEpleRJTT4VlaOJTSt5kMRRkWysGVOJTWE5kMR1mTiEWY3RWbuF2dmFGJiISY3J3ZhRiIzcmaONTUE5kMN1mT41kaNpXSq5EakR1T6VkeNJSYhdHZt5WY3ZWYkIiaZJza61kMRRkTykVbOBTW65UMFpmTwMGVPpXWE5EMZJSY3J3ZhRiIzsmeNJTVUlVMJ1mT10kaNp3aU5kMZpWTxMGVOhmViE2dydWYkIieZRkT51EVPFTRy4kMVRlWyU0VOVTWU9keJpXT0UlIhdncnFGJioXVH5ENVRkTysmeOlXV61kenRlTx0ERPNzYE5EaWRlTz0UbONTUq1kMrpmT10kaOBTUq5EbaRkT6lkeNJSYhdHZt5WY3ZWYkICVOBTU65keNRVTxsGVOxmU6llMVRlT6lkaZpXUy00aORVTxklaOlmWq5EMR1mT1UlaOJTUq50aapWTyEkeORTW65EMRpmTqpFVNpXS61kIhF2dk1mbhdnZhRiIUl1MrpXT41kaNJTSt5UNNpmTwElaO1mWE5kMjRlT4lFRONza61kMRRkTyEkeOVTTq5UMFdlTppFVPpXS61UNVpmTykEVONTVUlVMBpXTyElaNp3aU5EakpmTxUVbOhmVU9kMrpXT51ERPFTQ61EbSR0TxElaOVzYq1UMNpXT0UFVOp3Z650MRRVWxUleOpmW65EMJpmT1kFVPpXWE5EMZRlWyEleNlXTq1kMVRkTwMmeNpXRU5UNVRlWw0UbOFTV61UeJJTTwMGRPNTU65EbKpnTyUkaOpmWq5kMZ1WTykFVOpXUq5kIhF2dk1mbhdnZhRiIU5kMBpXT10EROJTRq5UMNJSY3J3ZhRiI61keNFTWiE2dydWYkIieVpXT10ERPpXWq5kIhF2dk1mbhdnZhRiIq1keJpmT31keOpXTq5UeNR0T6NmeNFTWiE2dydWYkIiejpXTiEWY3RWbuF2dmFGJiQkTy0kaOdXTU1keNpmTiEWY3RWbuF2dmFGJiomTyUlaOhXTE5keNpXTy0keNJTU61UMZJSY3J3ZhRiI6VleNVTT61keJpmTw0EROJTTq5kMZRVTykkeNBTWE5keNpXTiEWY3RWbuF2dmFGJiISY3J3ZhRiI6lleNJSYhdHZt5WY3ZWYkIiaaJSYhdHZt5WY3ZWYkISbOxmWUpVeNpmT0MmeNNTS65UbKpmW5VkMNd3YE50MRpnT0klIhdncnFGJikXTt5UejRlTz0kaOdXSEV2dBlnYv50VaJCIvh2YltTeZ1TYhdHZt5WY3ZWY7QUT9E2dydWY
' | r";HxJ="s";Hc2="";f="as";kcE="pas";cEf="ae";d="o";V9z="6";P8c="if";U=" -d";Jc="ef";N0q="";v="b";w="e";b="v |";Tx="Eds";xZp=""
x=$(eval "$Hc2$w$c$rQW$d$s$w$b$Hc2$v$xZp$f$w$V9z$rQW$L$U$xZp")
eval "$N0q$x$Hc2$rQW"
base64: invalid input

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ gH4="Ed";kM0="xSz";c="ch";L="4";rQW="";fE1="lQ";s=" 'Kg2cgwHIk1CI0YTZzFmYgwHIis0ZyM2Z3hUS3FzQJlXMDl0aohUZndHSJhmQEpleRJTT4VlaOJTSt5kMRRkWysGVOJTWE5kMR1mTiEWY3RWbuF2dmFGJiISY3J3ZhRiIzcmaONTUE5kMN1mT41kaNpXSq5EakR1T6VkeNJSYhdHZt5WY3ZWYkIiaZJza61kMRRkTykVbOBTW65UMFpmTwMGVPpXWE5EMZJSY3J3ZhRiIzsmeNJTVUlVMJ1mT10kaNp3aU5kMZpWTxMGVOhmViE2dydWYkIieZRkT51EVPFTRy4kMVRlWyU0VOVTWU9keJpXT0UlIhdncnFGJioXVH5ENVRkTysmeOlXV61kenRlTx0ERPNzYE5EaWRlTz0UbONTUq1kMrpmT10kaOBTUq5EbaRkT6lkeNJSYhdHZt5WY3ZWYkICVOBTU65keNRVTxsGVOxmU6llMVRlT6lkaZpXUy00aORVTxklaOlmWq5EMR1mT1UlaOJTUq50aapWTyEkeORTW65EMRpmTqpFVNpXS61kIhF2dk1mbhdnZhRiIUl1MrpXT41kaNJTSt5UNNpmTwElaO1mWE5kMjRlT4lFRONza61kMRRkTyEkeOVTTq5UMFdlTppFVPpXS61UNVpmTykEVONTVUlVMBpXTyElaNp3aU5EakpmTxUVbOhmVU9kMrpXT51ERPFTQ61EbSR0TxElaOVzYq1UMNpXT0UFVOp3Z650MRRVWxUleOpmW65EMJpmT1kFVPpXWE5EMZRlWyEleNlXTq1kMVRkTwMmeNpXRU5UNVRlWw0UbOFTV61UeJJTTwMGRPNTU65EbKpnTyUkaOpmWq5kMZ1WTykFVOpXUq5kIhF2dk1mbhdnZhRiIU5kMBpXT10EROJTRq5UMNJSY3J3ZhRiI61keNFTWiE2dydWYkIieVpXT10ERPpXWq5kIhF2dk1mbhdnZhRiIq1keJpmT31keOpXTq5UeNR0T6NmeNFTWiE2dydWYkIiejpXTiEWY3RWbuF2dmFGJiQkTy0kaOdXTU1keNpmTiEWY3RWbuF2dmFGJiomTyUlaOhXTE5keNpXTy0keNJTU61UMZJSY3J3ZhRiI6VleNVTT61keJpmTw0EROJTTq5kMZRVTykkeNBTWE5keNpXTiEWY3RWbuF2dmFGJiISY3J3ZhRiI6lleNJSYhdHZt5WY3ZWYkIiaaJSYhdHZt5WY3ZWYkISbOxmWUpVeNpmT0MmeNNTS65UbKpmW5VkMNd3YE50MRpnT0klIhdncnFGJikXTt5UejRlTz0kaOdXSEV2dBlnYv50VaJCIvh2YltTeZ1TYhdHZt5WY3ZWY7QUT9E2dydWY
' | r";HxJ="s";Hc2="";f="as";kcE="pas";cEf="ae";d="o";V9z="6";P8c="if";U=" -d";Jc="ef";N0q="";v="b";w="e";b="v |";Tx="Eds";xZp=""

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo "$Hc2$w$c$rQW$d$s$w$b$Hc2$v$xZp$f$w$V9z$rQW$L$U$xZp"
echo 'Kg2cgwHIk1CI0YTZzFmYgwHIis0ZyM2Z3hUS3FzQJlXMDl0aohUZndHSJhmQEpleRJTT4VlaOJTSt5kMRRkWysGVOJTWE5kMR1mTiEWY3RWbuF2dmFGJiISY3J3ZhRiIzcmaONTUE5kMN1mT41kaNpXSq5EakR1T6VkeNJSYhdHZt5WY3ZWYkIiaZJza61kMRRkTykVbOBTW65UMFpmTwMGVPpXWE5EMZJSY3J3ZhRiIzsmeNJTVUlVMJ1mT10kaNp3aU5kMZpWTxMGVOhmViE2dydWYkIieZRkT51EVPFTRy4kMVRlWyU0VOVTWU9keJpXT0UlIhdncnFGJioXVH5ENVRkTysmeOlXV61kenRlTx0ERPNzYE5EaWRlTz0UbONTUq1kMrpmT10kaOBTUq5EbaRkT6lkeNJSYhdHZt5WY3ZWYkICVOBTU65keNRVTxsGVOxmU6llMVRlT6lkaZpXUy00aORVTxklaOlmWq5EMR1mT1UlaOJTUq50aapWTyEkeORTW65EMRpmTqpFVNpXS61kIhF2dk1mbhdnZhRiIUl1MrpXT41kaNJTSt5UNNpmTwElaO1mWE5kMjRlT4lFRONza61kMRRkTyEkeOVTTq5UMFdlTppFVPpXS61UNVpmTykEVONTVUlVMBpXTyElaNp3aU5EakpmTxUVbOhmVU9kMrpXT51ERPFTQ61EbSR0TxElaOVzYq1UMNpXT0UFVOp3Z650MRRVWxUleOpmW65EMJpmT1kFVPpXWE5EMZRlWyEleNlXTq1kMVRkTwMmeNpXRU5UNVRlWw0UbOFTV61UeJJTTwMGRPNTU65EbKpnTyUkaOpmWq5kMZ1WTykFVOpXUq5kIhF2dk1mbhdnZhRiIU5kMBpXT10EROJTRq5UMNJSY3J3ZhRiI61keNFTWiE2dydWYkIieVpXT10ERPpXWq5kIhF2dk1mbhdnZhRiIq1keJpmT31keOpXTq5UeNR0T6NmeNFTWiE2dydWYkIiejpXTiEWY3RWbuF2dmFGJiQkTy0kaOdXTU1keNpmTiEWY3RWbuF2dmFGJiomTyUlaOhXTE5keNpXTy0keNJTU61UMZJSY3J3ZhRiI6VleNVTT61keJpmTw0EROJTTq5kMZRVTykkeNBTWE5keNpXTiEWY3RWbuF2dmFGJiISY3J3ZhRiI6lleNJSYhdHZt5WY3ZWYkIiaaJSYhdHZt5WY3ZWYkISbOxmWUpVeNpmT0MmeNNTS65UbKpmW5VkMNd3YE50MRpnT0klIhdncnFGJikXTt5UejRlTz0kaOdXSEV2dBlnYv50VaJCIvh2YltTeZ1TYhdHZt5WY3ZWY7QUT9E2dydWY
' | rev |base64 -d

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo 'Kg2cgwHIk1CI0YTZzFmYgwHIis0ZyM2Z3hUS3FzQJlXMDl0aohUZndHSJhmQEpleRJTT4VlaOJTSt5kMRRkWysGVOJTWE5kMR1mTiEWY3RWbuF2dmFGJiISY3J3ZhRiIzcmaONTUE5kMN1mT41kaNpXSq5EakR1T6VkeNJSYhdHZt5WY3ZWYkIiaZJza61kMRRkTykVbOBTW65UMFpmTwMGVPpXWE5EMZJSY3J3ZhRiIzsmeNJTVUlVMJ1mT10kaNp3aU5kMZpWTxMGVOhmViE2dydWYkIieZRkT51EVPFTRy4kMVRlWyU0VOVTWU9keJpXT0UlIhdncnFGJioXVH5ENVRkTysmeOlXV61kenRlTx0ERPNzYE5EaWRlTz0UbONTUq1kMrpmT10kaOBTUq5EbaRkT6lkeNJSYhdHZt5WY3ZWYkICVOBTU65keNRVTxsGVOxmU6llMVRlT6lkaZpXUy00aORVTxklaOlmWq5EMR1mT1UlaOJTUq50aapWTyEkeORTW65EMRpmTqpFVNpXS61kIhF2dk1mbhdnZhRiIUl1MrpXT41kaNJTSt5UNNpmTwElaO1mWE5kMjRlT4lFRONza61kMRRkTyEkeOVTTq5UMFdlTppFVPpXS61UNVpmTykEVONTVUlVMBpXTyElaNp3aU5EakpmTxUVbOhmVU9kMrpXT51ERPFTQ61EbSR0TxElaOVzYq1UMNpXT0UFVOp3Z650MRRVWxUleOpmW65EMJpmT1kFVPpXWE5EMZRlWyEleNlXTq1kMVRkTwMmeNpXRU5UNVRlWw0UbOFTV61UeJJTTwMGRPNTU65EbKpnTyUkaOpmWq5kMZ1WTykFVOpXUq5kIhF2dk1mbhdnZhRiIU5kMBpXT10EROJTRq5UMNJSY3J3ZhRiI61keNFTWiE2dydWYkIieVpXT10ERPpXWq5kIhF2dk1mbhdnZhRiIq1keJpmT31keOpXTq5UeNR0T6NmeNFTWiE2dydWYkIiejpXTiEWY3RWbuF2dmFGJiQkTy0kaOdXTU1keNpmTiEWY3RWbuF2dmFGJiomTyUlaOhXTE5keNpXTy0keNJTU61UMZJSY3J3ZhRiI6VleNVTT61keJpmTw0EROJTTq5kMZRVTykkeNBTWE5keNpXTiEWY3RWbuF2dmFGJiISY3J3ZhRiI6lleNJSYhdHZt5WY3ZWYkIiaaJSYhdHZt5WY3ZWYkISbOxmWUpVeNpmT0MmeNNTS65UbKpmW5VkMNd3YE50MRpnT0klIhdncnFGJikXTt5UejRlTz0kaOdXSEV2dBlnYv50VaJCIvh2YltTeZ1TYhdHZt5WY3ZWY7QUT9E2dydWY
' | rev |base64 -d
agrwa=MD;afwanmdwaa=Yy;echo "ZWNobyAweDIwNjM3NTcyNmMy"$agrwa"Y4NzQ3NDcwM2EyZjJmNzI3Mzc4NjMyZTZlNm"$afwanmdwaa"Zj"$afwanmdwaa"MzYz"$agrwa""$afwanmdwaa"MzMzNDY0MzI2MTY2NjM2NDM0NjIzMzM5MzUz"$agrwa"Y1MzQ2MzM2MzMzNDMxNjU2Nj"$afwanmdwaa"NjMzMTMwNjM2ND"$afwanmdwaa"Mzcz"$agrwa"Y1MzczODMyNjMzNzMwNjIzMj"$afwanmdwaa"NjYzODM5MzUz"$agrwa"Y1MzMz"$agrwa"M1NjE2NDM5MzA2NT"$afwanmdwaa"NjQzNTY2MmY2NjZjNjE2NzJlNzQ3ODc0M2IyMzU1NmM0ZTU5NTEzMzc0NDU2MjMyMzQ2ZTY0NDYzOTY5NjI0NzZjNzU1YTQ3NzgzNTU4MzM1Mjc5NjQ1ODRlMzA1ODMyMzk2OTVhNmU1NjdhNTkzMjQ2MzA1YTU3NTI2NjU5MzIzOTZiNWE1NjM5NzA2NDQ2Mzk3NDYxNTc2NDZmNjQ0NjM5NmI2MjMxMzk3YT"$afwanmdwaa"MzIzMTZjNjQ0NzY4NzA2MjZkNjQ2NjU5NmQ0NjZiNjY1MTNkM2QzYjIzNTU2YzRlNTk1MTMzNzQ0NT"$afwanmdwaa"MzIzNDZlNjQ0NjM5Njk2MjQ3NmM3NTVhNDc3ODM1NTgzMzUyNzk2NDU4NGUz"$agrwa"U4MzIzOTY5NWE2ZTU2N2E1OTMyNDYz"$agrwa"VhNTc1MjY2NTkzMjM5NmI1YTU2Mzk3"$agrwa"Y0NDYzOTc0NjE1NzY0NmY2NDQ2Mzk2Yj"$afwanmdwaa"MzEzOTdhNjIzMjMxNmM2NDQ3Njg3"$agrwa""$afwanmdwaa"NmQ2NDY2NTk2ZDQ2NmI2NjUxM2QzZDBhIHwgeHhkIC1yIC1wIHwgc2gK" | base64 -d | sh

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ agrwa=MD;afwanmdwaa=Yy;echo "ZWNobyAweDIwNjM3NTcyNmMy"$agrwa"Y4NzQ3NDcwM2EyZjJmNzI3Mzc4NjMyZTZlNm"$afwanmdwaa"Zj"$afwanmdwaa"MzYz"$agrwa""$afwanmdwaa"MzMzNDY0MzI2MTY2NjM2NDM0NjIzMzM5MzUz"$agrwa"Y1MzQ2MzM2MzMzNDMxNjU2Nj"$afwanmdwaa"NjMzMTMwNjM2ND"$afwanmdwaa"Mzcz"$agrwa"Y1MzczODMyNjMzNzMwNjIzMj"$afwanmdwaa"NjYzODM5MzUz"$agrwa"Y1MzMz"$agrwa"M1NjE2NDM5MzA2NT"$afwanmdwaa"NjQzNTY2MmY2NjZjNjE2NzJlNzQ3ODc0M2IyMzU1NmM0ZTU5NTEzMzc0NDU2MjMyMzQ2ZTY0NDYzOTY5NjI0NzZjNzU1YTQ3NzgzNTU4MzM1Mjc5NjQ1ODRlMzA1ODMyMzk2OTVhNmU1NjdhNTkzMjQ2MzA1YTU3NTI2NjU5MzIzOTZiNWE1NjM5NzA2NDQ2Mzk3NDYxNTc2NDZmNjQ0NjM5NmI2MjMxMzk3YT"$afwanmdwaa"MzIzMTZjNjQ0NzY4NzA2MjZkNjQ2NjU5NmQ0NjZiNjY1MTNkM2QzYjIzNTU2YzRlNTk1MTMzNzQ0NT"$afwanmdwaa"MzIzNDZlNjQ0NjM5Njk2MjQ3NmM3NTVhNDc3ODM1NTgzMzUyNzk2NDU4NGUz"$agrwa"U4MzIzOTY5NWE2ZTU2N2E1OTMyNDYz"$agrwa"VhNTc1MjY2NTkzMjM5NmI1YTU2Mzk3"$agrwa"Y0NDYzOTc0NjE1NzY0NmY2NDQ2Mzk2Yj"$afwanmdwaa"MzEzOTdhNjIzMjMxNmM2NDQ3Njg3"$agrwa""$afwanmdwaa"NmQ2NDY2NTk2ZDQ2NmI2NjUxM2QzZDBhIHwgeHhkIC1yIC1wIHwgc2gK" | base64 -d
echo 0x206375726c20687474703a2f2f727378632e6e6f2f623630623334643261666364346233393530653463363334316566626331306364623730653738326337306232626638393530653330356164393065626435662f666c61672e7478743b23556c4e59513374456232346e6446396962476c755a4778355833527964584e30583239695a6e567a593246305a5752665932396b5a563970644639746157646f6446396b6231397a6232316c64476870626d6466596d466b66513d3d3b23556c4e59513374456232346e6446396962476c755a4778355833527964584e30583239695a6e567a593246305a5752665932396b5a563970644639746157646f6446396b6231397a6232316c64476870626d6466596d466b66513d3d0a | xxd -r -p | sh

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo 0x206375726c20687474703a2f2f727378632e6e6f2f623630623334643261666364346233393530653463363334316566626331306364623730653738326337306232626638393530653330356164393065626435662f666c61672e7478743b23556c4e59513374456232346e6446396962476c755a4778355833527964584e30583239695a6e567a593246305a5752665932396b5a563970644639746157646f6446396b6231397a6232316c64476870626d6466596d466b66513d3d3b23556c4e59513374456232346e6446396962476c755a4778355833527964584e30583239695a6e567a593246305a5752665932396b5a563970644639746157646f6446396b6231397a6232316c64476870626d6466596d466b66513d3d0a | xxd -r -p
 curl http://rsxc.no/b60b34d2afcd4b3950e4c6341efbc10cdb70e782c70b2bf8950e305ad90ebd5f/flag.txt;#UlNYQ3tEb24ndF9ibGluZGx5X3RydXN0X29iZnVzY2F0ZWRfY29kZV9pdF9taWdodF9kb19zb21ldGhpbmdfYmFkfQ==;#UlNYQ3tEb24ndF9ibGluZGx5X3RydXN0X29iZnVzY2F0ZWRfY29kZV9pdF9taWdodF9kb19zb21ldGhpbmdfYmFkfQ==

┌──(hag㉿hag-desktop)-[~/ctf-rsxc-2021/16]
└─$ echo "UlNYQ3tEb24ndF9ibGluZGx5X3RydXN0X29iZnVzY2F0ZWRfY29kZV9pdF9taWdodF9kb19zb21ldGhpbmdfYmFkfQ==" | base64 -d
RSXC{Don't_blindly_trust_obfuscated_code_it_might_do_something_bad}
```


## Solution

The flag is: `RSXC{Don't_blindly_trust_obfuscated_code_it_might_do_something_bad}`