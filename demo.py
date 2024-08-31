from ssf import SSF

ssf = SSF(locale='en_us')
print(ssf.format('#,##0', 10004))

print(ssf.format('#,##0', 1000))
print(ssf.format('Currency', 1000.98))
print(ssf.format('Currency', 1000.98, locale='de-DE'))
print(ssf.format('General', 100000, width=5))
print(ssf.format('?/?', 3.14159))
