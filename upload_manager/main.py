import os
import zipfile

WORKSPACE_DIR = 'workspace_dir'
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
        # TODO
        # We need a clean code!
        if os.path.isfile(input_path):
            if not output_path:
                output_path = os.path.join(WORKSPACE_DIR, 'test1')

            file_format = os.path.basename(input_path).split('.')[-1]
            file_name = os.path.basename(input_path).split('.')[0]

            if file_format == 'zip':
                zipfile_size = os.path.getsize(input_path)
                if zipfile_size <= 5 * 1024000:
                    with zipfile.ZipFile(input_path) as archived:
                        file_contents = archived.namelist()
                        inner_files = []
                        if len(file_contents) >= 2:
                            for items in file_contents[1:]:
                                inner_files.append(items.split('.')[-1])
                        else:
                            raise Exception(f'{file_name}.zip is empty.')

                        # Check if bad format file like .msi , .exe, .sh, .bash, .bat, and .sql are exist
                        bad_format = []
                        for i in INVALID_FORMATS:
                            if i in ITEM_CONTENTS:
                                bad_format.append(i)
                        if bad_format:
                            bad_format_str = ', '.join(bad_format)
                            raise Exception(
                                f'Input file contains (.{bad_format_str}) format file.')
                        else:
                            extracted_archive = archived.extractall(
                                output_path)
                            extracted_archive = archived.namelist()
                            path = output_path
                            absolute_path = [
                                path+layer for layer in extracted_archive]
                            return (absolute_path)
                else:
                    raise Exception(
                        f'Input file ({zipfile_size / 1024000:.2f}MB) is larger than 5MB.')
            else:
                raise Exception(
                    f'Only <.zip> format is supported but (.{file_format}) was used.')
        else:
            raise FileNotFoundError(f'Input file ({input_path}) not found.')
    except Exception as e:
        raise Exception(
            f'Failed to decompress the ESRI archived file. => {str(e)}')
