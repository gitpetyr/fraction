class fraction():
	s=1
	f=1
	def __init__(self,s,f):
		s=s*10000000000000
		f=f*10000000000000
		def gcd(a,b):
			if a%b==0:
				return b;
			return gcd(b,a%b)
		c=gcd(s,f)
		self.s=s/c
		self.f=f/c
	def __str__(self):
		return str(int(self.s))+"/"+str(int(self.f))
	def get(self):
		return [int(self.s),int(self.f)]
	def fraction_to_float(self):
		return self.s/self.f
	def modify(self,s,f):
		def gcd(a,b):
			if a%b==0:
				return b;
			return gcd(b,a%b)
		c=gcd(s,f)
		self.s=s/c
		self.f=f/c