import os
import shutil
import pathlib

from inhouse_map_app.upload_manager.main import decompress_zip_file

# Test settings

# Fatema
# ROOT = r'C:\Users\User\Documents\GitHub\inhouse-map-app'

# Arash
ROOT = '/home/arash/Desktop/projects/RahaWorks'

INPUT_PATH = os.path.join(ROOT, 'inhouse_map_app/tests/data/Polygon.zip')
OUTPUT_PATH = os.path.join(ROOT, 'inhouse_map_app/tests/data/results')

# Create test results directory
pathlib.Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

try:
    # Source file was stored successfully.
    unzipped_dir = decompress_zip_file(
        input_path=INPUT_PATH,
        output_path=OUTPUT_PATH)

    assert os.path.isfile(unzipped_dir[0]), \
        f"Unzipped file not found => {unzipped_dir[0]}"
    shutil.rmtree(OUTPUT_PATH)

    # Invalid source file format.
    # INPUT_PATH = '/home/arash/Desktop/projects/RahaWorks/inhouse_map_app/tests/data/Polygon.rar'
    # decompress_zip_file(input_path=INPUT_PATH, output_path=OUTPUT_PATH)

    # SOurce file not exist.
    # INPUT_PATH = '/home/arash/Desktop/projects/RahaWorks/inhouse_map_app/tests/data/Polygon1.zip'
    # decompress_zip_file(input_path=INPUT_PATH, output_path=OUTPUT_PATH)

except Exception as e:
    print(f'\n\n..::: Test Failed :::..\n{str(e)}\n\n')
    # Remove test results directory if test crashed.
    shutil.rmtree(OUTPUT_PATH)
