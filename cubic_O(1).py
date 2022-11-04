print('Eneter the coefficients of the cubic function:')

a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))
d=int(input('d = '))

def cplxRound(cplx):
	return str(complex(round(cplx.real,8),round(cplx.imag,8)))

postive_term=( 0.5*((2*b*b*b - 9*a*b*c + 27*a*a*d + ( (2*b*b*b - 9*a*b*c + 27*a*a*d)**2 - 4*((b*b - 3*a*c)**3))**0.5 ) ))**(1/3)
negative_term=( 0.5*((2*b*b*b - 9*a*b*c + 27*a*a*d - ( (2*b*b*b - 9*a*b*c + 27*a*a*d)**2 - 4*((b*b - 3*a*c)**3))**0.5 ) ))**(1/3)

print('X1 = '+cplxRound((-b/(3*a) - (1/(3*a)) *postive_term - (1/(3*a)) *negative_term)))
print('X2 = '+cplxRound((-b/(3*a) + (complex(1,3**0.5)/(6*a))*postive_term + (complex(1,-3**0.5)/(6*a))*negative_term)))
print('X3 = '+cplxRound((-b/(3*a) + (complex(1,-3**0.5)/(6*a))*postive_term + (complex(1,3**0.5)/(6*a))*negative_term)))
