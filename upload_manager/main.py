import os
import zipfile

WORKSPACE_DIR = 'workspace_dir'
FILE_PATH = r'C:\Users\User\Documents\GitHub\inhouse-map-app\inhouse_map_app\tests\data\Polygon.zip'
OUTPUT_PATH = r'C:\Users\User\Documents\GitHub\inhouse-map-app\inhouse_map_app\test\data\result'
INVALID_FORMATS = ['sh', 'msi', 'bash', 'bat', 'sql', 'exe']
ITEM_CONTENTS = []

# with zipfile.ZipFile(FILE_PATH) as archived:
#     print('file_contents: ', archived.printdir())


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
                    file_contents = archived.ZipFile.namelist()
                    # Check if bad format file like .msi , .exe, .sh, .bash, .bat, and .sql are exist
                    if len(file_contents) >= 2:
                        for items in file_contents[1:]:
                            ITEM_CONTENTS = [items.split('.')[-1]] + ITEM_CONTENTS 
                    else:
                        raise Exception('This zipfile is empty.')

                    bad_format = []
                    for i in INVALID_FORMATS:
                        if i in ITEM_CONTENTS:
                            bad_format.append(i)

                    if bad_format:
                        bad_format_str = ', '.join(bad_format)
                        raise Exception(
                            f'This zipfile could not extract because it contains (.{bad_format_str}) format file.')
                    else:
                        archive.extractall(OUTPUT_PATH) 

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
