import PySimpleGUI as pg
from zip import make_arc

label_1 = pg.Text("Select Your Files TO Compress: ")
file_path = pg.Input()
choose_file_button = pg.FileBrowse("choose", key="files")

label_2 = pg.Text("Select Your OutPut Directory:     ")
file_output_dir = pg.Input()
output_file_button = pg.FolderBrowse("choose", key="folder")

compress_btn = pg.Button("Compress")
output_label = pg.Text(key="output")

win = pg.Window("file Compressor", layout=[[label_1,file_path,choose_file_button],
                                            [label_2,file_output_dir,output_file_button],
                                            [compress_btn,output_label]])

win.read()
win.close()
