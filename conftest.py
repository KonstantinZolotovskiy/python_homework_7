import os.path
import pytest
import zipfile
import shutil

tmp_dir = os.path.join(os.getcwd(), 'tmp')
zip_dir = os.path.join(os.getcwd(), "zip")
zip_path = os.path.join(os.getcwd(), 'zip', 'files.zip')


@pytest.fixture(scope='function', autouse=True)
def zip_files():
    if not os.path.exists(zip_dir):
        os.mkdir(zip_dir)

    with zipfile.ZipFile(zip_dir + '/files.zip', 'w') as zip_file:
        for file in os.listdir(tmp_dir):
            add_file = os.path.join(tmp_dir, file)
            zip_file.write(add_file, os.path.basename(add_file))

    yield

    shutil.rmtree(zip_dir)
