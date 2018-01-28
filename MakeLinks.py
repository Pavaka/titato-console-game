import os

def link(src_folder, dest_folder, linked_file):
    src = os.path.join(src_folder, linked_file)
    dest = os.path.join(dest_folder, linked_file)
    print("Linking {} -> {}".format(src, dest))
    os.symlink(src, dest)
def create_symlinks(conf):
    path_to_titato_lib =  os.path.join(os.getcwd(),"Projects", "external", "titato-lib", conf )
    build_dir = os.path.join(os.getcwd(), "Projects", conf);
    try:
        link(path_to_titato_lib, build_dir, "TitatoGameCore.lib")
        link(path_to_titato_lib, build_dir, "TitatoGameCore.dll")
        link(path_to_titato_lib, build_dir, "TitatoGameCore.pdb")
    except Exception as e:
        print(e)
        print("Coult not link {} Libraries".format(conf))

if __name__ == "__main__":
    create_symlinks("Debug")
    create_symlinks("Release")