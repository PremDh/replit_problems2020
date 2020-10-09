def server_time_check(task_config, task_times):
  x = task_config.split(" ")
  num_tasks = int(x[0])
  exec_time = int(x[1])
  
  # print(x[0])
  
  y = task_times.split(" ")
  curr_task = 0
  current_time = 0
  t_count = 0
  while current_time < exec_time:
    current_time += int(y[curr_task])
    if current_time > exec_time:
      break
    t_count += 1
    curr_task += 1
  print(t_count)
  return t_count
  

## Please do not change the code below this line
## These lines are how the tests interact with the code

##task_config = input("Please input the number of tasks, and the maximum total execution time:")
##task_times = input("Please input the execution times of each task, seperated with a space:")

##server_time_check(task_config, task_times)
