import os
import zipfile

workspace_dir = 'workspace_dir'
file_path = 'inhouse_map_app/test/data/Polygon.zip' 
VALID_FORMATS = ['shp', 'shx', 'dbf', 'prj']


def decompress_zip_file(input_path:str, output_path: str=''):
    """
    This function decompress the ESRI archived file.

    Parameters
    ----------
    input_path : str
        path to the ESRI archived file
    output_path : str
        path to the ESRI archived file

    Returns
    -------
    :str
        path to the decompress ESRI archived file
    """
    try:
        if not output_path :
            output_path = os.path.join(workspace_dir, 'test1')

        file_format = os.path.basename(input_path).split('.')[-1]
        file_name = os.path.basename(input_path).split('.')[0]
        if file_format == 'zip':
            zipfile_size = os.path.getsize(input_path)
            if zipfile_size <= 500000:
                with zipfile.ZipFile(input_path, 'r') as archived:
                    # TODO
                    # I need to check .msi file or .exe .sh .bash
                    # file_contents = archived.namelist()
                    # for item in file_contents:
                    #     if item is valid_format:
                    #         pass
                    archived.extractall(output_path)
                    

                
            else:
                raise('file size is bigger than 5 Mb')

        else:
            raise('this file is not a zipfile', zipfile.BadZipFile)

    except Exception as e:
        raise('failed to decompress the ESRI archived file. => ', str(e))