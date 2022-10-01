def directory():
      
  import os
  my_path = os.getcwd()
  files=os.listdir(my_path)
  # print(files)
  for f0 in files:
    ap0=f"{my_path}/{f0}/"
    # print(f0)
    if f0 == 'data':
      # print("data file path  ",ap0)
      return ap0
      # fp1=os.listdir(ap0)
      # for f01 in fp1:
        # if f01=="data":
          # ap1=ap0+f"{f01}/"
          # print(ap1)
root=directory()
# print(root)
        # fp2=os.listdir(ap1)
        # for f02 in fp2:
          # if f02=="Colab Notebooks":
            # ap2=ap1+f"{f02}/"
            # fp3=os.listdir(ap2)
            # for f03 in fp3:
              # print(f03)
              # if f03=="CycleMix-main 4":

                # ap3=ap2+f"{f03}/"
                # fp4=os.listdir(ap3)
                # for f04 in fp4:
                  # ap4=ap3+f"{f04}/"
# print(ap3)
# rootp=ap2
# print(rootp,"my path")
# import glob
# print(glob.glob(my_path))
# print(files)

git config user.email "salahalsalahi.king@gmail.com"
gti config user.name "Salah-alsalahi"
git add .
git commit -m "salah"
git push origin main
.