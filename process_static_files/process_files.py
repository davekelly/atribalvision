import os

# os.chdir()
# print(os.getcwd())
# COUNT = 1
  

def main():
    
    for f in os.listdir('../interviews'):
        f_name, f_ext = os.path.splitext(f)
    
        print(f_name)
        # os.rename(f_name, 'index.html')
        mode = 0o777
        new_dir = os.path.join('../new-interviews', f_name)
        os.mkdir(new_dir, mode)

        
        os.rename('../interviews/' + f_name, new_dir + '/index.html')
      

if __name__ == "__main__":
    main()