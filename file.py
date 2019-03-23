import os;
ptr=open("file.txt","w+");

if ptr:
   print("file is open ");

ptr.write("nitk hostel jvjij;n kjv ;ojhgvk ");

#ptr.close();
#ptr=open("file.txt","a");
ptr.write("in bangalore ljoije jemola");

ptr.close();
f=open("file.txt","r");

for i in f:
  print(i);
f.close();
os.rename("file.txt","file1.txt");

