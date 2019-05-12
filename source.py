import queue

def get_path(n, parents):
	path = [n]
	while(parents[n] is not -1):
		n = parents[n]
		path.insert(0, n)
	return path


def find_shortest_path(n, arr):
	q = queue.Queue()
	q.put(1)
	arr.sort()
	parents = {
		1: -1
	}
	while(q.empty() is not None):
		node = q.get()
		for item in arr:
			result = item * node
			if result > n:
				break
			if result in parents:
				continue
			parents[result] = node
			if result == n:
				return get_path(result, parents)
			q.put(result)


def main():
	inputFile = input("Enter input file name: ")

	file = open(inputFile)

	if file.mode == 'r':
		contents = file.read()
		nk = contents.split('\n')[0].split()
		n = int(nk[0])
		k = int(nk[1])
		arr = list(map(int, contents.split('\n')[1].strip().split()))
		result = find_shortest_path(n, arr)
		print(result)

if __name__ == "__main__":
	main()