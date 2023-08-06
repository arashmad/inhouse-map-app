import os
import zipfile

WORKSPACE_DIR = 'workspace_dir'
FILE_PATH = r'C:\Users\User\Documents\GitHub\inhouse-map-app\inhouse_map_app\tests\data\Polygon.zip'
OUTPUT_PATH = r'C:\Users\User\Documents\GitHub\inhouse-map-app\inhouse_map_app\test\data\result'
INVALID_FORMATS = ['sh', 'msi', 'bash', 'bat', 'sql', 'exe']
ITEM_CONTENTS = []


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
        # check file exist and raise FileNotFoundException() if it's necessary
        if os.path.isfile(input_path):
            if not output_path:
                output_path = os.path.join(WORKSPACE_DIR, 'test1')

            file_format = os.path.basename(input_path).split('.')[-1]
            file_name = os.path.basename(input_path).split('.')[0]

            # TODO
            # Better coding for if else
            if file_format == 'zip':
                zipfile_size = os.path.getsize(input_path)
                if zipfile_size <= 5 * 1024000:
                    with zipfile.ZipFile(input_path) as archived:
                        file_contents = archived.ZipFile.namelist()
                        # Check if bad format file like .msi , .exe, .sh, .bash, .bat, and .sql are exist
                        if len(file_contents) >= 2:
                            for items in file_contents[1:]:
                                ITEM_CONTENTS = [items.split(
                                    '.')[-1]] + ITEM_CONTENTS
                        else:
                            raise Exception(f'{file_name}.zip is empty.')
                        bad_format = []
                        for i in INVALID_FORMATS:
                            if i in ITEM_CONTENTS:
                                bad_format.append(i)
                        if bad_format:
                            bad_format_str = ', '.join(bad_format)
                            raise Exception(
                                f'This zipfile could not extract because it contains (.{bad_format_str}) format file.')
                        else:
                            extracted_archive = archived.extractall(
                                OUTPUT_PATH)
                            extracted_archive = archived.namelist()
                            path = OUTPUT_PATH
                            absolute_path = [
                                path+layer for layer in extracted_archive]
                            return (absolute_path)
                else:
                    # Fix the message
                    raise Exception(
                        f'{file_name}.zip size is {zipfile_size / 1024000:.2f} MB that is larger than 5 MB ')
            else:
                raise Exception(
                    f'Use .zip format as input => format (.{file_format}) is not supported.')
        else:
            raise Exception(
                f'There is no file in "{input_path}" directory.')
    except Exception as e:
        raise Exception(
            'Failed to decompress the ESRI archived file. => ', str(e))
