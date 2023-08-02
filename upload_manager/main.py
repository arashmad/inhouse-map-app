import os
import zipfile

workspace_dir = 'workspace_dir'
file_path = 'inhouse-map-app\test\data'

def decompress_zip_file(input_path:str, output_path: str=''):
    """
    this function decompress the ESRI archived file.
    parameter
    ---------
    path:str
        path to the ESRI archived file

    Returns
    -------
    :str
        path to the decompress ESRI archived file
    """
    try:
        output_path = os.path.join(workspace_dir, 'test1')

        file_format = os.path.basename('file_path').split('.')[1]
        file_name = os.path.basename('file_path').split('.')[0]
        if file_format == 'zip':
            with zipfile.ZipFile('file_path', 'r') as archived:
                info = archive.getinfo("file_name")
            if info.compress_size >= 5 :
                pass
            else:
                raise('file size is bigger than 5 Mb')

        else:
            raise('this file is not a zipfile', zipfile.BadZipFile)

    except Exception as e:
        raise('failed to decompress the ESRI archived file. => ', str(e))