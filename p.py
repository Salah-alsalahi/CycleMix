import os
my_path = os.getcwd()
files=os.listdir(my_path)
for f0 in files:
  ap0=f"{my_path}/{f0}/"
  # print(ap0)
  if f0 == 'drive':
    # print(ap0)
    fp1=os.listdir(ap0)
    for f01 in fp1:
      ap1=ap0+f"{f01}/"
      if f01=="MyDrive":
        # print(ap1)
        fp2=os.listdir(ap1)
        for f02 in fp2:
          if f02=="Colab Notebooks":
            ap2=ap1+f"{f02}/"
            fp3=os.listdir(ap2)
            for f03 in fp3:
              # print(f03)
              if f03=="CycleMix-main 4":

                ap3=ap2+f"{f03}/"
                fp4=os.listdir(ap3)
                for f04 in fp4:
                  ap4=ap3+f"{f04}/"
# print(ap3)
# rootp=ap2
# print(rootp,"my path")
# import glob
# print(glob.glob(my_path))
# print(files)