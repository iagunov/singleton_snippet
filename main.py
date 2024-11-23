from threading import Lock

class Singleton:
	"""
	Singleton pattern.
	"""
	__instance = None
	__lock = Lock()

	def __new__(cls, spark, log):
		with cls.__lock:
			if cls.__instance is None:
				cls.__instance = super().__new__(cls)
				cls.__instance.spark = spark
				cls.__instance.log = log
		return cls.__instance

pt = Singleton("spark", "log")
print(pt)
pt2 = Singleton("spark", "log")
print(pt2)
