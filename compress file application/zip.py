import zipfile as zf
import pathlib

#compress action
def make_arc(filepaths, dst_dir):
    dst_path = pathlib.Path(dst_dir, "zip_file.zip")
    with az.ZipFile in filepaths:
        filepath = pathlib.Path(filepath)
        archive.write(filepath, arcname=filepath.name)
