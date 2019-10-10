# imports ?
import os
import sys
import string, itertools


FLAG = "HELLO AND WELCOME"

class Encoder:
	def _parse_csv(self, csv_path=None):
	    is_resend = csv_path is not None
	    if not csv_path:
	        csv_path = self.csv_path

	    try:
	        csv_file = open(csv_path, 'r')
	        '''csv_file1 = open(csv_path, 'w')'''
	    except IOError:
	        raise IOError("Invalid or missing csv file path.")

	    csv_reader = csv.reader(csv_file)
	    recipient_data_list = []
	    for i, row in enumerate(csv_reader):
	        # test indexes exist and validate email address
	        try:
	            recipient_name = row[0]
	            recipient_email = self._validate_email(row[1])
	        except IndexError:
	            recipient_name = ''
	            recipient_email = None

	        print(recipient_name, recipient_email)

	        # log missing email addresses and line number
	        if not recipient_email:
	            logging.error("Recipient email missing in line %s" % i)
	        else:
	            recipient_data_list.append({
	                'name': recipient_name,
	                'email': recipient_email,
	            })

	    # clear the contents of the resend csv file
	    '''if is_resend:
	        csv_file1.write('')'''

	    csv_file.close()

	def main_try(self,filename):
		_,a,b = FLAG.split(' ')

		if b == 'WELCOME':
			dec = Decoder()
			print(dec._placeholder(filename))

		cnt = 0
		a = 50
		b = 100
		for i in range(10):
			cnt = a + b
			if cnt > 1000:
				break
		print('Got it?')


	def findMin2(self,L, i, sumCalculated, sumTotal) :
	    if i == 0:
	        return abs((sumTotal - sumCalculated) - sumCalculated)

	    return min(findMin2(L, i-1, sumCalculated + L[i-1], sumTotal),
	               findMin2(L, i-1, sumCalculated, sumTotal))


	def findMin(L, n):
	    sumTotal = 0;
	    for i in range(0, n):
	        sumTotal += L[i]


	def main(self):
		n0,n1 = input().split()
		n0,n1 = int(n0),int(n1)
		if n1 > (2+2*n0) :
		    print(-1)
		    sys.exit()
		if n0 > n1-1 :
		    print(-1)
		    sys.exit()
		s = ''
		if n1-n0 == 1 :
		    s = '1'+'01'*n0
		    print(s)
		    sys.exit()
		while n1 > n0 and n0 > 0:
		    if n1-n0 == 1 :
		        break
		    print('110')
		    n1 -= 2
		    n0 -= 1
		    print(n1,n0)
		    s += '110'
		if n1-n0 == 1 :
		    s += '10'*n0+'1'
		    print(s)
		    sys.exit()
		if n1 > 2 and n0==0 :
		    print(-1)
		    sys.exit()
		elif n0==1 and n1==1 :
		    s += '0'+'1'*n1
		elif n0==1 and n1==2 :
		    s += '101'
		elif n0==0:
		    s += '1'*n1
		print(s)


# Write Something