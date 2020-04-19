import os
filename1 = []
def file_name(file_path):
    for root,dirs,files in os.walk(file_path):
        for file in files:
            (filename, extension) = os.path.splitext(file)
            if (extension == '.xlsx'):
                filename1.append(file[0:9])
    print(filename1)
path =r'D:\testpath1\testpath2\testpath3\testpath4'
file_name(path)
