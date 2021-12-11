import argparse
import pickle
import time
import datetime


class Task():
    """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
    
    def __init__(self,created,completed,name,id,priority,due):
        self.created=created
        self.completed=completed
        self.name=name
        self.id=id
        self.priority=priority
        self.due=due

        



class Tasks:
    """A list of `Task` objects."""
   
    def __init__(self,file):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        # If the file .toto.pickle is empty, it raises EOFError
        with open(file,'rb+') as f:
            try:
                self.tasks=pickle.load(f)
            except EOFError:
                self.tasks=[]
            

    def pickle_tasks(self):
        """Picle your task list to a file"""
        with open('.todo.pickle','wb') as f:
            pickle.dump(self.tasks,f)

    # Add a task
    def add(self):
            parser = argparse.ArgumentParser(description='Command Line Task Manager')
            parser.add_argument('--add', type=str, required=True, help="the name of task")
            parser.add_argument('--due', required=False, help="the due date of task")
            parser.add_argument('--priority', type=int, default=1,required=False, help="priority of task; default value is 1")
            args = parser.parse_args()
            # Get the created time of the task.
            created=time.strftime("%a %b %d %H:%M:%S CST %Y", time.localtime())
            if len(self.tasks)==0:
                id=1
            else:
                id=self.tasks[-1].id+1
            new_task=Task(created,None,args.add,id,args.priority,due=args.due)
            print('Create task',new_task.id)
            self.tasks.append(new_task)
            
    
    # List the tasks that are not being completed
    def list(self):
        print("ID\tAge\tDue Date\tPriority\tTask")
        print("--\t---\t--------\t--------\t----")
        # Get the time now.
        year2=time.strftime("%Y", time.localtime())
        month2=time.strftime("%m", time.localtime())
        day2=time.strftime("%d", time.localtime())
        # Sort the task according to the due date and priority.
        task_list1=[]
        task_list2=[]
        # Put the task with due into a list2 and put the task with no due into list1.
        for task in self.tasks:
            if task.due==None:
                task_list1.append(task)
            else:
                task_list2.append(task)
        sorted_task1=sorted(task_list1,key=lambda x: x.priority,reverse=True)
        sorted_task2=sorted(task_list2,key=lambda x: time.strptime(x.due, "%m/%d/%Y"),reverse=True)
        # Print the tasks which are not being completed.
        for task in sorted_task2:
            if task.completed==None:
                # Calculate the age of task
                date=datetime.datetime.strptime(task.created,"%a %b %d %H:%M:%S CST %Y")
                year1=datetime.datetime.strftime(date,"%Y")
                month1=datetime.datetime.strftime(date,"%m")
                day1=datetime.datetime.strftime(date,"%d")
                # Use the time now minus the time of creating task to calculate the age of the task
                d1 = datetime.datetime(int(year1),int(month1),int(day1))   
                d2 = datetime.datetime(int(year2),int(month2),int(day2))   
                interval = d2 - d1                   
                age=interval.days
                print(str(task.id)+'\t'+str(age)+'d'+'\t'+task.due+'\t'+str(task.priority)+'\t'+'\t'+task.name)                                            
        for task in sorted_task1:
            if task.completed==None:
                # Calculate the age of task
                date=datetime.datetime.strptime(task.created,"%a %b %d %H:%M:%S CST %Y")
                year1=datetime.datetime.strftime(date,"%Y")
                month1=datetime.datetime.strftime(date,"%m")
                day1=datetime.datetime.strftime(date,"%d")
                # Use the time now minus the time of creating task to calculate the age of the task
                d1 = datetime.datetime(int(year1),int(month1),int(day1))   
                d2 = datetime.datetime(int(year2),int(month2),int(day2))   
                interval = d2 - d1                   
                age=interval.days
                print(str(task.id)+'\t'+str(age)+'d'+'\t\t'+'\t'+str(task.priority)+'\t'+'\t'+task.name)                                            

    # Report the information of all the tasks
    def report(self):
        print("ID\tAge\tDue Date\tPriority\tTask\t\tCreated\t\t\t\tCompleted")
        print("--\t---\t--------\t--------\t----\t\t---------------------------\t-------------------------")
        # Get the time now.
        year2=time.strftime("%Y", time.localtime())
        month2=time.strftime("%m", time.localtime())
        day2=time.strftime("%d", time.localtime())
        # Print the information of all the tasks.
        for task in self.tasks:
            date=datetime.datetime.strptime(task.created,"%a %b %d %H:%M:%S CST %Y")
            year1=datetime.datetime.strftime(date,"%Y")
            month1=datetime.datetime.strftime(date,"%m")
            day1=datetime.datetime.strftime(date,"%d")
            # Use the time now minus the time of creating task to calculate the age of the task
            d1 = datetime.datetime(int(year1),int(month1),int(day1))   
            d2 = datetime.datetime(int(year2),int(month2),int(day2))   
            interval = d2 - d1                   
            age=interval.days
            print(str(task.id)+'\t'+str(age)+'d'+'\t',task.due,'\t'+'\t'+str(task.priority)+'\t'+'\t'+task.name+'\t\t'+task.created+'\t',task.completed)                                            


    # Complete a task
    def done(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--done', type=int,required=False,help='Complete the task')
        args = parser.parse_args()
        # Get the id of the completed task
        id = args.done
        print("Complete task",id)
        for task in self.tasks:
            if id==task.id:
                # Get the time of being compeleted.
                completed=time.strftime("%a %b %d %H:%M:%S CST %Y", time.localtime())
                task.completed=completed
    
    # Delete a task
    def delete(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--delete', type=int,required=False,help='delete the task')
        args = parser.parse_args()
        # Get the id of the deleted task
        id = args.delete
        print("Delete task",id)
        # delete the task in list self.tasks
        task_list=self.tasks
        for task in task_list:
            if id==task.id:
                self.tasks.remove(task)




    def query(self):
        print("ID\tAge\tDue Date\tPriority\tTask")
        print("--\t---\t--------\t--------\t----")
        # Get the time now.
        year2=time.strftime("%Y", time.localtime())
        month2=time.strftime("%m", time.localtime())
        day2=time.strftime("%d", time.localtime())
        parser = argparse.ArgumentParser()
        parser.add_argument('--query', type=str, required=False, nargs="+", help="priority of task; default value is 1")
        args = parser.parse_args()
        # Put search terms into a term list
        terms = args.query
        # Determine whether the search term is in the name of task
        for term in terms:
            for task in self.tasks:
                if term in task.name:
                    date=datetime.datetime.strptime(task.created,"%a %b %d %H:%M:%S CST %Y")
                    year1=datetime.datetime.strftime(date,"%Y")
                    month1=datetime.datetime.strftime(date,"%m")
                    day1=datetime.datetime.strftime(date,"%d")
                    # Use the time now minus the time of creating task to calculate the age of the task
                    d1 = datetime.datetime(int(year1),int(month1),int(day1))   
                    d2 = datetime.datetime(int(year2),int(month2),int(day2))   
                    interval = d2 - d1                   
                    age=interval.days
                    print(str(task.id)+'\t'+str(age)+'d'+'\t'+task.due+'\t'+str(task.priority)+'\t'+'\t'+task.name)                                            

        

    
def main():
    # Create a Tasks object my_task
    my_task=Tasks('.todo.pickle')
    parser = argparse.ArgumentParser(description='Command Line Task Manager')
    parser.add_argument('--add',type=str,required=False,help="add the name of the task")
    parser.add_argument('--due', required=False, help="the due date of task")
    parser.add_argument('--priority', type=int, required=False, default='1',help="priority of task; default value is 1")
    parser.add_argument('--list',required=False,action='store_true',help='list the tasks not being completed')
    parser.add_argument('--report',required=False,action='store_true',help='report tasks')
    parser.add_argument('--query',required=False,type=str,nargs="+",help='query the tasks containing the search items')
    parser.add_argument('--done',type=int,required=False,help='Complete the task')
    parser.add_argument('--delete',type=int,required=False,help='Delete the task')
    args = parser.parse_args()
    if args.add!=None:
        my_task.add()
    elif args.list:
        my_task.list()
    elif args.report:
        my_task.report()
    elif args.query!=None:
        my_task.query()
    elif args.done!=None:
        my_task.done()
    elif args.delete!=None:
        my_task.delete()
    my_task.pickle_tasks()
    
if __name__ == '__main__':
    main()



