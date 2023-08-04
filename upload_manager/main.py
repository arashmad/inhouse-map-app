import os
import zipfile

workspace_dir = 'workspace_dir'
file_path = 'inhouse_map_app/test/data/Polygon.zip'
VALID_FORMATS = ['shp', 'shx', 'dbf', 'prj']


def decompress_zip_file(input_path: str, output_path: str = '') -> str:
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
        # TODO
        # check file exist and raise FileNotFoundException() if it's necessary
        if not os.path.isfile(input_path):
            pass

        if not output_path:
            output_path = os.path.join(workspace_dir, 'test1')

        file_format = os.path.basename(input_path).split('.')[-1]
        file_name = os.path.basename(input_path).split('.')[0]

        # TODO
        # Better coding for if else
        if file_format == 'zip':
            zipfile_size = os.path.getsize(input_path)
            if zipfile_size <= 500000:
                with zipfile.ZipFile(input_path) as archived:
                    # TODO
                    # I need to check .msi file or .exe .sh .bash
                    # file_contents = archived.namelist()
                    # for item in file_contents:
                    #     if item is valid_format:
                    #         pass

                    # TODO
                    # Not working
                    archived.extractall(output_path)

                    return (output_path)

            else:
                # TODO
                # Fix the message
                raise Exception('file size is bigger than 5 Mb')

        else:
            raise Exception(
                f'Use .zip format as input => format (.{file_format}) is not supported.')

    except Exception as e:
        raise Exception(
            'Failed to decompress the ESRI archived file. => ', str(e))
