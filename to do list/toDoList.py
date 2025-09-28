
# print(todo_list)

# todo_list.append("Nongki bareng temen")
# # print(f'Task "Nongki bareng temen" added.')
# print(todo_list)

# todo_list.append("Makan siang")
# print(todo_list)

# todo_list.append("Mengerjakan tugas")
# print(todo_list)

# print(len(todo_list)) # menampilkan jumlah item dalam list
# print(todo_list[2])

# todo_list.pop(1) # menghapus item index ke 1
# todo_list.remove("Mengerjakan tugas") # menghapus item berdasarkan value
# print(todo_list) # menampilkan isi list

todo_list = []

def add_task():
  input_task = input("Masukkan task yang ingin ditambahkan: ")
  todo_list.append(input_task)
  print(f"Task {input_task} added.")

def show_tasks():
  print('your to-do list:')
  for urut, item in enumerate(todo_list, start=1):
     print(urut, item)

def delete_task():
   show_tasks()
   choice = int(input("pilih nomor yang akan dihapus: " ))
   todo_list.pop(choice - 1)

def main():
  print("Welcome to the To-Do List App!")
   

main()
while True:
  print("=====**=====")
  print("1. Show Task!")
  print("2. Add Task!")
  print("3. Delete Task!")
  print("4. Exit App!")  
  pilihan = input("Masukkan pilihan (1/2/3/4): ")
  if pilihan == "1":
     show_tasks()
  elif pilihan == "2":
     add_task()
  elif pilihan == "3":
     delete_task()
  elif pilihan == "4":
      print("Exiting the app. Goodbye!")
      break
    
  else:
      print("Pilihan tidak valid.")

