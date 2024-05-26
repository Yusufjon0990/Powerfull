# 1-misol
# import time
#
# for j in  range(100, 100001, 100):
#     start = time.time()
#     a = 0
#     for i in range(j):
#         a += (i ** 100)
#     end = time.time()
#     print(f"Iteration: {j}\tTime taken: {(end - start) * 10 ** 3:.03f}ms")


class FileManager:
   def __init__(self, filename, mode):
       self.filename = filename
       self.mode = mode
       self.file = None

   def __enter__(self):
       self.file = open(self.filename, self.mode)
       return self.file

   def __exit__(self, exc_type, exc_value, traceback):
       if self.file:
           self.file.close()


# Example usage
if __name__ == "__main__":
   with FileManager("example.txt", "w") as file:
       file.write("Hello, world!\n")

import datetime


class FileManager:
   def __init__(self, filename, mode, log_filename="file_log.txt"):
       self.filename = filename
       self.mode = mode
       self.log_filename = log_filename
       self.file = None

   def log_action(self, action):
       timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       with open(self.log_filename, "a") as log_file:
           log_file.write(f"{timestamp} - {action}: {self.filename}\n")

   def __enter__(self):
       self.file = open(self.filename, self.mode)
       self.log_action("Opened")
       return self.file

   def __exit__(self, exc_type, exc_value, traceback):
       if self.file:
           self.file.close()
           self.log_action("Closed")


# Example Usage
with FileManager("example.txt", "r") as file:
   content = file.read()
   print(content)



