from pathlib import Path
import argparse
import shutil
import os


M2_PATH_TO_LIBS = f'C:\\Users\\{os.getlogin()}\\.m2\\repository'
PATH_TO_LIBS = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\maventemp'

all_libs = []
pom_and_file = {}


def go_to_folder(folder):
    for new_dir in os.listdir(folder):
        this_path = os.path.join(folder, new_dir)
        if os.path.isdir(this_path):
            go_to_folder(this_path)
        else:
            libs_with_path = []
            for i in os.listdir(folder):
                libs_with_path.append(os.path.normpath(folder) + '\\' + i)
            all_libs.append(libs_with_path)
            break


def get_jars_and_poms(libs):
    for lib in libs:
        pom_name = ''
        packed_name = ''

        for elem in lib:
            if '.pom' in Path(elem).suffix:
                pom_name = elem
            elif '.jar' in Path(elem).suffix or '.dll' in Path(elem).suffix:
                packed_name = elem
        if packed_name == '':
            packed_name = pom_name

        pom_and_file[pom_name] = packed_name


def deploy_files(pom_packed, url, repo_id):
    for pom_file in pom_packed:
        packed_file = pom_packed[pom_file]
        upload_method = f'mvn deploy:deploy-file -DpomFile={pom_file} -Durl={url} -DrepositoryId={repo_id} -Dfile={packed_file} -Dpackaging={Path(packed_file).suffix[1:]}'
        
        os.system(upload_method)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script to download maven libs to Nexus")
    
    parser.add_argument("-url", dest="nexus_url", required=True, type=str,
                        help='For example: https://example.com/repository/Example')
    parser.add_argument("-repoId", dest="nexus_repo_id", required=True, type=str,
                        help='Your maven repository id from settings.xml')
    
    args = parser.parse_args()

if os.path.exists(PATH_TO_LIBS):
    shutil.rmtree(PATH_TO_LIBS)

shutil.copytree(M2_PATH_TO_LIBS, PATH_TO_LIBS)

go_to_folder(PATH_TO_LIBS)
get_jars_and_poms(all_libs)
deploy_files(pom_and_file, args.nexus_url, args.nexus_repo_id)

shutil.rmtree(PATH_TO_LIBS)
input('Press ENTER to exit...')
