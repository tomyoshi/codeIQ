

def main():
	num = 11
	
	while True:
		if str(num) == str(num)[::-1] and \
		bin(num)[2::] == bin(num)[:1:-1] and \
		oct(num)[2::] == oct(num)[:1:-1]:
			print(num)
			break
		else:
			num = num + 1



if __name__ == "__main__":
	main()


