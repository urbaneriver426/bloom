class BloomFilter:

	def __init__(self, f_len):
		self.filter_len = f_len
		self.bf = bytearray(f_len) 
		# создаём битовый массив длиной f_len ...

	def hash1(self, str1):
		# 17
		code = 0
		result = 0
		for c in str1:
			code = ord(c)
			result = result * 17 + code
		result = result % self.filter_len
		return result

		# реализация ...

	def hash2(self, str1):
		code = 0
		result = 0
		for c in str1:
			code = ord(c)
			result = result * 223 + code
		result = result % self.filter_len
		return result
		# 223 
		# ...

	def add(self, str1):
		if self.is_value(str1) == False:
			self.bf[self.hash1(str1)] = 1
			self.bf[self.hash2(str1)] = 1

	def is_value(self, str1):
		if self.bf[self.hash1(str1)] == 1 and self.bf[self.hash2(str1)] == 1:
			return True
		else:
			return False
