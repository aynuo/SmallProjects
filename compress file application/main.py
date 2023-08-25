import PySimpleGUI as pg
from zip import make_arc

#implement input objects 
label_1 = pg.Text("Select Your Files TO Compress: ")
file_path = pg.Input()
choose_file_button = pg.FileBrowse("choose", key="files")

#implement output objects 
label_2 = pg.Text("Select Your OutPut Directory:     ")
file_output_dir = pg.Input()
output_file_button = pg.FolderBrowse("choose", key="folder")

#implement compress button
compress_btn = pg.Button("Compress")
output_label = pg.Text(key="output")

#compress action
win = pg.Window("file Compressor", layout=[[label_1,file_path,choose_file_button],
                                            [label_2,file_output_dir,output_file_button],
                                            [compress_btn,output_label]])

win.read()
win.close()
