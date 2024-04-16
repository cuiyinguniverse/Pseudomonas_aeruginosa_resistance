import numpy as np
import scipy.stats as stats

abcd1 =np.array([[69,24],[704,303]])
abcd2 =np.array([[24,16],[724,300]])
abcd3 =np.array([[55,24],[718,303]])
abcd4 =np.array([[14,6],[758,318]])
abcd5 =np.array([[8,0],[762,324]])
abcd6 =np.array([[4,0],[768,327]])
abcd7 =np.array([[0,0],[772,327]])
abcd8 =np.array([[12,2],[735,311]])
abcd9 =np.array([[0,0],[745,313]])
abcd10 =np.array([[0,0],[747,316]])
abcd11 =np.array([[0,0],[747,316]])
abcd12 =np.array([[8,6],[764,318]])
abcd13 =np.array([[2,0],[768,324]])
abcd14 =np.array([[4,0],[768,327]])
abcd15 =np.array([[0,0],[772,327]])

#
kj1 = stats.chi2_contingency(abcd1,correction=False)
kj2 = stats.chi2_contingency(abcd2,correction=False)
kj3 = stats.chi2_contingency(abcd3,correction=False)
kj4 = stats.chi2_contingency(abcd4,correction=False)
kj12 = stats.chi2_contingency(abcd12,correction=False)

oddsr5,p5=stats.fisher_exact(abcd5,alternative='two-sided')
oddsr6,p6=stats.fisher_exact(abcd6,alternative='two-sided')
oddsr7,p7=stats.fisher_exact(abcd7,alternative='two-sided')
oddsr9,p9=stats.fisher_exact(abcd9,alternative='two-sided')
oddsr10,p10=stats.fisher_exact(abcd10,alternative='two-sided')
oddsr11,p11=stats.fisher_exact(abcd11,alternative='two-sided')
oddsr13,p13=stats.fisher_exact(abcd13,alternative='two-sided')
oddsr14,p14=stats.fisher_exact(abcd14,alternative='two-sided')
oddsr15,p15=stats.fisher_exact(abcd15,alternative='two-sided')

kj8 = stats.chi2_contingency(abcd8,correction=True)

#
print('p1'+':'+str(kj1))
print('p2'+':'+str(kj2))
print('p3'+':'+str(kj3))
print('p4'+':'+str(kj4))
#
print('p5'+':'+str(p5))
print('oddsr5 is : ' + str(oddsr5))
print('p6'+':'+str(p6))
print('oddsr6 is : ' + str(oddsr6))
print('p7'+':'+str(p7))
print('oddsr7 is : ' + str(oddsr7))
#
print('p8'+':'+str(kj8))
#
print('p9'+':'+str(p9))
print('oddsr9 is : ' + str(oddsr9))
print('p10'+':'+str(p10))
print('oddsr10 is : ' + str(oddsr10))
print('p11'+':'+str(p11))
print('oddsr11 is : ' + str(oddsr11))
#
print('p12'+':'+str(kj12))
#
print('p13'+':'+str(p13))
print('oddsr13 is : ' + str(oddsr13))
print('p14'+':'+str(p14))
print('oddsr14 is : ' + str(oddsr14))
print('p15'+':'+str(p15))
print('oddsr15 is : ' + str(oddsr15))

