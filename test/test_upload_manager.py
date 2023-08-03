from upload_manager.main import decompress_zip_file

INPUT_PATH = 'inhouse-map-app/test/data/Polygon.zip' 
OUTPUT_PATH = 'inhouse-map-app/test/data/result'

decompress_zip_file(input_path=INPUT_PATH, output_path=OUTPUT_PATH)